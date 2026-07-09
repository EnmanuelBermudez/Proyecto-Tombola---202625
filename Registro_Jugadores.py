import struct
import datetime
import pygame

def Registro_Jugadores():
    Formato_Registro = '8s30s1s10s3s30s'
    Tamaño_Registro = struct.calcsize(Formato_Registro)
    FR_Estados = '20s3s'
    TR_Estados = struct.calcsize(FR_Estados)

    AF_REGJugadores = "REG_JUGADORES.bin"
    REG_Jugadores = open(AF_REGJugadores, 'wb')
    AF_Estados = "Estados.bin"
    Estados = open(AF_Estados, 'rb')

    EOF = False

    Respuesta = "S" #Cambiar a Booleano despues.
    while (Respuesta == 'S' or Respuesta == 's'):
        CedulaJugador = str(input("Ingrese su Cedula: "))
        NombreJugador = str(input("Ingrese su Nombre de Usuario: "))
        SexoJugador = str(input("Ingrese su Sexo: "))
        FechaJugador = str(input("Ingrese su Fecha y Año de Nacimiento [dd-mm-aaaa]: "))
        
        while (FechaJugador[2] != '-') and (FechaJugador[5] != '-'):
            FechaJugador = str(input("ERROR: La fecha de nacimiento ha sido colocada erroneamente. Intente nuevamente: "))
        
        InicialEstJugador = str(input("Ingrese las inicialiales de su estado de nacimiento: "))
        
        EstEncontrado = False

        while (EstEncontrado == False):
            Estados.seek(0)
            EOF = False
            while (EOF == False) and (EstEncontrado == False):
                BytesEstados = Estados.read(TR_Estados)

                if (BytesEstados):
                    NombreEstCodificado, InicialEstCodificado = struct.unpack(BytesEstados)
                    NombreEstado = NombreEstCodificado.decode('utf-8').strip()
                    InicialEstado = InicialEstCodificado.decode('utf-8').strip()

                    if (InicialEstJugador == InicialEstado):
                        EstadoJugador = NombreEstado
                else:
                    EOF = True

            if (EstEncontrado == False):
                InicialEstJugador = input("ERROR: La inicial de estado colocada no existe. Intente nuevamente: ")
        
        ClaveJugador = str(input("Ingrese su clave: "))

        CedulaCodificada = CedulaJugador.ljust(8).encode('utf-8')
        NombreCodificado = NombreJugador.ljust(30).encode('utf-8')
        SexoCodificado = SexoJugador.ljust(1).encode('utf-8')
        FechaCodificada = FechaJugador.ljust(10).encode('utf-8')
        InicialCodificada = InicialEstado.ljust(3).encode('utf-8')
        EstadoCodificado = EstadoJugador.ljust(20).encode('utf-8')
        ClaveCodificada = ClaveJugador.ljust(30).encode('utf-8')

        Registro_Binario = struct.pack(Formato_Registro, CedulaCodificada, NombreCodificado, SexoCodificado, FechaCodificada, InicialCodificada, EstadoCodificado, ClaveCodificada)
        REG_Jugadores.write(Registro_Binario)

        print("="*5 + f"El usuario [{NombreJugador}] ha sido registrado exitosamente." + "="*5)
        print("\n")

        Respuesta = input("¿Desea registrar otro usuario? [S/N]: ")
        