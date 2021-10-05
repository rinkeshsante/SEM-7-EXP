from queue import PriorityQueue
import random


def printGraph(graph):
    for i in graph:
        for j in i:
            print(j+' ', end='')

        print('')


def hamigtonDist(x1, y1, x2, y2):
    return max(x1-x2, x2-x1) + max(y1-y2, y2-y1)


def backTarck(path, start, goal, visited=[]):
    myg = graph.copy()
    myg[start[0]][start[1]] = 'O'
    myg[goal[0]][goal[1]] = '#'

    print('input :')
    printGraph(myg)

    try:
        val = goal
        ans = []
        while val != start:
            ans.append(val)
            val = path[val]

        ans.append(start)

        print('output: ')

        # for i in visited:
        #     if i not in [start, goal]:
        #         myg[i[0]][i[1]] = '*'

        for i in ans[1:-1]:
            myg[i[0]][i[1]] = '='

        printGraph(myg)
    except:
        print('no solution possible')


def aStar(graph, start, goal):

    pq = PriorityQueue()
    pq.put(start, 0)
    path = {}
    g = {}
    path[start] = None
    g[start] = 0
    visited = []

    while pq.empty() == False:
        element = pq.get()

        # print(element)

        if element == goal:
            print('solution Found with cost ', g[element])
            break

        neighbor = [
            (element[0], element[1]+1),
            (element[0], element[1]-1),
            (element[0]+1, element[1]),
            (element[0]-1, element[1]),
        ]

        new_ls = []

        for i in neighbor:
            try:
                if graph[i[0]][i[1]] == '.' and i[0] != -1 and i[1] != -1:
                    new_ls.append(i)
            except:
                pass

        neighbor = new_ls

        for n in neighbor:
            cost = g[element] + \
                hamigtonDist(element[0], element[1], n[0], n[1])

            # print(n)

            if (n not in g) or (g[n] > cost):
                # print(g)
                g[n] = cost
                pq.put(n, cost + hamigtonDist(goal[0], goal[1], n[0], n[1]))
                path[n] = element
                visited.append(element)

    backTarck(path, start, goal, visited)


if __name__ == '__main__':
    lx = 6
    ly = 6

    graph = [['.' for i in range(lx)] for j in range(ly)]

    start, goal = [
        (random.randrange(0, lx, 1), random.randrange(0, ly, 1)),
        (random.randrange(0, lx, 1), random.randrange(0, ly, 1))
    ]

    for i in range(15):
        x = random.randrange(0, lx, 1)
        y = random.randrange(0, ly, 1)

        if (x, y) != start and (x, y) != goal:
            graph[x][y] = '@'

    path = aStar(graph, start, goal)
