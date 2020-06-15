import random


# VALIDACIONES
def validacion_de_dominio():
    cont_error = cont_letra = cont_puntos = cont_arroba = 0
    bandera = banderaP = tiene_punto = False
    banderaA = True

    texto = input("INGRESE EL DOMINIO DE SU CUENTA:")
    texto = texto.lower()
    banderaA = comprobar_si_hay_arroba_texto(texto, cont_letra, banderaA, cont_arroba)
    bandera = comprobar_punto_y_arroba_inicio_final(texto, cont_letra, bandera)
    banderaP = comprobar_dos_punto_seguido(texto, cont_letra, banderaP, tiene_punto, cont_puntos)
    while texto == "" or bandera or banderaP or banderaA:
        cont_error += 1
        if cont_error < 3:
            print('EL DOMINIO INGRESADO ES INVALIDO VUELVA A INGRESAR')
            texto = input()
            bandera = banderaP = banderaA = False
            banderaA = comprobar_si_hay_arroba_texto(texto, cont_letra, banderaA, cont_arroba)
            bandera = comprobar_punto_y_arroba_inicio_final(texto, cont_letra, bandera)
            banderaP = comprobar_dos_punto_seguido(texto, cont_letra, banderaP, tiene_punto, cont_puntos)
        elif cont_error == 3:
            print("A SUPERADO LA CANTIDAD DE INTENTOS FALLIDOS ...GRACIAS ,LO ESPERAMOS DE NUEVO")
            exit()
    return texto


def comprobar_punto_y_arroba_inicio_final(texto, cont_letra, bandera):
    for usuario in texto:
        cont_letra += 1
        if cont_letra == 1 and (usuario == '.' or usuario == '@'):
            bandera = True

        if (usuario == '.' or usuario == '@') and cont_letra == len(texto):
            bandera = True

    return bandera


def comprobar_dos_punto_seguido(texto, cont_letra, banderaP, tiene_punto, cont_puntos):
    for usuario in texto:
        cont_letra += 1
        if usuario == '.':
            cont_puntos += 1
            if cont_puntos == 1:
                tiene_punto = True
            else:
                if tiene_punto and usuario == '.':
                    banderaP = True
                    tiene_punto = False

    return banderaP


def comprobar_si_hay_arroba_texto(texto, cont_letra, banderaA, cont_arroba):
    for usuario in texto:
        cont_letra += 1
        if cont_letra > 3:
            if usuario == '@':
                cont_arroba += 1
                if cont_arroba == 1:
                    banderaA = False
                else:
                    banderaA = True
    return banderaA


def validacion_de_cantidad_pacientes():
    print('INGRESE LA CANTIDAD DE PACIENTES A PROCESAR:')
    cantidad_de_pacientes = int(input())
    while cantidad_de_pacientes <= 0:
        print('ERROR!!! EL NUMERO DEBE SER MAYOR QUE "0"')
        print('VUELVA A INGRESAR LA  CANTIDAD DE PACIENTES A PROCESAR:')
        cantidad_de_pacientes = int(input())
    return cantidad_de_pacientes


def validacion_opcion(lim_inferior, lim_superior, mensaje):
    option = int(input(mensaje))
    while option < lim_inferior or option > lim_superior:
        print(
            'ERROR:EL  NUMERO DEBE ESTAR ENRE ' + str(lim_inferior) + 'y' + str(lim_superior) + ',VUELVA A INTENTARLO.')
        option = int(input(mensaje))
    return option


