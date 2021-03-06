class BrainFuckInterpreter:
    def __init__(self):
        self.list = [0]
        self.pointer = 0

    def interpret(self,inputData):
        self.list, self.pointer, l, i, j = [0], 0, 0, -1, 0
        output = ""
        if(inputData.count("[") != inputData.count("]")): return(None, False)
        while (i<len(inputData)-1):
            i+=1
            if (inputData[i]=="<"):
                if(self.pointer>=1):
                    self.pointer-=1
                else: return(None,False) # Non interpretable statement
            elif (inputData[i]==">"):
                if(self.pointer + 1 == len(self.list)):
                    self.list.append(0)
                self.pointer+=1
            elif (inputData[i]=="+"):
                self.list[self.pointer]+=1
                # Change to mod 127 for it to interpret properly
                self.list[self.pointer]%=95
            elif(inputData[i]=="-"):
                if(self.list[self.pointer]>0):
                    self.list[self.pointer]-=1
                else:
                    return (None,False) # Non interpretable expression
            elif(inputData[i]=="."):
                try:
                    # Take away +33
                    output+=chr(self.list[self.pointer] + 33) 
                except ValueError: return(None, False)
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
                if(self.list[self.pointer]>0):
                    i-=1
                    if(i>=0):
                        collate = 0
                        while(l>0 or inputData[i]!="["):
                            if(i==0):
                                return (None, False) # Non interpretable expression
                            if(inputData[i]=="]"): l+=1
                            elif(inputData[i]=="["): l-=1
                            if (inputData[i] in ["+","-",">","<"]): collate +=1
                            i-=1
                        if (collate==0): return(None, False) # Non interpretable expression
                    else: return(None,False)
            j+=1
            # Can't detect infinite loop due to Halting Problem 
            if(j>4000): return(None,False)
        if(output==""): return(None,False)
        return (output,True)

if __name__ == "__main__":
    BrainFuckInterpreter().interpret(input())
