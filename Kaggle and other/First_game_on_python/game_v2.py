import numpy as np

def random_predict(number:int=1) -> int:
# means that should be int as a result
    """ Self computering predicting of number

    Args:
        number (int, optional): predicted number. Defaults to 1.

    Returns:
        int: count chances
    """    
    count = 0

    while True:
        count +=1
        predictable_number = np.random.randint(1,101)
        if predictable_number == number:
            break
    print(f'Количество попыток: {count}')
    return count 



def score_game(random_predict) -> int:
    
    """
    How much chances in average should be to find the number

    Args:
        random_predict (_type_): previous function

    Returns:
        int: average number of chances in 1000 times
    """   
    
    count_ls =[]
    np.random.seed(1) #перезапуск фукнции дает один и тот же результат
    random_array = np.random.randint(1,101, size=(1000)) #формируется массив с рандомными числами
    
    for number in random_array:
        count_ls.append(random_predict(number)) #заполняем результатами прогона функции по поиску числа
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__': #специальная строка для вывода в юпитере
    score_game(random_predict)
    
#pip freeze > requirements.txt
#pip install -r requirements.txt