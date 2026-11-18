# Part 1: Positional and Keyword Arguments 
# 1. Create a function student_details() that accepts rollno, name, and age and prints all details.
def student_details(rollno, name, age):
    print("Student Roll Number:", rollno)
    print("Student Name:", name)
    print("Student Age:", age)
student_details(101, "Radhika", 22)

# 2. Create a function employee_details() that accepts eid, ename, and salary and returns the employee details.
def employee_details(eid,ename,salary):
    print("Employee ID:",eid)
    print("Employee Name:",ename)
    print("Employee Salary:",salary)
employee_details(11,"Neha Patil",30000)

# 3. Create a function addition() that accepts two numbers and returns their addition.
def addition(x,y):
    return x + y
result=addition(10,20)
print("Addition =",result)

# 4. Create a function student_marks() that accepts a student's name and marks in three subjects and prints the total marks.
def student_marks(name, sub1, sub2, sub3):
    total = sub1 + sub2 + sub3
    print("Student Name:", name)
    print("Total Marks:", total)
student_marks("Pratiksha", 85, 90, 80)

# 5. Create a function product_details() that accepts pid, pname, and price and prints the details.
def product_details(pid,pname,price):
    print("Product ID:",pid)
    print("Product Name:",pname)
    print("Product Price:",price)
product_details(101,"Laptop",75000)

# 6. Create a function rectangle_area() that accepts length and width and returns the area.
def rectangle_area(length,width):
    area=length * width
    return area
result=rectangle_area(length=10,width=5)
print("Area Of Rectangle:",result)

# 7. Create a function student_info() and call it using positional arguments
def student_info(rollno,sname,age):
    print("Student Roll No:",rollno)
    print("Student Name:",sname)
    print("Student Age:",age)
student_info(1,"Vrushali",23)

# 8. Create a function student_info() and call it using keyword arguments in a different order.
def student_info(rollno, sname, age):
    print("Roll Number:", rollno)
    print("Student Name:", sname)
    print("Age:", age)
student_info(age=22, sname="Radhika", rollno=101)

# 9. Create a function bank_details() that accepts account number, customer name, and balance. Call the function using both positional and keyword arguments separately.
def bank_details(ano,cname,bal):
    print("Account Number:",ano)
    print("Customer Name:",cname)
    print("Balance:",bal)
# Positional Arguments
bank_details(10125256,"Gayatri Shinde",150000)
# Keyword Arguments
bank_details(ano=1452636,cname="Poonam Jadhav",bal=75000)

# 10. Create a function calculate() that accepts three numbers and returns their sum, average, maximum,and minimum.
def calculate(num1,num2,num3):
    sum=num1+num2+num3
    average=sum/3
    maximum=max(num1,num2,num3)
    minimum=min(num1,num2,num3)
    return sum,average,maximum,minimum
result=calculate(10,20,30)
print("Sum=",result[0])
print("Average=",result[1])
print("Maximum=",result[2])
print("Minimum=",result[3])


# Part 2: Default Arguments
# 11. Create a function student_details() with city='Pune' as a default argument.
def student_details(rollno,sname,city="Pune"):
    print("Student Roll NO:",rollno)
    print("Student Name:",sname)
    print("Student City:",city)
student_details(1,"Radhika")

# 12. Create a function employee_details() with city='Pune' and company='TKA' as default arguments.
def employee_details(eid,ename,city="Pune",company="TKA"):
    print("Employee ID:",eid)
    print("Employee Name:",ename)
    print("Employee City:",city)
    print("Employee Company:",company)
employee_details(1,"Ankita Pawar")

# 13. Create a function product_details() where quantity=1 is the default value.
def product_details(pid,pname,quantity=1):
    print("Product ID:",pid)
    print("Product Name:",pname)
    print("Product Quantity:",quantity)
product_details(101,"Mobile")

# 14. Create a function bank_account() with a default branch name 'Karve Nagar'.
def bank_account(ano, cname, balance, branch='Karve Nagar'):
    print("Account Number:", ano)
    print("Customer Name:", cname)
    print("Balance:", balance)
    print("Branch Name:", branch)
bank_account(101, "Samiksha Patil", 50000)

# 15. Create a function course_details() with a default duration of '6 Months'.
def course_details(cname, fees, duration='6 Months'):
    print("Course Name:", cname)
    print("Course Fees:", fees)
    print("Course Duration:", duration)
