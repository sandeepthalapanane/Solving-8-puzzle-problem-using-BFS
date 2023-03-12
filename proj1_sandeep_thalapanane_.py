import copy
import numpy as np

visit = []
Path = {}
Q = []


def input_start_goal():
    print("Enter start node column wise (Sample:1 4 7 2 5 8 3 6 0): ")
    A = [int(i) for i in input().split()]
    A_1 = ([[A[0], A[3], A[6]], [A[1], A[4], A[7]], [A[2], A[5], A[8]]])
    print("Enter goal node column wise (Sample:1 4 7 2 5 8 3 6 0): ")
    B = [int(i) for i in input().split()]
    B_1 = ([[B[0], B[3], B[6]], [B[1], B[4], B[7]], [B[2], B[5], B[8]]])
    return A_1, B_1


def transpose_tup(tup):
    tt = tuple(zip(*tup))
    return tt


def find_element(x, lst):
    res = [(i, row.index(x)) for i, row in enumerate(lst) if x in row]
    return res[0] if res else (-1, -1)


def ActionMoveUp(a, b, queue):
    out = copy.deepcopy(queue)
    out[a][b] = out[a-1][b]
    out[a-1][b] = 0
    if out not in visit:
        visit.append(out)
        Q.append(out)
        queue_1 = tuple([tuple(x) for x in queue])
        out_1 = tuple([tuple(x) for x in out])
        Path[out_1] = queue_1


def ActionMoveDown(a, b, queue):
    out = copy.deepcopy(queue)
    out[a][b] = out[a+1][b]
    out[a+1][b] = 0
    if out not in visit:
        visit.append(out)
        Q.append(out)
        queue_1 = tuple([tuple(x) for x in queue])
        out_1 = tuple([tuple(x) for x in out])
        Path[out_1] = queue_1


def ActionMoveRight(a, b, queue):
    out = copy.deepcopy(queue)
    out[a][b] = out[a][b+1]
    out[a][b+1] = 0
    if out not in visit:
        visit.append(out)
        Q.append(out)
        queue_1 = tuple([tuple(x) for x in queue])
        out_1 = tuple([tuple(x) for x in out])
        Path[out_1] = queue_1


def ActionMoveLeft(a, b, queue):
    out = copy.deepcopy(queue)
    out[a][b] = out[a][b-1]
    out[a][b-1] = 0
    if out not in visit:
        visit.append(out)
        Q.append(out)
        queue_1 = tuple([tuple(x) for x in queue])
        out_1 = tuple([tuple(x) for x in out])
        Path[out_1] = queue_1


def generate_path(path, start, goal):
    backtrack = []
    start = tuple([tuple(x) for x in start])
    goal = tuple([tuple(x) for x in goal])
    key = path.get(goal)
    backtrack.append(transpose_tup(goal))
    backtrack.append(transpose_tup(key))
    while (key != start):
        key = path.get(key)
        backtrack.append(transpose_tup(key))
    backtrack.reverse()
    return (backtrack)


def nd_info(info, path, start):
    nodes_info = []
    for i in info:
        if i == start:
            Node_Index_i = info.index(i)
            nodes_info.append([Node_Index_i, 0, i])
        else:
            Node_Index_i = info.index(i)
            goal = tuple([tuple(x) for x in i])
            key = path.get(goal)
            Parent_Node_Index_i = info.index(list([list(x) for x in key]))
            nodes_info.append([Node_Index_i, Parent_Node_Index_i, i])
    return nodes_info


def bfs():
    Start, Goal = input_start_goal()
    Q.append(Start)
    visit.append(Start)
    while (len(Q) != 0):
        queue = Q.pop(0)
        a, b = find_element(0, queue)
        if (queue != Goal):
            if ((a-1) >= 0 and b < 3):
                ActionMoveUp(a, b, queue)
            if ((a+1) < 3 and b < 3):
                ActionMoveDown(a, b, queue)
            if ((a) < 3 and (b-1) >= 0):
                ActionMoveLeft(a, b, queue)
            if (a < 3 and (b+1) < 3):
                ActionMoveRight(a, b, queue)
        else:
            print('success')
            backtrack = generate_path(Path, Start, Goal)
            bt = []
            for i in backtrack:
                a = np.concatenate((i))
                b = "".join(str(a)[1:-1])
                bt.append(b)
            open('nodePath.txt', 'w').write('\n'.join('%s' % x for x in bt))

            ls = []
            for i in visit:
                lt = list(map(list, zip(*i)))
                a = np.concatenate((lt))
                b = "".join(str(a)[1:-1])
                ls.append(b)
            open('Nodes.txt', 'w').write('\n'.join('%s' % x for x in ls))

            node_inf = nd_info(visit, Path, Start)
            ni = []
            for i in node_inf:
                lt = list(map(list, zip(*i[2])))
                a = np.concatenate((lt))
                b = "".join(str(a)[1:-1])
                c = str(i[0])
                d = str(i[1])
                e = c + "      "+d+"       "+b
                ni.append(e)
            open('NodesInfo.txt', 'w').write('\n'.join('%s' % x for x in ni))
            break


bfs()
