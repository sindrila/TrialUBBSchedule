import uuid
from datetime import datetime

from Calendar.EventCreator import EventCreator
from Calendar.SemesterDates import SemesterDates
from Domain.Frequency import Frequency
from Domain.StudentClass import StudentClass
from icalendar import Event, vRecur

class StudentEventCreator(EventCreator):
    def __init__(self, given_event: StudentClass):
        '''
        Format a StudentClass into iCalendar Event.
        :param given_event: StudentEvent object
        '''
        super().__init__(given_event)

    def create_icalendar_event(self) -> Event:
        '''
        :return: An iCalendar event for the given ProfessorClass.
        '''
        event = Event()
        event.add('uid', uuid.uuid4())
        if self._given_event is None:
            return event
        # Issue: event.add probably has a maximum buffer size, which causes line breaks (\r\n) in the middle of string.
        # Not causing any problems on Apple Calendar or Microsoft Outlook. Needs to be tested.
        if self._given_event.class_type.value != "UNKOWN":
            class_type = ""
            if (self._given_event.class_type.value == "Curs"):
                class_type = "C"
            elif (self._given_event.class_type.value == "Seminar"):
                class_type = "S"
            elif (self._given_event.class_type.value == "Laborator"):
                class_type = "L"

            event.add('summary',f"[{class_type}] - {self._given_event.subject}")

        else:
            event.add('summary', self._given_event.subject)
        event.add('location', f"Room {self._given_event.room}")
        if self._given_event.professor:
            event.add('description', f"Profesor {self._given_event.professor}")

        current_semester = SemesterDates()
        first_class_start_date: datetime = current_semester.get_first_week_class_date(self._given_event.starting_hour,
                                                                                      self._given_event.day)
        first_class_end_date: datetime = current_semester.get_first_week_class_date(self._given_event.ending_hour,
                                                                                    self._given_event.day)

        if self._given_event.frequency == Frequency.SECOND_WEEK:
            first_class_start_date = current_semester.get_second_week_class_date(self._given_event.starting_hour,
                                                                                 self._given_event.day)
            first_class_end_date = current_semester.get_second_week_class_date(self._given_event.ending_hour,
                                                                               self._given_event.day)

        event.add('dtstart', first_class_start_date)
        event.add('dtend', first_class_end_date)

        recurrence_rule = vRecur()
        if self._given_event.frequency != Frequency.UNKNOWN:
            recurrence_rule['interval'] = 2
        recurrence_rule['freq'] = 'WEEKLY'
        recurrence_rule['byday'] = self._week_days_mapping[self._given_event.day]
        recurrence_rule['until'] = current_semester.get_final_date()
        event.add('rrule', recurrence_rule)

        event.add('transp', 'OPAQUE')
        return event