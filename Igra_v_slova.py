with open ('/Users/Nata Braun/Work Documents/russian_nouns.txt' , 'r', encoding='utf-8') as g:
    print ('Введите слово:')
    input_word = input().lower()
    counter = 0
    for s in g: #перебираем все слова (s) в словаре (g) 
        w = input_word
        for i in s.strip(): #для каждой буквы слова из словаря
            if i not in w: #если элемента нет во введенном слове, то завершаем цикл
                break
            w = w.replace(i,'',1) #если элемент есть, то удаляем его из слова 1 раз
        else: #когда пройдет весь цикл совпадений, то слово печатаем и добавляем к счетчику
            print (s) 
            counter+=1
print (counter)