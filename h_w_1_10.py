# Write a Python program to count the frequency of words in a file.

text = open("baby_lyrics.txt", "r")

d = dict()

for line in text:
    line = line.strip()
    line = line.lower()

    words = line.split()

    for w in words:
        if w in d:
            d[w] = d[w] + 1
        else:
            d[w] = 1
for key in list(d.keys()):
    print(key, ":", d[key])