CHAPTER 3 STARTING QUESTIONS 

a = True
b = False
c = True
print(a and a )
print(a and b)

n = int(input("enter ur salary man = "))
if n >= 1200*91:
	print("pay tax please")
else:
	print("no tax")
A = 1
B = 2
C = True
D = False
print(A>B and C or D)

grade1 = int(input("enter ur number of 1 subject = "))

grade2 = int(input("enter ur number of 2 subject = "))

grade3 = int(input("enter ur number of 3 subject = "))

mean = (grade1 + grade2 + grade3)/30

if (grade1 >= 7 and grade2 >= 7 and grade3 >= 7 and mean >= 21 ):
	print("everything ok man !!!")

else:
	print("sorry")

n = int(input("value of first number =="))
n1 = int(input("enter value of second #number == "))

print(n + n1)

n = int(input("value in cm = \n"))
print(n*10)

day = int(input("value in  day\n "))
hours = int(input("value in hrs \n"))
min = int(input("value of min \n"))
seconds = int(input("value in seconds \n"))

total = day*24*3600 + hours*3600 + min*60 + seconds
print(total)

n = float(input("value of ur salary =\n "))
percent = float(input("raised percentage = \n "))

new_salary = n + n*(percent/100)

print(f"the raised percentage of ur salary is {percent} and old slary is {n} by which ur salary is {new_salary} \n thanks!!!!!!")

n = float(input("value of price of the item \n"))
discount = float(input("value of discount \n"))
new_price = n - n*(discount/100)
print(f"the real price is {n} and discount is {discount} and yayyy!!! ur new price is {new_price}")

n = float(input("enter thr distance travelled = \n "))
avg_speed = float(input("enter the speed = \n "))
time = float(n/avg_speed)
print(f"the time of the trip is {time} ")

n = int(input("value in celsius = \n "))

fahrenheit = (9*n/5) + 32

print(f"the value in fahrenheit is {fahrenheit}")

n = float(input("the km distance car travelled = \n "))
n1 = int(input("the days car was rented"))
car rent per km = 0.15$
 days rent = 60$
for calculation in rupees₹
total = (n*0.15)*96 + (n1*60)*96

print(f"the total money to be paid is {total}")


n = int(input("value of cigrattes per day = \n"))
years_smoking = float(input("value of years = \n"))
reduction_in_minutes = years_smoking*365* n*10

reduction_in_days = reduction_in_minutes/(24*60)

print(f"ths life time reduction is {reduction_in_days} minutes")

CHAPTER 4 HERE WE START

speed = float(input("the speed of the car is == \n "))

if speed > 80:
	print(f"the speed is greater than 80km/h so u will be fined\n")
	fine = (speed - 80)*5
	print(f"the fine u should pay will be {fine}₹ \n")

else:
	print("everything OK!!!")

n1 = int(input("value of first number = \n"))
n2 = int(input("value of second number = \n"))
n3 = int(input("value of third number is = \n "))

if (n1> n2 and n1> n3):
	print(f"the {n1} is greatest ")
	
elif(n2>n1 and n2> n3 ):
	print(f"the {n2} is greatest")
else:
	print(f"the {n3} is greatest")
if (n1< n2 and n1< n3):
	print(f"the {n1} is smallest")
elif (n2< n1 and n2< n3):
	print(f"the {n2} is smallest")
else:
	print(f"the {n3} is smallest ")

n = float(input("enter ur salary = \n"))

if n >1250:
	rise = (10/100)
	total = n + n* (10/100)
	print(f"ur salary is {n} and u get {rise} extra  by company the new salary is\n {total} ")
elif n<=1250:
	rise = 15/100
	total = n + n*(rise)
	print(f"ur salary is {n} amd u get {rise} extra by company the new salary is \n {total}")
	
n = float(input("value of distance u #travelled by train please \n  :- "))
if n<= 200:
	rent = 0.50
	total = 0.50 * n
else:
	rent = 0.45
	total = 0.45* n
print(f"the distance u travelled in km is {n} and ur fare is {total} ")
plan = input("enter ur telephone plan :- \n")
if plan != "littletalk" and plan != "talkmore":
	print("dont know this plan")
else:
	if plan == "littletalk":
		min = 100
		extra = 0.20
		price = 50
	else:
		min = 500
		extra = 0.15
		price = 99
used = int(input("enter how many minutes u used that plan = \n"))
total = used*(min+extra+ price)

print(f"ur total money to be paid is:- \n {total} ")
n1 = float(input("enter frst number :- \n"))
n2 = float(input("enter second nunber :- \n"))
op = input("enter operation")

if op == "+":
	print(f"the sum of the number is {n1 + n2}")
elif op == "-":
	print(n1-n2)
elif op == "*":
	print(n1*n2)
elif op == "/":
	print(n1/n2)
else:
	print("think again only symbols or operational symbols only")

n = float(input("enter the amount of house u want to buy \n :- "))
n1 = float(input("the salary u take in from the company \n :-"))

n2 = int(input("enter the year u will pay it #\n :-  "))

months = 12* n2

installment = n/months 

if installment > n *0.3:
	print("unfortunately u cant it it")
else:
	print(f"the installment of the house u #be paid is {installment} thanks !!!!")

end = int(input("enter the number "))
x = 1

while x <= end:
	
	print(x)
	x = x+2

end = 30

x = 3
while x <= 30:
	print(x)
	x = x+3

end = int(input("enter thr table of \n :- "))

x = 1

while x<= 10:
	print(f"the multiplication of {end} × {x} #= {end*x} ")
	x = x + 1

n = int(input("the table u want"))
start = int(input("from which number"))
end = int(input("at last "))
x = start

while x <= end :
	print(f" the multi of {n} × {x} = {n*x} ")
	x = x+1



star#t = int(input("value of first \n"))
end = int(input("value of second \n "))

x = 1
result = 0

while x <= end:
	result = result + start
	x = x+1 
print(result)

n1 = int(input("enter frst num "))
n2 = int(input("enter second num "))

q = 0
x = n1

while x>= divisor:
	x = x - dividend
	q = q+1
remainder = x	
print(q)
print(remainder)


deposit = float(input("enter ur deposit amount"))
interest = float(input("interest rate =="))
month = 1
balance = deposit

while month<= 24:
	balance = balance + (balance * (interest/100))
	print(balance)
	month = month +1
print(balance - deposit)


#QUESTION 5.12