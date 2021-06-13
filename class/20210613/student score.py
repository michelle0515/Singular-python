alist = []
while True:
    while True:
        try:
            name = input('請輸入學生名稱:')
            subject = input('請輸入科目:')
            score = input('請輸入分數:')
        except:
            print('wrong')
        else:
            break

    for i in alist:
        if name in i:
            i.append([subject,score])
            break
    else:
        alist.append([name,[subject,score]])

    print(alist)
