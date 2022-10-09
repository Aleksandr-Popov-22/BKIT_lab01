import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        if index==1:
            cf = 'A'
        elif index ==2:
            cf = 'B'
        elif index==3:
            cf = 'C'
        try:
            coef = float(coef_str)
        except:
            flag = False
            while flag == False:
                print('Некорректный коэффициент', cf, 'введите вручную')
                coef_str = input()
                try:
                    coef = float(coef_str)
                    flag = True
                except:
                    flag = False
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
        try:
            coef = float(coef_str)
        except:
            flag = False
            while flag == False:
                print('Некорректный коэффициент, введите снова')
                coef_str = input()
                try:
                    coef = float(coef_str)
                    flag = True
                except:
                    flag = False
                
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef

def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        arg1 = b / (2.0*a)
        if arg1<0:
            root1 = math.sqrt(b / (2.0*a))
            result.append(root1)
        elif arg1>0:
            root1 = -math.sqrt(b / (2.0*a))
            root2 = math.sqrt(b / (2.0*a))
            result.append(root1)
            result.append(root2)
        elif arg1 == 0:
            root1 = math.sqrt(b / (2.0*a))
            result.append(root1)
    elif D > 0.0:
        sqD = math.sqrt(D)
        arg1 = (-b + sqD) / (2.0*a)
        arg2 = (-b - sqD) / (2.0*a)
        if (arg1<0 and arg2<0):
            result =[]
        elif arg1<0:
            root1 = math.sqrt(arg2)
            root2 = -math.sqrt(arg2)
            if root1 == root2:
                result.append(root1)
            else:
                result.append(root1)
                result.append(root2)
        elif arg2<0:
            root1 = math.sqrt(arg1)
            root2 = -math.sqrt(arg1)
            if root1 == root2:
                result.append(root1)
            else:
                result.append(root1)
                result.append(root2)
        elif (arg1>=0 and arg2>=0):
            root1 = math.sqrt(arg1)
            root2 = -math.sqrt(arg1)
            root3 = math.sqrt(arg2)
            root4 = -math.sqrt(arg2)
            if root1 == root2:
                result.append(root1)
            elif root3 == root4:
                result.append(root3)
            elif root1 == root3:
                result.append(root1)
            else:
                result.append(root1)
                result.append(root2)
                result.append(root3)
                result.append(root4)
        
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    else:
        print('Корни уравнения:', roots)    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
