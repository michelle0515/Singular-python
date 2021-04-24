'''
讓使用者輸入一個str，當str有在list裡面，就移除該str
沒有str就加入list, 並顯示最後的list，list初使值為
["apple", "ball" ,"car"]
'''
l=['apple','ball','banana']
a=input('word:')
if a in l:
    l.remove(a)
else:
    l.append(a)

print (l)


