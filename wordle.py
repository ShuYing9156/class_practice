import random
from termcolor import colored 


#分行讀取txt檔(單詞列表)
with open("C://Users/ruby2/OneDrive/桌面/class_practice/word/animal.txt",'r') as animal:
    word1 = animal.read().splitlines() 

with open("C://Users/ruby2/OneDrive/桌面/class_practice/word/food.txt",'r') as food:
    word2 = food.read().splitlines()

with open("C://Users/ruby2/OneDrive/桌面/class_practice/word/nature.txt",'r') as nature:
    word3 = nature.read().splitlines()



#選主題、挑單詞
print('主題:')

theme = ['動物','食物','大自然']
for i in range(len(theme)):
    print(i+1,theme[i])
print('\n')
    
while True:
    
    ChooseOneTheme = input('請選擇主題(輸入數字即可):')
    
    if int(ChooseOneTheme) not in range(1,len(theme)+1) :
        print('不好意思，我們沒有這個主題，如果您要提供，我們會很開心\n') ##確認輸入的數字沒超出範圍
    else:
        break
    
if int(ChooseOneTheme) == 1:
    word = random.choice(word1) ##從list中取一個元素(也就是單詞)
    
elif int(ChooseOneTheme) == 2:
    word = random.choice(word2)
    
elif int(ChooseOneTheme) == 3:
    word = random.choice(word3).lower() ##改為全部小寫

print(word,'(可隱藏)')



#猜字
while True:
    
    ##確認輸入的情況
    guess = input('\n來猜字吧：')
    result = ''
    
    if len(guess) != 5:
        print('別來亂，請輸入5個字母謝謝')
        continue
    
    ##比對位置
    for j in range(5):
        
        if guess[j] in word:
            
            if guess[j] == word[j]:
                letter = guess[j]
                letter = colored(letter,'grey', 'on_green',['bold'])  
                result += letter
            else:
                letter = guess[j]
                letter = colored(letter,'grey', 'on_yellow',['bold'])
                result += letter

        else:
            letter = guess[j]
            letter = colored(letter,'white','on_grey',['bold'])
            result += letter

    print(result)
    
    if guess == word:
        print('\n恭喜你猜對了! 是',word)
        break
       



            