course_details("Python Full Stack Development", 30000)

# 16. Create a function student_details() and call it once without passing the city and once by passing a different city.
def student_details(name, age, city='Pune'):
    print("Student Name:", name)
    print("Age:", age)
    print("City:", city)
# Without passing city
student_details("Radhika", 22)
print("--------------------")
# Passing a different city
student_details("Radhika", 22, "Mumbai")

# 17. Create a function calculate_bill() that accepts price, quantity=1, and discount=0.
def calculate_bill(price, quantity=1, discount=0):
    total = price * quantity
    final_amount = total - discount
    return final_amount
result = calculate_bill(500, 2, 100)
print("Final Bill Amount:", result)

# 18. Create a function employee_salary() with bonus=5000 as a default argument.
def employee_salary(name, salary, bonus=5000):
    total= salary + bonus
    print("Employee Name:", name)
    print("Basic Salary:", salary)
    print("Bonus:", bonus)
    print("Total Salary:", total)
employee_salary("Priya Jadhav", 30000)

# 19. Create a function movie_details() with language='Hindi' as a default argument.
def movie_details(mname,language='Hindi'):
    print("Movie Name:", mname)
    print("Language:", language)
movie_details("Padmaavat")

# 20. Create a function user_profile() with default values for city and country. Override only one default value while calling the function.
def user_profile(name, city="Pune", country="India"):
    print("Name:", name)
    print("City:", city)
    print("Country:", country)
# Override city
user_profile("Radhika", city="Mumbai")

# Part 3: return Statement
# 21. Create a function that accepts two numbers and returns their addition.
def addition(x , y):
    return x+y
result = addition(30, 20)
print("Addition:", result)

# 22. Create a function that accepts three numbers and returns all three numbers as a tuple.
def numbers(x, y, z):
    return x, y, z
result = numbers(10, 20, 30)
print("Tuple:", result)
print("Type:", type(result))

# 23. Create a function that accepts a student's marks and returns 'Pass' or 'Fail'.
def student_result(marks):
    if marks >= 35:
        return "Pass"
    else:
        return "Fail"
result = student_result(75)
print("Result:", result)

# 24. Create a function that accepts a number and returns its square and cube.
def Squarecube(num):
    square = num ** 2
    cube = num ** 3
    return square, cube
result = Squarecube(4)
print("Square:", result[0])
print("Cube:", result[1])

# 25. Create a function that accepts two numbers and returns addition, subtraction, multiplication, and division.
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division
result = calculate(30, 20)
print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])
print("Division:", result[3])

# 26. Create a function that accepts a string and returns its length
def Stringlength(text):
    return len(text)
result=Stringlength("Python")
print("Length Of String:",result)

# 27. Create a function that accepts a list of numbers and returns the maximum number.
def find_max(numbers):
    return max(numbers)
result = find_max([10, 25, 15, 40, 50])
print("Maximum Number:", result)

# 28. Create a function that accepts employee details and returns a formatted string containing all employee information.
def employee_details(eid, ename, salary):
    return f"Employee ID: {eid}, Name: {ename}, Salary: {salary}"
result = employee_details(101, "Preeti Jadhav", 30000)
print(result)

# Part 4: *args - Variable Number of Arguments
# 29. Create a function using *args to accept any number of integers and return them as a tuple.
def numbers(*args):
    return args
result = numbers(10, 20, 30, 40, 50)
print("Numbers:", result)
print("Type:", type(result))

# 30. Create a function using *args to calculate the sum of any number of values.
def addition(*args):
    total = sum(args)
    return total
result = addition(10, 20, 30, 40, 50)
print("Sum:", result)

# 31. Create a function using *args to find the maximum number.
def find_max(*args):
    maximum = max(args)
    return maximum
result = find_max(10, 25, 45, 15, 30)
print("Maximum Number:", result)

# 32. Create a function using *args to find the minimum number.
def find_max(*args):
    minimum = min(args)
    return minimum
result = find_max(10, 25, 45, 15, 30)
print("Minimum Number:", result)

# 33. Create a function using *args to calculate the average of all numbers.
def Calculateaverage(*args):
    total = sum(args)
    average = total / len(args)
    return average
