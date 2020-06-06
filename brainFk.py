class BrainFuckInterpreter:
    def __init__(self):
        self.list = [0]
        self.pointer = 0

    def interpret(self,inputData):
        self.list, self.pointer, l, i = [0], 0, 0, -1
        output = ""
        while i<len(inputData)-1:
            i+=1
            if (inputData[i]=="<"):
                self.pointer-=1
            elif (inputData[i]==">"):
                if(self.pointer + 1 == len(self.list)):
                    self.list.append(0)
                self.pointer+=1
            elif (inputData[i]=="+"):
                self.list[self.pointer]+=1
                self.list[self.pointer]%=95
            elif(inputData[i]=="-"):
                if(self.list[self.pointer]>0):
                    self.list[self.pointer]-=1
                else:
                    return (None,False) # Non interpretable expression
            elif(inputData[i]=="."):
                output+=chr(self.list[self.pointer] + 32)
            elif(inputData[i]=="["):
                if(self.list[self.pointer]==0):
                    try:
                        i+=1
                        while(l>0 or inputData[i]!="]"):
                            if(inputData[i]=="["): l+=1
                            elif(inputData[i]=="]"): l-=1
                            i+=1
                    except IndexError:
                        return (None,False) # Non interpretable expression
            elif(inputData[i]=="]"):
                if(self.list[self.pointer]!=0):
                    i-=1
                    if(i>=0):
                        while(l>0 or inputData[i]!="["):
                            if(i<0): return (None, False) # Non interpretable expression
                            if(inputData[i]=="]"): l+=1
                            elif(inputData[i]=="["): l-=1
                            i-=1
        print("\n"+output)
        return (output,True)

if __name__ == "__main__":
    BrainFuckInterpreter().interpret(input())
