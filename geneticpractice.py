import random
import pandas as pd
import operator

itemlist = pd.DataFrame()

'''generates the items with corresponding scores and weights'''
def generateitems(weightlimit, numberofitems):
    items = pd.DataFrame()
    for i in range(numberofitems):
        item = pd.DataFrame({'Item Number': int(i + 1), 'Weight': int(random.random()*(weightlimit/2+1)), 'Score':int(random.random()*11)}, index = [0])
        items = items.append(item, ignore_index = True)
    return items

'''generates the random combinations from the available items generated''' 
def generatepopulation(populationsize, numberofitems, weightlimit):
    global itemlist
    itemlist = generateitems(weightlimit, numberofitems)
    i = 0
    poplist = []
    for i in range(populationsize):
        weight = 0
        tempitemframe = pd.DataFrame()
        tempitemlist = itemlist
        ''' gets combination of items from the itemlist and checks 
        if selection of items are below the weight limit'''
        while weight <= weightlimit:
            if len(tempitemlist) == 0:
                break
            randomindex = int(random.random()*len(tempitemlist))
            itemrow = tempitemlist.iloc[[randomindex]]
            itemweight = itemrow.iloc[0]['Weight']
            if itemweight + weight > weightlimit:
                tempitemlist = tempitemlist.drop(tempitemlist.index[randomindex])
                continue
            tempitemframe = tempitemframe.append(itemrow, ignore_index = True)
            tempitemlist = tempitemlist.drop(tempitemlist.index[randomindex])
            weight = itemweight + weight
        '''groups each combination of items in a  dictionary'''
        scoredict = {}
        for index, row in tempitemframe.iterrows():
            scoredict[row['Item Number']] = [row['Score'], row['Weight']]
        poplist.append(scoredict)
    return poplist
        
def fitness(itempopulation):
    itempopwithfit = []
    for itemlist in itempopulation:
        totalscore = 0
        totalweight = 0
        for itemkey in itemlist:
            totalscore = totalscore + itemlist[itemkey][0]
            totalweight = totalweight + itemlist[itemkey][1]
        listwithfit = [itemlist, totalscore, totalweight]
        itempopwithfit.append(listwithfit)
    return sorted(itempopwithfit, key = operator.itemgetter(1), reverse = True)
    

def selectfrompopulation(fitness, samplesize):
    nextgeneration = []
    for i in range(samplesize):
        nextgeneration.append(fitness[i][0])
    return nextgeneration

def createchild(parent1, parent2, weightlimit):
    child = {}
    parents = []
    for itemparent1 in parent1:
        parents.append(parent1[itemparent1])
    for itemparent2 in parent2:
        parents.append(parent2[itemparent2])
    x = 0
    while x <= weightlimit:
        if len(parents) == 0:
            break
        index = int(random.random() * len(parents))
        if parents[index][1] + x > weightlimit:
            del parents[index]
            continue
        child[index] = parents[index]
        x = x + parents[index][1]
        del parents[index]
        print(parents)
    return child

def createchildren(breeders, number_of_children, weightlimit):
    nextpopulation = []
    x = 1
    for i in breeders:
        for j in range(number_of_children):
            nextpopulation.append(createchild(i,breeders[len(breeders)-x], weightlimit))
        x = x + 1
    return nextpopulation

def mutateitemlist(items):
    global itemlist
    indexmodify = int(random.random() * len(items))
    rowindex = int(len(itemlist.index)*random.random())
    keys = []
    x = 0
    for i in items:
        if x == indexmodify:
            items[i] = [itemlist.iloc[rowindex]['Score'], itemlist.iloc[rowindex]['Weight']]
            keys.append(i) 
        x + 1
    for key in keys:
        items[itemlist.iloc[rowindex]['Item Number']] = items[key]
        del items[key]
    return items

def mutatepopulation(population, chanceofmutation):
    x = 0
    for i in population:
        if random.random() * 100 < chanceofmutation:
            population[x] = mutateitemlist(population[x])
        x = x + 1
    return population

populationsize = 10
itemsavailable = 10
weightlimit = 50

pop = generatepopulation(populationsize, itemsavailable, weightlimit)
for i in range(0, 2):
    fpop = fitness(pop)
    print('\n-----Generation' + str(i + 1) + '-----')
    print(fpop[0])
    popselect = selectfrompopulation(fpop, len(fpop))
    children = createchildren(popselect, 1, weightlimit)
    pop = mutatepopulation(children, 5)


        
        
        
        