##########################################################################################
# CSC 280 - Programming Practice #5                                                                                                                                              # 
# Author: Nadia Barbosa                                                                                                                                                       #
# filename: Nadia_assignment5.py                                                                                                                 #
# date last modified: 03/26/13                                                           
# ---------------------------------------------------------------------------------------
# Loan Calculator:                                                                                                                                                    
# action: Calculates the cost of a loan based on several parameters                                                                                                             
# input: principal, period, and rate of the loan                                                                                                                                
# output: monthly payment, which is then used to output the total loan cost              
#                                                                                        
##########################################################################################

#Dialog:
""">>> 
Enter the amount of the loan, number of monthly payments, and the interest rate separated by a ',' 180000,360,8.25
You stated that your loan principal is $180000.0,
payment will be made for 360 months,
and the rate of your loan is 8.25%
The cost of your loan will be $123750.00
>>>"""

def monthlyPayment(principal,period,rate):
    payment=(rate/12)/(1-(1+(rate/12))**(-period))*principal
    return payment

def LoanCost(principal,period,payment):
    cost=period*payment-principal

def main(): #input here - you want inputs to be visible here
    my_list=raw_input("Enter the amount of the loan, number of monthly payments, and the interest rate separated by a ',' ")
    my_new_list=my_list.split(",")

    new_amountOfLoan=float(my_new_list[0])
    new_period=int(my_new_list[1])
    new_rate=float(my_new_list[2])

    print"You stated that your loan principal is $"+str(new_amountOfLoan)+","
    print"payment will be made for "+str(new_period)+" months,"
    print"and the rate of your loan is "+str(new_rate)+"%"
    print"The cost of your loan will be $"+str("%0.2f" %(monthlyPayment(new_amountOfLoan,new_period,new_rate)))+""
main()




