#Forma de importar 1
#import Clases.Persona
#Forma de importar 2
from Clases.Persona import *

p = Persona('Ivan','Narvaez')

#Asignar valor usando el metodo SET 
p.nombre = "Dario"

#Llamado al metodo GET usando la funcion PRINT
print(p.nombre)

print(p.apellido)