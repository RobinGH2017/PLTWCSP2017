#ROBIN BRAVO - PLTW CSP "RESTAURANT" Python Project
# July 28, 2017

def welcome_message():
    print "Welcome to Restaurant Bill Calculator"
    print "====================================="
    print
    print "You will be asked to enter : "
    print "    Number of Meals "
    print "    Number of Payers "
    
    print "    Cost of each meal "
    print
    print "Restaurant Bill Calculator will tell you : "
    print "    Total Meal Cost "
    print "    Tip Amount "
    print "    Total BILL Cost "
    print "    Cost per Payer "
    print "---------------------------------------- "
                  
def quit_message():
    print "QUIT - Zero Meals "
    
def get_number_of_payers(number_of_meals):
    number_of_payers = number_of_meals   # default : each person pays for their own meal
    print "Are you splitting the bill ?"
    split_answer = raw_input() 
    if split_answer == 'y':                        # splitting the bill means :
        print "Enter number of payers "   # some people paying for others
        number_of_payers = raw_input()   # as a treat - birthday, etc 
    return int(number_of_payers)
    
def get_total_meal_cost (number_of_meals):            
    n = 0                     #iterative counter
    total_meal_cost = 0.0     #initialize
    meal_cost = 0.0          #individual meal cost
    while n < number_of_meals:    #get price for each meal up to number_of_meals
        print "Enter meal #" + str(n+1) + " cost in dollars and cents "
        meal_cost = raw_input()    # type in price
        total_meal_cost += float(meal_cost) # add nth meal to running cost
        n += 1         # increment to get next meal's cost
    return (total_meal_cost)    # return cost as sum of all meals
    
                       
#def restaurant_bill_calculator(): main program
def rbc():    #shorten name for typing in during testing
    welcome_message()       # describe program to user
    print "Enter number of meals "
    number_of_meals = int(raw_input())   # number of meals
    
    if number_of_meals == 0:
        quit_message() # quit if no meals
    else:
        number_of_payers = get_number_of_payers(number_of_meals) # get number of people paying
        total_meal_cost = get_total_meal_cost(number_of_meals) # sum of all meals
                    
        print "Enter tip rate as a percent [whole number] "
        tip_rate = float(raw_input()) 
        total_bill = total_meal_cost * (1.00 + tip_rate*0.01)

        tip_msg = " "
        if tip_rate >= 20.00:
            tip_msg = "generous"        
        thankyou_msg = "Thank you for your " + tip_msg + " tip !"
        print
        print "--------- CALCULATOR RESULTS ----------- "
        print "Total Meal Cost       $" + "%.2f" % total_meal_cost 
        print "Tip Amount " + "(" + "%.2f" % (tip_rate) + "%)    " + "$" + "%.2f" % (total_meal_cost * tip_rate * 0.01) #str((100 * tip_rate)) + "%) $" + str(total_meal_cost * tip_rate)
        print "Total BILL Cost       $" + "%.2f" % total_bill   #str(total_bill)
        print "Number of Payers :    " + str(number_of_payers) 
        print "Cost per Payer        $" + "%.2f" % (total_bill/number_of_payers) #str((total_bill/number_of_payers))
        print "---------------------------------------- "
        print thankyou_msg
        print "------------------ END ----------------- "
        print
                     
        

            
            
                



                   
    
