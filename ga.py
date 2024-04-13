import random
import os

def genPop(nW, nB):
    pop = []
    for n in range(nW + nB):
        pop.append(random.random())
    return pop

# holds the neural net and plays a game for every chromosome
# the fitness list holds the resulting scores from each 
# chromosome's game
def fitness(pop, nW, nB):
    os.system("/Users/katemikels/Library/Python/3.9/bin/2048")
    f = open("score.txt", "r")
    score = f.read()
    print("what we got: ", score)
    fL = genPop(nW, nB)
    return fL

def main(numWeights, numBiases):
    pop = genPop(numWeights, numBiases)

    maxFitness=1
    averageFitness=0
    maxFitList=[]
    avgFitList=[]
    mostFitChromo=""
    fitnessList=[]
    gen=0

    fitnessList = fitness(pop, numWeights, numBiases)
    maxFit = max(fitnessList)
    mostFitChrom = pop[fitnessList.index(maxFit)]
    avgFit=sum(fitnessList)/len(fitnessList)
    avgFitList.append(avgFit)

    print(f"GENERATION: {gen}")
    for i in range(len(pop)):
        print(f'{fitnessList[i]:>4}, {pop[i]}')
    print(f"AVERAGE FITNESS: {avgFit}")
    print(f"BEST FITNESS: {maxFit}\n")

    while False:
        maxFit=max(fitnessList)
        mostFitPath=pop[fitnessList.index(maxFit)]
        maxFitList.append(maxFit)
        avgFit=sum(fitnessList)/len(fitnessList)
        avgFitList.append(avgFit)

        print(f"GENERATION: {gen}")
        for i in range(len(pop)):
            print(f'{fitnessList[i]:>4}, {pop[i]}')
        print(f"AVERAGE FITNESS: {avgFit}")
        print(f"BEST FITNESS: {maxFit}\n")

main(4, 4)
