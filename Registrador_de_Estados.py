# Registrador de Estados
import struct

Formato_Registro = '20s3s'
Tamaño_Registro = struct.calcsize(Formato_Registro)

Archivo_Fisico = "Estados.bin"
Estados = open(Archivo_Fisico, 'wb')

Respuesta = "S"
while (Respuesta == "S"):
    NombreEstado = str(input("Ingrese el Nombre de su Estado: "))
    InicialEstado = str(input("Ingrese las Iniciales de su Estado: "))

    NombreCodificado = NombreEstado.ljust(20).encode('utf-8')
    InicialCodificado = InicialEstado.ljust(3).encode('utf-8')

    Registro_Binario = struct.pack(Formato_Registro, NombreCodificado, InicialCodificado)
    Estados.write(Registro_Binario)

    print(f"El estado {NombreEstado} con las iniciales '{InicialEstado}' ha sido registrado.")

    Respuesta = str(input("¿Desea ingresar otro estado? [S/N]: "))
    print("\n")

print("Estados.bin HA SIDO CREADO.")

