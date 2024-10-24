from data import Book, Rectangle, Price, Circle, Employee, Point
import math
# Write your functions for each part in the space below.

# Part 1
def vowel_count(string: str) -> int:
    count = 0
    for char in string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            count += 1
    return count
#The purpose of this function is to take a string input from the user and then output the number of vowels present.
#The function takes in a string and creates a count variable of type integer, which is eventually outputted.
#def vowel_count(string: str) -> int:
#refer to hw1_test.py for testing

# Part 2
def short_lists(final: list[list[int]]) -> list:
    result = []
    for element in final:
        if len(element) == 2:
            result.append(element)
    return result
#The purpose of this function is to take in a list of integers with various sub-lists and return only the sub-lists whose length is equal to two.
#This function takes in the input of a list with sub-lists. Using a new variable with an empty list, I appended only the sub-lists with length 2 before returning it.
#def short_lists(final: list[list[int]]) -> list:
#refer to hw1_test.py for testing

# Part 3
def ascending_pairs(final: list[list[int]]) ->list:
    result = []
    for element in final:
        if len(element) == 2:
            if element[0] < element [1]:
                result.append(element)
            elif element[0] > element [1]:
                result.append([element[1], element[0]])
        else:
            result.append(element)
    return result
#The purpose of the function is to take in a list of integers with sub-lists and output a list where the sub-lists of length two are in ascending order.
#The function takes in an input of a list of integers with sub-lists and then filters for the sub-lists of length 2. Then using an empty list, I appended sub-lists of lengths not equal to two and appended the sub-lists of length two in ascending order, finally outputting it.
#def ascending_pairs(final: list[list[int]]) ->list:
#refer to hw1_test.py for testing

# Part 4
def add_prices(price1: Price, price2: Price):
    total = price1.cents + price2.cents
    dollar = 0
    cents = 0
    if total > 100:
        dollar = total//100
        cents = total % 100

    return price1.dollars + price2.dollars + dollar + cents
#The purpose of this function is to take in two prices (cents and dollars) and output the sum of the prices with the final cents < 100.
#The input this function takes is two price values in the Price class with a dollars and cents value. Then I created a variable sum to add the cents for both prices and finally output the cents after converting anything >100 to dollars.
#def add_prices(price1: Price, price2: Price):
#refer to data_tests.py for testing

# Part 5
def rectangle_area(rectangle: Rectangle)->float:
    xl, yl = rectangle.top_left.x, rectangle.top_left.y
    xb, yb = rectangle.bottom_right.x, rectangle.bottom_right.y

    return (xb-xl)*(yb-yl)
#The purpose of this function is to take in the coordinates of two points at different ends of a rectangle and return the area of the rectangle.
#The function takes in an input of the class Point and then sets the points equal to their respective coordinates. The final out put is the distance between the respective x and y coordinates multiplied by each other to give the rectangle area.
#def rectangle_area(rectangle: Rectangle)->float:
#refer to data_tests.py for testing

# Part 6 edit?
def books_by_author(author: str, books: list[Book])->list:
   result = []
   for book in books:
       for book_author in book.authors:
           if book_author == author:
               result.append(book)
   return result
#The purpose of this function is to take in a list of books (their titles and authors) and an author name from the user and return the books only for that specific author.
#This function takes in an input of the class Book. Then I created an empty list. If a book author for the list of books matched the author that was asked for by the user, it was appended to the empty list which was eventually returned.
#def books_by_author(author: str, books: list[Book])->list:
#refer to data_tests.py for testing


# Part 7
def circle_bound(rectangle: Rectangle)-> Circle:
    centerx = (rectangle.top_left.x + rectangle.bottom_right.x)/2
    centery = (rectangle.top_left.y + rectangle.bottom_right.y)/2
    center = Point(centerx, centery)

    radiusx = centerx - rectangle.top_left.x
    radiusy = centery - rectangle.top_left.y
    radius = math.sqrt(radiusx**2 + radiusy**2)

    return Circle (center, radius)

#The purpose of this function is to take in a rectangle object and return the smallest circle that can encloses the rectangle.
#This function take in an input of a rectangle object with points defining the top right, left, etc. Then the function finds the center of the two points for the rectangle using their x and y components. Then to find the radius of the circle I found the distance from the center of the rectangle to the corner, breaking it down into x and y components.
#def circle_bound(rectangle: Rectangle)-> Circle:
#refer to data_tests.py for testing

# Part 8
def below_pay_average(employees: list[Employee])->list:
    if len(employees) == 0:
        return []
    pay = 0
    for employee in employees:
        pay += employee.pay_rate

    average = pay / len(employees)
    return [employee.name for employee in employees if employee.pay_rate < average]


#The purpose of this function is to take a list of employees with information on their names as well as pay and return a list of their names whose pay are below the average pay for all employees.
#The function takes in an input of all the employees and their pay. Assuming the list is non empty, it sequentially adds the employee pay to a variable, pay, and then divides it by the number of employees. Finally the function outputs the list of employees whose pay is less than the average.
#def below_pay_average(employees: list[Employee])->list:
#refer to data_tests.py for testing