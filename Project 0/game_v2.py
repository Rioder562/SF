import numpy as np 

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 # счетчик попыток
    low = 0 # начало интервала загадываемого числа
    high = 100 # конец интервала загадываемого числа
    while True:
        count += 1
        predict_number = (low + high)//2 # предполагаемое число
        if predict_number == number:
            break
        elif predict_number > number:
            high = predict_number
        else:
            low = predict_number
    return(count)
    

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 100 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)