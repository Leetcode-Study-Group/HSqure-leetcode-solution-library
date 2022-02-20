class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        cnt = -1
        while not cnt+1 >= len(bits):
            cnt+=1
            if cnt+1 == len(bits):
                return True
            # 有1则跳过一个下标
            if bits[cnt] == 1:
                cnt+=1
            
        return False
