# Backdoor Python (Socket-based)
Este projeto implementa um **backdoor** simples em Python que utiliza comunicação cliente-servidor via sockets. O servidor atua como um agente de controle remoto, permitindo ao cliente executar comandos de terminal no sistema remoto. O cliente pode enviar comandos ao servidor e receber a saída desses comandos.

**Aviso Legal**: Este projeto é apenas para fins educacionais e de pesquisa. O uso inadequado, como atividades não autorizadas ou maliciosas, pode violar leis de privacidade e segurança digital. Use com responsabilidade!

## Visão Geral
O projeto é composto de dois scripts principais:

server.py: Executa o lado do servidor (agente backdoor) e aguarda por comandos.
main.py: Executa o lado do cliente, que envia comandos ao servidor e exibe a resposta.
O cliente se conecta ao servidor e pode executar comandos remotamente como cd, listar diretórios ou outros comandos de terminal. O servidor responde com a saída dos comandos ou mensagens de erro.

Requisitos
Python 3.x
Bibliotecas padrão do Python: socket, sys, os, subprocess, time
Instalação
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/socket-backdoor.git
cd socket-backdoor
Verifique se você tem o Python 3.x instalado:

bash
Copiar código
python3 --version
Como Usar
Passo 1: Inicie o servidor
No servidor, execute o script server.py para iniciar o "backdoor":

bash
Copiar código
python3 server.py
O servidor ficará escutando na porta 4065 do localhost (127.0.0.1), pronto para aceitar conexões de um cliente.

Passo 2: Conecte o cliente ao servidor
No cliente (máquina atacante), execute o script main.py passando o IP e a porta do servidor como parâmetros:

bash
Copiar código
python3 main.py 127.0.0.1 4065
Agora você pode enviar comandos de terminal para o servidor remotamente e visualizar as saídas.

Exemplos de Comandos
Navegação de diretórios:

bash
Copiar código
rce@noname404:~$ cd /path/to/directory
Listar arquivos no diretório:

bash
Copiar código
rce@noname404:~$ ls
Executar qualquer comando do sistema:

bash
Copiar código
rce@noname404:~$ whoami
Funcionalidades
Conexão via socket entre cliente e servidor.
Execução de comandos do sistema no servidor através do cliente.
Tratamento de erros para diretórios inexistentes ou comandos sem saída.
Reenvio automático de conexão em caso de falha de rede (cliente tenta reconectar).
Estrutura do Projeto
bash
Copiar código
.
├── main.py         # Script do cliente
└── server.py       # Script do servidor
Segurança
Este projeto não possui mecanismos avançados de segurança.
Não utilize em ambientes de produção ou redes inseguras.
Adicione criptografia (TLS/SSL) para proteger a comunicação entre cliente e servidor.
Melhorias Futuras
Adicionar autenticação para garantir que apenas usuários autorizados possam acessar o servidor.
Implementar criptografia para proteger a transmissão de dados.
Desenvolver um sistema de logs robusto para auditoria de comandos executados.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
