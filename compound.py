def calcInterest(principal, interest_rate, time_period, compounding_frequency):
    # Calculate the amount using the compound interest formula
    amount = principal * (1 + interest_rate / compounding_frequency) ** (compounding_frequency * time_period)
    
    # Calculate the total interest by subtracting the principal from the amount
    interestAmt = amount - principal
    
    # Return the total interest
    return interestAmt

# Get user input for principal, interest rate, time period, and compounding frequency
principal = float(input('Enter the principal amount: '))
interest_rate = float(input('Enter the interest rate (as a decimal): '))
time_period = float(input('Enter the time period in years: '))
compounding_frequency = float(input('Enter the compounding frequency in years: '))

# Calculate the amount using the compound interest formula
amount = principal * (1 + interest_rate / compounding_frequency) ** (compounding_frequency * time_period)

# Calculate the total interest using the calcInterest function
totalInterest = calcInterest(principal, interest_rate, time_period, compounding_frequency)

# Print the total interest accrued
print('Total interest accrued: £', round(totalInterest, 2))
