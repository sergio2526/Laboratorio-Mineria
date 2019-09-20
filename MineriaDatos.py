#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psycopg2
conexion = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="sergio")
# Creamos el cursor con el objeto conexion
cur = conexion.cursor()


# Ejecutamos una consulta con el numero de resgistros que se encuentra en la base de datos postgres


cur.execute( "SELECT count(*)  from infracciones")

infracciones = cur.fetchall()


numero_total = int(infracciones[0][0])

print("\nTotal de registros ",numero_total)

print("\n Ingrese el tipo_vehiculo")
tipo_vehiculo = input()

print("\n Ingrese el genero_conductor")
genero_conductor = input()

print("\n Ingrese el color_vehiculo")
color_vehiculo = input()

print("\n Ingrese la raza_conductor")
raza_conductor = input()

print("\n Ingrese el estado_registro_vehiculo")
estado_registro_vehiculo = input()

        
        # Ejecutamos una consulta con todos los tipos warning

cur.execute("select count(*) from infracciones where tipo_infraccion like 'Warning'")
infracciones = cur.fetchall()

resultado_warning = int(infracciones[0][0])
resultado2 = float(infracciones[0][0]/numero_total)



print ("Consulta warning ",resultado_warning," / " , numero_total ," = ",resultado2)

        
# Ejecutamos una consulta con todos los tipos Citation

cur.execute("select count(*) from infracciones where tipo_infraccion like 'Citation'")
infracciones = cur.fetchall()

resultado_citation = int(infracciones[0][0])
resultado3 = float(infracciones[0][0]/numero_total)



print ("Consulta warning ",resultado_citation," / " , numero_total ," = ",resultado3)
       

        
# Ejecutamos una consulta con todos los tipos ESERO

cur.execute("select count(*) from infracciones where tipo_infraccion like 'ESERO'")
infracciones = cur.fetchall()


resultado_esero = int(infracciones[0][0])
resultado4 = float(infracciones[0][0]/numero_total)



print ("Consulta warning ",resultado_esero," / " , numero_total ," = ",resultado4)


# Ejecutamos una consulta con todos los tipos ESERO

cur.execute("select count(*) from infracciones where tipo_infraccion like 'SERO'")
infracciones = cur.fetchall()


resultado_sero = int(infracciones[0][0])
resultado5 = float(infracciones[0][0]/numero_total)



print ("Consulta warning ",resultado_sero," / " , numero_total ," = ",resultado5)
    
    
#--------------------------------------------------WARNING -------------------------------------------------------    
    
# Ejecutamos una consulta con el numero de motocicletas con warning

cur.execute( "SELECT count(*) from infracciones where tipo_infraccion like 'Warning' and tipo_vehiculo like '"+tipo_vehiculo+"'")
infracciones = cur.fetchall()


#cur.execute( "SELECT gender FROM proceso where gender='"+cadena+"'" )


numero_motocicletas= int(infracciones[0][0])

resultado6 = float(infracciones[0][0]/resultado_warning)
    
for infracciones in infracciones:    
      print ("Numero de motocicletas con warning ",numero_motocicletas , " / ", resultado_warning, " = ", resultado6 )


        

# Ejecutamos una consulta con el numero de genero femenino de tipo warning

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'Warning' and genero_conductor like '"+genero_conductor+"'")

infracciones = cur.fetchall()

numero_femenino= int(infracciones[0][0])

resultado7 = float(infracciones[0][0]/resultado_warning)
    
for infracciones in infracciones:    
      print ("Numero de genero femenino tipo warning :",numero_femenino, " / ", resultado_warning, " = ", resultado7 )
        


        
#Ejecutamos una consulta con el numero de vehiculos color azul con warning

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'Warning' and color_vehiculo like '"+color_vehiculo+"'")

infracciones = cur.fetchall()

numero_vehiculos= int(infracciones[0][0])

resultado8 = float(infracciones[0][0]/resultado_warning)
    
for infracciones in infracciones:    
      print ("Numero de vehiculos color azul con warning :",numero_vehiculos , " / ", resultado_warning, " = ", resultado8 )
        


        
             
 # Ejecutamos una consulta con el numero de raza BLACK con warning

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'Warning' and raza_conductor like '"+raza_conductor+"'")

infracciones = cur.fetchall()

numero_raza= int(infracciones[0][0])

resultado9 = float(infracciones[0][0]/resultado_warning)
    
for infracciones in infracciones:    
      print ("Numero de raza black con warning :",numero_raza , " / ", resultado_warning, " = ", resultado9 )
        


   # Ejecutamos una consulta con el numero estado que se encontraba el condcutor con warning

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'Warning' and estado_registro_vehiculo like '"+estado_registro_vehiculo+"'")

infracciones = cur.fetchall()

numero_estado= int(infracciones[0][0])

resultado10 = float(infracciones[0][0]/resultado_warning)
    
for infracciones in infracciones:    
      print ("Numero estado del condcutor con warning :",numero_estado , " / ", resultado_warning, " = ", resultado10 )
        

