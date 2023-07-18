'''Loan EMI Basic Calculator'''

#Taking inputs from user
amt=float(input("Loan Amount : "))
roi=float(input("Interest  % : "))
time=int(input("Loan Period in months: "))
#calulcate loan EMI
r = roi/(12*100)    #ROI per month
emi=amt*r*((1+r)**time)/((1+r)**time-1) #Calucate EMI
print(f"Exact EMI is {emi}")    #display exact emi
print(f"Recommended Payment is {round(emi+1)}")     #Recommended Payment is always 1 + EMI in fraction
