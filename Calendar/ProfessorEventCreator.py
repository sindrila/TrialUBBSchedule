import uuid
from datetime import datetime
from Calendar.EventCreator import EventCreator
from icalendar import Event, vRecur
from Calendar.SemesterDates import SemesterDates
from Domain.ProfessorClass import ProfessorClass
from Domain.Frequency import Frequency


class ProfessorEventCreator(EventCreator):
    def __init__(self, given_event: ProfessorClass):
        '''
        Format a ProfessorClass into an iCalendar Event.
        '''
        super().__init__(given_event)

    def create_icalendar_event(self) -> Event:
        '''
        :return: An iCalendar event for the given ProfessorClass.
        '''
        event = Event()
        event.add('uid', uuid.uuid4())
        # Issue: event.add probably has a maximum buffer size, which causes line breaks (\r\n) in the middle of string.
        # Not causing any problems on Apple Calendar or Microsoft Outlook. Needs to be tested.
        if self._given_event.class_type.value != "UNKOWN":
            event.add('summary',
                      f"{self._given_event.class_type.value} - {self._given_event.subject} - {self._given_event.formation} ")
        else:
            event.add('summary', self._given_event.subject)
        event.add('location', f"Room {self._given_event.room}")
        if self._given_event.year_of_study:
            event.add('description', f"Year {self._given_event.year_of_study}")

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
