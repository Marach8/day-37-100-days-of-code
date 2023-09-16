
a = input('''
\033[31mEnter your details in this order! \033[0mFirstname, Lastname, Mother's maiden name and City you were born in:
>> \033[32m''')
b = a.split()
c = b[0][:3]
d = b[1][:3]
first_name = (c + d).lower().capitalize()
e = b[2][:2]
f = b[3][-3:]
last_name = (e + f).lower().capitalize()
print()
print(f'\033[34mYour Star Wars name is {first_name} {last_name} 😂😂')