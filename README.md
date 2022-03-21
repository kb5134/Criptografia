# Criptografia
Projeto criado anteriormente como projeto de um APS solicitada no primeiro semestre do curso de Ciencia da Computação da UNIP-Limeira, porém visando a melhora do mesmo e a consistencia das informações, sua ideia foi completamente alterada mantendo apenas em seu nucleo a funcionalidade de exibir a chave de acesso para o usuário final através de um Qrcode
## Como funciona:
Atualmente o sistem gera um dicionario de numeros aleatórios para cada letra do alfabeto e salva estes numeros em um dicionario.
![image](https://user-images.githubusercontent.com/57547119/159199644-c0a65dec-9621-44bb-8991-6a82350c4bef.png)

Após criar o dicionario, o sistema irá exibir para o usuário a mensagem que o mesmo inseriu porém utilizando os valores de cada letra como os valores do dicionario que foi criado

Junto do texto criptografado, o sistema exibe uma mensagem solicitando que o usuário escaneie o QrCode para acessar a chave que será utilizada para descriptografar.

![image](https://user-images.githubusercontent.com/57547119/159199909-c3a3fc81-d708-4817-accb-bc7b4bf414f8.png)

![image](https://user-images.githubusercontent.com/57547119/159199925-9f34865a-99fd-4531-9a91-062c52474e41.png)

Tendo enviado para o usuário todas as informações, o sistema salva no banco de dados a chave e o diconario criado

![image](https://user-images.githubusercontent.com/57547119/159200027-cba1fe4c-f0eb-4995-b8d2-990c192bdf42.png)

#### Descriptografando:

Para descriptografar, o sistema solicita para o usuário a chave de acesso e verifica no banco de dados a existencia da mesma, caso exista a a chave no banco de dados, o sistema gera um novo dicionario utilizando as chaves do banco de dados para cada letra do dicionario

![image](https://user-images.githubusercontent.com/57547119/159200249-5ee7a064-43c4-4aeb-ba55-8e403a8ca682.png)

Após gerar o dicionario, o sistema verifica se os numeros inseridos pelo usuário existem no dicionario e se existirem, exibe os mesmos finalizando assim o processo de descriptografia

![image](https://user-images.githubusercontent.com/57547119/159200358-6d93f519-8213-4514-8ce7-3d6e6d1e7284.png)
