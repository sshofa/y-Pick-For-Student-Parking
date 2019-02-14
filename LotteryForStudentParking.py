import random

def pickStudent(numStudent, numTrials):
    #apply weights to certain students. i.e. imagine that students 0-10 bought 7 tickets
    studentNumber = 7*list(range(0,10)) + 5*list(range(11,30)) + 3*list(range(31,333)) + list(range(334,449))
    result = []
    numHits = 0
    for t in range(numTrials):
        chosenStudent = random.choice(studentNumber)
        result.append(chosenStudent)
        studentNumber.remove(chosenStudent)
        if chosenStudent == numStudent:
            numHits += 1
        probability = round((numHits / numTrials)*100,3)
    print('The probability that I will get picked is ', probability,'%')

pickStudent(3, 50)



