'''
In a given array of non negative integers, find all subset combinations which add up to a particular variable.
Also, you may not repeat these numbers.
'''

class Sol:
    
    
    def __init__(self, nums, key):
        self.nums = nums
        self.key = key
        self.res = []
        self.x = []
        self.count = 0
        self.lis = []

    
    def check(self):
        flag = False
        if not self.nums: 
            # print(self.nums)
            exit()
        self.x = []
        for i in (self.nums):
            self.x.append([i])
        # print(self.x)
        while len(self.x[0]) < len(self.nums):
            for i in self.x: 
                if sum(i) == self.key:
                    self.lis.append(i)
                    for k in i: 
                        if k in self.nums: self.nums.remove(k)
                        # print(self.nums)
                        flag = True
            if flag: self.check()
            y = []
            for i in range(len(self.x)):
                for j in range(i+1, len(self.x)):
                    for k in self.x[j]:
                        if k not in self.x[i]:
                            z = self.x[i].copy()
                            z.append(k)
                            z.sort()
                            if z not in y: y.append(z)
            self.x = y.copy()
            # print(y)
        if sum(self.x[0]) == self.key: self.lis.append(self.x[0])
        print(self.lis)
        exit()
        

def main():
    arr = list(map(int, input("enter array\n").split(' ')))
    key = int(input("enter sum key\n"))
    sol = Sol(arr, key)
    sol.check()
    sol.display()


if __name__ == "__main__":
    main()