count = 0
text = "sahana"
for i in text:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1 # count = count + 1

print(f"Vowels: {count} \nConsonents: {len(text) - count}")
