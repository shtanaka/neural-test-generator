import os
import errno

from src.calculator import Calculator
from random import randint


def generate_data():
    calc = Calculator()
    with open('datasetx1.arff', 'a') as filex1:
        with open('datasetx2.arff', 'a') as filex2:
            filex1.write('@relation eq_segundo_grau_x1\n\n')
            filex1.write('@attribute a NUMERIC\n')
            filex1.write('@attribute b NUMERIC\n')
            filex1.write('@attribute c NUMERIC\n')
            filex1.write('@attribute x1 NUMERIC\n\n')
            filex1.write('@data\n')
            filex2.write('@relation eq_segundo_grau_x2\n\n')
            filex2.write('@attribute a NUMERIC\n')
            filex2.write('@attribute b NUMERIC\n')
            filex2.write('@attribute c NUMERIC\n')
            filex2.write('@attribute x2 NUMERIC\n\n')
            filex2.write('@data\n')
            for i in range(0, 1000000):
                a = 0
                while a is 0:
                    a = randint(-100, 100)
                b = randint(-100, 100)
                c = randint(-100, 100)
                xs = calc.resolve_eq(a, b, c)
                if xs[0] is not "nr":
                    filex1.write(str(a) + ', ' + str(b) + ', ' + str(c)
                                 + ', ' + str(xs[0]) + '\n')
                    filex2.write(str(a) + ', ' + str(b) + ', ' + str(c)
                                 + ', ' + str(xs[1]) + '\n')

def generate_file_path(filePath):
    if not os.path.exists(os.path.dirname(filePath)):
        try:
            os.makedirs(os.path.dirname(filePath))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def generate_controlled_data():
    calc = Calculator()
    file_path = 'data/eq2/'
    generate_file_path(file_path)
    with open(file_path + 'datasetx1.arff', 'a') as filex1:
        with open(file_path + 'datasetx2.arff', 'a') as filex2:
            filex1.write('@relation eq_segundo_grau_x1\n\n')
            filex1.write('@attribute a NUMERIC\n')
            filex1.write('@attribute b NUMERIC\n')
            filex1.write('@attribute c NUMERIC\n')
            filex1.write('@attribute x1 NUMERIC\n\n')
            filex1.write('@data\n')
            filex2.write('@relation eq_segundo_grau_x2\n\n')
            filex2.write('@attribute a NUMERIC\n')
            filex2.write('@attribute b NUMERIC\n')
            filex2.write('@attribute c NUMERIC\n')
            filex2.write('@attribute x2 NUMERIC\n\n')
            filex2.write('@data\n')
            for i in range(-25, 25):
                for j in range(-25, 25):
                    for k in range(-25, 25):
                        if i is not 0:
                            a = i
                            b = j
                            c = k
                            xs = calc.resolve_eq(a, b, c)
                            if xs[0] is not "nr":
                                filex1.write(str(a) + ', ' + str(b) + ', ' + str(c)
                                             + ', ' + str(xs[0]) + '\n')
                                filex2.write(str(a) + ', ' + str(b) + ', ' + str(c)
                                             + ', ' + str(xs[1]) + '\n')


def generate_logarithm_data():
    calc = Calculator()
    file_path = 'data/log/'
    generate_file_path(file_path)
    with open(file_path + 'datasetlog.arff', 'a') as filelog:
        filelog.write('@relation logaritmo\n\n')
        filelog.write('@attribute base NUMERIC\n')
        filelog.write('@attribute num NUMERIC\n')
        filelog.write('@attribute x NUMERIC\n\n')
        filelog.write('@data\n')
        for i in range(2, 64):
            for j in range(1, 1000):
                a = i
                b = j
                x = calc.resolve_log(a, b)
                filelog.write(str(a) + ', ' + str(b) + ', ' + str(x) + '\n')
