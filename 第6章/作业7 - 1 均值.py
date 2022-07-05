import csv

file_name = r"D:\华师\Python\第6章\iris.csv"
with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    iris = [iris_item for iris_item in reader]

count = 0
s_len_avg = 0; s_wid_avg = 0; p_len_avg = 0; p_wid_avg = 0
for i in iris:
    s_len_avg += eval(i['sepal length (cm)'])
    s_wid_avg += eval(i['sepal width (cm)'])
    p_len_avg += eval(i['petal length (cm)'])
    p_wid_avg += eval(i['petal width (cm)'])
    count = count + 1
else:
    s_len_avg /= count
    s_wid_avg /= count
    p_len_avg /= count
    p_wid_avg /= count

headers = ['Avg sepal length (cm)', 'Avg sepal width (cm)', 'Avg petal length (cm)', 'Avg petal width (cm)']
avg_value = [s_len_avg, s_wid_avg,p_len_avg,p_wid_avg]
file_name = r"D:\华师\Python\第6章\my_iris.csv"
with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerow(avg_value)
