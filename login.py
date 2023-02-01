import mysql.connector
print("Database bağlantısı oluşturuluyor...")
connection = mysql.connector.connect(host='localhost',database='ugurdeneme',user='root',password='')
data = connection.cursor()

print(""" Giriş ekranına hoşgeldiniz. Giriş yapmadan önce kayıt olmanız gerekmektedir.

                1-) Giriş Yap
                2-) Kayıt Ol
                3-) Çıkış Yap
     """)

while True:
    
    option = input("Giriş yapmak için 1 girin, Kayıt olmak için 2 girin, Çıkış için 3 girin:")
    if (option == "1"):
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        sqlselectQuery = "select * from ugurdeneme.user"
        data.execute(sqlselectQuery)
        records = data.fetchall()
        for i in records:
            if(username == i[0] and password == i[1]):
                print("Hoşgeldiniz.")
            else:
                continue
        break


        
    elif (option == "2"):
        registerUserName = input("Kullanıcı Adı ?")
        registerPassword = input("Şifre ?")
        email = input("E posta hesabı ?")
        title = input("Ünvan ?")
        while True:
            print("Hesap Oluşturuluyor...")
            #sql = ("""INSERT INTO user(username, password, email, role) VALUES (f'{registerUserName}', f'{registerPassword}', f'{email}', f'{title}')""")
            sql = ("INSERT INTO user(username, password, email, role)"
            "VALUES (%s, %s, %s, %s)")
            userdata = (f'{registerUserName}',f'{registerPassword}',f'{email}',f'{title}')
            data.execute(sql, userdata)
            connection.commit()
            print("Hesap oluşturuldu.")
            break
        break
    elif (option == "3"):
        connection.commit()
        connection.close()
        break
    else:
        print("Hatalı giriş yaptınız..")
        continue

    

    
    

    


    





