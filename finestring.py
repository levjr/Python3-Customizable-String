def finestring(input_str, input_symbol, input_pos, input_length):
    ''' 
        #The function is designed to beautifully display a string with characters with the ability to...
         #...centered, left and right
        
        #finestring("Your string", "Symbol", "Position", String length)
        
        #"Your string" - your text
        #"Symbol" - char/string. For example: "*" |
        #"Position" - "^" -> centering, ">" -> symbols from the right, "<" -> symbols on the left
        #String length - the length of the string to be output

        #Example: 
        #Input: finestring("Jessica", "_", "^", 15)
        #Output: ____Jessica_____
    '''
    length = input_length
    if(len(input_str) % 2):
        length += 1
    print(('{0:' + str(input_symbol) + str(input_pos) +str(length)+'}').format(input_str))

