# #1
# def hello_function(name):
#   print(f'Hello {name}')
# hello_function('Sabrina')


#2
# import matplotlib
# from matplotlib import pyplot

# def f(x):
#      return x + 1

# xs = list(range(-3, 4))
# ys = []

# for x in xs:
#      ys.append(f(x))

# pyplot.plot(xs, ys)
# pyplot.show()

#3
# import matplotlib
# from matplotlib import pyplot

# def f(x):
#   return x**2

# xs = list(range(-100, 101))
# ys = []

# for x in xs:
#   ys.append(f(x))

# pyplot.plot(xs, ys)
# pyplot.show()



#4
# import matplotlib
# from matplotlib import pyplot

# def f(x):
#   if(x % 2 == 1):
#     return 1
#   else:
#     return -1

# xs = list(range(-5, 6))
# ys = []

# for x in xs:
#   ys.append(f(x))

# pyplot.bar(xs, ys)
# pyplot.show()




#5
# import matplotlib
# from matplotlib import pyplot
# import math
# from math import *

# def f(X):
#   return sin(x)

# xs = list(range(-5, 6))
# ys = []

# for x in xs:
#   ys.append(f(x))

# pyplot.plot(xs, ys)
# pyplot.show()



#6
# import matplotlib
# from matplotlib import pyplot
# import math
# from math import *
# from numpy import arange

# def f(X):
#   return sin(x)

# xs = arange(-5, 6, 0.1)
# ys = []

# for x in xs:
#   ys.append(f(x))

# pyplot.plot(xs, ys)
# pyplot.show()




#7
# import matplotlib
# from matplotlib import pyplot

# def f(x):
#   return x*(9/5) + 32

# xs = list(range(0, 101))
# ys = []

# for x in xs:
#   ys.append(f(x))

# pyplot.plot(xs, ys)
# pyplot.show()




#8
# answer = input('Do you want to play again? Y/N ')

# def play_again(ans):
#   if(ans == 'Y'):
#     return True
#   else:
#     return False

# play_again(answer)




#10
# answer = input('Do you want to play again? Y/N ')

# def play_again(ans):
#   if(ans == 'Y'):
#     print(True)
#   elif(ans == 'N'):
#     print(False)
#   else:
#     print('invalid input')
#     ans = input('Do you want to play again? Y/N ')
#     play_again(ans)

# play_again(answer)
