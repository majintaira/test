import csv

with open('./sample.csv', 'r') as f:
    reader = csv.reader(f)
#    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:
        print (row)          # 1行づつ取得できる