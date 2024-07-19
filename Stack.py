class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

# Пример: поддержка операций в калькуляторе
def evaluate_expression(expression):
    # Функция для выполнения арифметических операций
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.push(left + right)
        elif operator == '-':
            values.push(left - right)
        elif operator == '*':
            values.push(left * right)
        elif operator == '/':
            values.push(left / right)

    operators = Stack()
    values = Stack()
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i] in '0123456789':
            j = i
            while j < len(expression) and expression[j] in '0123456789':
                j += 1
            values.push(int(expression[i:j]))
            i = j
        elif expression[i] in '+-*/':
            while (not operators.is_empty() and
                   precedence(operators.peek()) >= precedence(expression[i])):
                apply_operator(operators, values)
            operators.push(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.push(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators.peek() != '(':
                apply_operator(operators, values)
            operators.pop()
            i += 1

    while not operators.is_empty():
        apply_operator(operators, values)

    return values.pop()

def precedence(operator):
    if operator in '+-':
        return 1
    if operator in '*/':
        return 2
    return 0

# Пример использования функции для выражения "3 + 5 * ( 2 - 8 )"
expression = "3 + 5 * ( 2 - 8 )"
result = evaluate_expression(expression)
print(result)  # Вывод: -13
