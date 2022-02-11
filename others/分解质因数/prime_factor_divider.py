class Solution:
    def devprime(self, n: int) -> List[str]:
        prime_factor_list=[]
        while num!=1:
            for i in range(2,int(num+1)):
                if num % i == 0:
                    prime_factor_list.append(i)
                    num = int(num / i)
                    break
        return prime_factor_list
