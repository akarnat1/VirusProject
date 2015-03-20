'''

Anthony Karnati
Rafi Schulman
akarnat1@binghamton.edu
rschulm4@binghamton.edu
5/2/14
CS110-A55
Chelsea Montgomery'''


class CounterWP:
  
  # --------------------------------------------------------------------------
  # Constructor
  
  def __init__(self):
    self.__value = 0

  # ---------------------------------------------------------------------------
  # Predicates
  
  def isNegative(self):
    return self.__value < 0

  # ---------------------------------------------------------------------------
  # Accessors

  # returns value (int)
  def getValue(self):
    return self.__value
  
  # ---------------------------------------------------------------------------
  # Mutators
  
  def increment(self):
    self.__value += 1

  # Does NOT stop at 0
  def decrement(self):
    self.__value -= 1

  def reset(self):
    self.__value = 0

  # param value (int)
  def set(self, value):
    self.__value = value

  # --------------------------------------------------------------------------
  # toString()
  def __str__(self):
    return str(self.__value)
  

