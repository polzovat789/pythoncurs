import re

# Исправление ошибок повторов слов
def fix_repeats(text):
    return re.sub(r'\b(\w+)\s+\1\b', r'\1', text)

text = input("Введите текст с ошибками: ")
fixed_text = fix_repeats(text)
print(f"Исправленный текст: {fixed_text}")
