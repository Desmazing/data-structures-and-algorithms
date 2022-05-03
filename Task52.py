# get statement from user
# reverse the sentence
# enclose in double quotes
# put fullstop at sentence end

sentence = input("Enter your statement here: ")

rev_sent = ""

for letter in sentence:
    rev_sent = letter + rev_sent

print('"'+rev_sent+'."')