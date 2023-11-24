def count_words(sentence):
    words = sentence.split()
    
    
    word_count = {}
    
    for word in word_count:
        
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
            
    print(f"มีคำทั้งหมด {len(words)} คำ")
    lem = print(f"มีคำที่ซ้ำกันมากกว่า 1 ครั้ง :")
    for word, count in word_count.items():
        if count > 1:
            print(f"คำว่า '{word} กับ {count} ครั้ง")
        
print('-------------------------------------')
user_sentence = input("ป้อนข้อความ :")
print('-------------------------------------')
count_words(user_sentence)
print('-------------------------------------')