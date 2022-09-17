
n=int(input("Del 1 al 5, escriba el número del ejercicio que quiera ejecutar"))

if n==1:

    P1 = [2.0, 2.0, 3.0]; P2 = [2.0, 3.0, 4.0]; P3 = [1.0, 1.0, 3.0]; P4 = [0.5, 0.5, 2.0]; P5 = [1.0, 2.0, 1.0]
    P6  = [1.0, 0.5, 1.0]; P7  = [3.0, 2.0, 0.5]; P8  = [3.0, 1.0, 2.0]; P9  = [0.0, 0.0, 0.0]; P10 = [2.0, 0.0, 0.5]

    Puntos = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]
 
    Distancia=[]  
    DistanciaPuntos=[] 

    for Punto1 in Puntos:
        for Punto2 in Puntos:     
            Suma=0
                
            if Punto1!=Punto2:
                for i in range(len(Punto1)):
                    Dist=(Punto1[i]-Punto2[i])**2 
                    Suma=Suma+Dist
                    
                DistanciaPuntos.append([Punto1,Punto2,Suma])
                Distancia.append(Suma)
        
    Menor=min(Distancia)
    Posicion=Distancia.index(Menor)
        
    P_1=DistanciaPuntos[Posicion][0]
    P_2=DistanciaPuntos[Posicion][1]
    Distancia=(DistanciaPuntos[Posicion][2])**0.5

    parCercano='P%s - P%s'%((Puntos.index(P_1)+1),Puntos.index(P_2)+1)

    print('-> Los puntos más cercanos entre sí, son: %s. Ubicados a una distancia entre sí de: %s'%(parCercano, Distancia))


            

elif n==2:
    
    lista1=[None]*26
    lista2=[None]*200
    lista3=[None]*360
    
    i=0
    while i<26:      
        lista1[i]=(-1)**(i)
        i=i+1
        
              
    j=0
    while j<200:      
        if j%2==0:
            lista2[j]=100-j/2
        
        if j%2!=0:
            lista2[j]=-1
        
        j=j+1
                 

    k=0   
    while k<2: 
        lista3[k]=2*k+2 
        k=k+1 

    k=2   
    while k<9:       
        lista3[k]=2*k      
        k=k+1  

    k=9
    m=0   
    while k<359:            
        if m%2==0:        
            lista3[k]=2*k-m-2
        
        if m%2!=0:
            lista3[k]=2*k-m-1
        
        if (k+1)%3==0:
            m=m+1
             
        k=k+1  
    
    k=0
    m=1    
    while k<361:  
        if (k+1)%3==0:      
            lista3[k]=5*m
            m=m+1
       
        k=k+1      


    listadeListas=[lista1,lista2,lista3]
    
    print(listadeListas)
    

            
     
elif n==3: 
    
    c01=[1.0*0.1, 1.1*0.2, 2.3*0.15, 1.1*0.2]  
    c02=[3.1*0.1, 3.1*0.2, 1.2*0.15, 3.0*0.2]
    c03=[5.0*0.1, 4.0*0.2, 2.5*0.15, 5.0*0.2]
    c04=[3.1*0.1, 1.0*0.2, 2.6*0.15, 1.0*0.2]
    c05=[3.2*0.1, 4.0*0.2, 1.1*0.15, 3.0*0.2]
    c06=[5.0*0.1, 5.0*0.2, 5.0*0.15, 3.9*0.2]
    c07=[3.4*0.1, 4.0*0.2, 2.6*0.15, 3.2*0.2]
    c08=[2.0*0.1, 2.2*0.2, 2.1*0.15, 4.2*0.2]
    c09=[3.7*0.1, 4.1*0.2, 4.7*0.15, 4.0*0.2]
    c10=[4.1*0.1, 4.7*0.2, 4.4*0.15, 5.0*0.2]
    c11=[5.0*0.1, 5.0*0.2, 1.0*0.15, 3.2*0.2]
    c12=[5.0*0.1, 4.2*0.2, 2.1*0.15, 5.0*0.2]
    c13=[3.2*0.1, 4.1*0.2, 2.2*0.15, 3.3*0.2]       
        
    notas=[c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12, c13]
    
    promedio=0
    
    Cantidad_que_pierden=0
    Cantidad_que_ganan=0
    Cantidad_con_posibilidades=0
    
    for i in range(len(notas)):
        for j in range(4):
            promedio=promedio+notas[i][j]
                
        if promedio>=3:
            Cantidad_que_ganan+=1
            
        promedio=0
    
    promedio=0
                
    for i in range(len(notas)):
        
        for j in range(4):
            promedio=promedio+notas[i][j]
        
        promedio+=5*0.35
        
        if promedio<3:
            Cantidad_que_pierden+=1
        
        if promedio>=3:
            Cantidad_con_posibilidades+=1
            
        promedio=0
            
    Cantidad_con_posibilidades=Cantidad_con_posibilidades-Cantidad_que_ganan
    
    estudiantes = [Cantidad_que_pierden, Cantidad_que_ganan, Cantidad_con_posibilidades]            
    print(estudiantes)
                               



