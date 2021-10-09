class Rational:
    def __init__(self,sz,n):
        self.sz=sz
        self.n=n

    def __str__(self):
        return "Tört: {}/{}".format(self.sz,self.n)

    def __mul__(self, other):
        if isinstance(other,Rational):
            ujsz=self.sz*other.sz
            ujn=self.n*other.n
            if ujsz!=0:
                return "Szorzat: {}/{}".format(ujsz,ujn)
            else:
                return "Szorzat: 0"

    def __add__(self, other):
        if isinstance(other, Rational):
            sz1=other.n*self.sz
            sz2=other.sz*self.n
            ujn = other.n * self.n
            ujsz= sz1+sz2
            if ujsz != 0:
                return "Összeg: {}/{}".format(ujsz, ujn)
            else:
                return "Összeg: 0"

    def __sub__(self, other):
        if isinstance(other, Rational):
            sz1=other.n*self.sz
            sz2=other.sz*self.n
            ujn = other.n * self.n
            ujsz= sz1-sz2
            if ujsz != 0:
                return "Különbség: {}/{}".format(ujsz, ujn)
            else:
                return "Különbség: 0"

    def __truediv__(self, other):
        if isinstance(other,Rational):
            ujsz=self.sz*other.n
            ujn=self.n*other.sz
            if ujsz != 0:
                return "Hányados: {}/{}".format(ujsz,ujn)
            else:
                return "Hányados: 0"

    def __eq__(self, other):
        if isinstance(other, Rational):
            if (self.sz/self.n)==(other.sz/other.n):
                return "Igaz"
            else:
                return "Hamis"

    def __gt__(self, other):
        if isinstance(other, Rational):
            if (self.sz/self.n)>(other.sz/other.n):
                return "Igaz"
            else:
                return "Hamis"

    def __ge__(self, other):
        if isinstance(other, Rational):
            if (self.sz / self.n) >= (other.sz / other.n):
                return "Igaz"
            else:
                return "Hamis"

    def __lt__(self, other):
        if isinstance(other, Rational):
            if (self.sz / self.n) < (other.sz / other.n):
                return "Igaz"
            else:
                return "Hamis"

    def __le__(self, other):
        if isinstance(other, Rational):
            if (self.sz / self.n) <= (other.sz / other.n):
                return "Igaz"
            else:
                return "Hamis"

    def __ne__(self, other):
        if isinstance(other, Rational):
            if (self.sz / self.n) != (other.sz / other.n):
                return "Igaz"
            else:
                return "Hamis"


t1=Rational(1,2)
t2=Rational(1,4)
# print(t1)
# print(t1*t2)
print(t1+t2)
print(t1>t2)
