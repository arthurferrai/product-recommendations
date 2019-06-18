# Como rodar o projeto

Execute o comando `./run.sh`
Caso queira alterar o IP do servidor e/ou a porta usada padrões,
passe como parâmetro posicional:
```
run.sh <host> <port>
```
O IP padrão usado é `127.0.0.1` e a porta padrão é `3000`.

# Como rodar os testes unitários

Execute o comando `./test_flask.sh`. O teste irá certificar que
os métodos da camada de modelo serão chamados conforme esperado. 
