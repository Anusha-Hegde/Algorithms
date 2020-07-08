class Stack:

    '''
    implements stack operations with keeping track of min value at a given time
    structure: [element, current min]
    '''

    def __init__(self, num = None):
        self.stack = []
        if num :
            self.stack.append([num, num])
        

    def insert(self, num):
        min = self.stack[-1][1]
        self.stack.append([num, num]) if  min > num else self.stack.append([num, min])

    
    def pop(self, pos = None) -> [int, int]:
        if not pos: return self.stack.pop(-1)

        min = self.stack[pos][1]
        next_min = self.stack[pos-1][1]
        '''
        example: [2,2],[1,1],[3,1],[0,0]  and  pos: 2
        '''
        if next_min == min: return self.stack.pop(pos)


        '''
        example: [2,2],[1,1],[3,1],[0,0]  and  pos: 1
        after removing [1,1] all min elements after it must be updated
        '''
        i = pos + 1
        while i < len(self.stack) and self.stack[i][1] == min:
            self.stack[i][1] = next_min
            i += 1
        return self.stack.pop(pos)


    def get_min(self):
        '''
        returns current minimum number
        '''
        return self.stack[-1][1]


    def display(self):
        print(self.stack)