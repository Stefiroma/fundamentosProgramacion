def derivative(x):
    h = 0.0001  # valor cercano a cero
    y = (4*(x+h)*2 + 5(x+h)) / h
    y_0 = (4*x**2 + 5*x) / h
    return (y - y_0) / h

def lim_derivative(x):
    return 8*x + 5

x = 2 # valor de x en el cual se evalúa la derivada
print("Derivada aproximada:", derivative(x)) # output: 16.00010000002709
print("Límite de la derivada:", lim_derivative(x)) # output: 21

