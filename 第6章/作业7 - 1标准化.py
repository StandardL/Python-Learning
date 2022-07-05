import csv

file_name = r"D:\华师\Python\第6章\iris.csv"
with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    iris = [iris_item for iris_item in reader]
s_len = []
s_wid = []
p_len = []
p_wid = []

for i in iris:
    s_len.append(eval(i['sepal length (cm)']))
    s_wid.append(eval(i['sepal width (cm)']))
    p_len.append(eval(i['petal length (cm)']))
    p_wid.append(eval(i['petal width (cm)']))

slmax = max(s_len)
slmin = min(s_len)
swmax = max(s_wid)
swmin = min(s_wid)
plmax = max(p_len)
plmin = min(p_len)
pwmax = max(p_wid)
pwmin = min(p_wid)

for i in iris:
    i['sepal length (cm)'] = (eval(i['sepal length (cm)']) - slmin) / (slmax - slmin)
    i['sepal width (cm)'] = (eval(i['sepal width (cm)']) - swmin) / (swmax - swmin)
    i['petal length (cm)'] = (eval(i['petal length (cm)']) - plmin) / (plmax - plmin)
    i['petal width (cm)'] = (eval(i['petal width (cm)']) - pwmin) / (pwmax - pwmin)

headers = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
file_name = r"D:\华师\Python\第6章\standard_iris.csv"
with open(file_name, 'w', newline='') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(iris)
