Ler o nome e o sexo da pessoa
nome  =  input ( "Digite o nome da pessoa: " )
sexo  =  input ( "Digite o sexo da pessoa (M para masculino ou F para feminino): " )

# Verifique o sexo e apresente a saudação
if  sexo . upper () ==  "M" :
    print ( f"Ilmo. Sr. Tenha um bom dia sr. { nome } " )
elif  sexo . upper () ==  "F" :
    print ( f"Ilma. Sra. tenha um bom dia sra. { nome } " )