multiplicacion_warning = float(resultado6*resultado7*resultado8*resultado8*resultado10)
print (" \n Resultado  warning : ", multiplicacion_warning)
        
        
        

#------------------------------------CITATION------------------------------------

# Ejecutamos una consulta con el numero de motocicletas con citation

cur.execute( "SELECT count(*) from infracciones where tipo_infraccion like 'Citation' and tipo_vehiculo like '"+tipo_vehiculo+"'" )
infracciones = cur.fetchall()

numero_motocicletas_citation = int(infracciones[0][0])

resultado11 = float(infracciones[0][0]/resultado_citation)
    
for infracciones in infracciones:    
      print ("  \n  Numero de motocicletas con citation ",numero_motocicletas_citation , " / ", resultado_citation, " = ", resultado11 )


        

# Ejecutamos una consulta con el numero de genero masculino de tipo citation

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'Citation' and genero_conductor like '"+genero_conductor+"'" )

infracciones = cur.fetchall()

numero_femenino_citation = int(infracciones[0][0])

resultado12 = float(infracciones[0][0]/resultado_citation)
    
for infracciones in infracciones:    
      print ("Numero de genero masculino tipo citation :",numero_femenino_citation, " / ", resultado_citation, " = ", resultado12 )
        



#Ejecutamos una consulta con el numero de vehiculos color azul con citation

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'Citation' and color_vehiculo like '"+color_vehiculo+"'" )

infracciones = cur.fetchall()

numero_vehiculos_citation= int(infracciones[0][0])

resultado13 = float(infracciones[0][0]/resultado_citation)
    
for infracciones in infracciones:    
     print ("Numero de vehiculos color azul con citation :",numero_vehiculos_citation , " / ", resultado_citation, " = ", resultado13 )
        


        
             
 # Ejecutamos una consulta con el numero de raza BLACK con citation

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'Citation' and raza_conductor like '"+raza_conductor+"'" )

infracciones = cur.fetchall()

numero_raza_citation= int(infracciones[0][0])

resultado14 = float(infracciones[0][0]/resultado_citation)
    
for infracciones in infracciones:    
      print ("Numero de raza black con citation :",numero_raza_citation , " / ", resultado_citation, " = ", resultado14 )
        


   # Ejecutamos una consulta con el numero estado que se encontraba el condcutor con citation

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'Citation' and estado_registro_vehiculo like '"+estado_registro_vehiculo+"'" )

infracciones = cur.fetchall()

numero_estado_citation= int(infracciones[0][0])

resultado15 = float(infracciones[0][0]/resultado_citation)
    
for infracciones in infracciones:    
      print ("Numero estado del condcutor con citation :",numero_estado_citation , " / ", resultado_citation, " = ", resultado15)
        

multiplicacion_citation = float(resultado11*resultado12*resultado13*resultado14*resultado15)
print (" \n Resultado  Citation : ", multiplicacion_citation)
        

    
    
    
    
#------------------------------------ESERO------------------------------------------

# Ejecutamos una consulta con el numero de motocicletas con ESERO

cur.execute( "SELECT count(*) from infracciones where tipo_infraccion like 'ESERO' and tipo_vehiculo like '"+tipo_vehiculo+"'")
infracciones = cur.fetchall()

numero_motocicletas_esero = int(infracciones[0][0])

resultado16 = float(infracciones[0][0]/resultado_esero)
    
for infracciones in infracciones:    
      print ("  \n  Numero de motocicletas con ESERO ",numero_motocicletas_esero , " / ", resultado_esero, " = ", resultado16 )


        

# Ejecutamos una consulta con el numero de genero masculino de tipo ESERO

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'ESERO' and genero_conductor like '"+genero_conductor+"'" )

infracciones = cur.fetchall()

numero_femenino_esero = int(infracciones[0][0])

resultado17 = float(infracciones[0][0]/resultado_esero)
    
for infracciones in infracciones:    
      print ("Numero de genero masculino tipo ESERO :",numero_femenino_esero, " / ", resultado_esero, " = ", resultado17 )
        


        
#Ejecutamos una consulta con el numero de vehiculos color azul con ESERO

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'ESERO' and color_vehiculo like '"+color_vehiculo+"'" )

infracciones = cur.fetchall()

numero_vehiculos_esero= int(infracciones[0][0])

resultado18 = float(infracciones[0][0]/resultado_esero)
    
for infracciones in infracciones:    
     print ("Numero de vehiculos color azul con ESERO :",numero_vehiculos_esero , " / ", resultado_esero, " = ", resultado18 )
        


        
             
 # Ejecutamos una consulta con el numero de raza BLACK con ESERO

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'ESERO' and raza_conductor like '"+raza_conductor+"'" )

infracciones = cur.fetchall()

numero_raza_esero= int(infracciones[0][0])

resultado19 = float(infracciones[0][0]/resultado_esero)
    
