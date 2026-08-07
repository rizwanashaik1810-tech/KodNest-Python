n = int(input())
scores = []

for i in range(n):
    score = int(input())
    scores.append(score)

search_score = int(input())

highest = max(scores)
lowest = min(scores)
total = sum(scores)

print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Total Score: {total}")

if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")
