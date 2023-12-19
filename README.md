# AED3

## TSP Solution Implementation

Este repositório contém implementações de dois algoritmos em Python que resolvem o Travelling Salesman Problem (TSP): algoritmo de força bruta e outro utilizando Kruskal

Como Executar
  1. Configuração do Ambiente

Abra o terminal de acordo com o sistema operacional:

    Para Linux/MacOS, utilize o terminal do sistema.
    Para Windows, abra o Prompt de Comando. Também é possível usar um terminal integrado em um ambiente de desenvolvimento.

Certifique-se de ter a biblioteca scipy instalada. Para instalá-la, execute o seguinte comando no terminal:

    pip install scipy

Navegue até o diretório do script usando o comando cd:

    cd caminho/para/o/diretorio

  2. Execução do Programa

Utilize um dos seguintes comandos, dependendo da configuração do seu ambiente Python:

    python tsp.py nome_arquivo.txt numero_source a

ou

    python tsp.py nome_arquivo.txt numero_source b

  Substitua nome_arquivo.txt pelo nome do arquivo de texto que contém a matriz (por exemplo, tsp1_253.txt).
  Substitua numero_source por um número inteiro que indica a origem a partir da qual a matriz será lida (por exemplo, 0).
  Escolha a se desejar utilizar o algoritmo aproximativo (Kruskal), ou b se preferir o algoritmo de força bruta.

Exemplo:

    python tsp.py tsp1_253.txt 0 a

Isso executará o programa com o arquivo tsp1_253.txt, começando da origem 0 e utilizando o algoritmo aproximativo.
