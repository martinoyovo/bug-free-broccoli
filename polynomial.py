from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, a, b, c):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        self.a = self.a + other.a
        self.b = self.b + other.b
        self.c = self.c + other.c
        return self

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        self.a = self.a - other.a
        self.b = self.b - other.b
        self.c = self.c - other.c
        return self

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        return "{}X^2{:+}X{:+}".format(self.c,self.b,self.a)

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        a = self.c
        b = self.b
        c = self.a

        dis = b * b - 4 * a * c 
        sqrt_val = sqrt(dis)
        
        # checking condition for discriminant
        if dis > 0: 
            x1 = (-b - sqrt_val) /(2*a)
            x2 = (-b + sqrt_val) /(2*a)
            return x1, x2
      
        
        elif dis == 0: 
            return f"{-b / (2 * a)}"
        
        # when discriminant is less than 0
        else:
            x1 = (-b - sqrt_val) /(2*a)
            x2 = (-b + sqrt_val) /(2*a)
            return x1, x2
    


    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        return x*x+1
        

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        
    
        # La courbe
        plt.plot(self.a, self.b, self.c)

        # Les axes
        plt.axvline(x=0, color ='r')
        plt.axhline(y=0, color ='r')   
        axes = plt.gca()
        axes.set_xlabel('x : abscisse')
        axes.set_ylabel('f(x) : ordonnée')

        plt.show()

if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)
    
    baz = [1, 1, 1]
    p2 = Poly2(*baz)
    
    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png