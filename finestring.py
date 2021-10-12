def finestring(input_str, input_symbol, input_pos, input_length):
    ''' 
        #Функция предназначена для красивого вывода строки с символами с возможностью... 
        #...расположение по центру, слева и справа
        
        #finestring("Ваша строка", "Символ", "Позиция", Длина строки)
        #
        #"Ваша строка" - string
        #"Символ" - char/string. Например: "*" |
        #"Позиция" - "^" -> центрировать, ">" -> символы с права, "<" -> символы слева
        #Длина строки - длина string/строки для вывода

        #Пример: 
        #Ввод: finestring("Jessica", "_", "^", 15)
        #Вывод____Jessica_____
    '''
    length = input_length
    if(len(input_str) % 2):
        length += 1
    print(('{0:' + str(input_symbol) + str(input_pos) +str(length)+'}').format(input_str))

