

### Лабораторна зі сроком сдачі до 01.10 (Файли) ###
def task_1(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8') as outfile:

        for line in infile:
            long_words = [word for word in line.split() if len(word) >= 7]
            outfile.write(' '.join(long_words) + '\n')

def task_2(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8') as outfile:

        outfile.writelines(infile)

def task_3(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(reversed(lines))

def task_4(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()


    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line)
        if any(',' not in line for line in lines):
            outfile.write('************\n')
        else:
            outfile.write('************\n')

def task_5(input_file, starting_char):
    count = 0
    with open(input_file, 'r', encoding='utf-8') as infile:
        count = sum(word.startswith(starting_char) for line in infile for word in line.split())
    return count

def task_6(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line.replace('*', '&').replace('&', '*'))

def task_9(input_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        return sum(len(line) for line in infile)

def task_10(input_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        return sum(1 for _ in infile)








# Самостійна робота: файли(срок до 01.10)


#1
def cmp_files(f1, f2):
    with open(f1, 'r', encoding='utf-8') as file1, open(f2, 'r', encoding='utf-8') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
        
        for i, (l1, l2) in enumerate(zip(lines1, lines2), start=1):
            if l1 != l2:
                print(f"Line {i} mismatch:")
                print(f"File 1: {l1.strip()}")
                print(f"File 2: {l2.strip()}")

#2
def stats(in_file, out_file):
    vows = "EYUOIAaeyioйуеаіояєЄЙУЕОАІЯЮ"
    cons = "ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮйцукенгшщзхфівапролджєячсмитьбюQWERTYUIOPASDFGHJKLZXCVBNM"
    
    with open(in_file, 'r', encoding='utf-8') as f:
        text = f.read()
        lines = text.splitlines()
        
        chars = len(text)
        ln = len(lines)
        v = sum(1 for ch in text if ch in vows)
        c = sum(1 for ch in text if ch in cons)
        nums = sum(1 for ch in text if ch.isdigit())
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(f"Chars: {chars}\nLines: {ln}\nVowels: {v}\nConsonants: {c}\nDigits: {nums}\n")

#3
def rm_last_line(in_file, out_file):
    with open(in_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    with open(out_file, 'w', encoding='utf-8') as f:
        f.writelines(lines[:-1])

#4
def longest_line(f_name):
    with open(f_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        long_ln = max(lines, key=len)
    
    print(f"Longest: {long_ln.strip()}\nLength: {len(long_ln.strip())}")

#5
def count_word(f_name, word):
    with open(f_name, 'r', encoding='utf-8') as f:
        text = f.read()
        count = text.lower().count(word.lower())
    
    print(f"'{word}' found {count} times.")

#6
def replace_word(in_file, out_file, target, replace):
    with open(in_file, 'r', encoding='utf-8') as f:
        text = f.read()
        
    new_text = text.replace(target, replace)
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(new_text)








# Самостійна робота: файли, ч.2 (срок до 03.10)


def load(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return [line.strip().split(',') for line in f]
    except FileNotFoundError:
        return []

def save(file, emps):
    with open(file, 'w', encoding='utf-8') as f:
        for emp in emps:
            f.write(','.join(emp) + '\n')

def add(emps):
    emps.append([input("Ім'я: "), input("Прізвище: "), input("Вік: ")])

def edit(emps):
    ln = input("Прізвище: ")
    for emp in emps:
        if emp[1] == ln:
            emp[0] = input("Нове ім'я: ")
            emp[1] = input("Нове прізвище: ")
            emp[2] = input("Новий вік: ")
            break

def delete(emps):
    ln = input("Прізвище: ")
    emps[:] = [emp for emp in emps if emp[1] != ln]

def search(emps):
    ln = input("Прізвище: ")
    for emp in emps:
        if emp[1] == ln:
            print(emp)

def list_emps(emps):
    for emp in emps:
        print(emp)

def main():
    file = input("Файл: ")
    emps = load(file)

    while True:
        cmd = input("Команда (add/edit/delete/search/list/save/exit): ").lower()
        if cmd == 'add': add(emps)
        elif cmd == 'edit': edit(emps)
        elif cmd == 'delete': delete(emps)
        elif cmd == 'search': search(emps)
        elif cmd == 'list': list_emps(emps)
        elif cmd == 'save': save(file, emps)
        elif cmd == 'exit':
            save(file, emps)
            break

main()









# Лабораторна робота: Файли, частина 2 (срок до 03.10)


#1
def remove_unacceptable_words(input_file, unacceptable_file, output_file):
    unacceptable_words = []
    with open(unacceptable_file, 'r', encoding='utf-8') as uf:
        unacceptable_words = [word.strip().lower() for word in uf]

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            filtered_words = [word for word in line.split() if word.lower() not in unacceptable_words]
            outfile.write(' '.join(filtered_words) + '\n')

#2
def transliterate(input_file, output_file, direction):
    uk_to_en = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'yu', 'я': 'ya'
    }

    translit_dict = uk_to_en if direction == 'uk_to_en' else {v: k for k, v in uk_to_en.items()}

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            transliterated_line = ''.join(translit_dict.get(char, char) for char in line)
            outfile.write(transliterated_line)

#3
def merge_files():
    filenames = []
    while True:
        filename = input("Введіть назву файлу, або 'вихід' для завершення: ")
        if filename.lower() == 'вихід':
            break
        filenames.append(filename)

    with open('merged.txt', 'w', encoding='utf-8') as outfile:
        for filename in filenames:
            try:
                with open(filename, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read() + '\n')
            except FileNotFoundError:
                print(f"Файл {filename} не знайдено.")

#4
def common_characters():
    filenames = []
    while True:
        filename = input("Введіть назву файлу, або 'вихід' для завершення): ")
        if filename.lower() == 'вихід':
            break
        filenames.append(filename)

    common_chars = set()
    for filename in filenames:
        try:
            with open(filename, 'r', encoding='utf-8') as infile:
                file_chars = set(infile.read())
                common_chars = common_chars.intersection(file_chars) if common_chars else file_chars
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")

    with open('common_characters.txt', 'w', encoding='utf-8') as outfile:
        if common_chars:
            outfile.write(''.join(common_chars))
        else:
            outfile.write('Немає спільних символів у файлах.')






# Ситстема контролю версій (срок до 08.10)

# Я розпишу послідовність своїх дій відповідно до ТЗ
"""
1. Встановив Git по вашому посиланню
1.2. зареєструвався командами:
    git config --global user.name, та git config --global user.email 
    
2. Створив папку командою - mkdir, та перейшов у терміналі за її репозиторієм

2.2. Командами echo "Перший файл" > file1.txt, створив 2 текстові файли з текстом у них
3. Ініціалізую git командою - git init

4. Додав два файли в індекс командою:
   git add file1.txt file2.txt

5. Створив перший commit:
   git commit -m "Перший коміт: додано file1.txt і file2.txt"

6. Змінив вміст file1.txt, додав новий рядок:
   echo "Додано новий рядок до file1.txt" >> file1.txt
   Додав змінений файл в індекс та створив новий commit:
   git add file1.txt
   git commit -m "Оновлено file1.txt"

7. Створив новий файл file3.txt:
   echo "Новий файл" > file3.txt
   Додав новий файл в індекс і створив commit:
   git add file3.txt
   git commit -m "Додано file3.txt"

8. Вніс зміни в file1.txt, зберіг їх, а потім скасував зміни:
   git checkout -- file1.txt

9. Вніс зміни в file1.txt, додав в індекс, а потім скасував зміни в індексі:
   git add file1.txt
   git reset file1.txt

10. Вніс зміни в file1.txt, додав в індекс, створив новий commit:
    git add file1.txt
    git commit -m "Нове оновлення file1.txt"
    Скасував зміни останнього commit:
    git revert HEAD

11. Видалив кілька останніх commit:
    git reset --hard HEAD~2
"""
