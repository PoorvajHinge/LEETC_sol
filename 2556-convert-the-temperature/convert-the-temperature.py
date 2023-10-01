class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ls1=[]
        ls1.append(celsius + 273.15)
        ls1.append(celsius * 1.80 + 32.00)
        return ls1
        
