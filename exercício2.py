n1  =  float ( input ( "dígito o valor da primeira nota:" ))
n2  =  float ( input ( "dígito o valor da segunda nota:" ))
n3  =  float ( input ( "dígito o valor da terceira nota:" ))
n4  =  float ( input ( "dígito do valor da nota de quarta:" ))
nf  = ( n1  +  n2  +  n3  +  n4 ) /  4
if nf >= 7 :
    print ( "Aprovado" )
else :
    print ( "suas notas não foram bastante." )
    nn  =  float ( input ( "digite a nota do exame final:" ))
    if ( nf  +  nn ) /  2  >=  5 :
        print ( "Aprovado no exame final" )
    else :
        print ( "Reprovado" )