# ----------------------------------------------------------------------------------------------------------------------#
# INGRESO DE DATOS
def ingreso_datos(cantidad_de_pacientes):
    # contadores
    cont_pos = cont_edad = cont_aut = con_conf = cont_personal_salud = cont_casos_confirmados = cont_autoctonos = \
        cont_negativo = cont_exterior = cont_region_c = cont_region_gc = cont_region_n = cont_region_s = cont_positivos = cont_positi = 0
    cont_region_nc = cont_region_ngc = cont_region_nn = cont_region_ns = 0
    # acumuladores

    suma_edad = suma_edad_confirmado = 0
    # porcentaje y promedios

    porcentaje_salud = promedio = promedio_edad = porcentaje_autoctonos = porcentaje_c \
        = porcentaje_gc = porcentaje_n = porcentaje_s = 0
    consultas = " "
    menor = 0

    print('MUESTRA DE PACIENTES')
    for paciente in range(cantidad_de_pacientes):

        print('*' * 80)
        edad = random.randint(65, 95)
        resultado_test = ["positivo", "negativo"]
        resultado = random.choice(resultado_test)
        region = ["Capital", "Gran Córdoba", "Norte", "Sur"]
        regionPrincipal = random.choice(region)
        confirmado = ["si", "no"]
        caso_confirmado = random.choice(confirmado)
        personal_salud = random.choice(confirmado)
        viajo_al_exterior = random.choice(confirmado)
        if resultado == "positivo" and caso_confirmado == "no" and personal_salud == "no" and viajo_al_exterior == "no":
            mensaje = "SI"
        else:
            mensaje = "NO"

        print('Paciente N° :', paciente + 1)
        print("Edad :", edad)
        print("Resultado del test :", resultado)
        print("Region :", regionPrincipal)
        print("Estuvo en contacto con casos confirmados ?", caso_confirmado)
        print("Es  personal de salud ?", personal_salud)
        print("viajo al exterior ?", viajo_al_exterior)
        print("Es Autóctono :", mensaje)

        # OPCION 1
        cont_pos, porcentaje_confirmados = cantidad_casos_confirmados_porcentaje(resultado,
                                                                                 cantidad_de_pacientes,
                                                                                 cont_pos)
        # OPCION 2
        promedio, cont_edad, suma_edad = edad_promedio_paciente_grupo_riesgo(resultado, edad, cont_edad, suma_edad,
                                                                             promedio)
        # OPCION 3
        porcentaje_salud, cont_personal_salud = cantidad_porcentaje_personas_salud(personal_salud,
                                                                                   cantidad_de_pacientes,
                                                                                   cont_personal_salud)
        # OPCION 4
        promedio_edad, cont_casos_confirmados, suma_edad_confirmado = edad_promedio_entre_casos_confirmados(
            resultado, edad, cont_casos_confirmados, suma_edad_confirmado, promedio_edad)

        # OPCION 5
        menor, cont_aut = menor_edad_entre_casos_autoctonos(mensaje, edad, cont_aut, menor)

        # OPCION 6
        cont_region_c, cont_region_gc, cont_region_n, cont_region_s, cont_positivos, porcentaje_c, porcentaje_gc, porcentaje_n, porcentaje_s = cantidad_porcentaje_casos_confirmados_region(
            resultado, cont_positivos, regionPrincipal, cont_region_c, cont_region_gc, cont_region_n, cont_region_s,
            porcentaje_c, porcentaje_gc, porcentaje_n, porcentaje_s)

        # OPCION 7
        cont_exterior = cantidad_de_casos_confirmados_con_viaje_exterior(resultado, viajo_al_exterior, cont_exterior)

        # OPCION 8
        con_conf = cantidad_sospechosos_en_contacto_casos_confirmados(caso_confirmado, con_conf)

        # OPCION 9
        cont_region_nc, cont_region_ngc, cont_region_nn, cont_region_ns, cont_negativo = regiones_sin_casos_confirmados(
            resultado,
            cont_negativo,
            regionPrincipal,
            cont_region_nc,
            cont_region_ngc,
            cont_region_nn,
            cont_region_ns)

        # OPCION 10
        porcentaje_autoctonos, cont_autoctonos, cont_positi = porcentaje_casos_positivos_autoctonos(resultado, mensaje,
                                                                                                    cont_positi,
                                                                                                    cont_autoctonos,
                                                                                                    porcentaje_autoctonos)

        consultas = [cont_pos, porcentaje_confirmados, promedio, porcentaje_salud, cont_personal_salud,
                     promedio_edad, menor, cont_region_c, cont_region_gc, cont_region_n, cont_region_s, porcentaje_c,
                     porcentaje_gc, porcentaje_n, porcentaje_s, cont_positivos, cont_exterior, con_conf,
                     cont_region_nc, cont_region_ngc, cont_region_nn, cont_region_ns,
                     porcentaje_autoctonos
                     ]
    return consultas


