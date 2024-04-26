import csv

path='D:/zzh/DATA2.csv'
out_path='D:/zzh/out.csv'
currentID=''
CN_NUM=0
EN_NUM=0
with open(path, 'r', encoding='GBK') as f1, open(out_path, 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=',')
    reader = csv.reader(f1)
    for row in reader:
        if row[0] != 'appln_id':
            if row[0]!=currentID:
                currentID=row[0]
                print(currentID)
                if row[7]=='en':
                    EN_NUM+=1
                if row[7] == 'zh':
                    CN_NUM+=1
                    writer.writerow(row)
        else:
            writer.writerow(row)
print(EN_NUM)
print(CN_NUM)