from datetime import datetime

import pytz


class SemesterDates:
    def __init__(self):
        '''
        Temporary fix for calculating the current semester date.
        Hardcoded values, will break for the next university year.
        '''
        self._starting_year = 2024
        self._ending_year = 2025

        self._starting_month_first_week = 9
        self._starting_month_second_week = 10
        self._starting_day_first_week = 30
        self._number_of_days_in_starting_month_first_week = 30
        self._starting_day_second_week = 7
        self._number_of_days_in_starting_month_second_week = 31

        self._ending_month = 1
        self._ending_day = 21

        self._week_day_to_int_mapping = {
            'Luni': 0,
            'Marti': 1,
            'Miercuri': 2,
            'Joi': 3,
            'Vineri': 4,
            'Sambata': 5,
            'Duminica': 6
        }

    @property
    def starting_year(self):
        return self._starting_year

    @property
    def ending_year(self):
        return self._ending_year

    @property
    def starting_month_first_week(self):
        return self._starting_month_first_week

    @property
    def starting_month_second_week(self):
        return self._starting_month_second_week

    @property
    def starting_day_first_week(self):
        return self._starting_day_first_week

    @property
    def starting_day_second_week(self):
        return self._starting_day_second_week

    @property
    def ending_month(self):
        return self._ending_month

    @property
    def ending_day(self):
        return self._ending_day

    @starting_year.setter
    def starting_year(self, year):
        self._starting_year = year

    @ending_year.setter
    def ending_year(self, year):
        self._ending_year = year

    @starting_month_first_week.setter
    def starting_month_first_week(self, month):
        self._starting_month_first_week = month

    @starting_month_second_week.setter
    def starting_month_second_week(self, month):
        self._starting_month_second_week = month

    @starting_day_first_week.setter
    def starting_day_first_week(self, day):
        self._starting_day_first_week = day

    @starting_day_second_week.setter
    def starting_day_second_week(self, day):
        self._starting_day_second_week = day

    @ending_month.setter
    def ending_month(self, month):
        self._ending_month = month

    @ending_day.setter
    def ending_day(self, day):
        self._ending_day = day

    def get_first_week_class_date(self, hour: int, day: str) -> datetime:
        '''
        :return: the first week class date for the given hour and day.
        '''
        year = self._starting_year
        month = self._starting_month_first_week
        day_number = self._starting_day_first_week + self._week_day_to_int_mapping[day]

        if day_number > self._number_of_days_in_starting_month_first_week:
            day_number = day_number % self._number_of_days_in_starting_month_first_week
            month += 1
            if month == 13:
                month = 1
                year += 1
        return datetime(year, month, day_number, hour)

    def get_second_week_class_date(self, hour: int, day: str) -> datetime:
        '''
        :return: the second week class date for the given hour and day.
        '''
        year = self._starting_year
        month = self._starting_month_second_week
        day_number = self._starting_day_second_week + self._week_day_to_int_mapping[day]

        if day_number > self._number_of_days_in_starting_month_second_week:
            day_number = day_number % self._number_of_days_in_starting_month_second_week
            month += 1
            if month == 13:
                month = 1
                year += 1
        return datetime(year, month, day_number, hour)

    def get_final_date(self) -> datetime:
        '''
        :return: the final date for the current semester date.
        '''
        return datetime(self._ending_year, self._ending_month, self._ending_day, 23, 59)
