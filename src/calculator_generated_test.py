import unittest
from src.calculator import Calculator


def func(a, b, c):
    x1 = None
    if b > -3.5 and c > -0.5 and c > 7.5 and a <= -7.5: 
        x1 = -0.0187 * a + 0.0229 * b - 0.0303 * c 
    elif b > -2.5 and c <= -0.5 and c <= -8.5 and a > 7.5: 
        x1 = -0.0193 * a - 0.0232 * b - 0.0297 * c 
    elif b > -1.5 and c <= -0.5 and c > -8.5: 
        x1 = -0.0062 * a - 0.0227 * b - 0.0687 * c 
    elif a <= -4.5 and b <= -3.5 and a <= -11.5: 
        x1 = -0.055 * a + 0.0425 * b - 0.0354 * c 
    elif a <= 3.5 and b > -3.5 and c > -0.5 and c <= 7.5 and b > 7.5: 
        x1 = 0.0001 * a + 0.0003 * b - 0.0007 * c 
    elif a > 3.5 and b <= 3.5 and a > 10.5: 
        x1 = -0.0599 * a - 0.0456 * b - 0.036 * c 
    elif b > -3.5 and c > -0.5 and c > 6.5 and b > 10.5: 
        x1 = -0.0354 * a + 0.0481 * b - 0.0589 * c 
    elif b > -4.5 and c > -0.5 and c <= 7.5 and b > 1.5: 
        x1 = 0.0001 * a + 0.0003 * b - 0.0012 * c 
    elif a > 0 and a > 2.5 and b > -8.5 and b <= 7.5 and a > 4.5: 
        x1 = -0.1467 * a - 0.0848 * b - 0.0586 * c 
    elif a <= -2.5 and b <= -8.5 and a <= -5.5 and a <= -7.5: 
        x1 = -0.2067 * a + 0.0921 * b - 0.0451 * c 
    elif a <= 0 and a <= -2.5 and b > -8.5 and c > 0.5 and c > 7.5: 
        x1 = -0.1917 * a + 0.1021 * b - 0.0532 * c 
    elif a > 2.5 and b > 4.5: 
        x1 = -0.0038 * a - 0.0011 * b - 0.0005 * c 
    elif a > 0 and a > 2.5 and a > 5.5 and b > -17.5: 
        x1 = -0.2332 * a - 0.1058 * b - 0.0518 * c 
    elif a > 0 and a > 2.5 and a > 6.5: 
        x1 = -0.3189 * a - 0.115 * b - 0.0443 * c 
    elif a <= 0 and a <= -2.5 and b <= -8.5 and a <= -4.5 and b <= -17.5: 
        x1 = -0.6162 * a + 0.1706 * b - 0.049 * c 
    elif a <= 0 and b > -4.5 and c <= -6.5: 
        x1 = -0.0018 * a - 0.0775 * b - 0.0714 * c 
    elif a <= 0 and a <= -2.5 and b <= -8.5 and a <= -4.5: 
        x1 = -0.3909 * a + 0.149 * b - 0.0583 * c 
    elif a <= 0 and b <= -8.5 and a <= -1.5 and a <= -2.5 and b > -18.5: 
        x1 = -1.1951 * a + 0.2771 * b - 0.0682 * c 
    elif a <= 0 and b > -8.5 and a <= -3.5 and a > -11.5: 
        x1 = -0.1018 * a + 0.1076 * b - 0.107 * c 
    elif a <= 0 and b > -4.5 and a <= -7.5: 
        x1 = -0.0039 * a + 0.0107 * b - 0.0042 * c 
    elif a > 0 and a > 2.5 and b <= -12.5 and a > 3.5 and a > 4.5: 
        x1 = -0.7363 * a - 0.1899 * b - 0.0506 * c 
    elif a > 0 and b <= -7.5 and a > 1.5 and a > 2.5 and b > -16.5: 
        x1 = -0.8648 * a - 0.253 * b - 0.0697 * c 
    elif a > 0 and b > -7.5 and b <= 10.5 and a > 1.5 and b <= -0.5: 
        x1 = -0.7014 * a - 0.2449 * b - 0.0923 * c 
    elif a > 0 and b > -0.5 and b <= 10.5 and c <= -10.5: 
        x1 = -0.4825 * a - 0.2002 * b - 0.0821 * c 
    elif a > 0 and b > -4.5 and b > 10.5: 
        x1 = -0.0718 * a - 0.0141 * b - 0.0056 * c 
    elif a <= 0 and a <= -1.5 and b <= -8.5 and a > -3.5 and b <= -15.5 and a <= -2.5: 
        x1 = -0.2811 * a + 0.3549 * b - 0.0486 * c 
    elif a <= 0 and b > -8.5 and b > -1.5: 
        x1 = -0.6102 * a + 0.2166 * b - 0.1127 * c 
    elif a > 0 and a > 1.5 and a > 2.5 and a > 3.5: 
        x1 = -0.1151 * a - 0.2218 * b - 0.0512 * c 
    elif a > 0 and a > 1.5 and b <= -13.5 and a > 2.5: 
        x1 = -0.1966 * a - 0.3537 * b - 0.0511 * c 
    elif a <= 0 and a <= -1.5 and b <= -10.5 and a > -3 and b > -18.5: 
        x1 = -0.112 * a + 0.5127 * b - 0.0724 * c 
    elif a <= 0 and a <= -1.5 and b <= -14.5 and a > -3: 
        x1 = -0.1999 * a + 0.4994 * b - 0.0471 * c 
    elif a <= 0 and a <= -1.5 and b <= -8.5: 
        x1 = -0.0357 * a + 0.0864 * b - 0.0559 * c 
    elif a > 0 and b <= -14.5 and a > 1.5 and b > -20.5: 
        x1 = -0.3069 * a - 0.5205 * b - 0.0589 * c 
    elif a > 0 and b > -14.5 and b <= -4.5 and a > 1.5: 
        x1 = -0.3786 * a - 0.4936 * b - 0.0869 * c 
    elif a <= 0 and b > -12.5 and a <= -1.5: 
        x1 = -0.8802 * a + 0.3787 * b - 0.1072 * c 
    elif a <= 0 and b <= -15.5 and b <= -20.5: 
        x1 = 0.1536 * a + 0.9873 * b - 0.0449 * c 
    elif a > 0 and b <= -11.5 and a > 1.5: 
        x1 = -0.6411 * a - 0.5318 * b - 0.0446 * c 
    elif a <= 0 and b <= -12.5 and b <= -16.5: 
        x1 = 0.2116 * a + 0.9773 * b - 0.0556 * c 
    elif a <= 0 and b <= -10.5 and b <= -13.5: 
        x1 = 0.2368 * a + 0.9724 * b - 0.0695 * c 
    elif a > 0 and b <= -13.5 and b <= -19.5 and b <= -22.5: 
        x1 = 0.1044 * a - 0.995 * b - 0.0427 * c 
    elif a > 0 and b <= -12.5 and b > -17.5 and b > -15.5: 
        x1 = 0.1177 * a - 1.0054 * b - 0.0708 * c 
    elif a > 0 and b > -14 and b <= -0.5 and b <= -7.5 and c <= -0.5: 
        x1 = 0.1364 * a - 0.9049 * b - 0.0848 * c 
    elif a <= 0 and b <= -8.5 and b <= -11.5: 
        x1 = 0.2597 * a + 0.9759 * b - 0.0853 * c 
    elif b > -14 and a <= 0 and b <= -6.5 and c > 1.5: 
        x1 = 0.3704 * a + 0.8229 * b - 0.0904 * c 
    elif b <= -14 and b <= -19.5 and b > -21.5: 
        x1 = 0.2699 * a - 0.9957 * b - 0.0472 * c 
    elif b <= -14 and b > -18.5: 
        x1 = 0.3679 * a - 0.9947 * b - 0.0556 * c 
    elif a <= 0 and b > -8.5 and c > 11.5: 
        x1 = 0.3527 * a + 0.6732 * b - 0.1105 * c 
    elif a > 0 and b > -11.5 and b > -0.5 and c <= 4: 
        x1 = -0.0869 * a - 0.226 * b - 0.1784 * c 
    elif a > 0 and b > -15.5 and b <= -2.5 and b > -9.5 and c <= -11.5: 
        x1 = 0.2248 * a - 0.7816 * b - 0.1024 * c 
    elif a > 0 and b <= -15.5 and b <= -20.5: 
        x1 = 0.2584 * a - 0.3177 * b - 0.0463 * c 
    elif a > 0 and b <= -11.5 and b <= -15.5: 
        x1 = 0.2831 * a - 0.3347 * b - 0.0524 * c 
    elif a > 0 and b <= -1.5 and b > -9.5 and b > -5.5 and c <= -4.5: 
        x1 = 0.2966 * a - 0.8049 * b - 0.1375 * c 
    elif a > 0 and b > 2.5: 
        x1 = 0.3311 * a + 0.1357 * b - 0.1464 * c 
    elif a > 0 and b > -9.5 and b <= -5.5 and c > 4.5: 
        x1 = 0.4326 * a - 1.1743 * b - 0.1893 * c 
    elif a > 0 and b > -6.5 and b > -5.5 and c > -14.5: 
        x1 = 0.5394 * a - 0.8849 * b - 0.1931 * c 
    elif a <= 0 and b <= -8.5 and c > -11.5: 
        x1 = 0.5327 * a + 1.0333 * b - 0.116 * c 
    elif a <= 0 and b <= -5.5 and b > -9.5 and c <= -3.5: 
        x1 = 0.6146 * a + 0.8864 * b - 0.1332 * c 
    elif a <= 0 and b > -5.5 and c > 3.5: 
        x1 = 0.7975 * a + 0.5645 * b - 0.0971 * c 
    elif a <= 0 and b > -5.5: 
        x1 = 1.0589 * a + 0.8868 * b - 0.2027 * c 
    elif a > 0 and b <= -8.5 and b <= -11.5: 
        x1 = 0.8172 * a - 0.3683 * b - 0.0716 * c 
    elif a > 0 and b > -8.5 and b <= -3.5 and b <= -6.5: 
        x1 = 0.9649 * a - 0.5089 * b - 0.0323 * c 
    elif a <= 0 and b > -10.5 and b > -7.5: 
        x1 = 1.6701 * a + 0.2716 * b - 0.0303 * c 
    elif a <= 0: 
        x1 = 2.8552 * a + 0.8334 * b - 0.1525 * c 
    elif b <= -7.5 and c <= 14.5 and b <= -10.5 and c > 7.5: 
        x1 = -0.5728 * b - 0.0783 * c 
    elif b <= -7.5: 
        x1 = -0.8925 * b - 0.0903 * c 
    elif b > -3.5 and c <= -19.5: 
        x1 = -0.0212 * c 
    elif b > -3.5: 
        x1 = -0.0301 * c 
    elif c <= -3.5 and c <= -7.5: 
        x1 = -0.1379 * c 
    elif c <= -1.5: 
        x1 = -0.1522 * c 
    return x1


class TestStringMethods(unittest.TestCase):
    pass
