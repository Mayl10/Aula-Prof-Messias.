a  =  float ( input ( "Dígito ou valor de a: " ))
b  =  float ( input ( "Dígito ou valor de b: " ))
c  =  float ( input ( "Dígito ou valor de c: " ))

# Calcular o delta
delta  =  b ** 2  -  4 * a * c

if  a  !=  0  and b  !=  0  and  c  !=  0 :

    if  delta  <  0 :
        print ( "A descoberta não possui raízes reais." )
    elif  delta  ==  0 :
        raiz  =  - b  / ( 2 * a )
        print ( "A propriedade possui uma raiz real:" , raiz )
    else :
        raiz1  = ( - b  + ( delta  **  0,5 )) / ( 2 * a )
        raiz2  = ( - b  - ( delta  **  0,5 )) / ( 2 * a )
        print ( "A descoberta possui duas raízes reais:" , raiz1 , "e" , raiz2 )
else :
    print ( "A pesquisa não é completa. Certifique-se de que a, sejam diferentes de zero." )