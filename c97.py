name='sparsh'
print(name)
n=15
print(n)
friendlist=['sparsh','kabir','hriday']
print(friendlist)
print(friendlist[2])

for friend in friendlist:
    print(friend)

count=5
while(count>=0):
    print(count)
    count=count-1



pocketmoney=int(input('enter your pocket money'))
print(pocketmoney)
if (pocketmoney>500):
    print('great pocketmoney')
elif (pocketmoney>100):
    print('good enough')
else:
    print('need a raise')


intro=input("tell us about you")
print(intro)
charcount=0
wordcount=1
for i in intro:
    charcount=charcount+1
    if (i==" "):
        wordcount=wordcount+1

print('number of words in the string ')
print(wordcount)
print('number of char')
print(charcount)