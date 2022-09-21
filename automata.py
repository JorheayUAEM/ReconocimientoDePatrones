#JORGE ALBERTO AYALA HERNANDEZ

class cAutomata:

    #VALORES PARA INTERVALOS Y EQUIVALENTES CODIGO ASCCI
    #INTERVALO A-Z
    (A, Z) = (65, 91)
    #INTERVALO a-z
    (a, z) = (97, 123)
    #INTERVALO 0-9
    (zero, nine) = (48, 58)
    #GUION BAJO
    hyphen = 95
    #ESPACIO
    blankspace = 32
    #PALABRAS RESERVADAS
    RESERVADAS = ["if", "else", "for", "while", "string", "int", "as", "double", "main", "False", "True"]

    def __init__(self, path):
        self.path = path


    def show(self):
        return [line.rstrip() for line in open(self.path)]


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
        i = 0
        multilinea = []
        estado = 1
        flag = False
        while i < len(lineas):
            linea = lineas[i]
            aux = 0
            while estado != 3:
                if estado == 5:
                    estado = 2
                    aux = 1
                if estado == 1:
                    if linea.startswith("/*"):
                        estado = 2
                    else:
                        estado = 3
                        break
                if estado == 2:
                    if linea[-2:] == "*/":
                        if aux == 1:
                            estado = 5
                            flag = True
                            break
                        else:
                            estado = 4
                            break
                    else:
                        if i + 1 == len(lineas):
                            estado = 3
                            break
                        else:
                            estado = 5
                            break

            if estado == 3:
                if multilinea:
                    multilinea.append(lineas[i])
                    print("NO COMMENTARIO: ")
                    for line in multilinea:
                        print(line)
                    break
                else:
                    print(f"NO COMENTARIO: {lineas[i]}")
                    i += 1
            if estado == 4:
                print(f"COMENTARIO: {lineas[i]}")
                i += 1
                estado = 1
            if estado == 5:
                multilinea.append(lineas[i])
                i += 1
                if flag:
                    print("COMENTARIO MULTILINEA:")
                    for line in multilinea:
                        print(line)
                    multilinea = []
                    estado = 1
                    flag = False
            

    def commentLine(self, lineas):
        i = 0
        multilinea = []
        estado = 1
        flag = False
        while i < len(lineas):
            linea = lineas[i]
            aux = 0
            while estado != 3:
                if estado == 5:
                    estado = 2
                    aux = 1
                if estado == 1:
                    if linea.startswith("/*"):
                        estado = 2
                    elif linea.startswith("//"):
                        estado = 4
                        break
                    else:
                        estado = 3
                        break
                if estado == 2:
                    if linea[-2:] == "*/":
                        if aux == 1:
                            estado = 5
                            flag = True
                            break
                        else:
                            estado = 4
                            break
                    else:
                        if i + 1 == len(lineas):
                            estado = 3
                            break
                        else:
                            estado = 5
                            break

            if estado == 3:
                if multilinea:
                    multilinea.append(lineas[i])
                    print("NO COMMENTARIO: ")
                    for line in multilinea:
                        print(line)
                    del lineas[0:i+1]
                    return lineas
                else:
                    print(f"NO COMENTARIO: {lineas[i]}")
                    i += 1


            if estado == 4:
                print(f"COMENTARIO: {lineas[i]}")
                del lineas[0]
                return lineas


            if estado == 5:
                multilinea.append(lineas[i])
                i += 1
                if flag:
                    print("COMENTARIO MULTILINEA:")
                    for line in multilinea:
                        print(line)
                    del lineas[0:i]
                    return lineas



    def validaLineas(self, lineas):
        for linea in lineas:
            invalid_line = False
            for palabra in linea.split():
                if palabra in self.RESERVADAS:
                    print(f"PALABRA RESERVADA: {palabra}")
                    continue
                
                is_number = self.is_number(palabra)
                if is_number:
                    print(f"NUMERO: {palabra}")
                    continue

                estado = 1
                cadena = list(palabra)
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
                        print(f"PALABRA NO VALIDA: {palabra}")
                        invalid_line = True
                        break
                            
                    if estado == 2:
                        #print(f"PALABRA VALIDA: {palabra}")
                        pass
            
            if invalid_line:
                print(f"LINEA NO VALIDA: {linea}")
                del lineas[0]
                return lineas
            else:
                print(f"LINEA VALIDA: {linea}")
                del lineas[0]
                return lineas


    def is_number(self, string):
        try: 
            int(string)
            return True
        except ValueError:
            return False


    def automata(self):
        lineas = self.show()
        while lineas:
            if lineas[0].startswith("/*") or lineas[0].startswith("//"):
                lineas = self.commentLine(lineas)
            else:
                lineas = self.validaLineas(lineas)
            
    

            