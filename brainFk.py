class BrainFuckInterpreter:
    def __init__(self):
        self.list = [0]
        self.pointer = 0

    def interpret(self,inputData):
        self.list, self.pointer, l, i = [0], 0, 0, -1
        pattern, instrCheck, countReps = "", "",0
        output = ""
        while (i<len(inputData)-1):
            i+=1
            print("Pattern:",pattern)
            print("Input at Index:",inputData[i])
            print("Input index:",i)
            if(pattern!=""):
                instrCheck+=inputData[i]
                if(pattern == instrCheck):
                    instrCheck = ""
                    countReps+=1
                else:
                    if(len(pattern) == len(instrCheck)):
                        print(instrCheck)
                        patternCheck, instrCheck, countReps = "", "", 0
            if(countReps>10): return(None,False)
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
                self.list[self.pointer]%=95
            elif(inputData[i]=="-"):
                if(self.list[self.pointer]>0):
                    self.list[self.pointer]-=1
                else:
                    return (None,False) # Non interpretable expression
            elif(inputData[i]=="."):
                try:
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
                    print("Input Data:",inputData)
                    i-=1
                    if(i>=0):
                        collate = 0
                        boolPattCheck = True if(pattern=="") else False
                        while(l>0 or inputData[i]!="["):
                            if(boolPattCheck): pattern+=inputData[i+1]
                            if(i==0):
                                return (None, False) # Non interpretable expression
                            if(inputData[i]=="]"): l+=1
                            elif(inputData[i]=="["): l-=1
                            if (inputData[i] in ["+","-",">","<"]): collate +=1
                            i-=1
                        if (collate==0): return(None, False) # Non interpretable expression
                        if(boolPattCheck):
                            pattern+=inputData[i+1]
                            pattern = "".join(reversed(pattern))
                    else: return(None,False)
                else: pattern, instrCheck, countReps = "", "", 0
        if(output==""): return(None,False)
        print(output)
        print(inputData)
        print("reached")
        return (output,True)

if __name__ == "__main__":
    BrainFuckInterpreter().interpret(input())
