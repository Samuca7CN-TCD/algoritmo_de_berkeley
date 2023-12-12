# Sincronização de Relógios usando o Algoritmo de Berkeley em MPI

## Disciplina

Sistemas Distribuídos

Professor: Paulo André Sperandio Giacomin

## Autor

Samuel Correia Nascimento

Matrícula: 201920081

## Escolha da Linguagem Python

Este código foi desenvolvido em Python devido à sua simplicidade, legibilidade e ampla adoção na comunidade de desenvolvimento. A linguagem Python é particularmente adequada para expressar algoritmos de forma concisa.

## MPI (Message Passing Interface)

O código utiliza a biblioteca MPI (Message Passing Interface) para programação paralela e distribuída. MPI permite a comunicação entre processos, sendo essencial para a implementação de algoritmos distribuídos.

## Algoritmo de Berkeley

O Algoritmo de Berkeley é uma abordagem para sincronização de relógios em sistemas distribuídos. O processo coordenador, chamado "Daemon" neste código, desempenha um papel crucial na coleta e cálculo das diferenças de tempo entre os diferentes processos.

### Passos do Algoritmo:

1. **Geração de Tempos Iniciais Aleatórios:** Cada processo gera um tempo inicial aleatório com uma variação de 10 a 1000 segundos.

2. **Envio do Tempo do Daemon:** O Daemon envia seu tempo inicial para todos os processos.

3. **Cálculo da Diferença:** Cada processo calcula a diferença entre seu próprio tempo e o tempo do Daemon.

4. **Envio das Diferenças ao Daemon:** Todos os processos enviam suas diferenças de volta para o Daemon.

5. **Cálculo da Média das Diferenças:** O Daemon calcula a média das diferenças recebidas.

6. **Cálculo dos Ajustes:** O Daemon calcula os ajustes necessários para sincronização.

7. **Envio dos Ajustes:** O Daemon envia os ajustes para cada processo.

8. **Soma dos Ajustes:** Cada processo soma seu próprio tempo com o ajuste recebido, resultando nos tempos sincronizados.

O código inclui comentários detalhados para cada parte do algoritmo, facilitando a compreensão do seu funcionamento.

## Execução do Código

Para executar o código, é necessário ter a biblioteca MPI instalada. Utilize o seguinte comando:

OBS: Guia de instalação da biblioteca MPICH2: https://mpitutorial.com/tutorials/installing-mpich2/

```bash
mpirun -n 5 python main.py
```

OBS: Observe que o número de processos criado é 5, pois é o resto da divisão da soma dos algarismos do meu número de matrícula por 6, assim como especificado na descrição do projeto: (2+0+1+9+2+0+0+8+1) % 6 = 5
