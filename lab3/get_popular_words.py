"""
1-The program takes a command line argument, this argument is the name of a text file.
the program reads all the text and split them and calulate the 20 most used words in
the file and then write them to a file called popular_words.txt
"""


def get_popular_words(file_name):
    words_count = {}
    with open(file_name, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in words_count:
                    words_count[word] += 1
                else:
                    words_count[word] = 1
    most_popular = sorted(words_count.items(), key=lambda w: w[1], reverse=True)[:20]
    with open("popular_words.txt", "w") as f:
        f.write("Most Popular Words\n")
        f.write("-" * 30 + "\n")
        f.write(f"{'Rank':4s} | {'Word':10s} | Occurrences\n")
        f.write("-" * 30 + "\n")
        for i, (word, count) in enumerate(most_popular, 1):
            f.write(f"{i:4d} | {word:10s} | {count:5d}\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total unique words analyzed: {len(words_count)}")


get_popular_words("mockingjay.txt")
