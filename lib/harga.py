
class upahpemborong:
  def add(self, x, p, l):
        return x*(p*l*1000000)

class materialbawah:
  def add(self, x, p, l):
        return x*(p*l*3000000)

class materialatapprisma:
  def add(self, p, l, t):
        return ((2*p*l)+(2*1/2*l*t))*500000

class materialatapkerucut:
  def add(self, r, s):
        return (22/7*r*s)*500000

class materialatapsetengahbola:
  def add(self, r):
        return (1/2*4*22/7*r*r)*500000

class totalprisma:
  def add(self, x, p, l, t):
        return (x*(p*l*1000000))+(x*(p*l*3000000))+(((2*p*l)+(2*1/2*l*t))*500000)

class totalkerucut:
  def add(self, x, p, l, r, s):
        return (x*(p*l*1000000))+(x*(p*l*3000000))+((22/7*r*s)*500000)

class totalsetengahbola:
  def add(self, x, p, l, r):
        return (x*(p*l*1000000))+(x*(p*l*3000000))+((1/2*4*22/7*r*r)*500000)