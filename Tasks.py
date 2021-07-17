# 1) დაწერეთ ფუნქცია, რომელსაც გადაეცემა string-ი და აბრუნებს True-ს თუ  გადაცემული string-ი პალინდრომია, წინააღმდეგ
# შემთხვევაში False-ს. პალინდრომი არის ტექსტი რომელიც ერთნაირად იკითხება ორივე მხრიდან, მაგ: radar, level, rotor, abcdcba.


# def check_str(value):
#     if value != value[::-1]:
#         print("It's not palindrome")
#     else:
#         print("It's palindrome")


# check_str('abcdcba')
# check_str('radar')
# check_str('level')
# check_str('rotor')
# check_str('world')
# check_str('python')

# 2) გვაქვს 1,5,10,20 და 50 თეთრიანი მონეტები. დაწერეთ ფუნქცია, რომელსაც გადაეცემა თანხა (თეთრებში) და აბრუნებს მონეტების
# მინიმალურ რაოდენობას, რომლითაც შეგვიძლია ეს თანხა დავახურდაოთ.
# მაგ: ყველაზე მოკლე გზა 70 თეთრის დასაშლელად არის 50+20 თეთრიანი მონეტები, შესაბამისად ფუნქციამ უნდა დააბრუნოს 2.



# 3) მოცემულია string-ი რომელიც შედგება “(“ და “)“ ელემენტებისგან. დაწერეთ ფუნქცია რომელიც აბრუნებს ფრჩხილები არის თუ არა
# მათემატიკურად სწორად დასმული. მაგ: “(()())” სწორი მიმდევრობაა, “())()” არასწორია


# def correct_brackets(text, brackets="()"):
#     open, close = brackets[::2], brackets[1::2]
#     stack = []
#     for character in text:
#         if character in open:
#             stack.append(open.index(character))
#         elif character in close:
#             if stack and stack[-1] == close.index(character):
#                 stack.pop()
#             else:
#                 return False
#     return not stack


# exp1 = correct_brackets('(()())')
# exp2 = correct_brackets('()())')
# exp3 = correct_brackets('(((((((')
# exp4 = correct_brackets('((()(())(()))())')
# print(exp1)
# print(exp2)
# print(exp3)
# print(exp4)


# 4) გვაქვს n სართულიანი კიბე, ერთ მოქმედებაში შეგვიძლია ავიდეთ 1 ან 2 საფეხურით. დაწერეთ ფუნქცია რომელიც დაითვლის n
# სართულზე ასვლის ვარიანტების რაოდენობას.


# def stairs(lvl):
#     str1 = 1
#     str2 = 1
#     i = 0
#     while i < lvl - 1:
#         str_sum = str1 + str2
#         str1 = str2
#         str2 = str_sum
#         i = i + 1

#     print("ვარიანტების რაოდენობა", str2)


# exp1 = int(input('სართულის ნომერი: '))
# stairs(exp1)


# 5) გვაქვს teacher ცხრილი, რომელსაც აქვს შემდეგი მახასიათებლები: სახელი, გვარი, სქესი, საგანი. გვაქვს pupil ცხრილი, რომელსაც
# აქვს შემდეგი მახასიათებლები: სახელი, გვარი, სქესი, კლასი. ააგეთ ნებისმიერ რელაციურ ბაზაში ისეთი დამოკიდებულება, რომელიც
# საშუალებას მოგვცემს, რომ მასწავლებელმა ასწავლოს რამოდენიმე მოსწავლეს და ამავდროულად მოსწავლეს ჰყავდეს რამდენიმე
# მასწავლებელი (როგორც რეალურ ცხოვრებაში).
# 1. დაწერეთ SQL რომელიც ააგებს შესაბამის table-ებს.
# 2. დაწერეთ SQL რომელიც დააბრუნებს ყველა მასწავლებელს, რომელიც ასწავლის მოსწავლეს, რომელის სახელია: “გიორგი”.

# import sqlite3

# conn = sqlite3.connect('my_database.sqlite3')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS teacher
#                 (t_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 fname VARCHAR(50),
#                 lname VARCHAR(50),
#                 gender VARCHAR(50),
#                 subject VARCHAR(50))''')
# conn.commit()

# cursor.execute('''CREATE TABLE IF NOT EXISTS pupil
#                 (p_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 fname VARCHAR(50),
#                 lname VARCHAR(50),
#                 gender VARCHAR(50),
#                 class INTEGER)''')
# conn.commit()


# conn.close()


# 6) არსებობს ასეთი ფაბლიქ API https://api.chucknorris.io/ რომელიც რანდომად აბრუნებს ხუმრობებს ჩაკ ნორისზე. დაწერეთ თქვენი
# API ნებისმიერ პითონის web framework-ში როგორიცაა მაგ: Django, Flask, FastAPI ან სხვა ნებისმიერი შემდეგი ენდფოინთებით:
# /random_joke რომელიც წამოიღებს რანდომ ხუმრობას შესაბამისი API-დან და შეინახავს ლოკალურად(შეგიძლიათ შეინახოთ sqlite
# ბაზაში ან ტექსტურ ფაილში ნებისმიერი ფორამტით). აუცილებელია რომ შეინახოთ მინიმუმ ხუმრობის ტექსტი.
# /saved_joks რომელიც დააბრუნებს ყველა ლოკალურად შენახულ ხუმრობას(ბაზიდან ან ფაილიდან, იმის მიხედვით სად ინახავს პირველი
# ენდფოინთი) JSON ფორმატში.