# ----------------------------------------------------------------------------------------------------------------------#

# OPCION 1
def cantidad_casos_confirmados_porcentaje(resultado, cantidad_de_pacientes, cont_pos):
    if resultado == 'positivo':
        cont_pos += 1
    porcentaje_confirmados = (cont_pos * 100) / cantidad_de_pacientes
    return cont_pos, porcentaje_confirmados


# OPCION 2
def edad_promedio_paciente_grupo_riesgo(resultado, edad, cont_edad, suma_edad, promedio):
    if resultado == 'negativo' and edad > 60:
        cont_edad += 1
        suma_edad += edad
        promedio = suma_edad / cont_edad
    return promedio, cont_edad, suma_edad


# OPCION 3
def cantidad_porcentaje_personas_salud(personal_salud, cantidad_de_pacientes, cont_personal_salud):
    if personal_salud == 'si':
        cont_personal_salud += 1
    porcentaje_salud = (cont_personal_salud * 100) / cantidad_de_pacientes
    return porcentaje_salud, cont_personal_salud


# OPCION 4
def edad_promedio_entre_casos_confirmados(resultado, edad, cont_casos_confirmados, suma_edad_confirmado, promedio_edad):
    if resultado == 'positivo':
        cont_casos_confirmados += 1
        suma_edad_confirmado += edad
        promedio_edad = suma_edad_confirmado / cont_casos_confirmados
    return promedio_edad, cont_casos_confirmados, suma_edad_confirmado


# OPCION 5
def menor_edad_entre_casos_autoctonos(mensaje, edad, cont_aut, menor):
    if mensaje == 'SI':
        cont_aut += 1
        if cont_aut == 1:
            menor = edad
        else:
            if edad < menor:
                menor = edad
    return menor, cont_aut


# OPCION 6
def cantidad_porcentaje_casos_confirmados_region(resultado, cont_positivos, regionPrincipal, cont_region_c,
                                                 cont_region_gc, cont_region_n, cont_region_s, porcentaje_c,
                                                 porcentaje_gc, porcentaje_n, porcentaje_s):
    if resultado == 'positivo':
        cont_positivos += 1
        if regionPrincipal == "Capital":
            cont_region_c += 1
        elif regionPrincipal == "Gran Córdoba":
            cont_region_gc += 1
        elif regionPrincipal == "Norte":
            cont_region_n += 1
        elif regionPrincipal == "Sur":
            cont_region_s += 1
        porcentaje_c = (cont_region_c * 100) / cont_positivos
        porcentaje_gc = (cont_region_gc * 100) / cont_positivos
        porcentaje_n = (cont_region_n * 100) / cont_positivos
        porcentaje_s = (cont_region_s * 100) / cont_positivos
    return cont_region_c, cont_region_gc, cont_region_n, cont_region_s, cont_positivos, porcentaje_c, porcentaje_gc, porcentaje_n, porcentaje_s


# OPCION 7
def cantidad_de_casos_confirmados_con_viaje_exterior(resultado, viajo_al_exterior, cont_exterior):
    if resultado == 'positivo' and viajo_al_exterior == 'si':
        cont_exterior += 1
    return cont_exterior


# OPCION 8
def cantidad_sospechosos_en_contacto_casos_confirmados(caso_confirmado, con_conf):
    if caso_confirmado == 'si':
        con_conf += 1
    return con_conf


