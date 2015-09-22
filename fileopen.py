#Clase para leer Tweets
def leerTweets():
    #funcion open, parametro 1 es el nombre
    #Parametro 2 es 
    #'r' Abre el archivo para lectura (debe existir el archivo)
    #'w' Crea el archivo y lo abre para escribir
    #'a' Abre el archivo para escribir. Se crea si el archivo no existe. Solo podemos agregar datos al final 
    
    archivo = open('Tweets.txt','r')
    
    #Le quito el salto de linea que pone el txt con el rstrip()
    linea = archivo.readline().rstrip('\n')
    
    #Contador para las lineas
    nLinea = 1;        
            
    #Mientras la linea contenga texto
    while linea!="":
        #Separo por palabras cada linea, por defecto el separador es el espacio
        palabras = linea.split()        
        print nLinea,' -> (', linea, ') contiene ', len(linea), ' caracteres y ', len(palabras), ' palabras'        
        #Con la funcion len() conocemos la cantidad que contiene un string                
        linea=archivo.readline().rstrip('\n')
        nLinea = nLinea + 1
        
    #Se cierra el archivo
    archivo.close()
    
#Ejecuto la funcion
leerTweets()