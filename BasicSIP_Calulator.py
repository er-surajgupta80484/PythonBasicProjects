
#Take inputs

sip=float(input("Enter Monthly Deposit Amount : "))
period=int(input("Investment Period in years : "))
roi=float(input("Expected Yearly Returns (%): "))
monthlyReturn = roi/12/100   # Converting yearly ROI in monthly
months = period * 12      #years of period in number of months
finalValue = sip * ((((1 + monthlyReturn)**(months))-1) * (1 + monthlyReturn))/monthlyReturn
finalValue = round(finalValue)      #rounding off the Final Amount
print("The expected amount you will get is:",finalValue)
