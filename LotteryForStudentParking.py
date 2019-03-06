import random

def pickStudent(numStudent, numPicks):
    #apply weights to certain students. i.e. imagine that students 0-10 bought 7 tickets
    studentNumber = 100*list(range(0,4)) + 3*list(range(4,30)) + list(range(31,333))
    result = []
    numHits = 0
    for t in range(numPicks):
        chosenStudent = random.choice(studentNumber)
        result.append(chosenStudent)
        studentNumber.remove(chosenStudent)
        if chosenStudent == numStudent:
            numHits += 1
        probability = round((numHits / numPicks)*100,3)
    return probability

def simulate(numStudent, numPicks, numTrials):
    for t in range(numTrials):
        probability = []
        probability.append(pickStudent(numStudent, numPicks))
        true_probability = sum(probability)/len(probability)
    print('The probability that I will get picked is ', true_probability,'%')

for simulations in (1000, 10000, 100000, 1000000, 10000000):
    print("Simulation iterations: ", simulations)
    simulate(3, 100, simulations)