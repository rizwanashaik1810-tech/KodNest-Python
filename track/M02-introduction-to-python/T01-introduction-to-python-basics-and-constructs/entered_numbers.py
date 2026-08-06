number = int(input())
positive_count = 0
negative_count = 0
zero_count = 0
total = 0

for i in range(1,number+1):
    number = int(input())
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1
    total += number

print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")
print(f"Total: {total}")
