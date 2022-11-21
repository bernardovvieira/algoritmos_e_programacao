# Importar todo o módulo (utiliza-se prefixo)
import math

a = math.pi
print(a)

# Importar apenas uma função do módulo (o prefixo não é necessário)
from math import pi

b = pi
print(b)

# Importar todo o módulo com apelido (utiliza-se o apelido como prefixo)
import math as m

c = m.pi
print(c)
