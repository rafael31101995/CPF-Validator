# Validador de CPF

#### Sobre a lógica

Após a inserção de um CPF, ele passa por um filtro que vai retirar qualquer caractere especial que exista dentro da string. Após isso é feita a verificação\
se essa string tem todos os números iguais, caso tenha ele finaliza dizendo que não se trata de um CPF, o retorno é False.

Caso o número não tenha todos os números iguais, ele é apto a passar pelo filtro que determina se um número é um CPF válido.

https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
    
No site acima temos as formulas utilizadas para a criação da lógica deste código. <strong>Ao final deste mesmo site, temos o algoritmo que o autor \
fez para a validação, favor desconsiderar este algoritmo, pois ele não foi utilizado para a criação do código deste repositório.</strong>

#### Métodos

O código contem uma classe e 4 metodos, sendo um deles um metodo estatico.

* retira_formatacao
    * O nome do metodo deixa claro o que ela faz, basicamente recebe um CPF que pode estar formatado ou não, e retorna uma string sem caracteres especiais.
* check_characters
    * Esse metodo recebe um CPF não formatado e diz se ele é um CPF ou não checando se os digitos são iguais ou não. Isso é feito pois a lógica utilizada\
    valida um CPF que tenha todos os digitos iguais. Então, esse metodo trata esse erro.
* valida_cpf_logic - metodo estatico
    * Essa é a lógica por trás da validação do CPF, ela é bem descrita no site dado na parte de "Sobre a lógica".
    * Ele basicamente pega os dois ultimos digitos do CPF dado, guarda ele em uma variavel. 
    * Os calculos para pegar os dois ultimos digitos são realizados.
    * E após isso é feita uma verificação que diz se os dois números obtidos através dos calculos são iguais ao número guardado inicialmente.
    * Caso sim, a validação retorna um True, indicando que se trata de um CPF válido. Lembrando que pode ser valido mais não existente.
    * Caso não, ele retorna um False.
* valida_cpf
    * Aqui é onde chamamos os outros metodos em sequencia.
    
#### TDD - Test Driven Development

Aqui são testados os retornos de cada um dos metodos. São testados os seguintes objetos:
*   464.946.958-92
*   12345678988
*   212548465481
*   111.111.111-11
*   1.1.1.1.1.1.789-01