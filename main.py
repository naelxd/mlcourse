import math

functions = {
        "cos": math.cos,
        "sin": math.sin,
        "exp": math.exp,
        "sqrt": math.sqrt,
        "log": math.log,
        }

def sqrt_der(x):
    return (1/(2 * math.sqrt(x)))

def sin_der(x):
    return math.cos(x)

def cos_der(x):
    return -1 * math.sin(x)

def exp_der(x):
    return math.exp(x)

def log_der(x):
    return 1/x

def pow_der(x, n):
    return n * (x**(n - 1))

def mul_der(x, n):
    return n

def add_der():
    return 0

def grad(f, x):
    tmp = x
    for func in f[:-1]:
        if func in functions:
            tmp = functions[func](tmp)
        else:
            if func[0] == '^':
                tmp = tmp ** int(func[1:])
            elif func[0] == '*':
                tmp = tmp * int(func[1:])
            elif func[0] == '+':
                tmp = tmp + int(func[1:])

    if f[-1] == 'cos':
        deriv = cos_der(tmp)
    elif f[-1] == 'sin':
        deriv = sin_der(tmp)
    elif f[-1] == 'sqrt':
        deriv = sqrt_der(tmp)
    elif f[-1] == 'exp':
        deriv = exp_der(tmp)
    elif f[-1] == 'log':
        deriv = log_der(tmp)
    else:
        if f[-1][0] == '^':
            deriv = pow_der(tmp, int(f[-1][1:]))
        elif f[-1][0] == '*':
            deriv = mul_der(tmp, int(f[-1][1:]))
        elif f[-1][0] == '+':
            deriv = add_der()

    if len(f) == 1:
        return deriv
    return grad(f[:-1], x) * deriv

if __name__ == '__main__':
    f = ["sin", "^2"]
    x = 10
    assert grad(f, x) == 2 * math.sin(x) * math.cos(x)

    f = ["^2", "sin"]
    x = 1.5
    # функция f(x) = sin(x^2)
    assert grad(f, x) == math.cos(x**2) * 2 * x

    f = ["^2", "*3"]
    x = 4
    assert grad(f, x) == 6 * x

    f = ["exp", "^3"]
    x = 2

    # функция f(x) = (e^x)^3
    # производная f'(x) = 3 * (e^x)^2 * e^x = 3 * e^(3x)
    # они очень близко, но из-за ошибки дискретизации выходит ошибка 
    assert grad(f, x) == 3 * math.exp(3 * x)
