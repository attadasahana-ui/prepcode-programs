data = input()
data = data.split()
salary = int(data[0])
hra = int(data[1]) * salary / 100
da = int(data[2]) * salary / 100
pf = int(data[3]) * salary / 100
allowance = data[4]

if allowance == "A":
    print(salary + hra + da - pf + 1500)
if allowance == "B":
    print(salary + hra + da - pf + 1700)
if allowance == "C":
    print(salary + hra + da - pf + 1900)