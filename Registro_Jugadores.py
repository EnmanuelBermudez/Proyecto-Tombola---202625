import struct
import datetime

def Registro_Jugadores(Cedula, Nombre, Sexo, Fecha, InicialEstado, NombreEstado, Clave):
    Formato_Registro = '8s30s1s10s3s20s30s'
    Tamaño_Registro = struct.calcsize(Formato_Registro)
    FR_Estados = '20s3s'
    TR_Estados = struct.calcsize(FR_Estados)

    AF_JUGADORES = "JUGADORES.bin"
    JUGADORES = open(AF_JUGADORES, 'ab')
    AF_ESTADOS = "ESTADOS.bin"
    ESTADOS = open(AF_ESTADOS, 'rb')

    EOF = False
        
    while (len(Fecha) > 10) or (Fecha[2] != '-' and Fecha[2] != '/') or (Fecha[5] != '-' and Fecha[5] != '/'):
        Fecha = str(input("ERROR: La fecha de nacimiento ha sido colocada erroneamente. Intente nuevamente: "))
    
    EstEncontrado = False

    while (EstEncontrado == False):
        ESTADOS.seek(0)
        EOF = False
        while (EOF == False) and (EstEncontrado == False):
            BytesEstados = ESTADOS.read(TR_Estados)
            if (BytesEstados):
                NombreEstCodificado, InicialEstCodificado = struct.unpack(FR_Estados, BytesEstados)
                NombreEstExistente = NombreEstCodificado.decode('utf-8').strip()
                InicialEstExistente = InicialEstCodificado.decode('utf-8').strip()

                if (InicialEstado == InicialEstExistente):
                    NombreEstado = NombreEstExistente
                    EstEncontrado = True
            else:
                EOF = True

        if (EstEncontrado == False):
            InicialEstado = input("ERROR: La inicial de estado colocada no existe. Intente nuevamente: ")
    
    CedulaCodificada = Cedula.ljust(8).encode('utf-8')
    NombreCodificado = Nombre.ljust(30).encode('utf-8')
    SexoCodificado = Sexo.ljust(1).encode('utf-8')
    FechaCodificada = Fecha.ljust(10).encode('utf-8')
    InicialCodificada = InicialEstado.ljust(3).encode('utf-8')
    EstadoCodificado = NombreEstado.ljust(20).encode('utf-8')
    ClaveCodificada = Clave.ljust(30).encode('utf-8')

    Registro_Binario = struct.pack(Formato_Registro, CedulaCodificada, NombreCodificado, SexoCodificado, FechaCodificada, InicialCodificada, EstadoCodificado, ClaveCodificada)
    JUGADORES.write(Registro_Binario)

    print("="*5 + f"El usuario [{Nombre}] ha sido registrado exitosamente." + "="*5)
    print("\n")

    JUGADORES.close()
    ESTADOS.close()


def main():
    Respuesta = "S"
    while (Respuesta == 'S' or Respuesta == 's'):
        Cedula = str(input("Ingrese su Cedula: "))
        Nombre = str(input("Ingrese su Nombre de Usuario: "))
        Sexo = str(input("Ingrese su Sexo: "))
        Fecha = str(input("Ingrese su Fecha y Año de Nacimiento [dd-mm-aaaa]: "))
        InicialEstado = str(input("Ingrese las inicialiales de su estado de nacimiento: "))
        Clave = str(input("Ingrese su clave: "))

        Registro_Jugadores(Cedula, Nombre, Sexo, Fecha, InicialEstado, Clave)

        Respuesta = input("¿Desea registrar otro usuario? [S/N]: ")

if __name__ == "__main__":
    main()