for infracciones in infracciones:    
      print ("Numero de raza black con ESERO :",numero_raza_esero , " / ", resultado_esero, " = ", resultado19 )
        


   # Ejecutamos una consulta con el numero estado que se encontraba el condcutor con ESERO

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'ESERO' and estado_registro_vehiculo like '"+estado_registro_vehiculo+"'" )

infracciones = cur.fetchall()

numero_estado_esero= int(infracciones[0][0])

resultado20 = float(infracciones[0][0]/resultado_esero)
    
for infracciones in infracciones:    
      print ("Numero estado del condcutor con ESERO :",numero_estado_esero, " / ", resultado_esero, " = ", resultado20)
        

multiplicacion_esero = float(resultado16*resultado17*resultado18*resultado19*resultado20)
print (" \n Resultado  ESERO : ", multiplicacion_esero)
        
  
        

#------------------------------------SERO------------------------------------------

# Ejecutamos una consulta con el numero de motocicletas con SERO

cur.execute( "SELECT count(*) from infracciones where tipo_infraccion like 'SERO' and tipo_vehiculo like '"+tipo_vehiculo+"'" )
infracciones = cur.fetchall()

numero_motocicletas_sero = int(infracciones[0][0])

resultado21 = float(infracciones[0][0]/resultado_sero)
    
for infracciones in infracciones:    
      print ("  \n  Numero de motocicletas con SERO ",numero_motocicletas_sero , " / ", resultado_sero, " = ", resultado21 )


        

# Ejecutamos una consulta con el numero de genero masculino de tipo SERO

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'SERO' and genero_conductor like '"+genero_conductor+"'")

infracciones = cur.fetchall()

numero_femenino_sero = int(infracciones[0][0])

resultado22 = float(infracciones[0][0]/resultado_sero)
    
for infracciones in infracciones:    
      print ("Numero de genero masculino tipo SERO :",numero_femenino_sero, " / ", resultado_sero, " = ", resultado22 )
        


 #Ejecutamos una consulta con el numero de vehiculos color azul con SERO

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'SERO' and color_vehiculo like '"+color_vehiculo+"'" )

infracciones = cur.fetchall()

numero_vehiculos_sero= int(infracciones[0][0])

resultado23 = float(infracciones[0][0]/resultado_sero)
    
for infracciones in infracciones:    
     print ("Numero de vehiculos color azul con SERO :",numero_vehiculos_sero , " / ", resultado_sero, " = ", resultado23 )
        


        
             
 # Ejecutamos una consulta con el numero de raza BLACK con SERO

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'SERO' and raza_conductor like '"+raza_conductor+"'")

infracciones = cur.fetchall()

numero_raza_sero= int(infracciones[0][0])

resultado24 = float(infracciones[0][0]/resultado_sero)
    
for infracciones in infracciones:    
      print ("Numero de raza black con SERO :",numero_raza_sero , " / ", resultado_sero, " = ", resultado24 )
        


   # Ejecutamos una consulta con el numero estado que se encontraba el condcutor con SERO

cur.execute( "select count(*) from infracciones where tipo_infraccion like 'SERO' and estado_registro_vehiculo like '"+estado_registro_vehiculo+"'" )

infracciones = cur.fetchall()

numero_estado_sero= int(infracciones[0][0])

resultado25 = float(infracciones[0][0]/resultado_sero)
    
for infracciones in infracciones:    
      print ("Numero estado del condcutor con SERO :",numero_estado_sero, " / ", resultado_sero, " = ", resultado25)
        

multiplicacion_sero = float(resultado21*resultado22*resultado23*resultado24*resultado25)
print (" \n Resultado  SERO : ", multiplicacion_sero)
        

    
#Acontinuacion multiplicamos el peso de cada tipo_infraccion * resultado de cada una

warning_peso = float(multiplicacion_warning*resultado2)
print (" \n Resultado  peso warning : ", warning_peso)
        
citation_peso = float(multiplicacion_citation*resultado3)
print (" \n Resultado  peso citation : ", citation_peso)
        
esero_peso = float(multiplicacion_esero*resultado4)
print (" \n Resultado  peso ESERO : ", esero_peso)
        
sero_peso = float(multiplicacion_sero*resultado5)
print (" \n Resultado  peso sero : ", sero_peso)
        

# Acontinuacion sacamos la probabilidades de cada infracción

wpf = (warning_peso/(warning_peso+citation_peso+esero_peso+sero_peso))
print (" \n LA PROBABILIDAD DE WARNING ES :", wpf ,"%")

wpc = (citation_peso/(warning_peso+citation_peso+esero_peso+sero_peso))
print (" \n LA PROBABILIDAD DE CITATION ES :", wpc ,"%")

wpe = (esero_peso/(warning_peso+citation_peso+esero_peso+sero_peso))
print (" \n LA PROBABILIDAD DE ESERO ES :", wpe ,"%")
    
wps = (sero_peso/(warning_peso+citation_peso+esero_peso+sero_peso))
print (" \n LA PROBABILIDAD DE SERO ES :", wps ,"%")    
    
        
# Cerramos la conexión
conexion.close()


# In[ ]:




