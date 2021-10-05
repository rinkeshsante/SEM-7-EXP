import random


def printGraph(graph):
    for i in graph:
        for j in i:
            print(j+' ', end='')

        print('')


def getNeighbor(graph, element):
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

    return new_ls


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


def bfs(graph, start, goal):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    path = {}

    while len(queue) != 0:
        element = queue.pop(0)
        if element == goal:
            print('found')
            break

        neighbor = getNeighbor(graph, element)

        for n in neighbor:
            if n not in visited:
                queue.append(n)
                visited.append(n)
                path[n] = element

    backTarck(path, start, goal, visited)


if __name__ == '__main__':
    lx = 6
    ly = 6

    graph = [['.' for i in range(lx)] for j in range(ly)]

    start, goal = [
        (random.randrange(0, lx, 1), random.randrange(0, ly, 1)),
        (random.randrange(0, lx, 1), random.randrange(0, ly, 1))
    ]

    for i in range(10):
        x = random.randrange(0, lx, 1)
        y = random.randrange(0, ly, 1)

        if (x, y) != start and (x, y) != goal:
            graph[x][y] = '@'

    bfs(graph, start, goal)
