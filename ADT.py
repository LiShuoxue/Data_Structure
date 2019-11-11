class LNode():
    def __init__(self, elem=None, nxt=None):
        self._elem = elem
        self._next = nxt

class StackUnderflow(ValueError):
    pass

class QueueUnderflow(ValueError):
    pass

class PrioQueueError(ValueError):
    pass      

class TreeUnderFlow(ValueError):
    pass

class GraphError(ValueError):
    pass

class MyStack:
        
    def __init__(self):
        self._top = None
        
    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in MyStack.top()")
        return self._top._elem

    def push(self,elm):
        self._top = LNode(elm,self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in MyStack.top()")
        p = self._top
        self._top = p._next
        return p._elem

    def __len__(self):
        k = 0
        a = self._top
        while a is not None:
            a = a._next
            k += 1 
        return k
    
    def __str__(self):
        astr = '--'
        a = self._top
        while a is not None:
            bstr = ' ' + str(a._elem) + ' '    
            astr = bstr + astr
            a = a._next
        astr = '--' + astr
        return astr

class MyQueue:

    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    def enqueue(self,elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear._next = LNode(elem)
            self._rear = self._rear._next

    def dequeue(self):
        if self._head is None:
            raise QueueUnderflow('in MyQueue.dequeue()')
        else:
            p = self._head
            self._head = self._head._next
            return p._elem

    def top(self):
        if self._head is None:
            raise QueueUnderflow('in MyQueue.top()')
        else:
            return self._head._elem

    def bottom(self):
        if self._head is None:
            raise QueueUnderflow('in MyQueue.bottom()')
        else:
            return self._rear._elem

    def __len__(self):
        p = self._head
        counter = 0
        while p != None:
            p = p._next
            counter += 1
        return counter

    def __str__(self):
        p = self._head
        astr = ' --'
        while p != None:
            bstr = str(p._elem) 
            astr = astr + bstr
            p = p._next
        astr += '-- '
        return astr
    
class MyBinTree:
    
    def __init__(self, data = None, left = None, right  = None):
        self._data = data
        self._left = left
        self._right = right
        
    def is_empty(self):
        return self._data is None
    
    def data(self):
        return self._data
    
    def left(self):
        return self._left
    
    def right(self):
        return self._right
    
    def set_left(self, btree):
        self._left = btree
        
    def set_right(self, btree):
        self._right = btree
        
    def num_nodes_rec(self):
        if self._left is None and self._right is None:
            return 1 
        elif self._left is None and self._right is not None:
            return 1 + self._right.num_nodes_rec()
        elif self._right is None and self._left is not None:
            return 1 + self._left.num_nodes_rec()
        else:
            return 1 + self._left.num_nodes_rec() + self._right.num_nodes_rec()
        
    def preorder_nonrec(self):
        bt = self
        alist = []
        st = MyStack()
        while bt is not None or not st.is_empty():
            while bt is not None:
                alist.append(bt._data)
                st.push(bt._right)
                bt = bt._left
            bt = st.pop()
        return alist
    
    def postorder_nonrec(self):
        bt = self 
        alist = []
        st = MyStack()
        while bt is not None or not st.is_empty():
            while bt is not None:
                st.push(bt)
                bt = bt._left if bt._left is not None else bt._right
            bt = st.pop()
            alist.append(bt._data)
            if not st.is_empty() and st.top()._left == bt:
                bt = st.top()._right
            else:
                bt = None
        return alist

    def inorder_nonrec(self):
        bt = self
        alist = []
        st = MyStack()
        while bt is not None or not st.is_empty():
            while bt is not None:
                st.push(bt)
                bt = bt._left
            bt = st.pop()
            alist.append(bt._data)
            bt = bt._right
        return alist
    
class MyPrioQueue:
    def __init__(self, elist = []):
        self._elems = list(elist)
        if elist:
            self.buildheap()
            
    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self._elems[0]
    
    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)
        
    def siftup(self, e, last):
        elems, i, j = self._elems, last , (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e
        
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self._elems 
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0
    
    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e
        
    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

    
class MyTree_Firstson_Brother:
    def __init__(self, data=None, forest=[]):
        self._data = data
        self._firstson = None
        self._brother = None
        
        if len(forest) == 0:
            self._data = data
        elif len(forest) == 1:
            self._firstson = forest[0] 
        else:
            for x in range(len(forest)-2, -1, -1):
                forest[x]._brother = forest[x+1] 
            self._firstson = forest[0]
            
    def is_empty(self):
        return self._data is None
        
    def data(self):
        return self._data
    
    def first_child(self, node):
        return node._firstson
    
    def children(self, node):
        alist = []
        forest = node._firstson
        alist.append(forest)
        while forest._brother is not None:
            forest = forest._brother
            alist.append(forest)
        return alist
    
    def set_first(self, tree):
        self._firstson = tree
        
    def insert_child(self, i, tree):
        node = self
        a = len(self.children(node))
        if i > a:
            raise TreeUnderFlow('in insert_child')
        else:
            if i <= 0:
                self.set_first(tree)
            else:
                forest = self._firstson
                for x in range(i-1):
                    forest = forest._brother
                tree._brother = forest._brother
                forest._brother = tree

    def preorder(self):
        alist = []
        tr = self
        st = MyStack()
        while not tr is None or not st.is_empty():
            while not tr is None:
                alist.append(tr._data)
                st.push(tr)
                tr = tr._firstson
            while tr is None and not st.is_empty():
                tr = st.pop()._brother
        return alist
    
    def inorder(self):
        alist = []
        tr = self
        qu = MyQueue()
        if tr is None:
            return []
        qu.enqueue(tr)
        while not qu.is_empty():
            tr = qu.dequeue()
            if tr is None:
                continue
            alist.append(tr._data)
            tr = tr._firstson
            while tr is not None:
                qu.enqueue(tr)
                tr = tr._brother
        return alist
    
class MyGraph_Matrix:
    
    def __init__(self, vnum, inf=1024):
        self._inf = inf
        self._vnum = vnum
        self._enum = 0
        self._mat = [[self._inf for x in range(self._vnum)] for y in range(self._vnum)]
        
    def is_empty(self):
        return self._vnum == 0        
    def vertex_num(self):
        return self._vnum    
    def edge_num(self):
        return self._enum    
    def vertex_invalid(self, v):
        return 0 > v or v > self._vnum
    
    def add_edge(self, vi, vj, weight = 1):
        if self.vertex_invalid(vi) or self.vertex_invalid(vj):
            raise GraphError('In \'add_edge\': The vertex may be out of range!')
        else:
            if self._mat[vi][vj] is not self._inf:
                print('Only change the element self._mat[%d][%d] from %d to %d.'%(vi, vj, self._mat[vi][vj], weight))
                pass
            else:
                self._enum += 1
            self._mat[vi][vj] = weight
        
    def delete_edge(self, vi, vj):
        if self.vertex_invalid(vi) or self.vertex_invalid(vj):
            raise GraphError('In \'delete_edge\': The vertex may be out of range!')
        else:
            if self._mat[vi][vj] != self._inf:
                print('The element self._mat[%d][%d] is just infinite.'%(vi, vj))
                pass
            else:
                self._enum -= 1
                self._mat[vi][vj] = self._inf
            
    def get_edge(self, vi, vj):
        if self.vertex_invalid(vi) or self.vertex_invalid(vj):
            raise GraphError('In \'get_edge\': The vertex may be out of range!')
        else:
            return self._mat[vi][vj]
        
    def add_vertex(self):
        for x in range(self._vnum):
            self._mat[x].append(self._inf)
        self._vnum += 1
        self._mat.append([self._inf for y in range(self._vnum)])
        
    def out_edges(self, vi):
        if self.vertex_invalid(vi):
            raise GraphError('In \'out_edges\': The vertex may be out of range!')
        else:
            alist = []
            for x in range(self._vnum):
                if self._mat[vi][x] != self._inf:
                    alist.append([x, self._mat[vi][x]])
            return alist
        
    def in_edges(self, vi):
        if self.vertex_invalid(vi):
            raise GraphError('In \'in_edges\': The vertex may be out of range!')
        else:
            alist = []
            for x in range(self._vnum):
                if self._mat[x][vi] != self._inf:
                    alist.append([x, self._mat[x][vi]])
            return alist
        
    def all_edges(self):
        edges = []
        for vi in range(self._vnum):
            for x in self.out_edges(vi):
                vj = x[0]
                weight = x[1]
                edges.append((vi, vj, weight))
        return edges
        
    def __str__(self):
        bstr = ''
        for x in range(self._vnum):
            astr = ''
            for y in range(self._vnum):
                astr += str(self._mat[y][x])
                astr += '\t'
            bstr += astr
            bstr += '\n'
        return bstr
    
    @staticmethod
    def import_graph(vnum = 10):
        data = open(r'D:\李硕学\数据结构\graph_point.txt').readlines()
        edgelist = [[int(y) for y in x.split()] for x in data]
        gr = MyGraph_Matrix(vnum)
        for x, y, w in edgelist:
            gr.add_edge(x, y, w)
        return gr 
    
class MyGraph_Table:
    def __init__(self, vnum, alist):
        self._vnum = vnum
        self._enum = 0
        self._table = [[x, []] for x in alist]
    
    def is_empty(self):
        return self._table == []
    def vertex_num(self):
        return self._vnum    
    def edge_num(self):
        return self._enum    
    def vertex_invalid(self, v):
        return 0 > v or v >= self._vnum
    
    def add_edge(self, vi, vj, weight = 1):
        if self.vertex_invalid(vi) or self.vertex_invalid(vj):
            raise GraphError('In \'add_edge\': The vertex may be out of range!')
        else:
            for x in self._table[vi][1]:
                if x[0] == vj:
                    print('Only change the element self._mat[%d][%d] from %d to %d.'%(vi, vj, x[1], weight))
                    x[1] = weight
                    break
            else:
                self._table[vi][1].append([vj, weight])
                self._enum += 1
        
    def delete_edge(self, vi, vj):
        if self.vertex_invalid(vi) or self.vertex_invalid(vj):
            raise GraphError('In \'delete_edge\': The vertex may be out of range!')
        else:
            for x in self._table[vi][1]:
                if x[0] == vj:
                    self._table[vi][1].remove(x)
                    self._enum -= 1
                    break
            else:
                print('The element self._mat[%d][%d] is just infinite.'%(vi, vj))
        
    def get_edge(self, vi, vj):
        if self.vertex_invalid(vi) or self.vertex_invalid(vj):
            raise GraphError('In \'get_edge\': The vertex may be out of range!')
        else:
            for x in self._table[vi][1]:
                if x[0] == vj:
                    return x[1]
                    break
            else:
                raise GraphError('In \'get_edge\': The vertex(%d, %d) you search do not have an edge!'%(vi, vj))
                
    def add_vertex(self, name = None):
        if name == None:
            self._table.append([self._vnum, []])
        else:
            self._table.append([name, []])
        self._vnum += 1
        
    def out_edges(self, vi):
        if self.vertex_invalid(vi):
            raise GraphError('In \'out_edges\': The vertex may be out of range!')
        else:
            return self._table[vi][1]
        
    def in_edges(self, vi):
        if self.vertex_invalid(vi):
            raise GraphError('In \'in_edges\': The vertex may be out of range!')
        else:
            alist = []
            for x in range(self._vnum):
                for y in self._table[x][1]:
                    if y[0] == vi:
                        alist.append([x, y[1]])
                        break
            return alist
        
    def __str__(self):
        astr = ''
        for x in self._table:
            astr += str(x[0])
            astr += ':\t'
            bstr = ''
            for y in x[1]:
                bstr += str(y)
                bstr += '\t'
            astr += bstr
            astr += '\n'
        return astr
    
    @staticmethod
    def import_graph(vnum = 10, path):
        data = open(r'%s'%(path)).readlines()
        edgelist = [[int(y) for y in x.split()] for x in data]
        gr = MyGraph_Table(vnum, range(vnum))
        for x, y, w in edgelist:
            gr.add_edge(x, y, w)
        return gr 
