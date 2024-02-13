from Calendar.ProfessorEvent import ProfessorEvent
from Calendar.ProfessorScheduler import ProfessorScheduler
from Domain.Professor import Professor
from Parsers.ProfessorPageParser import ProfessorPageParser
import pickle

from Service.ProfessorScheduleService import ProfessorScheduleService
from UI import UI

if __name__ == "__main__":
    ui = UI()
    ui.start()
