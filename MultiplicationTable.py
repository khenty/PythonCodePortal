# a multiplication table for digits
def multiplication_table():
    '''multiplication_table() -> none
    prints a multiplication table for base 10
    that is 10 x 10.'''
    # prints the top row
    string = ''
    topRowString = ''
    for column in range(1,11):
        topRowString += '\t' + str(column)
    print(topRowString)
    string += topRowString + '\n'
    
    # print each subsequent row
    for row in range(1,11):
        rowString = str(row)
        for column in range(1,11):
            rowString += '\t' + str(row*column)
        print(rowString)
        string += rowString + '\n'
    return string
multiplication_table()
