import csv
def obtener_fichero():
    lista=[]
    with open(r"C:\Users\cetecom\Downloads\calificaciones.csv","r", newline="") as archivo:
        lector_csv=csv.reader(archivo, delimiter=";")
        pos=0
        for linea in lector_csv:
            if pos != 0:
                for i in range(2,len(linea)):
                    if linea[i]=='':
                        linea[i]="0,0"
                apellidos=linea[0]
                nombre=linea[1]
                asistencia=float(linea[2].replace("%",''))
                parcial1=float(linea[3].replace(",",'.'))
                parcial2=float(linea[4].replace(",",'.'))
                ordinario1=float(linea[5].replace(",",'.'))
                ordinario2=float(linea[6].replace(",",'.'))
                practicas=float(linea[7].replace(",",'.'))
                ordinariopractivas=float(linea[8].replace(",",'.'))
                lista.append({
                    "apellidos":apellidos,
                    "nombre":nombre,
                    "asistencia":asistencia,
                    "parcial1":parcial1,
                    "parcial2":parcial2,
                    "ordinario1":ordinario1,
                    "ordinario2":ordinario2,
                    "practicas":practicas,
                    "ordinariopractivas":ordinariopractivas
                })
                print(lista)
            else:
                pos=1
        return lista
obtener_fichero()
    