result = Calculateaverage(10, 20, 30, 40, 50)
print("Average:", result)

# 34. Create a function using *args to print all student names passed to the function.
def student_names(*args):
    for name in args:
        print(name)
student_names("Aarti", "Pratiksha", "Radhika", "Sneha", "Vrushali")

# 35. Create a function using *args that counts how many values are passed to the function.
def Countvalues(*args):
    count = len(args)
    return count
result = Countvalues(10, 20, 30, 40, 50)
print("Total values:", result)

# 36. Create a function using *args that returns all even numbers from the given arguments.
def even_numbers(*args):
    even = []
    for num in args:
        if num % 2 == 0:
            even.append(num)
    return even
result = even_numbers(10, 15, 20, 25, 30, 35, 40)
print("Even numbers:", result)

# Part 5: **kwargs - Keyword Variable Arguments 
# 37. Create a function using **kwargs to accept student details and return them as a dictionary.
def student_details(**kwargs):
    return kwargs
result = student_details(name="Rahul",roll_no=101,course="Python",marks=85)
print(result)

# 38. Create a function using **kwargs to accept employee information such as eid, ename, salary, and city.
def employee_info(**kwargs):
    return kwargs
result = employee_info(eid=101,ename="Rahul",salary=25000,city="Pune")
print(result)

# 39. Create a function using **kwargs to print all key-value pairs.
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
print_details(name="Rahul",age=22,course="Python",city="Pune")

# 40. Create a function using **kwargs to accept product details.
def product_details(**kwargs):
    return kwargs
result = product_details(pid=101,pname="Laptop",price=50000,quantity=2,brand="HP")
print(result)

# 41. Create a function using **kwargs to accept bank customer details.
def bank_customer(**kwargs):
    return kwargs
result = bank_customer(cid=101,cname="Rahul",ano=123456,balance=25000,branch="Pune")
print(result)

# 42. Create a function that prints 'Task Started', returns the **kwargs dictionary, and observe whether the code after return executes.
def task(**kwargs):
    print("Task Started")
    return kwargs
    print("Code after return")
result = task(tid=101,tname="Python Programming",status="Pending")
print(result)

# 43. Create a function using **kwargs and count the total number of key-value pairs received.
def count_details(**kwargs):
    return len(kwargs)
result = count_details(name="Radhika",age=22,course="Python",city="Pune")
print("Total key value pairs:", result)

# Part 6: yield and Generator Functions 
# 44. Create a generator function that accepts student details using **kwargs and yields the dictionary.
def student_details(**kwargs):
    yield kwargs
result = student_details(name="Radhika",roll_no=101,course="Python",marks=85)
for data in result:
    print(data)

# 45. Create a generator function that yields numbers from 1 to 10.
def numbers():
    for i in range(1, 11):
        yield i
result = numbers()
for num in result:
    print(num)

# 46. Create a generator function that accepts a number n and yields numbers from 1 to n.
def numbers(n):
    for i in range(1, n + 1):
        yield i
result = numbers(5)
for num in result:
    print(num)

# 47. Create a generator function that accepts multiple numbers using *args and yields each number one by one.
def numbers(*args):
    for num in args:
        yield num
result = numbers(10, 20, 30, 40, 50)
for n in result:
    print(n)

# Part 7: Positional-Only Arguments
# 48. Create a function student_info(sid, sname, /) and call it correctly using positional arguments.
def student_info(sid, sname, /):
    print("Student ID:", sid)
    print("Student Name:", sname)
student_info(101, "Radhika")

# 49. Create a function with rollno, name, and age as positional-only arguments.
def student_info(rollno, name, age, /):
    print("Roll Number:", rollno)
    print("Name:", name)
    print("Age:", age)
student_info(101, "Radhka", 22)

# 50. Create a function addition(num1, num2, /) and perform addition. Try different valid function calls.
def addition(num1, num2, /):
    return num1 + num2
print(addition(10, 20))
print(addition(50, 30))
print(addition(100, 200))


# Part 8: Keyword-Only Arguments 
# 51. Create a function student_info(*, sid, sname) and call it using keyword arguments.
def student_info(*, sid, sname):
    print("Student ID:", sid)
    print("Student Name:", sname)
student_info(sid=101, sname="Radhika")

