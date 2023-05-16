import sys

while True:
    contraseña1 = input("Ingrese una contraseña con un numero: ")
         
    if contraseña1[0].isdigit() :
        confirmacion = input("Ingrese la contraseña nuevamente: ")
        if contraseña1 == confirmacion:
            print("Contraseña establecida correctamente.")
            break
        
        else :
            print ("Las contraseñas no coinciden")  
              
    else :
        print("la contraseña debe empezar con un numero")    
        
print("Fin del programa")        

        #for contraseña1[0] in contraseña1 :
        
            #print("Ingrese la contraseña nuevamente")
    
#if contraseña1[0] == int :
# print("Ingrese la contraseña nuevamente")
    