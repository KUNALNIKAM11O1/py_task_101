#Task : quiz game
#5 questions,MCQ(4),answers,guess,score
# stop quiz game when user enters "Quit"
# questions = []
#MCQs = [[],[],[],[]]
# answers= []
# guess=input()
#score = 0
#d.value


# l = [4,5,6,4,7,5,9]

# for i in l:
#     if l.count(i) == 1:
#         print(i,end=" ")

from collections import Counter

s = input().strip()

freq = Counter(s)

odd_freq = []
even_freq = []

for count in freq.values():
    if count % 2 == 0:
        even_freq.append(count)
    else:
        odd_freq.append(count)

max_odd = max(odd_freq) if odd_freq else 0
min_even = min(even_freq) if even_freq else 0

print(abs(max_odd - min_even))