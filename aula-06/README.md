# Métodos privados e estáticos

Métodos privados se comportam semelhantemente ao atributos privados.  

Métodos estáticos são aqueles que podem ser chamados a partir da classe, sem a necessidade de instanciar um objeto antes. Usamos o decorator @staticmethod 
para definir esse tipo de método.
```
@staticmethod
def codigo_do_banco():
	return 'Código: 001'   # valor fixo
```
Repare que métodos estáticos não recebem __self__ como parâmetro. Isso pq eles não tem a referência em memória, já que podem ser invocados a partir da classe e não do objeto. 

Nessa aula vimos:
* Métodos privados
* Métodos da classe, métodos estáticos