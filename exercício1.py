#1 – Ler valores de quatro notas escolares de um aluno. Calcular a média aritmética e apresentar a mensagem “Aprovado” se a média obtida for maior ou igual a 7; caso
#contrario, apresente uma mensagem “Reprovado”. Informar junto de cada mensagem o valor da média obtida.

n1 = float ( input ( "dígito o valor da primeira nota:" ))
n2 = float ( input ( "dígito o valor da segunda nota:" ))
n3 = float ( input ( "dígito o valor da terceira nota:" ))
n4 = float ( input ( "dígito do valor da nota de quarta:" ))


nf=(n1+n2+n3+n4)/4

if nf>=7:
    print(f"Aprovado com media {nf}")
else:
    print(f"Reprovado,pois sua media foi inferior a 7({nf})")