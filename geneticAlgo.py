from brainFk import BrainFuckInterpreter
import sys
import random

class Chromosome:
    commands = ["<",">","+","-",".","[","]"]
    interpreter = BrainFuckInterpreter()
    def __init__(self, contents, prediction,target):
        self.contents = contents
        self.prediction = prediction
        self.target = target
        self.fitness = self.fitnessFunc(self.target)

    def fitness(self,target):
        prediction = self.interpreter.interpret(self.contents)
        self.fitness = abs(len(target)-len(prediction))
        if (len(target)<len(prediction)): p=len(target)
        else: p = len(prediction)

        for i in range(p):
            self.fitness+=(abs(ord(target[i])-ord(prediction[i])))/94
        try:
            self.fitness = 1 / self.fitness
        except ZeroDivisionError:
            print("Prediction is Target")
            print(self.contents)
            sys.exit()

    def crossover(self,p2):
        p1,p2 = list(self.contents),list(p2.contents)
        if(len(p1)<len(p2)): while (len(p1)<len(p2)): p1.append(None)
        else: while(len(p2)<len(p2)): p2.append(None)
        currCrossover = False
        for i in range(len(p1)):
            if(random.random()<0.1): currCrossover = not currCrossover
            if(currCrossover):
                temp = p1[i]
                p1[i] = p2[i]
                p2[i] = temp
        p1,p2 = "".join([k for k in p1 if k!=None]), "".join([r for r in p2 if r!=None])
        return ((Chromosome(len(p1),p1,self.target)),(Chromosome(len(p2),p2,self.target)))

    def mutate(self,mutateRate):
        output = list(self.contents)
        for i in range(len(output)):
            k = random.random()
            if(k<mutateRate): output[i] = random.choice(Chromosome.commands)
            elif(k>1-mutateRate):
                if(k<1-(mutateRate/2)): output.insert(i,random.choice(Chromosome.commands))
                else: output.pop(i)
            else: pass
        self.contents = "".join(output)

class Population:
    commands = ["<",">","+","-",".","[","]"]
    interpreter = BrainFuckInterpreter()
    def __init__(self, popSize, target, chromosomeLen, mutateRate, oldPopPercentage):
        self.popSize = popSize
        self.mutateRate = mutateRate
        self.popu = []
        self.popu.extend(Population.fillPop(len(popu),self.popSize,self.chromosomeLen))
        self.percentCrossover = oldPopPercentage # Percentage of population not randomised
        self.chromosomeLen = chromosomeLen # Maximum Chromosome Length
        self.target = target

    def evolvePop(self):
        newPop = self.selectCrossover(self.percentCrossover)
        newPop = self.removeUnInterpretable(newPop)
        for i in newPop:
            if (random.random()<self.mutateRate): i.mutate(self.mutateRate)
        self.popu = newPop
        self.popu.extend(Population.fillPop(len(popu),self.popSize,self.chromosomeLen))

   def selectCrossover(self,percentCrossover):
       sumFitness = sum([k.fitness for k in self.popu])
       boundsList = [0]
       boundsDict = {0:None}
       for i in range(len(self.popu)-1):
           scaledFitness = self.popu[i].fitness/sumFitness
           appendVal = boundsList[-1] + round(scaledFitness,3)
           boundsList.append(appendVal)
           boundsDict[appendVal] = self.popu[i]
       boundsList.append(100)
       boundsDict[appendVal] = self.popu[-1]
       newPop = []
       noCrossover = int(len(self.popu)*percentCrossover)
       if (noCrossover % 2 == 1): noCrossover-=1
       for i in range(noCrossover/2):
           arrList = []
           for k in range(2):
               p = boundsList.copy()
               leave = False
               r = round(random.random(),5)
               while(not leave):
                   q = int((len(p)-1)/2)
                   if(len(p)==2):
                       arrList[k] = p[1]
                       leave = True
                   elif(r>p[q]):
                       p = p[q:]
                   elif(r<p[q]):
                       p = p[0:q+1]
           children = boundsDict[arrList[0]].crossover(boundsDict[arrList[1]])
           newPop.extend(children)
           # Consider adding while loop to remove all uninterpretable chromosomes
       return newPop

    @staticmethod
    def fillPop(currLen, reqLen, chromosomeMaxLength):
        appendTuple, contents = [], ""
        interpretable = False
        for i in range(reqLen-currLen):
            interpretable = False
            while(not interpretable):
                contents = "".join[random.choice(Population.commands) for _ in range(random.randint(1,chromosomeMaxLength))]
                textOutput = Population.interpreter.interpret(contents)
                if (textOutput[1]):
                    interpretable = True
                    appendTuple.append(Chromosome(contents,textOutput[0],self.target))
        return tuple(appendTuple)

if __name__ == "__main__":
    BrainFuckInterpreter().interpret(input())
