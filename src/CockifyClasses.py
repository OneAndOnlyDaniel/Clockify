import datetime as dt

class Event:
       def __init__(self, startTime, endTime, name="Add Name", description=""):
              self.name = name
              self.startTime = startTime
              self.endTime = endTime
              self.description = description

       def __str__(self):
              return "{0},{1},{2},{3}".format(self.name, str(self.startTime), str(self.endTime), self.description)

class Project:
       def __init__(self, name: str, events):
              self.name = name
              self.events = events

       def __str__(self):
              temp = self.name + ","
              for ev in self.events[:-1]:
                     temp = temp + str(ev) + ","

              temp = temp + str(self.events[-1])

              return temp