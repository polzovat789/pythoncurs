a = 'www.my_site.com#about'
b = a.replace('#', '/')
print(b)
S1 = 'first'
S2 = "ing"

print(S1 + S2)
msg = "Ivanou Ivan"

arr = msg.split()
print(arr)

msg = " ".join(arr[::-1])
print(msg)
test_string = " onetesttwo three "
print(test_string.strip())
txt = "pARiS"
print(txt.capitalize())
input_string = "Robin    Singh"
c = input_string.split()
print(c)
input_string = "I love arrays they are my favorite"
d = input_string.split()
print(d)
name_list = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
full_name = " ".join(name_list)
result = f"Привет, {full_name}! Добро пожаловать в {city} {country}"
print(result)
e = ["I", "love", "arrays", "they", "are", "my", "favorite"]
f = " ".join(e)
print(f)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
my_list.insert(2, 15)
print(my_list)
removed_element = my_list.pop(6)
print(my_list)
print(removed_element)
