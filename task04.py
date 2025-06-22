template = "Bugun {week_day} kuni, dars soat {oclock} da."
week_day = input()
oclock = float(input())

print(template.format(week_day=week_day, oclock=oclock))