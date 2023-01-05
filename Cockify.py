import datetime as dt

class Event:
       def __init__(self, name, startTime, endTime, description):
              self.name = name
              self.startTime = startTime
              self.endTime = endTime
              self.description = description

class Project:
       def __init__(self, name, events):
              self.name = name
              self.events = events

ev1 = Event("Cockify", dt.datetime.today(), dt.datetime(2015, 7, 18, 9, 50, 20), "Putting in IO work")
ev2 = Event("Cockify", dt.datetime.today(), dt.datetime(2019, 7, 18, 9, 50, 20), "Gettings to work")
ev3 = Event("Cockify", dt.datetime.today(), dt.datetime(2017, 7, 18, 9, 50, 20), "Hell yeah")

progEvents = [ev1, ev2, ev3]
prog = Project("Programming", progEvents)

# Programming,Cockify,2023-01-06 00:04:54, 2023-01-06 01:12:54,Trying out this Program
# (activity, project, startTime, endTime, description)
# curr = dt.datetime.today().replace(microsecond=0)
# Project,eventName1,eventName2,...

s = "Cockify,2023-01-06 00:04:54,2023-01-06 01:12:54,Trying out this Program"

ss = s.split(",")
ev4 = Event()

for r in ss:
       print(r)