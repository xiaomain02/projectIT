import csv
with open("3_10705.csv", "r", encoding="utf-8", newline="") as f:
    reader=csv.reader(f, delimiter=",")
    rows=list(reader)[1:]

k=0
for i in range(len(rows)):
    if rows[i][2]=="Батончик соевый":
        if rows[i][3]=="грамм": k+=int(rows[i][4])
        if rows[i][3]=="кг": k+=int(rows[i][4])*1000
print(k)
