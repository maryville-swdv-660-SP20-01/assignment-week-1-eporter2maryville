import requests
import random2
import json

#Call Cat Fact service and return 10 different cat facts at random from library
response = requests.get(
    'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10')
catFact = response.json()
catFactList = []
for d in catFact:
    fact = d['text']
    catFactList.append(fact)

#Generate Random Number to pick from list of cat facts returned
rand=random2.random()
rand10=rand*10
rand10Int=int(rand10)

#Generate another random number to comically number the cat fact a la Zombie Land Rules
rand2 = random2.random()
rand210=rand2*10
catFactNumber=round(rand10*rand210)

#Print Cat fact e.g. Cat Fact 7: Cats are not Dogs
print('Cat Fact #{1}: {0}'.format(catFactList[rand10Int], catFactNumber))