from ADT import MyBinTree, MyGraphAl, MyStack, MyQueue

class Transition_System(MyGraphAl):
    def __init__(self, states):
        self._vnum = len(states)
        self._table = [[] for x in range(self._vnum)]
        self._dict = dict(zip(states,range(self._vnum)))
        self._states = states
        
    def add_action(self, start, end, action):
        self.add_edge(self._dict[start], self._dict[end], action)
        
class Formula_Tree(MyBinTree):
    def __init__(self, vnum):
        self._bool = [False for x in range(vnum)]
        self._eg = [[] for x in range(vnum)]
        
    def boolean(self):
        return self._bool
    
    def example(self):
        return self._eg
        
class Checking:
    def __init__(self, tree, TS):
        self._TS = TS
        self._vnum = self._TS.vertex_num()
        self._bool = [False for x in range(self._vnum)]
        self._eg = [[x] for x in range(self._vnum)]
        self._syntax = tree.data()
        if not self._syntax in self._TS._states:
            self._rbool = tree.right().boolean()
            self._reg = tree.right().example()
            if self._syntax in ['until','and','forall_until','exists_until']:
                self._lbool = tree.left().boolean()
                self._leg = tree.left().example()
        
    def check_state(self):
        self._bool[self._TS._dict[self._syntax]] = True
        
    def check_true(self):
        self._bool = [True for x in range(self._vnum)]
            
    def check_not(self):
        self._bool = [not(x) for x in self._rbool]
        self._eg = self._reg

    def check_and(self):            
        for x in range(self._vnum):
            self._bool[x] = self._lbool[x] and self._rbool[x]
            if not (self._bool[x] or self._lbool[x]):
                self._eg[x] = self._leg[x]
            else:
                self._eg[x] = self._reg[x]
                
    def check_next(self):
        for vi in range(self._vnum):
            for out in self._TS.out_edges(vi):
                if not self._rbool[out]:
                    self._bool[vi] = False
                    self._eg[vi] = [vi] + self._reg[out]
                    break
            else:
                self._bool[vi] = True
                self._eg[vi] = [vi]
                
    def check_forall_next(self): #CTL
    	self.check_next()
        
    def check_exists_next(self): #CTL
        for vi in range(self._vnum):
            for out in self._TS.out_edges(vi):
                if self._rbool[out]:
                    self._bool[vi] = True
                    self._eg[vi] = [vi] + self._reg[out]
                    break
            else:
                self._bool[vi] = False
                self._eg[vi] = vi
    
    def check_until(self):
        vnum = self._vnum
        boo = [-1]*vnum
        eg = self._eg 
        count = 0
        for x in range(vnum):
            if self._rbool[x] == True:
                boo[x] = True
                eg[x] = self._reg[x]
            elif self._lbool[x] == False:
                boo[x] = False
                eg[x] = self._leg[x]
            else:
                count += 1
        
        while count != 0:
            rec = [None]*vnum
            qu = MyQueue()
            for x in range(vnum):
                if boo[x] == -1:
                    qu.enqueue((-1, x))
                    break  
            ttag = []
            while not qu.is_empty():
                state = 1
                vi, vj = qu.dequeue()
                if boo[vj] == -1:
                    if rec[vj]:
                        flist = []
                        t = vi
                        while t != -1:
                            flist.append(t)
                            t = rec[t]
                        ind = flist.index(vj)
                        for x in range(len(flist)):
                            boo[flist[x]] = False
                            count -= 1
                            if x <= ind:
                                eg[flist[x]] = list(reversed(flist[0:x+1])) + list(reversed(flist[x:ind+1]))
                            else:
                                eg[flist[x]] = list(reversed(flist[0:x+1])) +[vj]
                        state = 0
                        break                       
                    else:
                        for vk in self._TS.out_edges(vj):
                            qu.enqueue((vj, vk))
                        rec[vj] = vi                              
                else:
                    if boo[vj]:
                        rec[vj] = vi
                        ttag.append(vj)                     
                    else:
                        flist = []
                        rec[vj] = vi
                        t= vj
                        while rec[t] !=  -1:
                            t = rec[t]
                            flist.append(t)
                        for x in range(len(flist)):
                            count -= 1
                            boo[flist[x]] = False
                            eg[flist[x]] = list(reversed(flist[0:x+1])) + eg[vj]
                        state = 0                        
                        break                
            if state == 1:
                tset = set()
                for vj in ttag:
                    t = vj
                    while rec[t] != -1:
                        t = rec[t]
                        tset.add(t)
                for v in tset:
                    count -= 1
                    boo[v] = True
                    eg[v] = [v]  
        self._bool = boo
                      
    def check_forall_until(self): #CTL
        self.check_until()
                      
    def check_exists_until(self): #CTL
        vnum = self._vnum
        boo = [-1]*vnum
        eg = self._eg 
        count = 0
        for x in range(vnum):
            if self._rbool[x] == True:
                boo[x] = True
                eg[x] = self._reg[x]
            elif self._lbool[x] == False:
                boo[x] = False
                eg[x] = self._leg[x]
            else:
                count += 1
        
        while count != 0:
            rec = [None]*vnum
            qu = MyQueue()
            for x in range(vnum):
                if boo[x] == -1:
                    qu.enqueue((-1, x))
                    break
                
            ftag = []
            while not qu.is_empty():
                state = 0
                vi, vj = qu.dequeue()
                
                if boo[vj] == -1:
                    if rec[vj]:
                        ftag.append(vi)
                    else:
                        rec[vj] = vi
                        for vk in self._TS.out_edges(vj):
                            qu.enqueue((vj, vk))
                else:
                    if boo[vj]:
                        tlist = []
                        rec[vj] = vi
                        t = vi
                        while t != -1:
                            tlist.append(t)
                            t = rec[t]
                        tlist.reverse()
                        for x in range(len(tlist)):
                            count -= 1
                            boo[tlist[x]] = True
                            eg[tlist[x]] = tlist[x:] + eg[vj]
                        state = 1
                        break
                    else:
                        ftag.append(vi)

            if state == 0:
                fset = set()
                for vi in ftag:
                    t = vi
                    while t != -1:
                        fset.add(t)
                        t = rec[t]
                for x in fset:
                    boo[x] = False
                    count -= 1
                    eg[x] = [x]
        self._bool = boo
                    
    def do(self):
        if self._syntax in self._TS._states:
            self.check_state()
        else:
            astr = 'self.check_%s()'%(self._syntax)
            eval(astr)
        return (self._bool, self._eg)
