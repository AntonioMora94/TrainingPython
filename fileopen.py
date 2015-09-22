#Clase para leer Tweets
def leerTweets():
    #funcion open, parametro 1 es el nombre
    #Parametro 2 es 
    #'r' Abre el archivo para lectura (debe existir el archivo)
    #'w' Crea el archivo y lo abre para escribir
    #'a' Abre el archivo para escribir. Se crea si el archivo no existe. Solo podemos agregar datos al final 
    
    archivo = open('Tweets.txt','r')
    linea = archivo.readline().rstrip('\n')
    
    nLinea = 1;        
            
    while linea!="":
        palabras = linea.split()
        print nLinea,' -> (', linea, ') contiene ', len(linea), ' caracteres y ', len(palabras), ' palabras'
        linea=archivo.readline().rstrip('\n')
        nLinea = nLinea + 1
    archivo.close()
    
leerTweets()