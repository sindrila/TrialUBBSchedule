import re

from Domain.ClassType import ClassType, get_class_type_from_str
from Domain.Frequency import Frequency, get_frequency_from_string
from Domain.GroupClasses import GroupClasses
from Domain.Professor import get_name_from_title_and_name
from Domain.Professor import get_title_from_title_and_name
from Domain.Professor import Professor
from Domain.Room import Room
from Domain.StudentClass import StudentClass
from Domain.Subject import Subject
from Parsers.BaseWebsiteParser import BaseWebsiteParser
import pandas as pd
from Repository import PickleSerializer


class StudentYearScheduleParser(BaseWebsiteParser):
    def __init__(self, given_url: str):
        '''
        Parser for student year schedule website.
        :param given_url: The url of schedule for a student year website.
        '''
        super().__init__(given_url)
        self._table_data_frame: pd.DataFrame = None

    def _get_year_groups_subgroups_from_table_data_frame(self) -> (str, set, dict):
        # TODO: for Inteligenta Artificiala in limba engleza, group 1012 has only one group, and the table entry is both 1012 and 1012/1
        # TODO: Psiho not supported
        # TODO: For groups that only attend year-wide classes, this function does NOT extract the group strings

        year_of_study: str = ""
        # groups: set of group strings
        groups: set = set()
        # subgroups: dictionary of subgroup strings for group string
        subgroups: dict = {}



        groups_subgroups_year: list[str] = self._table_data_frame["formation"].unique()
            # groups_subgroups_year: list[str] = self._table_data_frame.sort_values(by="formation")["formation"].unique()

        # year of study regex
        year_of_study_pattern = re.compile(r'[a-zA-Z]+\d*')

        # group regex
        group_pattern = re.compile(r'^\d{3,}$')

        for element in groups_subgroups_year:
            year_of_study_match = year_of_study_pattern.match(element)
            group_match = group_pattern.match(element)

            if year_of_study_match:
                year_of_study = year_of_study_match.group()
            elif group_match:
                group = group_match.group()
                groups.add(group)
            else:
                group = element.split('/')[0]
                subgroup = element.split('/')[1]

                # for tables with only subgroups entries, automatically add the group
                groups.add(group)

                if group in subgroups.keys():
                    subgroups[group] += subgroup
                else:
                    subgroups[group] = [subgroup]

        return (year_of_study, groups, subgroups)

    def _get_table_data(self) -> list[dict]:
        data = []
        for index in range(0, len(self._elements), 8):
            row = {"day": self._elements[index].text,
                   "start_hour": (self._elements[index + 1].text.split('-'))[0],
                   "end_hour": (self._elements[index + 1].text.split('-'))[1],
                   "frequency": self._elements[index + 2].text,
                   "room": Room(self._elements[index + 3].text, None),
                   "formation": self._elements[index + 4].text,
                   "class_type": get_class_type_from_str(self._elements[index + 5].text),
                   "subject": Subject(self._elements[index + 6].text),
                   "professor": self._elements[index + 7].text}
            data.append(row)
        return data

    def _get_student_classes(self, classes: list[dict]) -> list[StudentClass]:
        '''
        Get student classes list object.
        :param classes: list of dictionaries containing class data
        :return: list of StudentClass objects
        '''
        student_classes = []
        for class_data in classes:
            professor_name = get_name_from_title_and_name(class_data["professor"])
            professor_title = get_title_from_title_and_name(class_data["professor"])
            professor = Professor(professor_name, professor_title)
            student_class: StudentClass = StudentClass(class_data["day"],
                                                       class_data["start_hour"],
                                                       class_data["end_hour"],
                                                       get_frequency_from_string(class_data["frequency"]),
                                                       class_data["room"],
                                                       class_data["formation"],
                                                       class_data["class_type"],
                                                       class_data["subject"],
                                                       professor)
            student_classes.append(student_class)
        return student_classes

    def _get_student_classes_for_formation(self, formation: str) -> list[StudentClass]:
        '''
        Gets group-specific student classes.
        :param formation: The formation string.
        :return: A list of student classes.
        '''
        group_rows = self._table_data_frame[self._table_data_frame["formation"] == formation].drop_duplicates(
            subset=['day', 'start_hour', 'end_hour', 'frequency'])
        if group_rows.empty:
            raise RuntimeError(f"No data under formation {formation}.")
        classes: list[dict] = group_rows.to_dict('records')
        return self._get_student_classes(classes)

    def get_data(self) -> dict:
        '''
        Parse student year schedule website using an xpath and formats it for groups/semigroups.
        :return: Dictionary, where the keys are the group/semigroup and the values are the student classes.
        TODO: MaIS2 does not work
        '''
        pd.set_option('display.max_columns', None)

        self.get_browser()
        xpath = '//tbody/tr[position() > 0]/td[position() <= 8]'
        self._elements = self.get_elements_xpath(xpath)

        if not self._elements:
            return None

        headers = self.get_elements_xpath("//h1")
        headers = [header.text for header in headers]
        year_header = headers[0]
        groups_headers: list[str] = headers[1:]

        table_data = self._get_table_data()
        self._table_data_frame = pd.DataFrame(table_data)

        year_abbreviation, groups, subgroups = self._get_year_groups_subgroups_from_table_data_frame()
        year_wide_student_classes = []
        if year_abbreviation:
            year_wide_student_classes: list[StudentClass] = self._get_student_classes_for_formation(year_abbreviation)


        year_formation_schedule: dict = {}
        for group in groups_headers:
            group: str = group.split('Grupa ')[1]
            if group in groups:
                group_wide_student_classes: list[StudentClass] = self._get_student_classes_for_formation(group)
                if group in subgroups.keys():
                    for subgroup in subgroups[group]:
                        classes: list[StudentClass] = year_wide_student_classes.copy()
                        classes.extend(group_wide_student_classes)
                        classes.extend(self._get_student_classes_for_formation(f"{group}/{subgroup}"))
                        # classes.sort(key=lambda x: (x.day, x.starting_hour))
                        year_formation_schedule[f"{group}/{subgroup}"] = classes
                else:
                    classes: list[StudentClass] = year_wide_student_classes.copy()
                    classes.extend(group_wide_student_classes)
                    year_formation_schedule[f"{group}"] = classes

            else:
                classes: list[StudentClass] = year_wide_student_classes.copy()
                year_formation_schedule[f"{group}"] = classes


        # for group in year_formation_schedule.keys():
        #     classes = year_formation_schedule[group]
        #     for class_data in classes:
        #         print(class_data)

        return year_formation_schedule
