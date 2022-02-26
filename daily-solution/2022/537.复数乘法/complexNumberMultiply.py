class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, image1 = map(int, num1[:-1].split('+'))
        real2, image2 = map(int, num2[:-1].split('+'))
        return f'{real1*real2-image1*image2}+{real1*image2+image1*real2}i'
