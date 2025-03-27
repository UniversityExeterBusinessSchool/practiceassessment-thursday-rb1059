#######################################################################################################################################################
# 
# Name: Rose Bijo
# SID: 750014063
# Exam Date: 27/03/2025
# Module: BEMM458_ Programming For Business Analytics
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-rb1059.git
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
keys = [7, 3]

# Get words for our keys
words = [key_comments[k] for k in keys]

# List to store positions
my_list = []

# Find where each word starts and ends
for word in words:
    start = customer_feedback.find(word)  # Find position
    if start != -1:
        end = start + len(word) - 1
        my_list.append((start, end))

# Show result
print('My List: ',my_list)

#output :My List:  [(129, 135), (88, 93)]


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:75
# Insert last two digits of ID number here:63

# Write your code for Operating Profit Margin
def operating_profit_margin(revenue,operating_profit):
    return(operating_profit/revenue)*100 if revenue!=0 else 0
# Write your code for Revenue per Customer
def revenue_per_customer(total_revenue, total_customers):
    return total_revenue/total_customers if total_customers !=0 else 0

# Write your code for Customer Churn Rate
def customer_churn_rate(lost_customers,total_customers):
    return(lost_customers/total_customers)*100 if total_customers != 0 else 0
# Write your code for Average Order Value
def average_order_value(total_revenue, total_orders):
    return total_revenue/total_orders if total_orders != 0 else 0

#Given  values based on ID number
revenue=7500   #eg value based on 1st two digits (75*100)
operating_profit=630  #eg value based on last two digits(63*10)
total_customers=75  #eg customers
lost_customers=63  #eg lost customers
total_orders=75  # eg orders
total_revenue=7500

# Call your designed functions here
opm= operating_profit_margin(revenue,operating_profit)
rpc=revenue_per_customer(total_revenue, total_customers)
ccr = customer_churn_rate(lost_customers, total_customers)
aov = average_order_value(total_revenue, total_orders)
#display the result
print('operating_profit_margin :', opm)
print('revenue_per_customer :', rpc)
print('customer_churn_rate :', ccr)
print('average_order_value :', aov)

#output: 
#operating_profit_margin : 8.4
#revenue_per_customer : 100.0
#customer_churn_rate : 84.0
#average_order_value : 100.0
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)  # Price levels
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])  # Corresponding demand

# Create a linear regression model
model = LinearRegression()
model.fit(price, demand)


#  calculate the coefficient of the linear regression (slope) to approximate the demand function
slope = model.coef_[0]

# predict the demand for a specific price (Price = 52)
price_52 = 52
demand_at_52 = model.predict([[price_52]])

# Plot the linear regression line
plt.scatter(price, demand, color='blue', label='Data points')
plt.plot(price, model.predict(price), color='red', label='Linear regression line')
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.title('Price vs Demand')
plt.legend()
plt.show()

# Print the predicted demand at price 52
print("Predicted demand when price is £52:", demand_at_52[0])

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0, 100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')
plt.title('Line Chart of 100 Random Numbers')
plt.xlabel('Index')
plt.ylabel('Random Number')
plt.legend()
plt.grid(True)
plt.show()


