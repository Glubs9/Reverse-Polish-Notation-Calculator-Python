class stack:
        def __init__(self):
                self.stck = []
        def add_num(self, num_in):
                self.stck.append(num_in)
        def apply_func(self, f_in):
                n1 = self.stck.pop()
                n2 = self.stck.pop()
                self.stck.append(f_in(n2, n1))
        def ret(self):
                return self.stck[0]

exprs = {
        "+" : lambda a,b:a+b,
        "*" : lambda a,b:a*b,
        "-" : lambda a,b:a-b,
        "/" : lambda a,b:a/b
}

while True:
        inp = raw_input("enter string: ")
        if inp == "EXIT":
                exit()
        tokens = inp.split()
        stck = stack()
        for n in tokens:
                if n in exprs:
                        stck.apply_func(exprs[n])
                else:
                        stck.add_num(int(n))
        print(stck.ret())
