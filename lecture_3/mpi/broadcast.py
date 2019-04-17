from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'key1' : [1,2,3],
            'key2' : ('type', 'cat')}
else:
    data = None

data = comm.bcast(data, root=0)
print("Rank %s recieved %s" % (rank, data))
