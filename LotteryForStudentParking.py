import random

class lottery():
    def __init__(self):
        self.student=[]
        for i in range (1,299):
            self.student.append(i)
        self.student.extend([300]*50)
        self.pick=None
    def pickStudent(self):
        self.pick=random.choice(self.student)
    def winner(self, numStudent):
        if str(numStudent) == str(self.pick):
            return 1
        else:
            return 0

def testMyLuck(numStudent, numPicks, game):
    numHits = 0
    for t in range(numPicks):
        game.pickStudent()
        numHits += game.winner(numStudent)
    probability = (numHits / numPicks)*100
    return probability
    
game = lottery()
def simulation (numSim):
    probabilityArray = []
    for i in range(numSim):
        probabilityArray.append(testMyLuck(300,50,game))
    avgProbability = sum(probabilityArray)/len(probabilityArray)
    print ('The probablity that I will get chosen is', avgProbability, '%')
    
for simulations in (10, 100, 1000, 10000, 100000):
    print ('Number of simulations =', simulations)
    simulation(simulations)
#for simulations in (1000, 10000, 100000, 1000000):
#    print("Simulation iterations: ", simulations)
 #   pickStudent(300, simulations, lottery())