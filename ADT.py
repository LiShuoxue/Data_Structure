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
