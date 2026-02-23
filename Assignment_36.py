#Problem Statement - Create a program to  Find all Numbers in a Range which are Perfect Squares 
# and Sum of all Digits in the Number is Less than 10  
list = input("Enter a range of numbers (start end) : ").split()
start = int(list[0])
end = int(list[1])
perfect_squares = []
for i in range(start, end + 1):
    if int(i**0.5)**2 == i:
        perfect_squares.append(i)  
result = []
for i in perfect_squares:
    if sum(int(j) for j in str(i)) < 10:
        result.append(i)
print("The numbers in the range that are perfect squares and sum of digits is less than 10 are: ", result)
