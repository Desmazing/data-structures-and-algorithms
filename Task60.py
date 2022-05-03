# get 5 authors and their books 
# display the first author with book name
# keep in mind that we can't have repeated keys

author_books = {}

for i in range(2):
	author = input("Enter the author name: ")
	book = input("Enter their book name: ")
	author_books[author] = book

print(author_books)
print(f'{list(author_books.keys())[0]} wrote {list(author_books.values())[0]}')
