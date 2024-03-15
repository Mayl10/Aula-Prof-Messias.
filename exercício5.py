# Ler quatro valores inteiros
valor1  =  int ( input ( "Dígito ou 1º valor inteiro: " ))
valor2  =  int ( input ( "Dígito ou 2º valor inteiro: " ))
valor3  =  int ( input ( "Dígito ou 3º valor inteiro: " ))
valor4  =  int ( input ( "Dígito ou 4º valor inteiro: " ))

# Verifique os valores divisíveis por 2 e 3
if  valor1  %  2  ==  0  and  valor1  %  3  ==  0 :
    print ( valor1 , "é divisível por 2 e 3" )
else :
    print ( valor1 , 'não é divisível nem por 2 e nem por 3' )

if  valor2  %  2  ==  0  and  valor2  %  3  ==  0 :
    print ( valor2 , "é divisível por 2 e 3" )
else :
    print ( valor2 , 'não é divisível nem por 2 e nem por 3' )

if  valor3  %  2  ==  0  and valor3  %  3  ==  0 :
    print ( valor3 , "é divisível por 2 e 3" )
else :
    print ( valor3 , 'não é divisível nem por 2 e nem por 3' )

if  valor4  %  2  ==  0  and  valor4  %  3  ==  0 :
    print ( valor4 , "é divisível por 2 e 3" )
else :
    print ( valor4 , 'não é divisível nem por 2 e nem por 3' )