# 52. Create a function employee_info(*, eid, ename, salary) using keyword-only arguments.
def employee_info(*,eid,ename,salary):
    print("Employee ID:",eid)
    print("Employee Name:",ename)
    print("Employee Salary:",salary)
employee_info(eid=101,ename="Radhika",salary=35000)

# 53. Create a function where name is positional and city and salary are keyword-only arguments.
def employee_info(*,ename,city,salary):
    print("Name:",ename)
    print("City:",city)
    print("Salary:",salary)
employee_info(ename="Radhika",city="Pune",salary=35000)


# Part 9: Global and Local Variables
# 54. Create a global variable num1 = 10 and a function containing a local variable num2 = 20. Print their addition inside the function.
num1=10
def Addition():
    num2=20
    print("Additon:",num1+num2)
Addition()

# 55. Create a global variable and modify its value inside a function using the global keyword.
num = 10
def changevalue():
    global num
    num = 20
    print("Inside function:", num)
changevalue()
print("Outside function:", num)

# 56. Create a program where a local variable and global variable have the same name. Observe and understand their behavior.
num=10
def Samename():
    num=20
    print("Inside Function",num)
Samename()
print("Outside Function",num)


# Part 10: Recursive Functions
# 57. Create a recursive function to print numbers from 10 to 1.
def numbers(n):
    if n==0:
        return
    print(n)
    numbers(n - 1)
numbers(10)

# 58. Create a recursive function to print numbers from 1 to 10.
def numbers(n):
    if n>10:
        return
    print(n)
    numbers(n + 1)
numbers(1)

# 59. Create a recursive function to calculate the sum of the first n natural numbers.
def Naturalnosum(n):
    if n == 0:
        return 0
    return n + Naturalnosum(n - 1)
result = Naturalnosum(10)
print("Sum:", result)

# 60. Create a recursive function to calculate the factorial of a number.
def Factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * Factorial(n - 1)
result = Factorial(8)
print("Factorial:", result)

# Part 11: Advanced Recursive Function Tasks 
# 61. Create a recursive function to check whether a given string is a palindrome or not. Example: 'madam'-> Palindrome.
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
text = "madam"
if palindrome(text):
    print("String is a Palindrome")
else:
    print("String is Not Palindrome")

# 62. Create a recursive function to calculate the factorial of a given number. Example: 5! = 120.
def Factorial(n):
    if n == 1:
        return 1
    return n * Factorial(n - 1)
print(Factorial(5))

# 63. Create a recursive function to print or generate the Fibonacci series up to n terms.
def Fibonacci(a, b, n):
    if n == 0:
        return
    print(a, end=" ")
    Fibonacci(b, a + b, n - 1)
Fibonacci(0, 1, 10)

# 64. Create a recursive function to reverse a given string. Example: 'Python' -> 'nohtyP'.
def Reversestring(s):
    if s == "":
        return s
    return Reversestring(s[1:]) + s[0]
print(Reversestring("Python"))

# 65. Create a recursive function to calculate the sum of digits of a number. Example: 12345 -> 15.
def Digitsum(n):
    if n == 0:
        return 0
    return n % 10 + Digitsum(n // 10)
print(Digitsum(15412))

# 66. Create a recursive function to calculate the power of a number. Example: 2 raised to power 5 -> 32.
def Power(a, b):
    if b == 0:
        return 1
    return a * Power(a, b - 1)
print(Power(2, 5))

# 67. Create a recursive function to count the total number of digits in a given number. Example: 123456 -> 6.
def Digitcount(n):
    if n == 0:
        return 0
    return 1 + Digitcount(n // 10)
print(Digitcount(123456))

# 68. Create a recursive function to find the Greatest Common Divisor (GCD) of two numbers. Example: 12 and 18 -> 6.
def Gcd(a, b):
    if b == 0:
        return a
    return Gcd(b, a % b)
print(Gcd(12, 18))

# 69. Create a recursive function to calculate the product of numbers from 1 to n.
def Product(n):
    if n == 1:
        return 1
    return n * Product(n - 1)
print(Product(5))

# 70. Create a recursive function to count the total number of vowels in a given string. Example: 'Education'-> 5
def Vowels(s):
    if s == "":
        return 0
    if s[0] in "aeiouAEIOU":
        return 1 + Vowels(s[1:])
    return Vowels(s[1:])
print(Vowels("Python"))

