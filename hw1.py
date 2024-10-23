from data import Book, Rectangle, Price, Circle
# Write your functions for each part in the space below.

# Part 1
def vowel_count(string):
    count = 0
    for char in string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            count += 1
    return count


# Part 2
def short_lists(lst: list[list[int]]):
    result = []
    for element in lst:
        if len(element) == 2:
            result.append(element)
    return result


# Part 3
def ascending_pairs(lst: list[list[int]]):
    result = []
    for element in lst:
        if len(element) == 2:
            if element[0] < element [1]:
                result.append(element)
            elif element[0] > element [1]:
                result.append([element[1], element[0]])
        else:
            result.append(element)
    return result

# Part 4
def add_prices(price1: Price, price2: Price):
    total = price1.cents + price2.cents
    dollar = 0
    cents = 0
    if total > 100:
        dollar = total//100
        cents = total % 100

    return price1.dollars + price2.dollars + dollar + cents

# Part 5
def rectangle_area(rectangle: Rectangle):
    xl, yl = rectangle.top_left.x, rectangle.top_left.y
    xb, yb = rectangle.bottom_right.x, rectangle.bottom_right.y

    return (xb-xl)*(yb-yl)


# Part 6 edit?
def books_by_author(author: str, books: list[Book]):
   result = []
   for book in books:
       for book_author in book.authors:
           if book_author == author:
               result.append(book)
   return result

# Part 7


# Part 8

