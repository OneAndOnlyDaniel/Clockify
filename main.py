import datetime as dt
import CockifyIO as IO
from CockifyClasses import *

# Projects have a name and a list of NAMES of events that are associated to it
# But the events themselves aren't saved in the project, might change that later

ev1 = Event(dt.datetime.today(), dt.datetime(2015, 7, 18, 9, 50, 20), "Cockify", "Putting in IO work")
ev2 = Event(dt.datetime.today(), dt.datetime(2019, 7, 18, 9, 50, 20), "Cockify", "Gettings to work")
ev3 = Event(dt.datetime.today(), dt.datetime(2017, 7, 18, 9, 50, 20), "Cockify", "Hell yeah")

proj = Project("POGramming", ["Cockify", "Clockify"])

print(proj)

IO.readFile('example.csv')