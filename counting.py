# словарь с функциями
calc = {
    'plus': lambda x, y: x + y,
    'minus': lambda x, y: x - y,
    'division': lambda x, y: x / y,
    "multiply": lambda x, y: x * y,
}

def action(match, dictionary, default="NO CALC"):
    """шаблон фабрики функций"""
    if match in dictionary:
        return dictionary[match]
    return lambda *x: default

plus = action('plus', calc)
minus = action('minus', calc)
multiply = action('multiply', calc)
division = action('division', calc)


def counting(expression):
    ex = expression.split()
    output = []             # для чисел
    operator_stack = []     # для стека операторов
    for i in ex:
        if i.isdigit():
            output.append(i)
        else:
            operator_stack.append(i)
    if len(output) == 3:
        z = int(output.pop())
        y = int(output.pop())
        x = int(output.pop())    
        if operator_stack[0] == '+':
                res = plus(x, y)     
        elif operator_stack[0] == '-':
                res = minus(x, y)   
        elif operator_stack[0] == '/':
                res = division(x, y)   
        elif operator_stack[0] == '*':
                res = multiply(x, y)   
        if operator_stack[1] == '+':
                res2 = plus(res, z)  
        elif operator_stack[1] == '-':
                res2 = minus(res, z)
        elif operator_stack[1] == '/':
            if operator_stack[0] == '+':
                res2 = division(y, z) + x 
            else:
                res2 = x - division(y, z)    
        elif operator_stack[1] == '*':
            if operator_stack[0] == '+':
                res2 = x + multiply(y, z)
            else:
                res2 = x - division(y, z)     
       
    return res2

try:
    expression = '1 + 2 * 3'
    print(f'Результат полученного выражения: {expression} = ', counting(expression))
    exp = str(input('Введите свое выражение по образцу выше(выполняет две арифметические операции) '))
    print(f'Результат полученного выражения: {exp} = ', counting(exp))
except:
    print('Введите арифметическое выражение такого вида, в котором выполняется 2 операции (- или + или / или *) например: 1 - 2 * 3')    