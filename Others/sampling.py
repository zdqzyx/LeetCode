
import random

class ReservoirSampling:

    def __init__(self,  pools):
        self.pools = pools

    def sampling(self, k):
        assert k <= len(self.pools), 'k should be less than n'
        res = []
        # 前 K 个元素直接放入蓄水池中
        for i in range(k):
            res.append(self.pools[i])
        
        # K+1个元素开始进行概率采样，如果采样的r小于k，则用当前的j元素替换蓄水池中的r元素
        for j in range(k, len(self.pools)):
            r = random.randint(0, j)
            if r<k:
                res[r] = self.pools[j]
        return res

# 测试
res = []
for i in range(100000):
    k = 5
    N = 100
    pools = list(range(1, N+1))
    rs = ReservoirSampling(pools)
    s_res = rs.sampling(k)
    res += s_res

from collections import Counter

d = Counter(res)
print(d)

        