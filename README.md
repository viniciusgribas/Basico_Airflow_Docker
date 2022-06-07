### Introdução

O que é um container:

-   A origem do nome container, para software, detém o mesmo significado de containers físicos. Ambos, inclusive, tem a mesma finalidade de' compartimentação, transporte e armazenamento.
  
-   A compartimentação, possibilita que conteiners carreguem qualquer tipo de produto em um único ambiente, sendo práticos, principalmente quando se pretende abri-los e fecha-los em qualquer lugar, independente do tipo de transporte utilizado ou o que se quer armazenar.

-   A analogia acima é muito válida para se explicar conteiners em software, uma vez que buscamos armazenar códigos e todo o seu ambiente em um único local, de forma que seja possível compartilha-lo e roda-lo em qualquer outro computador. Este local é o container.

-   O intuito disto é certificar que o mesmo ambiente em que o código foi desenvolvido por mim, seja o mesmo ambiente em que o código vai rodar para você e pra qualquer outra pessoa, uma vez que todo o ambiente é armazenado em um container.

-  Isso certifica que não teremos problemas de ambientes distintos como configurações de máquina, atualizações de bibliotecas e virtualização de máquinas.

-  Portanto, o container é uma unidade padrão para software. Assim como o metro é uma unidade padrão para medir distância.

Vantagens de se usar um container:

- Ao contrário de máquinas virtuais, os containers são unidades específicas para rodar ambientes de códigos e todas as suas dependências.

- Containers são Consistentes, ideais para ambientes de testes, execução e desenvolvimento.

- São versáteis e adaptáveis, rodam em qualquer Sistema Operacional.

- O conceito é: Construa uma vez, rode-os sempre e em qualquer lugar.

- Conteiners apresentam a vantagem de serem menos pesados quando em comparação à uma virtualização de máquina.
  
- Apresentam a possibilidade de criação de imagens, que são uma "foto" do que contém no container, estas consistem em um arquivo binário (como um arquivo .txt), sendo então mais leves ainda.

- A vantagem consiste no fato de que apenas a leitura do arquivo imagem, já possibilita a execução de um arquivo container. Possibilitando a reprodução exata do ambiente armazenado no container.

O que é o software Docker:

- O docker é por essência uma ferramenta de linha de comando, ou seja, uma ferramenta de CLI (Command Line Tool) que executa comandos específicos para tratar containers. Ele em si não é um container e sim uma ferramenta que permite a operacionalização de containers (principalmente Construir, Rodar e Compartilhar).

- Logo o docker é um dos softwares para se trabalhar com containers. Sendo por muitos, considerado o mais popular.

Fluxo padrão:

1) Os arquivos do ambiente são armazenados em um "container file" via Docker-CLI (comando: BUILD), gerando um "Dockerfile";
2) Via Docker-CLI (comando: BUILD) o docker constroi uma imagem container a partir do "dockerfile";
3) Docker-CLI (comando: RUN) o docker utiliza de sua "Container Execution Engine" para executar a imagem de container;
4) Após a execução do container, é possível armazená-lo em núvem em um "Container Registry" via Docker-CLI(comando: PUSH); e
5) De forma análoga, é possível "puxar" os containers armazenados em um "Container Registry" via Docker-CLI(comando: PULL).
