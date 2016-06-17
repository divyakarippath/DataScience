import numpy as np
np.random.seed(0)

totals = {20:0,30:0,40:0,50:0,60:0,70:0} #total number of people in each age grp
purchases = {20:0,30:0,40:0,50:0,60:0,70:0} # total purchase done by each age group
totalpurchases = 0

for _ in range(100000):
    ageDecade = np.random.choice([20,30,40,50,60,70])
    totals[ageDecade]+=1
    purchaseProbability = float(ageDecade)/100.0 # to assign lesser probability for young people
    if (np.random.random() < purchaseProbability):
        totalpurchases+=1
        purchases[ageDecade]+=1

print totals
print purchases
print totalpurchases

# Probability of buying something given that you are in your 30's, P(E|F)
# Equivalent to the percentage of how many 30 year old bought something

PEF = float(purchases[30])/float(totals[30])
print "P(Purchases | 30)" , PEF
        
# Probablity of being 30 in the data set , p(F)
PF = float(totals[30])/100000.0 
print "P(30)" , PF

#Overall probability of buying something , P(E)
PE = float(totalpurchases) / 100000.0
print "P(Purchase)" , PE

#Since P(E) and P(E|F) are different , that means purchase and age are dependent

print "P(30)*P(Purchase)",PE*PF

#Probability of both being in 30's and purchasing , P(E,F) = P(E)*P(F).
#Here it might defer due to random nature of data

print "P(purchase,30)" , float(purchases[30])/100000.0

#P(E,F)/P(F) = P(E|F)

print (float(purchases[30])/100000.0)/PF # Equal to P(E|F)

    