elif n==4:
    Lunes=[1,1,1,1,1,1]; Martes=[1,0,0,1,0,0]; Miercoles=[1,1,1,1,0,1]; Jueves=[1,0,1,0,1,0]; Viernes=[0,1,0,0,1,0]
    LunesR=[1,1,1,0,0,1]; MartesR=[1,0,0,0,0,0]; MiercolesR=[1,0,1,1,0,1]; JuevesR=[0,0,1,0,1,0]; ViernesR=[0,0,0,0,0,0]

    Ida=[Lunes, Martes, Miercoles, Jueves, Viernes]
    Regreso=[LunesR, MartesR, MiercolesR, JuevesR, ViernesR]

    Pago=[None]*6
    
    for i in range(len(Ida)):
        total=0

        for j in range(6):
            total=total+Ida[i][j]

        for j in range(6):
            if total==0:
                Ida[i][j]=10000/6
            else:
                Ida[i][j]=(Ida[i][j]/total)*15000

    for i in range(len(Regreso)):
        total=0

        for j in range(6):
            total=total+Regreso[i][j]

        for j in range(6):
            if total==0:
                Regreso[i][j]=10000/6
            else:
                Regreso[i][j]=(Regreso[i][j]/total)*15000

    for i in range(6):
        pago=0

        for j in range(5):
            pago=pago+Ida[j][i]+Regreso[j][i]

        Pago[i]=pago   


    diccionarioPagos={'JUAN':Pago[0], 'CAMILA':Pago[1], 'JOSE':Pago[2], 'MARIA':Pago[3], 'ESTEBAN':Pago[4], 'ANGIE':Pago[5]}

    print(diccionarioPagos)    
    
    
  
    
