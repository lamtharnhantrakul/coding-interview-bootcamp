import sys
"""
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("not the right value mannnn")
except:
    print("Unexpected error")
"""

try:
    spam = 89
    print(spam)
except NameError:
    print("spam was not defined")
except:
    print("not really sure what happened")
else:
    print("function executed successfully")
