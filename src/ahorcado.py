import random

def cargar_palabras(ruta):
    '''
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res

def elegir_palabra(palabras):
    '''
    Elige la palabra a adivinar:
    - Selecciona una palabra aleatoria de la lista 'palabras'
    - Devuelve la palabra seleccionada
    Ayuda: 
    - La función 'random.choice' del paquete 'random' recibe una lista de opciones y 
      devuelve una de ellas seleccionada aleatoriamente.
    '''
    return random.choice(palabras)
    
def enmascarar_palabra(palabra, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    lista_caracteres = [] # Inicializar una lista vacía
    for letra in palabra: # Recorrer cada letra de la palabra
        # Si la letra está en la lista letras_probadas
        if letra in letras_probadas:                   # ESCRIBIR CONDICIÓN
            # Añadir a lista_caracteres la letra
            lista_caracteres.append(letra)       # COMPLETAR
        else:
            # Añadir a lista_caracteres un guión bajo '_'
            lista_caracteres.append('_')       # COMPLETAR
    
    return ' '.join(lista_caracteres)

def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''
    letra = input("Adivina una letra: ").lower()
    while letra in letras_probadas:
        letra = input("Ya has probado con esa letra. Intenta con otra: ").lower()
    return letra

def comprobar_letra(palabra_secreta, letra):
    '''
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Mostrar el mensaje correspondiente informando al usuario
    - Devolver True si estaba y False si no
    '''
    if letra in palabra_secreta:
        print("¡Bien hecho! Esa letra está en la palabra.")
        return True
    else:
        print("Lo siento, esa letra no está en la palabra.")
        return False
    
def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    '''
    res = True
    if letras_probadas != {}:
        for letra in letras_probadas:
            if letra not in palabra_secreta:
                res = False
    else:
        res = False
    return res

def ejecutar_turno(palabra_secreta, letras_probadas):
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Añadir la letra al conjunto de letras probadas
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla
    '''
    
    print('Palabra: ',enmascarar_palabra(palabra_secreta, letras_probadas))
    letra = pedir_letra(letras_probadas)
    letras_probadas.add(letra)
    return comprobar_letra(palabra_secreta, letra)
    