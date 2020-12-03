class Paciente:
   def __init__(self,nombre, apellido):
       self.nombre = nombre
       self.apellido = apellido
   def saludar(self):
       return f"hola mi nombre es  {self.nombre} {self.apellido}"
class Doctor:
   def saludardoctor(self,especialidad):
       return f"hola mi nombre es  {self.nombre} {self.apellido} y mi especialidad es {self.especialidad}"
print("BIENVENIDOS AL HOSPITAL HANSA")
print("""

1.RESERVAR CITA
2.ESPECIALIDADES
3.EMERGEGENCIAS


""")
usuario = input("ingrese su eleccion -> ")
if (usuario == "1"):
   print("""
   SELECCIONE SU DOCTOR
   1.DR.SALAS
   2.DR.DURAN
   
    """)
   doc = input("medico-> ")
   if (doc == "1"):
       diego = Doctor("diego","Salas","medico general")
       print(diego.saludardoctor())
   if (doc == "2")
       tania = Doctor("Marco","Duran","medico general")
       print(tania.saludardoctor("cuido a los pacientes"))


if (usuario == "2"):
