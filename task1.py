def check_rhythm(poem):
   words = poem.split()  
   syllables = []  

   for word in words:
      syllable_count = 0
      for char in word:
            if char in "aeiouyAEIOUY": 
               syllable_count += 1  
      syllables.append(syllable_count)  

   if len(set(syllables)) == 1:  
      return "Парам пам-пам"
   else:
      return "Пам парам"


poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)