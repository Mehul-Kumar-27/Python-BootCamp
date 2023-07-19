def domainDetector(domain):
    intial_string = domain
    domainIndex = intial_string.find("@")
    substring = intial_string[domainIndex + 1 :]
    print(substring)


def findWord(string):
    myString = string
    if "dog" in myString:
        print(True)
    else:
        print(False)


def countTheOccurance(string):
    myString = string.split()
    count = 0
    for word in myString:
        if word == "dog":
            count += 1

    print(count)


if __name__ == "__main__":
    domainDetector("mehul2002kumar@gmail.com")
    findWord("This place is a good for a dog")
    countTheOccurance("This place is a good for a dog , so get a dog")

names = ["Alice", "Bob", "Charlie", "David", "Ella", "Frank"]

# Using lambda function to filter names starting with the letter 'C'
names_with_c = list(filter(lambda name: name.startswith("C"), names))

print(names_with_c)  # Output: ['Charlie']