# OPTION 9
def regiones_sin_casos_confirmados(resultado, cont_negativo, regionPrincipal, cont_region_nc, cont_region_ngc,
                                   cont_region_nn, cont_region_ns):
    if resultado == 'positivo':
        cont_negativo += 1
        if regionPrincipal == "Capital":
            cont_region_nc += 1
        elif regionPrincipal == "Gran Córdoba":
            cont_region_ngc += 1
        elif regionPrincipal == "Norte":
            cont_region_nn += 1
        elif regionPrincipal == "Sur":
            cont_region_ns += 1
    return cont_region_nc, cont_region_ngc, cont_region_nn, cont_region_ns, cont_negativo


# OPTION 10
def porcentaje_casos_positivos_autoctonos(resultado, mensaje, cont_positi, cont_autoctonos, porcentaje_autoctonos):
    if resultado == 'positivo':
        cont_positi += 1
        if mensaje == 'SI':
            cont_autoctonos += 1
        porcentaje_autoctonos = cont_autoctonos * 100 / cont_positi
    return porcentaje_autoctonos, cont_autoctonos, cont_positi


# ----------------------------------------------------------------------------------------------------------------------#
# MENU
def mostrar_menu():
    print('\x1b[1;32m ')
    print("*" * 150)
    print("                                           Estadística de Pacientes con COVID-19(Coronavirus)")
    print("*" * 150)
    print("                                                 I N F O R M E    G E N E R A L")
    print("-" * 150)
    print('1-CANTIDAD DE CASOS CONFIRMADOS(TEST POSITIVO) Y PORCENTAJE SOBRE EL TOTAL DE CASOS :')
    print('2-EDAD PROMEDIO DE LOS PACIENTES QUE PERTENCEN A GRUPO DE RIESGO(PARA PERTENECER AL'
          ' GRUPO DE RIESGO EL TEST DEBE SER NEGATIVO Y TENER MAS DE 60 AÑOS:')
    print('3-CANTIDAD Y PORCENTAJE QUE EL PERSONAL DE SALUD REPRESENTA SOBRE EL TOTAL DE CASOS:')
    print('4-EDAD PROMEDIO ENTRE LOS CASOS CONFIRMADOS:')
    print('5-MENOR EDAD ENTRE LOS CASOS AUTOCTONOS:')
    print('6-CANTIDAD DE CASOS CONFIRMADOS POR REGION Y PORCENTAJE QUE REPRESENTA CADA UNO SOBRE EL '
          'TOTAL DE LOS CASOS:')
    print('7-CANTIDAD DE CASOS CONFIRMADOS CON VIAJE AL EXTERIOR:')
    print('8-CANTIDAD DE CASOS SOSPECHOSOS EN CONTACTO CON CASOS CONFIRMADOS:')
    print('9-LAS REGIONES SIN CASOS CONFIRMADOS:')
    print('10-PORCENTAJE DE CASOS POSITIVOS AUTÓCTONOS SOBRE EL TOTAL DE POSITIVOS:')
    print('11-SALIDA:')
    print("-" * 150)
    print("Seleccione una Opción de Menú")
    print(' \x1b[1;30m ')


