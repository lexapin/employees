import math
import copy
import threading


m_16 = (5, 7, 11, 13, 17)
m_32 = (7, 11, 13, 17, 19, 23, 29, 31)


class DigitConvert(threading.Thread):
  """docstring for DigitConvert"""
  def __init__(self, multiply, base):
    super(DigitConvert, self).__init__()
    self.multiply = multiply
    self.base = base
  
  def run(self):
    M = int(self.multiply/self.base)
    b = self.equation(M, self.base, 1)
    self.result = M*b

  def equation(self, number, modal, residue):
    eq_lambda = lambda b: number*b-residue
    digit = 1
    while eq_lambda(digit)%modal!=0:
      digit+=1
    return digit


class SetDigit(threading.Thread):
  """docstring for SetDigit"""
  def __init__(self, digit, base):
    super(SetDigit, self).__init__()
    self.digit = digit
    self.base = base

  def run(self):
    self.result = self.digit%self.base


class GetDigit(threading.Thread):
  """docstring for GetDigit"""
  def __init__(self, digit_1, digit_2):
    super(GetDigit, self).__init__()
    self.digit_1 = digit_1
    self.digit_2 = digit_2

  def run(self):
    self.result=self.digit_1*self.digit_2


class MultiplyDigits(threading.Thread):
  """docstring for MultiplyDigits"""
  def __init__(self, digit_1, digit_2, base):
    super(MultiplyDigits, self).__init__()
    self.digit_1 = digit_1
    self.digit_2 = digit_2
    self.base = base
  
  def run(self):
    self.result = (self.digit_1*self.digit_2)%self.base


class AddDigits(threading.Thread):
  """docstring for AddDigits"""
  def __init__(self, digit_1, digit_2, base):
    super(AddDigits, self).__init__()
    self.digit_1 = digit_1
    self.digit_2 = digit_2
    self.base = base
  
  def run(self):
    self.result = (self.digit_1+self.digit_2)%self.base


class ModularDigit(object):
  """docstring for ModularDigit"""
  def __init__(self, base):
    super(ModularDigit, self).__init__()
    self.base = base
    self.convert = self.get_converter()
    self.digit = None

  def get_converter(self):
    self.multiply = 1
    for number in self.base: self.multiply*=number
    objects = []
    for number in self.base:
      DC = DigitConvert(self.multiply, number)
      DC.start()
      objects.append(DC)
    for dc in objects:
      dc.join()
    return tuple(dc.result for dc in objects)

  def set(self, digit):
    objects=[]
    for number in self.base:
      SD = SetDigit(digit, number)
      SD.start()
      objects.append(SD)
    for sd in objects:
      sd.join()
    self.digit = tuple(sd.result for sd in objects)
    # self.digit = tuple(digit%iter_base for iter_base in self.base)

  def get(self):
    objects=[]
    for i in range(len(self.base)):
      GD = GetDigit(self.digit[i], self.convert[i])
      GD.start()
      objects.append(GD)
    for gd in objects:
      gd.join()
    return sum(gd.result for gd in objects)%self.multiply

  def __mul__(self, other):
    if not isinstance(other, ModularDigit):
      return None
    if self.base!=other.base:
      return None
    objects = []
    for i in range(len(self.base)):
      MD = MultiplyDigits(self.digit[i], other.digit[i], self.base[i])
      MD.start()
      objects.append(MD)
    for md in objects:
      md.join()
    result = ModularDigit(self.base)
    result.digit = tuple(md.result for md in objects)
    return result

  def __add__(self, other):
    if not isinstance(other, ModularDigit):
      return None
    if self.base!=other.base:
      return None
    objects = []
    for i in range(len(self.base)):
      AD = AddDigits(self.digit[i], other.digit[i], self.base[i])
      AD.start()
      objects.append(AD)
    for ad in objects:
      ad.join()
    result = ModularDigit(self.base)
    result.digit = tuple(ad.result for ad in objects)
    return result


if __name__=="__main__":
  a = 123
  b = 256
  md = ModularDigit(m_16)
  md.set(a)
  print(md.get())
  ms = ModularDigit(m_16)
  ms.set(b)
  print(ms.get())
  print((md*ms).get(), a*b)
  print((md+ms).get(), a+b)
  import time
  t_s = time.time()
  for i in range(1000):
    a*b
    a+b
  print('t:',time.time()-t_s)
  t_s = time.time()
  for i in range(1000):
    md*ms
    md+ms
  print('t:',time.time()-t_s)