import sys

while True:
    contraseña1 = input("Ingrese una contraseña con un numero: ")
       
    if contraseña1[0].isdigit() :
        confirmacion = input("Ingrese la contraseña nuevamente: ")
        if contraseña1 != confirmacion:
            print("Las contraseñas no coinciden.")
        elif contraseña1 != confirmacion: 
            print ('La contraseñas no coiciden saldremos del programa') 
            break
        else :
            print ("Contraseña establecida correctamente.")  
            
    else :
        print("la contraseña debe empezar con un numero")    
    
print("Fin del programa")       

        # for contraseña1[0] in contraseña1 :
        
        #     print("Ingrese la contraseña nuevamente")
    
#if contraseña1[0] == int :
# print("Ingrese la contraseña nuevamente")Contraseña establecida correctamente.
    