# ----------------------------------------------------------------------------------------------------------------------#
# TEST
def test():
    print('\x1b[1;34m ')
    print("BUENOS DIAS, BUENAS TARDES O BUENAS NOCHE...")
    print("PARA INGRESAR AL PROGRAMA SE LE SOLICITA LA CUENTA DE CORREO(ej: gabriel@hotmail) : \n")
    print('\x1b[1;30m ')
    validacion_de_dominio()
    print("SU CORREO FUE VALIDADO")
    print('*' * 80)
    cantidad_de_pacientes = validacion_de_cantidad_pacientes()
    print("LA CANTIDAD DE PACIENTES PROCESADOS ES DE:", cantidad_de_pacientes, "\n")
    print('*' * 80)
    input('Por favor presione la tecla INTRO para continuar ')
    consultas = ingreso_datos(cantidad_de_pacientes)
    print('*' * 80)
    option = 0
    while option != 11:
        input('Por favor presione la tecla INTRO para continuar ')
        mostrar_menu()
        option = validacion_opcion(1, 11, 'INGRESE SU OPCION POR FAVOR:')
        if option == 1:
            print('*' * 80)
            print('\n1) LA CANTIDAD DE CASOS CONFIRMADOS SERIA:', round(consultas[0]), '\n')
            print('2) EL PORCENTAJE TOTAL DE CASOS SERIA:', round(consultas[1], 2), '%\n')
            print('*' * 80)
        elif option == 2:
            print('*' * 80)
            print('\n1) LA EDAD PROMEDIO DE LOS PACIENTES QUE PERTENCEN A GRUPO DE RIESGO SERIAN:', round(consultas[2]),
                  'AÑOS\n')
            print('*' * 80)
        elif option == 3:
            print('*' * 80)
            print('\n1) LA CANTIDAD DEL PERSONAL DE SALUD QUE REPRESENTA SERIAN :',
                  consultas[4],
                  '\n')
            print('2) EL PORCENTAJE DEL PERSONAL DE SALUD QUE REPRESENTA SERIA:',
                  round(consultas[3], 2),
                  '%\n')
            print('*' * 80)
        elif option == 4:
            print('-' * 80)
            print('\n1) LA EDAD PROMEDIO ENTRE LOS CASOS CONFIRMADOS  SERIA:', round(consultas[5]), 'AÑOS\n')
            print('-' * 80)
        elif option == 5:
            print('-' * 80)
            print('\n1) LA MENOR EDAD ENTRE LOS CASOS AUTOCTONOS ES DE:', consultas[6], 'AÑOS\n')
            print('-' * 80)
        elif option == 6:
            print('-' * 80)
            print(
                '\n1) LA CANTIDAD DE CASOS CONFIRMADOS POR REGION Y EL PORCENTAJE QUE REPRESENTA CADA UNO ES : ')

            print('CAPITAL :', consultas[7], 'CASOS ES', round(consultas[11], 2), '%')
            print('GRAN CORDOBA :', consultas[8], 'CASOS ES', round(consultas[12], 2), '%')
            print('NORTE :', consultas[9], 'CASOS ES', round(consultas[13], 2), '%')
            print('SUR :', consultas[10], 'CASOS  ES', round(consultas[14], 2), '%')
            print('-' * 80)
        elif option == 7:
            print('-' * 80)
            print('\n1) LA CANTIDAD DE CASOS CONFIRMADOS CON VIAJE AL EXTERIOR SERIAN:', consultas[16],"PACIENTES")
            print('-' * 80)
        elif option == 8:
            print('-' * 80)
            print('\n1) LA CANTIDAD DE CASOS SOSPECHOSOS EN CONTACTO SERIAN :', consultas[17])
            print('-' * 80)
        elif option == 9:

            print('*' * 80)
            if consultas[18] == 0:
                print("\n1)NO HAY CASOS EN CAPITAL")
            elif consultas[19] == 0:
                print("\n1)NO HAY CASOS EN GRAN CORDOBA")
            elif consultas[20] == 0:
                print("\n1)NO HAY CASOS EN NORTE")
            elif consultas[21] == 0:
                print("\n1)NO HAY CASOS EN SUR")
            else:
                print("\n1) EN TODAS LAS PROVINCIAS HAY CASOS")
            print('*' * 80)
        elif option == 10:
            print('*' * 80)
            print('\n1) EL PORCENTAJE DE CASOS POSITIVOS AUTOCTONOS :', round(consultas[22], 2), '%\n')
            print('*' * 80)
        elif option == 11:
            print('¡Gracias por Utilizar Nuestro Programa !')
            option = input('Presione la tecla "1" para información sobre los programadores)\n')
            if option == '1':
                print(
                    '\n(T.P N° 2) diseñado por los Alumnos:  \nDel Castillo - LN.:53067-1k12 \nFlores - LN.:56731- 1k16 ')
                print('Cátedra de Algoritmos y Estructuras de Datos 2020 - UTN Córdoba')
                input()

test()
