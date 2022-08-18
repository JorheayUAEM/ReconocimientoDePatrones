#JORGE ALBERTO AYALA HERNANDEZ

class cAutomata:

    #VALORES PARA INTERVALOS Y EQUIVALENTES CODIGO ASCCI
    #INTERVALO A-Z
    (A, Z) = (65, 90)
    #INTERVALO a-z
    (a, z) = (97, 122)
    #INTERVALO 0-9
    (zero, nine) = (48, 57)
    #GUION BAJO
    hyphen = 95
    #ESPACIO
    blankspace = 32

    def __init__(self, path):
        self.path = path


    def show(self):
        alist = [line.rstrip() for line in open(self.path)]
        aux = 1
        for line in alist:
            print(f"{aux}.- {line}")
            aux += 1

        return alist


    def reconoceNV(self):

        lineas = self.show()

        for linea in lineas: 
            estado = 1
            cadena = list(linea)
            i = 0

            while i < len(cadena):
                codigoA = ord(cadena[i])
                if estado == 1:
                    if codigoA in range(self.A, self.Z) or codigoA in range(self.a, self.z):
                        estado = 2
                        i += 1
                    else:
                        estado = 3
                if estado == 2:
                    if codigoA in range(self.A, self.Z) or codigoA in range(self.a, self.z) or codigoA in range(self.zero, self.nine) or codigoA == self.hyphen or codigoA == self.blankspace:
                        estado = 2
                        i += 1
                    else:
                        estado = 3

                if estado == 3: 
                    print(f"NO VALIDA: {linea}")
                    break

            if estado == 2:
                print(f"VALIDA: {linea}")


    def reconoceComent(self):
        lineas = self.show()
        for linea in lineas:
            estado = 1
            cadena = list(linea)
            i = 0
            while i < len(cadena):
                if estado == 1:
                    if cadena[i] == "/":
                        estado = 2 
                        i += 1
                    else:
                        estado = 6
                if estado == 2:
                    if cadena[i] == "*":
                        estado = 3 
                        i += 1
                    else:
                        estado = 6
                if estado == 3:
                    while cadena[i] != "*":
                        i += 1
                        if i + 1 == len(cadena):
                            estado = 6
                            break
                    if i + 1 == len(cadena):
                        estado = 6
                    else:
                        estado = 4
                        i += 1
                if estado == 4:
                    if cadena[i] == "/":
                        estado = 5
                    else:
                        estado = 3
                if estado == 5:
                    break
                if estado == 6:
                    break
            
            if estado == 5:
                print(f"COMENTARIO: {linea}")
            elif estado == 6:
                print(f"NO COMENTARIO: {linea}")
                

    def comment(self):
        lineas = self.show()
        for linea in lineas:
            estado = 1
            while estado != 3:
                if estado == 1:
                    if linea.startswith("/*"):
                        estado = 2
                    else:
                        print(f"NO COMENTARIO: {linea}")
                        estado = 3
                if estado == 2:
                    if linea[-2:] == "*/":
                        print(f"COMENTARIO: {linea}")
                        break
                    else:
                        print(f"NO COMENTARIO: {linea}")
                        estado = 3
            
                

            