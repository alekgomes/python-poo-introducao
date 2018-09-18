# Usando propriedades

Nessa aula vimos sobre getters e setters, que são métodos quase sempre
presentes em códigos que adotam o paradigma OO. Como os atributos desse 
paragigma são 'privados', é necessário que se tenha métodos que retornem 
e alterem esses atributos.
Exemplos: 
```  
# getter de saldo
def get_saldo(self):
	return self.__saldo

# setter para limite
def set_limites(self, limite):
	self.__limite = limite
```
Métodos getter SEMPRE têm algum valor de retorno, enquanto setters alteram
algum atributo.

Python apresenta substitutos para os getters e setters. Através da @property, atributos privados podem ser chamados através de funções, mas com a sintaxe de acesso a atributos.

O que aprendemos: 
* Método de leitura de atributos, os _getters_ 
* Método de modificação de atributos, os _setters_
* Uso de propriedades   
