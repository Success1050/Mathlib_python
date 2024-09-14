with open("story.txt", "r") as f:
    story= f.read()

start_of_word= -1

target_start= "<"
target_end= ">"
words= set()

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    elif char == target_end and start_of_word != -1:
        word= story[start_of_word: i + 1]
        words.add(word) 

answers= {}

for word in words:
    user_input= input(f"Enter your answers {word}")
    answers[word]= user_input 

for word in words:
    story = story.replace(word, answers[word])

with open("story.txt", "w") as f:
    f.write(story)