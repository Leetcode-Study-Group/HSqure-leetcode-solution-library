class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions_list=[]
        for nn in range(2, n+1):
            for i in range(1, nn):
                dividable_tag=False
                # checking
                for elem in range(2,i+1):
                    if (i%elem==0 and nn%elem==0):
                        dividable_tag=True
                if not dividable_tag:
                    fractions_list.append(f'{i}/{nn}')
        return fractions_list
