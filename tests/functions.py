import math

def arsh_math(x):
  return math.asinh(x)


def arsh_log(x):
  return math.log(x+math.sqrt(x*x+1))


def fact(n):
  a = (-1)**n*math.factorial(2*n)
  b = 2**(2*n)*(math.factorial(n))**2
  c = 2*n+1
  return float(a)/float(b)/float(c)


def arsh_t(x, accuracy=0.00000001, max_itertions=100):
  get_value = lambda n: float(x**(2*n+1))*fact(n)
  try:
    if math.fabs(x)>=1.0: raise ValueError
    i = 0
    t_sum = 0
    while True:
      old_sum = t_sum
      value = get_value(i)
      i+=1
      t_sum+=value
      if math.fabs(t_sum-old_sum)<accuracy: break
      if i>max_itertions: raise StopIteration
  except OverflowError as err:
    result = {
              'result': False,
              'value': None,
              'iteration': i,
              'error': err
           }
  except StopIteration as err:
    result = {
              'result': False,
              'value': t_sum,
              'iteration': i,
              'error': err
           }
  except ValueError as err:
    result = {
              'result': False,
              'value': None,
              'iteration': -1,
              'error': err
           }
  else:
    result = {
              'result': True,
              'value': t_sum,
              'iteration': i,
              'error': None
           }
  finally:
    return result

digits = [
            0.001,
            0.01,
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.7,
            0.8,
            0.89,
            0.9,
            0.91,
            0.95,
            0.98,
            0.99,
            0.999,
            1.0,
            1.0001,
            1.01,
            1.1
          ]
print(arsh_math(0.754378))
print(arsh_log(0.754378))
for digit in digits:
  print(digit, arsh_t(digit))