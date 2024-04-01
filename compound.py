def calcInterest (principal, interest_rate, time_period, compounding_frequency):
    amount = principal * (1+interest_rate / compounding_frequency) ** (compounding_frequency * time_period)
    interestAmt = amount - principal
    return interestAmt



principal = float(input('the principal amount value is: '))
interest_rate = float(input('enter interest rate: '))
time_period = float(input('enter time period in years: '))
compounding_frequency = float(input('enter compounding frequency in years: '))

amount = principal * (1+interest_rate / compounding_frequency) ** (compounding_frequency * time_period)

totalInterest = calcInterest(principal, interest_rate, time_period, compounding_frequency)

print ('total interest acrudes: £', round(totalInterest, 2))
