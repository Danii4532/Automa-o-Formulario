# Automa-o-Formulario
<h>Introdução</h2>
Este código é perfeito para quem precisa automatizar o processo de enviar várias informações para um formulário web, este código pode facilitar muito a vida de quem quiser usar, economizando horas de trabalho da pessoa.

<h2>Para que serve?</h2>
Este software recebe dados do usuario, acessa um formulário web que esteja disponivel na internet, e usando os dados recebidos, preencha cada campo que o usuario especificar

<h2>Como usar?</h2>
O primeiro passo é executar o codigo, apos isso, o software solicitará as seguintes informações.

1 - Link do formulario
Nesse campo, o usuário digita o link completo da pagina do formulario, esse link precisa estar online, caso contrario o codigo pode não funcionar.

2 - Quantos campos serão preenchidos:
Aqui o usuário digita quantos campos o formulário tem, exemplo: Nome, Idade, Sexo, Celular, etc.

OBS: Não é possivel inserir mais de 10 campos

3 - Digite quantos dados cada planilha possui:
Aqui o usuário digita quantas informações cada campo vai receber, ex: o primeiro campo vai receber 10 nomes , o segundo campo vai receber 10 idades, etc

OBS: cada campo do formulario precisa receber as mesmas quantidades de dados, ou seja, se nome vai receber 10, idade tambem precisa receber 10 e todos os outros campos tambem precisam receber 10 valores.

4 - Digite o nome do campo:

Aqui, o usuário digita o nome do primeiro campo do formulario, ex:se o primeiro campo do formulario for Nome, então aqui você digita Nome
Esse 'Digite o nome do campo' vai aparecer de acordo com o numero que o usuario inseriu em 'Quantos campos serão preenchidos:'

5 - Digite o xpath do campo:

Aqui o usuario vai precisar saber o Xpath que é um identificador que cada elemento do site possui, é meio dificil explicar por aqui, então recomendo que pesquise na internet para saber como obter o xpath do campo.
Obter o xpath é um processo muito simples, em alguns minutos o usuario consegue aprender a obter ele.

A informação 4 e 5 acima vão aparecer de acordo com o numero que foi inserido na instrução 2.

6 - Digite o xpath do botão:

Aqui o usuario terá que digitar o xpath do botao que envia as informações, isso é para o programa conseguir se orientar corretamento no formulario.

7 - Para prencher o campo será usado:

1 - Planilha

2 - Texto

3 - Lista

4 - Valor fixo

Aqui o usuario vai escolher que tipo de dado ele vai usar para preencher cada campo, o usuario poderá escolher entra planilha, texto, lista e valor fixo.
Planilha - o usuario ira selecionar uma planilha do computador, e o programa pergunta:
'Digite o nome da coluna: ' - O usuario digita o nome da coluna da planilha que sera usada,

OBS: a coluna da planilha deve conter o numero de informações inseridas na instrução 3, e a coluna não deve conter valores em BRANCO ou NULO.

Texto - O usuario seleciona um arquivo de texto do computador

OBS: o arquivo deve conter a quantidade de linhas inseridas na intrução 3, e não deve conter linhas em branco, caso contrario ocorrerá um erro.

Lista - O usuario insere manualmente os valores que quiser, que podem ser letra ou numero, de acordo com a quantidade na instrução 3.

Valor Fixo - o usuario insere um unico valor apenas uma vez e esse valor sera usado em todas as vezes que o formulario for preenchido.

Após inserir todas essas informações, o programa começa a preencher o formulario com as informações repassadas.

AVISO
Tenha cuidado ao inserir as informações, caso o programa não consiga encontrar a pagina do link ou não encontre algum dos xpath fornecidos, ele retornará erro.
Se for usar Texto ou Planilha, verifique se ambos possui as mesmas quantidades de dados e se não possuem valores nulos ou em branco, senão o programa pode retornar erro.

Se tiver alguma dúvida, entre em contato que eu ajudarei com prazer.

Aproveite :)
