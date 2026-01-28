code = """import json
import pandas as pd

# Load the books data preview
books_preview = [{"title": "Chaucer", "subtitle": "Hardcover \u2013 Import, January 1, 2004", "author": "{\"avatar\": \"https://m.media-amazon.com/images/I/21Je2zja9pL._SY600_.jpg\", \"name\": \"Peter Ackroyd\", \"about\": [\"Peter Ackroyd, (born 5 October 1949) is an English biographer, novelist and critic with a particular interest in the history and culture of London. For his novels about English history and culture and his biographies of, among others, William Blake, Charles Dickens, T. S. Eliot and Sir Thomas More, he won the Somerset Maugham Award and two Whitbread Awards. He is noted for the volume of work he has produced, the range of styles therein, his skill at assuming different voices and the depth of his research.\", \"He was elected a fellow of the Royal Society of Literature in 1984 and appointed a Commander of the Order of the British Empire in 2003.\", \"Bio from Wikipedia, the free encyclopedia.\"]}", "rating_number": "29", "features": "[]", "description": "[]", "price": "8.23", "store": "Peter Ackroyd (Author)", "categories": "[\"Books\", \"Literature & Fiction\", \"History & Criticism\"]", "details": "Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.", "book_id": "bookid_1"}, {"title": "Notes from a Kidwatcher", "subtitle": "First Edition", "author": "{\"avatar\": \"https://m.media-amazon.com/images/I/01Kv-W2ysOL._SY600_.png\", \"name\": \"Yetta M. Goodman\", \"about\": [\"Discover more of the author\u2019s books, see similar authors, read author blogs and more\"]}", "rating_number": "1", "features": "[\"Contains 23 selected articles by this influential writer, researcher, educator, and speaker. They're grouped around six major themes inherent in teacher education: culture and community; miscue analysis, reading strategies and comprehension; print awareness and the roots of literacy; the writing process; kidwatching; and whole language theory. No index. Annotation c. by Book News, Inc., Portland, Or.\"]", "description": "[\"About the Author\", \"SANDRA WILDE, Ph.D., is widely recognized for her expertise in developmental spelling and her advocacy of holistic approaches to spelling and phonics. She is Professor of Curriculum and Instruction at Portland State University in Oregon. She is best known for her work in invented spelling, phonics and miscue analysis. She specializes in showing teachers how kids' invented spellings and miscues can help us work with them in more sophisticated and learner-centered ways. Looking at what kids do as they read and write is at the heart of Sandra's presentations and workshops. She can do lively keynote presentations that highlight the interesting things that we can learn by paying close attention to students' invented spellings and miscues, as well as workshops of varying lengths that focus on student-centered teaching of spelling and phonics. She has recently begun offering workshops that focus on understanding students' miscues as a guide to appropriate instruction, p\"]", "price": "3.52", "store": "Sandra Wilde (Editor)", "categories": "[\"Books\", \"Reference\", \"Words, Language & Grammar\"]", "details": "This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.", "book_id": "bookid_2"}]

# Check the structure
print("Books preview loaded")
print(f"Number of books: {len(books_preview)}")

# Show first book's fields
first_book = books_preview[0]
print("\nFirst book fields:")
for key, value in first_book.items():
    print(f"{key}: {type(value)} - {str(value)[:100]}...")

# Check if categories contains Literature & Fiction
print("\nChecking categories...")
for book in books_preview:
    cats_str = book.get('categories', '[]')
    print(f"Title: {book['title']}")
    print(f"Categories: {cats_str}")
    
    try:
        cats_list = eval(cats_str)
        print(f"Categories list: {cats_list}")
        if "Literature & Fiction" in cats_list:
            print(">>> IS Literature & Fiction")
    except:
        print("Could not parse categories")
    print()

print("-----END PRINT FORMAT-----")"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
