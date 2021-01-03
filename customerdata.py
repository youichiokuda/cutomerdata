import qrcode
import datetime
import csv

name=input('氏名は?')
address=input('住所は？')
age=input('年齢は？')
tel=input('電話番号は？')
mail=input('メールは?')


dt_now=datetime.datetime.now()
dt=dt_now.strftime('%Y年%m月%d日 %H時%M分')

img=qrcode.make( ' 電話番号: ' + str(tel) +'メール: ' +str(mail)+'氏名：'+str(name)  + '住所:'+ str(address)+'作成日時:'+ str(dt))
img.save(str(name)+str(tel))


with open('customer_data.csv','a') as f:
    writer = csv.writer(f)
    #次の行は初回登録のみ。２回目以降の登録時はコメントアウト！！
    writer.writerow(['氏名','年齢','住所','電話番号','メール','登録日'])
    writer.writerow([str(name),str(age),str(address),str(tel),str(mail),str(dt)])
    f.close()