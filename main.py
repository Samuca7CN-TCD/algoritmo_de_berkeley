from mpi4py import MPI
import time
import random


def berkeley_algorithm(rank, size):
    comm = MPI.COMM_WORLD
    daemon = 0  # O processo 0 é o daemon

    # Passo 0: Todos os processos geram um tempo inicial aleatório
    # Adiciona uma variação de -5 a 5 segundos
    my_time = int(random.uniform(10, 100))
    print(f"Processo {rank}: Tempo inicial: {my_time}")

    # Passo 1: Coordenador (Daemon) envia seu tempo para todos os processos
    if rank == daemon:
        current_time = my_time
        print(
            f"Daemon ({rank}): Enviando tempo {current_time} para todos os processos")
        for i in range(size):
            if i != daemon:
                comm.send(current_time, dest=i)

    # Passo 2: Cada processo calcula a diferença entre seu próprio tempo e o tempo do daemon
    else:
        daemon_time = comm.recv(source=daemon)
        difference = my_time - daemon_time
        print(f"Processo {rank}: Diferença calculada: {difference}")

        # Passo 3: Todos os relógios enviam a diferença calculada de volta para o daemon
        comm.send(difference, dest=daemon)

    # Passo 4: O daemon recebe todas as diferenças
    if rank == daemon:
        differences = []
        for i in range(1, size):
            difference = comm.recv(source=i)
            differences.append(difference)
            print(
                f"Daemon ({rank}): Recebida diferença {difference} do processo {i}")

        # Passo 5: O daemon calcula a média das diferenças
        average_difference = sum(differences) / (len(differences) + 1)
        print(f"Daemon ({rank}): Média das diferenças: {average_difference}")

        # Passo 6: O daemon calcula o ajuste que precisa ser feito em cada relógio
        adjustments = [average_difference - diff for diff in differences]
        print(f"Daemon ({rank}): Ajustes calculados: {adjustments}")

        # Passo 7: O daemon envia cada ajuste para o seu respectivo processo
        current_time += average_difference
        print(f"Processo {0}: Tempo sincronizado: {current_time}")
        for i in range(1, size):
            comm.send(adjustments[i - 1], dest=i)
            print(
                f"Daemon ({rank}): Enviando ajuste {adjustments[i - 1]} para o processo {i}")

    # Passo 7: Cada processo soma seu próprio tempo com o tempo do ajuste recebido
    else:
        adjustment = comm.recv(source=daemon)
        my_time += adjustment
        print(f"Processo {rank}: Tempo sincronizado: {my_time}")


if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    berkeley_algorithm(rank, size)
