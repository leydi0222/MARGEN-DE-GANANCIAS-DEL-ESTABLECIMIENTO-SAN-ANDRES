'''el motel san andres necesita realizar el respectivo pago de nominas y saber el margen total de ganancias a 
partir de sus ingresos, egresos y pago de nominas a traves de su libro de cuentas'''
# Clase padre
class LibroCuentas:
    def __init__(self,totalG):
        self.__totalG = totalG#total ganancias privado 

    def get_total_general(self):# ver ganacias 
        return self.__totalG

    def set_total_general(self, nuevo_totalG):# modificar ganacias
        self.__totalG = nuevo_totalG

# Clase hija
class Nomina(LibroCuentas):
    def __init__(self, nombre, totalG, CHE, CHN, CHF, CHFN):
        super().__init__(totalG)# se llama al constructor de la clase padre
        self.nombre = nombre
        self.CHE = CHE
        self.CHN = CHN
        self.CHF = CHF
        self.CHFN = CHFN
        self.H_extra = 6711
        self.H_nocturna = 8479
        self.H_festiva = 10833
        self.H_festiva_nocturna = 13542
        self.Aux_transporte = 162000
        self.smmlv = 1300000


    def calcular_pago(self):
        sueldo = (self.smmlv / 2) + (self.Aux_transporte / 2) + (self.CHE * self.H_extra) + \
                 (self.CHN * self.H_nocturna) + (self.CHF * self.H_festiva) + (self.CHFN * self.H_festiva_nocturna)
        return sueldo

    def nuevo_total(self):
        ganancia_hotel = self.get_total_general() - self.calcular_pago()
        return ganancia_hotel


# Creación del método main(funcionalidad del programa)
def main():
    print("Motel San Andrés")
    ingresos_h = int(input('¿Cuánto dinero ingresó al hotel?\n'))
    egresos_h = int(input('¿Cuánto dinero perdió el hotel en gastos netos del hotel sin nómina?\n'))
    VEntrada=ingresos_h-egresos_h
    
    while True:
        empleado = input('Digite el nombre del empleado:\n')
        h_extras = int(input('Digite la cantidad de horas extras que hizo el empleado:\n'))
        h_extras_nocturnas = int(input('Digite la cantidad de horas extra nocturnas que hizo el empleado:\n'))
        h_extras_festivas = int(input('Digite la cantidad de horas extras festivas que hizo el empleado:\n'))
        h_extras_festivas_nocturnas = int(input('Digite la cantidad de horas extras festivas nocturnas que hizo el empleado:\n'))
        
        # Creación de objetos
        employee = Nomina(nombre=empleado, totalG=VEntrada, CHE=h_extras, CHN=h_extras_nocturnas, CHF=h_extras_festivas, CHFN=h_extras_festivas_nocturnas)

        print(f'Total general actual del hotel: {employee.get_total_general()}')
        print(f"Pago a {empleado}: {employee.calcular_pago()}")
        
        nuevo_total=employee.nuevo_total()
        employee.set_total_general(nuevo_total)
        VEntrada=nuevo_total
        
        # Acabar programa
        confirmacion = input('¿Terminaste con la nómina? (si/no)\n').lower()
        if confirmacion == 'si':
            print(f"El nuevo total de ganancias con nóminas del hotel es: {employee.get_total_general()}")
            break
        elif confirmacion == 'no':
            print('Ok, continúa con el siguiente empleado.')
        else:
            print('Digita una opción válida.')

main()