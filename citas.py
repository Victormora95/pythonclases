def selectespeciality ():
    print("""
        1. Dr. Mendoza: Oculista.
        2. Dr. Mamani: Psicologo.
        3. Dr. Ramirez: Urologo.
        4. Dr. Cardona: Ginecologo
        5. Dr. Lazcano: Otorrinolaringologo.
        6. Dr. Ordonez: Cardiologo.
        """)
    es = input("Seleccione Especialidad")
    return es

class HospitalHANSA:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

        self.nombrePaciente = ""
        self.apellidoPaciente = ""

        self.nombreEspecialista = ""
        self.apellidoEspecialista = ""
        self.especiality = ""

    def iniciarservicio (self, opcion):
        self.opcion = opcion

    def definePaciente (self, nombre, apellido):
        self.nombrePaciente = nombre
        self.apellidoPaciente = apellido

    def definespecialista (self, es):
        if (es == "1"):
            self.especiality = "Oculista."
            self.nombreEspecialista = "Juancito"
            self.apellidoEspecialista = "Mendoza"
        if (es == "2"):
            self.especiality = "Psicologo."
            self.nombreEspecialista = "Luis"
            self.apellidoEspecialista = "Mamani"
        if (es == "3"):
            self.especiality = "Urologo."
            self.nombreEspecialista = "Pedro"
            self.apellidoEspecialista = "Fernandez"
        if (es == "4"):
            self.especiality = "Ginecologo."
            self.nombreEspecialista = "Federico"
            self.apellidoEspecialista = "Cardona"
        if (es == "5"):
            self.especiality = "Otorrinolaringolo."
            self.nombreEspecialista = "Klisman"
            self.apellidoEspecialista = "Lazcano"
        if (es == "6"):
            self.especiality = "Cardiologo."
            self.nombreEspecialista = "Pepe"
            self.apellidoEspecialista = "ordoñez"



hospital = HospitalHANSA("Gerardo", "Lopez") # Instanciando el objeto HospitalHANSA
print("BIENVENIDO AL HOSPITAL HANSA")
nombreCliente = input("Cual es su nombre? ")
apellidoCliente = input("... Y cual su apellido? ")
hospital.definePaciente(nombreCliente, apellidoCliente)

print("""1. Consulta
2. Especialidad
3. Emergencia """)
op = input("Seleccione una Opcion: ")

if (op == "3"):
    print("Por espere un momento, su atencion esta ciendo procesado")
elif (op == "2"):
    hospital.definespecialista(selectespeciality())
    print(f"Señor: {hospital.nombrePaciente} {hospital.apellidoPaciente}")
    print(f"Usted Sera atendido por el {hospital.especiality} Dr. {hospital.apellidoEspecialista} {hospital.nombreEspecialista}")
elif (op == "1"):
    hospital.definespecialista(selectespeciality())
    print(f"Soy el Dr. Gral. {hospital.nombre} {hospital.apellido} por favor...")
    print(f"Cliente: {hospital.nombrePaciente} {hospital.apellidoPaciente}")
    print(f"Usted Sera atendido por el {hospital.especiality}, Dr. {hospital.apellidoEspecialista} {hospital.nombreEspecialista}")
apellidoCliente