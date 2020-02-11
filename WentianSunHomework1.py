#Wentian Sun Homework 1

#Part A
pagination = 'Page 1 of 12'
pageindex = pagination.index('f')
substring = int(pagination[pageindex+1:])
intsubstring = int(substring)
print(intsubstring)

#Part B
runner1 = 300.25 #Finish time in Minutes
runner2 = 260.75
runner3 = 315.75
runner4 = 245.25
average = (runner1+runner2+runner3+runner4)/4
print('Average:', average)
variance = ((runner1-average)**2+(runner2-average)**2+(runner3-average)**2+(runner4-average)**2)/4
print('Variance:', variance)

#Part C
principle = input('Please enter the bill principle:\n>>')
interest = input('Please enter annual interest rate (example 5.2 for 5.2%):\n>>')
years = input('Please enter the term in years:\n>>')
compound = input('Please enter number of times the interest will compound per year:\n>>')
principlefloat = float(principle)
interestfloat = float(interest)
yearsfloat = float(years)
compoundfloat = float(compound)
total = principlefloat*(1+interestfloat*.01/compoundfloat)**(yearsfloat*compoundfloat)
print('In', yearsfloat, 'years, at the interest rate of',interestfloat, '% compounded', compound, 'times per year, the initial amount of $', principlefloat, ' will be worth','${0:,.2f}'.format(total))