class TimeOfDay:
   def __init__(self, hour, minute, second):
      self.hour = hour
      self.minute = minute
      self.second = second
      
   def __init__(self, timeTuple):
      self.hour = timeTuple[0]
      self.minute = timeTuple[1]
      self.second = timeTuple[2]
   
   def __str__(self):
      return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
   
   def __repr__(self):
      return "TimeOfDay(" + str(self.hour) + "," + str(self.minute) + "," + str(self.second) + ")"
   
   def __eq__(self, other):
      return self.hour == other.hour and self.minute == other.minute and self.second == other.second
   
   def __lt__(self, other):
      if self.hour < other.hour:
         return True
      elif self.hour == other.hour:
         if self.minute < other.minute:
            return True
         elif self.minute == other.minute:
            if self.second < other.second:
               return True
      return False
   
   def __gt__(self, other):
      if self.hour > other.hour:
         return True
      elif self.hour == other.hour:
         if self.minute > other.minute:
            return True
         elif self.minute == other.minute:
            if self.second > other.second:
               return True
      return False
   
   def __le__(self, other):
      return self < other or self == other
   
   def __ge__(self, other):
      return self > other or self == other
   
   def __ne__(self, other):
      return not self == other