import numpy as np

def advanced_predict(number:int=1) -> int: # means that should be int as a result
    """ Addvanced self computering predicting of number

    Args:
        number (int, optional): predicted number. Defaults to 1.

    Returns:
        int: count chances
    """    
    print(f'Угадываем число: {number}')
    count = 0
    min = 1
    max = 101
    predictable_number = np.random.randint(1,101)
    while True:
        count +=1
        if predictable_number == number:
            break
        elif predictable_number > number:
            max = predictable_number
            print(f'Предсказываемое число: {predictable_number} больше загаданного в условии. Текущие максимум: {max}, минимум: {min}')
            predictable_number = (max+min)//2
        else:
            min = predictable_number
            print(f'Предсказываемое число: {predictable_number} меньше загаданного в условии. Текущие максимум: {max}, минимум: {min}')
            predictable_number = (max+min)//2
                        
    print(f'Число отгадано! Количество попыток: {count}')
    return count 

number = np.random.randint(1,101)
advanced_predict(number)