from time import time
from bfs import bfs_search
from rbfs import rbfs_search
from puzzle import Puzzle


state=[[1, 2, 3,
        0, 4, 5,
        7, 8, 6],

       [0, 2, 3,
        1, 4, 5,
        7, 8, 6]]
for i in range(0,2):
    Puzzle.num_of_instances=0
    t0=time()
    bfs=bfs_search(state[i])
    t1=time()-t0
    print('BFS:')
    print('space:',Puzzle.num_of_instances)
    print('time:', t1)
    print()

    print('------------------------------------------')

    Puzzle.num_of_instances = 0
    t0 = time()
    RBFS = rbfs_search(state[i])
    t1 = time() - t0
    print('RBFS:',)
    print('space:', Puzzle.num_of_instances)
    print('time:', t1)
    print()

    print('------------------------------------------')