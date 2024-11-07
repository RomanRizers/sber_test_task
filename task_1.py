"""
Есть текст с произвольными символами. Нужно определить, корректно ли в нем
расположены квадратные скобки (правильно открыты и закрыты).
"""

def check_brackets(text):
    """Проверяем корректность открытия и закрытия скобок"""
    stack = []
 
    for char in text:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0


test_strings = [
    "[hello] world]",
    "hello [world",
    "[]]",
    "[[hello][world]]]",
    "]hello[",
    "[hello] world",
    "he[ll[o[worl]d]ok]",
    "[[hello][world]]",
    "[[]]",
    "s[[][][ber]]"
]

for text in test_strings:
    result = check_brackets(text)
    print(f"{text}: {'Корректно' if result else 'Некорректно'}")
