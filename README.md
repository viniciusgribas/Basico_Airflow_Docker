# Introdução

## Conceitos básicos para o Docker

### O que é um container:

-   A origem do nome container, para software, detém o mesmo significado de containers físicos. Ambos, inclusive, tem a mesma finalidade de compartimentação, transporte e armazenamento.
  
-   A compartimentação, possibilita que conteiners carreguem qualquer tipo de produto em um único ambiente, sendo práticos, principalmente quando se pretende abri-los e fecha-los em qualquer lugar, independente do tipo de transporte utilizado ou o que se quer armazenar.

-   A analogia acima é muito válida para se explicar conteiners em software, uma vez que buscamos armazenar códigos e todo o seu ambiente em um único local, de forma que seja possível compartilha-lo e roda-lo em qualquer outro computador. Este local é o container.

-   O intuito disto é certificar que o mesmo ambiente em que o código foi desenvolvido por mim, seja o mesmo ambiente em que o código vai rodar para você e pra qualquer outra pessoa, uma vez que todo o ambiente é armazenado em um container.

-  Isso certifica que não teremos problemas de ambientes distintos como configurações de máquina, atualizações de bibliotecas e virtualização de máquinas.

-  Portanto, o container é uma unidade padrão para software. Assim como o metro é uma unidade padrão para medir distância.

### Vantagens de se usar um container:

- Ao contrário de máquinas virtuais, os containers são unidades específicas para rodar ambientes de códigos e todas as suas dependências.

- Containers são Consistentes, ideais para ambientes de testes, execução e desenvolvimento.

- São versáteis e adaptáveis, rodam em qualquer Sistema Operacional.

- O conceito é: Construa uma vez, rode-os sempre e em qualquer lugar.

- Conteiners apresentam a vantagem de serem menos pesados quando em comparação à uma virtualização de máquina.
  
- Apresentam a possibilidade de criação de imagens, que são uma "foto" do que contém no container, estas consistem em um arquivo binário (como um arquivo .txt), sendo então mais leves ainda.

- A vantagem consiste no fato de que apenas a leitura do arquivo imagem, já possibilita a execução de um arquivo container. Possibilitando a reprodução exata do ambiente armazenado no container.

### O que é o software Docker:

- O docker é por essência uma ferramenta de linha de comando, ou seja, uma ferramenta de CLI (Command Line Tool) que executa comandos específicos para tratar containers. Ele em si não é um container e sim uma ferramenta que permite a operacionalização de containers (principalmente Construir, Rodar e Compartilhar).

- Logo o docker é um dos softwares para se trabalhar com containers. Sendo por muitos, considerado o mais popular.

### Fluxo padrão para criação de um dockerfile:

1) Os arquivos do ambiente são armazenados em um "container file" via Docker-CLI (comando: BUILD), gerando um "Dockerfile";
2) Via Docker-CLI (comando: BUILD) o docker constroi uma imagem container a partir do "dockerfile";
3) Docker-CLI (comando: RUN) o docker utiliza de sua "Container Execution Engine" para executar a imagem de container;
4) Após a execução do container, é possível armazená-lo em núvem em um "Container Registry" via Docker-CLI(comando: PUSH); e
5) De forma análoga, é possível "puxar" os containers armazenados em um "Container Registry" via Docker-CLI(comando: PULL).
6) A boa notícia é que para projetos em python, toda a etapa acima já foi construída e [disponibilizada pela comunidade](https://hub.docker.com/_/python).
7) Logo, uma prática comum ao se desenvolver em python, é já utilizar esta base disponibilizada para construir os arquivos "dockerfile".
8) A sintaxe do arquivo "dockerfile" pode variar de projeto para projeto, uma vez que o ambiente e as bibliotecas utilizadas, também variam. Logo, pode-se fazer necessário alterar os seus parâmetros para adequa-los aos mesmos do ambiente de desenvolvimento.

## Conceitos básicos para o airflow

---
# Passo a Passo da execução de um container contendo um projeto orquestrado pelo airflow:

## Criando um Conteiner Docker executável com o Airflow
Fluxo de trabalho com o docker
1) Crie um projeto de análise exploratória:
   1) Para este projeto, foi utilizado um projeto previamente realizado por mim, onde é feita uma raspagem de dados no site da CNN. O projeto está no repositório [Energy News Scrapping](https://github.com/viniciusgribas/EnergyNewsScrapping).
   2) Para a criação do dockerfile deste projeto, foi gerado um arquivo "requiriments.txt", contendo as informações referentes às bibliotecas de desenvolvimento do projeto [WebScrape_CNN_NEWS.py](https://github.com/viniciusgribas/Basico_Airflow_Docker/blob/main/CNN%20News/py/CNN_WordCloud.py).
   
2) Crie o arquivo 'requiriments.txt' contendo informações das bibliotecas python do projeto:
   1) A criação do arquivo "requiriments.txt" foi feita pela biblioteca pireqs. A melhor prática para esta biblioteca, é isolar o projeto python em uma única pasta, onde contém o código e posteriormente será gerado o "requiriments.txt".
 > `` $YOUR_PROJECT_PATCH> pipreqs``

3) Crie um dockerfile para python, com as informações necessárias para aplicar o airflow:
   1) Sobreponha as bibliotecas que estão importadas no arquivo dockerfile padrão e cole as do 'requiriments.txt'.

   
4) Auxilie a ambientação do airflow:
   1) Crie um entrypoint.sh com as configurações padrões.
   2) Crie um airflow_settings.yaml com as configurações padrões.
   3) Crie um airflow.cfg com as configurações padrões.
   4) Crie uma pasta com de nome 'dags'.
   
5) Entre na pasta onde está o dockerfile via 'Windows Power Shell', faça a construção e dê nome à imagem do docker com base no dockerfile e arquivos criados:
   1) Para isso, utilize o comando abaixo, formalizando a criação da imagem do docker, executável pelo airflow, de nome 'nome_da_imagem_airflow.
   > `  docker build -t nome_da_imagem_airflow .`

6) Rode a imagem 'nome_da_imagem_airflow ' no airflow:
   1) Para esta etapa, a imagem já foi criada pelo docker e já está em execução.
   2) agora, devemos criar e nomear uma instância da imagem para o airflow, aqui vou utilizar o nome 'nome_da_instancia_aiflow'.
   3) por padrão, esta instância airflow será criada na porta 8080.
   4) como já explicado, deve-se ter a pasta 'dags'.
   5) o comando abaixo executa o airflow web localmente via docker:
   > `docker run -p 8080:8080 -it -v ${PWD}/dags/:/root/airflow/dags --name nome_da_instancia_aiflow nome_da_imagem_airflow bash`
   - conforme o comando acima, o airflow será executado na porta [8080](http://localhost:8080).

     
