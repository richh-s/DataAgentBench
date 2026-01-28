code = """import json
import re

# Read the book data from the file
file_path = var_functions
books_data = json.load(open(file_path, 'r'))

def extract_year_from_details(details_text):
    """Extract publication year from details text"""
    if not details_text:
        return None
        
    patterns = [
        r'released on [A-Za-z]+ \d+, (\d{4})',
        r'first edition on [A-Za-z]+ \d+, (\d{4})',
        r'published on [A-Za-z]+ \d+, (\d{4})',
        r'published by [A-Za-z0-9 &,]+ on ([A-Za-z]+ \d+, )?(\d{4})',
        r'published independently on [A-Za-z]+ \d+, (\d{4})',
        r'in its (first|second|third|2013th|revised|supplement) edition on ([A-Za-z]+ \d+, )?(\d{4})',
        r'in its (first|second|third|2013th|revised|supplement|reprint) edition (in|on) ([A-Za-z]+ )?(\d{4})',
        r'(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (\d{4})',
        r'\b(19\d{2}|20\d{2})\b'  # Fallback: any 4-digit year starting with 19 or 20
    ]
    
    # Try each pattern
    for pattern in patterns:
        match = re.search(pattern, details_text)
        if match:
            try:
                # Find the last group that looks like a 4-digit year
                groups = match.groups()
                for group in reversed(groups):
                    if group and len(group) == 4 and group.isdigit():
                        year = int(group)
                        if 1900 <= year <= 2023:
                            return year
            except:
                continue
    
    return None

# Extract publication years
books_with_years = []
for book in books_data:
    year = extract_year_from_details(book.get('details', ''))
    if year:
        books_with_years.append({
            'book_id': book['book_id'],
            'publication_year': year
        })

# Show some examples
result = {
    'total_books': len(books_data),
    'books_with_years': len(books_with_years),
    'sample_books': books_with_years[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': [{'title': 'Chaucer', 'subtitle': 'Hardcover – Import, January 1, 2004', 'author': '{"avatar": "https://m.media-amazon.com/images/I/21Je2zja9pL._SY600_.jpg", "name": "Peter Ackroyd", "about": ["Peter Ackroyd, (born 5 October 1949) is an English biographer, novelist and critic with a particular interest in the history and culture of London. For his novels about English history and culture and his biographies of, among others, William Blake, Charles Dickens, T. S. Eliot and Sir Thomas More, he won the Somerset Maugham Award and two Whitbread Awards. He is noted for the volume of work he has produced, the range of styles therein, his skill at assuming different voices and the depth of his research.", "He was elected a fellow of the Royal Society of Literature in 1984 and appointed a Commander of the Order of the British Empire in 2003.", "Bio from Wikipedia, the free encyclopedia."]}', 'rating_number': '29', 'features': '[]', 'description': '[]', 'price': '8.23', 'store': 'Peter Ackroyd (Author)', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'book_id': 'bookid_1'}, {'title': 'Notes from a Kidwatcher', 'subtitle': 'First Edition', 'author': '{"avatar": "https://m.media-amazon.com/images/I/01Kv-W2ysOL._SY600_.png", "name": "Yetta M. Goodman", "about": ["Discover more of the author’s books, see similar authors, read author blogs and more"]}', 'rating_number': '1', 'features': '["Contains 23 selected articles by this influential writer, researcher, educator, and speaker. They\'re grouped around six major themes inherent in teacher education: culture and community; miscue analysis, reading strategies and comprehension; print awareness and the roots of literacy; the writing process; kidwatching; and whole language theory. No index. Annotation c. by Book News, Inc., Portland, Or."]', 'description': '["About the Author", "SANDRA WILDE, Ph.D., is widely recognized for her expertise in developmental spelling and her advocacy of holistic approaches to spelling and phonics. She is Professor of Curriculum and Instruction at Portland State University in Oregon. She is best known for her work in invented spelling, phonics and miscue analysis. She specializes in showing teachers how kids\' invented spellings and miscues can help us work with them in more sophisticated and learner-centered ways. Looking at what kids do as they read and write is at the heart of Sandra\'s presentations and workshops. She can do lively keynote presentations that highlight the interesting things that we can learn by paying close attention to students\' invented spellings and miscues, as well as workshops of varying lengths that focus on student-centered teaching of spelling and phonics. She has recently begun offering workshops that focus on understanding students\' miscues as a guide to appropriate instruction, p"]', 'price': '3.52', 'store': 'Sandra Wilde (Editor)', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'book_id': 'bookid_2'}], 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': [{'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!', 'text': 'Lucky for me it\'s more than a cookbook.<br /><br />The story of a modern Daniel Boone, growing up in Michigan, one of three sons of a hunter.  Beginning at age eight when he shot a squirrel, to age 13 his first deer, then hunting his way through college, a career as a fur trapper, hunting sheep in Alaska, canoeing the Missouri River for deer and ending in Brooklyn age 37. Brooklyn?<br /><br />I especially liked that I share his disgust at catch & release fishing - if you fish it, you have to eat it - anything else is sadism (my words).<br /><br />My brother in law is the cook in the family and I wanted to see if this would be a good gift for him and I struck pay dirt following each chapter are "Tasting Notes" where the author speaks of cooking wild game.<br /><br />I also enjoyed it for the history of the land he has hunted as well as the history of the hunt (I too was a big Daniel Boone fan growing up!).<br /><br />I think more pictures (everything but dead things) would have made this a keeper.', 'review_time': '2012-11-24 18:52:00', 'helpful_vote': '0', 'verified_purchase': '0', 'purchase_id': 'purchaseid_186'}, {'rating': '4', 'title': 'Four Stars', 'text': 'Not as developed as Stephanie but I like the characters so far.', 'review_time': '2015-12-31 13:35:00', 'helpful_vote': '0', 'verified_purchase': '1', 'purchase_id': 'purchaseid_191'}], 'var_functions.execute_python:10': [2004, 1996], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
