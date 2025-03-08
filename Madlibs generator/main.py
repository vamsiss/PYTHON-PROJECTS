# provide some context for the file
with open("story.txt", "r") as f:
    story =f.read()
words = []
start_of_word = -1

target_start = "<"
target_end = ">"
# Here enumurate gives access to index and element at that position
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word !=-1:
        word = story[start_of_word: i + 1]
        if word not in words:
            words.append(word)
        start_of_word = -1
# create a dictonary
answers = {}
for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)