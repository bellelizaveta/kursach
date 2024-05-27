import sympy
import time

def is_irreducible(poly):
    """Проверка, является ли многочлен неприводимым над полем GF(2)"""
    x = sympy.symbols('x')
    poly = sympy.Poly(poly, x, modulus=2)
    return sympy.ntheory.isprime(sympy.degree(poly))

def is_primitive(poly, n):
    """Проверка, является ли многочлен примитивным над полем GF(2)"""
    x = sympy.symbols('x')
    poly = sympy.Poly(poly, x, modulus=2)
    order = 2**n - 1
    field = sympy.GF(2)
    
    for d in sympy.divisors(order):
        if d == order:
            continue
        test_poly = x**d - 1
        gcd = sympy.gcd(sympy.Poly(test_poly, x, modulus=2), poly)
        if not gcd.is_one:
            return False
    return True

def generate_primitive_polynomials(n):
    """Генерация примитивных многочленов степени n"""
    x = sympy.symbols('x')
    primitive_polynomials = []
    
    for coeff in range(2**n, 2**(n+1)):
        binary_coeff = [int(bit) for bit in bin(coeff)[2:].zfill(n + 1)]
        poly = sympy.Poly(binary_coeff, x, modulus=2)
        if is_irreducible(poly) and is_primitive(poly, n):
            primitive_polynomials.append(poly)
    
    return primitive_polynomials

start = time.time()
if __name__ == "__main__":
    degree = 5
    prim_polys = generate_primitive_polynomials(degree)
    for poly in prim_polys:
        print("Примитивный многочлен:", poly)
finish = time.time()
res = finish - start
print ('Время работы в секундах:', res)