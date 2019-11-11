from ADT import MyPrioQueue
class Algorithm:

    @staticmethod
    def Prim(graph):
        mst = [None for x in range(graph._vnum)]
        cands = MyPrioQueue([(0,0,0)])
        counter = 0
        while  counter < graph._vnum and not cands.is_empty():
            atuple = cands.dequeue()
            cand_weight, vi, vj = atuple[0], atuple[1], atuple[2]
            if mst[vj]:
                continue
            mst[vj] = ((vi, vj), cand_weight)
            counter += 1
            alist = graph.out_edges(vj)
            for blist in alist:
                vk, cand_weight2 = blist[0], blist[1]
                if not mst[vk]:
                    cands.enqueue((cand_weight2, vj, vk))
        return mst[1:]

    @staticmethod
    def Kruskal(graph):
        vnum = graph._vnum
        reps = [i for i in range(vnum)]
        mst, edges = [], []
        for vi in range(vnum):
            for x in graph.out_edges(vi):
                vj = x[0]
                weight = x[1]
                edges.append((weight, vi, vj))
        edges.sort()
        for atuple in edges:
            w, v_from, v_to = atuple[0], atuple[1], atuple[2]
            if reps[v_from] != reps[v_to]:
                mst.append(((v_from, v_to), w))
                if len(mst) == vnum - 1:
                    break
                rep, orep = reps[v_from], reps[v_to]
                for i in range(vnum):
                    if reps[i] == orep:
                        reps[i] = rep
        return mst
    
    @staticmethod
    def Dijkstra(graph, v0):
        vnum = graph.vertex_num()
        assert 0 <= v0 < vnum
        paths = [None]*vnum
        count = 0
        cands = MyPrioQueue([(0, v0, v0)])
        while count < vnum and not cands.is_empty():
            plen, u, vmin = cands.dequeue()
            if paths[vmin]:
                continue
            paths[vmin] = (u, plen)
            for v, w in graph.out_edges(vmin):
                if not paths[v]:
                    cands.enqueue((plen+w, vmin, v))
            count += 1
        return paths
    
    @staticmethod
    def Floyd(graph):
        vnum = graph.vertex_num()
        a = [[graph.get_edge(i, j) for j in range(vnum)] for i in range(vnum)]
        nvertex = [[-1 if a[i][j] > 1000 else j for j in range(vnum)] for i in range(vnum)]
        
        for k in range(vnum):
            for i in range(vnum):
                for j in range(vnum):
                    if a[i][j] > a[i][k] + a[k][j]:
                        a[i][j] = a[i][k] + a[k][j]
                        nvertex[i][j] = nvertex[i][k]
                        
        for x in range(vnum):
            a[x][x] = 0
            nvertex[x][x] = 0
        return(a, nvertex)
        
    @staticmethod
    def toposort(graph):
        vnum = graph.vertex_num()
        indegree, toposeq = [0]*vnum, []
        zerov = -1
        for vi in range(vnum):
            for v, w in graph.out_edges(vi):
                indegree[v] += 1
        for vi in range(vnum):
            if indegree[vi] == 0:
                indegree[vi] = zerov
                zerov = vi    
        for n in range(vnum):
            if zerov == -1:
                return False
            vi = zerov
            zerov = indegree[zerov]
            toposeq.append(vi)
            for v, w in graph.out_edges(vi):
                indegree[v] -= 1
                if indegree[v] == 0:
                    indegree[v] = zerov
                    zerov = v
        return toposeq
