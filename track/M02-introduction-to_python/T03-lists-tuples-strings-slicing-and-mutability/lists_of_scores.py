n = int(input())
scores = []

for i in range(n):
    score = int(input())
    scores.append(score)

search_score = int(input())

print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Total Score: {sum(scores)/len(scores)}")

if search_score in scores:
    print("Search Result:", Found)
else:
    print("Search Result:", Not Found)
    