# This program prints out the rows of pascal's triangle
# Bonga Njamela
# 28/05/20

def pascal_rows(row, height):
    """Function accepts previous rows and returns the next row of pascal's 
    triangle"""
    
    new_row = [0]
    new_item = 0
    current_row = row
    
    for i in range(len(row)+1):
        row = current_row
        if 1 <= i < len(row):
            new_item = row[i]+row[i-1]
            new_row.append(new_item)
    new_row.append(0)
    return new_row

def main():
    
    height = eval(input("Enter the height of the triangle:\n"))
    second_row = [0,1,1,0]
    first_row = 1
    
    
    print("The triangle is:")
    if height == 1:
        print(first_row)
    
    elif height == 2:
        
        print(first_row)
        
        for i in range(1,3):
            print(second_row[i], end=" ")
    
    else:
        
        print(1)
        
        for i in range(1,3):
            print(second_row[i], end=" ")
        print()
        
        for row in range(2, height):
            new_row = pascal_rows(second_row, height)
            second_row = new_row
            for pos in range(1, len(new_row)-1):
                print(new_row[pos], end=" ")
            print()

if __name__ == "__main__":
    main() 
