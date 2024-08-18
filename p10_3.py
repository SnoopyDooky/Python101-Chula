class piggybank:
    def __init__(self):
        self.coin = {}

    def add(self, v, n):
        if sum(self.coin.values()) + n > 100:
            return False
        v = float(v)
        if v not in self.coin:
            self.coin[v] = 0
        self.coin[v] += n
        return True

    def __float__(self):
        s = 0
        for k, v in self.coin.items():
            s += (k * v)
        return float(s)

    def __str__(self):
        l = []
        for k in sorted(self.coin):
            l.append(str(k) + ":" + str(self.coin[k]))
        return "{" + ", ".join(l) + "}"


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
