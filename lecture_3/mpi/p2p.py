from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    print("Rank 0: sending")
    data = {'a': 7, 'b': 'cat'}
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print("Rank %s recieved %s" % (rank, data))