elif n==5:
    c001=[20*50000*0.05, 22*70000*0.04, 30*40000*0.06, 2 *25000*0.07, 40*35000*0.05, 20*80000*0.03, 3 *95000*0.02]   
    c002=[31*50000*0.05, 14*70000*0.04, 32*40000*0.06, 15*25000*0.07, 13*35000*0.05, 20*80000*0.03, 11*95000*0.02]   
    c010=[24*50000*0.05, 32*70000*0.04, 40*40000*0.06, 9 *25000*0.07, 12*35000*0.05, 50*80000*0.03, 13*95000*0.02]   
    c020=[42*50000*0.05, 12*70000*0.04, 33*40000*0.06, 24*25000*0.07, 22*35000*0.05, 32*80000*0.03, 23*95000*0.02]   
    c021=[51*50000*0.05, 21*70000*0.04, 25*40000*0.06, 10*25000*0.07, 19*35000*0.05, 14*80000*0.03, 2 *95000*0.02]   
    c022=[22*50000*0.05, 31*70000*0.04, 51*40000*0.06, 21*25000*0.07, 35*35000*0.05, 15*80000*0.03, 11*95000*0.02]   
    c023=[21*50000*0.05, 36*70000*0.04, 22*40000*0.06, 32*25000*0.07, 39*35000*0.05, 32*80000*0.03, 15*95000*0.02]   
    c024=[22*50000*0.05, 33*70000*0.04, 41*40000*0.06, 21*25000*0.07, 43*35000*0.05, 31*80000*0.03, 36*95000*0.02]   
    c025=[33*50000*0.05, 31*70000*0.04, 20*40000*0.06, 42*25000*0.07, 33*35000*0.05, 42*80000*0.03, 35*95000*0.02]   
    c031=[22*50000*0.05, 47*70000*0.04, 5 *40000*0.06, 28*25000*0.07, 37*35000*0.05, 31*80000*0.03, 32*95000*0.02]   
    c032=[24*50000*0.05, 38*70000*0.04, 33*40000*0.06, 21*25000*0.07, 41*35000*0.05, 31*80000*0.03, 16*95000*0.02]   
    c033=[21*50000*0.05, 18*70000*0.04, 32*40000*0.06, 37*25000*0.07, 39*35000*0.05, 22*80000*0.03, 12*95000*0.02]   
    c041=[33*50000*0.05, 31*70000*0.04, 21*40000*0.06, 21*25000*0.07, 33*35000*0.05, 39*80000*0.03, 25*95000*0.02]   
    c042=[25*50000*0.05, 39*70000*0.04, 20*40000*0.06, 48*25000*0.07, 15*35000*0.05, 30*80000*0.03, 32*95000*0.02]   
    c043=[27*50000*0.05, 32*70000*0.04, 29*40000*0.06, 28*25000*0.07, 37*35000*0.05, 35*80000*0.03, 16*95000*0.02]   
    c121=[24*50000*0.05, 12*70000*0.04, 31*40000*0.06, 21*25000*0.07, 39*35000*0.05, 32*80000*0.03, 13*95000*0.02]   
    c122=[31*50000*0.05, 31*70000*0.04, 50*40000*0.06, 22*25000*0.07, 13*35000*0.05, 30*80000*0.03, 21*95000*0.02]   
    c123=[23*50000*0.05, 35*70000*0.04, 35*40000*0.06, 39*25000*0.07, 31*35000*0.05, 19*80000*0.03, 19*95000*0.02]   
    c351=[26*50000*0.05, 36*70000*0.04, 39*40000*0.06, 27*25000*0.07, 35*35000*0.05, 32*80000*0.03, 16*95000*0.02]   
    c352=[25*50000*0.05, 31*70000*0.04, 21*40000*0.06, 21*25000*0.07, 25*35000*0.05, 37*80000*0.03, 15*95000*0.02]   
    c353=[23*50000*0.05, 34*70000*0.04, 35*40000*0.06, 32*25000*0.07, 37*35000*0.05, 20*80000*0.03, 49*95000*0.02]   
    c368=[31*50000*0.05, 14*70000*0.04, 29*40000*0.06, 39*25000*0.07, 25*35000*0.05, 37*80000*0.03, 16*95000*0.02]   
    c369=[26*50000*0.05, 31*70000*0.04, 31*40000*0.06, 27*25000*0.07, 37*35000*0.05, 32*80000*0.03, 41*95000*0.02]   
    c461=[40*50000*0.05, 42*70000*0.04, 23*40000*0.06, 11*25000*0.07, 21*35000*0.05, 15*80000*0.03, 19*95000*0.02]   
    c466=[27*50000*0.05, 31*70000*0.04, 39*40000*0.06, 21*25000*0.07, 31*35000*0.05, 32*80000*0.03, 25*95000*0.02]   
    c469=[38*50000*0.05, 32*70000*0.04, 19*40000*0.06, 29*25000*0.07, 35*35000*0.05, 50*80000*0.03, 16*95000*0.02]  

    codigos=[c001,c002,c010,c020,c021,c022,c023,c024,c025,c031,c032,c033,c041,c042,c043,c121,c122,c123,c351,c352,c353,c368,c369,c461,c466,c469]
    codigosName=['001','002','010','020','021','022','023','024','025','031','032','033','041','042','043','121','122','123','351','352','353','368','369','461','466','469']

    suma=[None]*26

    for i in range(len(codigos)):

        salario=0

        for j in range(6):
            salario=salario+codigos[i][j]

        suma[i]=salario

    mayor1=max(suma)
    pos1=suma.index(mayor1)

    mayor2=0
    mayor3=0

    for i in range(len(suma)):
        if suma[i]>mayor2 and suma[i]!=mayor1:
            mayor2=suma[i]
    pos2=suma.index(mayor2)

    for i in range(len(suma)):
        if suma[i]>mayor3 and suma[i]!=mayor1 and suma[i]!=mayor2:
            mayor3=suma[i]
    pos3=suma.index(mayor3)        


    codigosAltosSalarios=[codigosName[pos1],codigosName[pos2],codigosName[pos3]]
    print(codigosAltosSalarios)            
                     
                            


