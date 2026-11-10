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