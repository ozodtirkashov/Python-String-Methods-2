template = ("Salom, mening ismim {name} va yoshim {age}")
name = input() 
age = int(input())

print(template.format(name=name, age=age))