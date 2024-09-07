class Solution:
    def sortSentence(self, s: str) -> str:
        index = []
        new1 = s.split()
        for i in range(0,len(new1)):
            index.append(new1[i][-1])
        s_without_nums =''.join([char for char in s if not char.isdigit()])
        new1 = s_without_nums.split()
        paired_list = sorted(list(zip(index , new1)))
        new2=[]
        for num,char in paired_list:
            new2.append(char)
        result = ' '.join(new2)
        return result
        