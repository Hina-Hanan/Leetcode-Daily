class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        minus = 0
        ind = 0
        start = 0
        while ind < len(cost):
            total = gas[ind] - cost[ind]
            cur += total
            if cur < 0:
                start = ind + 1
                minus += -cur
                cur = 0
            ind += 1
        cur -= minus
        if cur >= 0: return start
        return -1


        
                
