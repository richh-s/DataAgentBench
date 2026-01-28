code = """import json, re, pandas as pd
with open(var_call_5dwCE4tu8xQa66eB3wyRTBzu, 'r', encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_V2MudqENPjmroLDcBNOyV1cj, 'r', encoding='utf-8') as f:
    avgs = json.load(f)

df_books = pd.DataFrame(books)
df_avgs = pd.DataFrame(avgs)

# functions
year_re = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")
num_re = re.compile(r"(\d+)")

def extract_num_id(s):
    if not isinstance(s, str):
        return None
    m = num_re.search(s)
    return int(m.group(1)) if m else None

def extract_year_any(fields):
    # fields: list of strings to search
    for s in fields:
        if not isinstance(s, str):
            continue
        # first try 4-digit
        m = year_re.search(s)
        if m:
            y = int(m.group(1))
            if 1000 <= y <= 2099:
                return y
        # try patterns like "Published ... on Month Day, YEAR"
        m2 = re.search(r"Published.*?(?:on|in) [A-Za-z]+ \d{1,2}, (\d{4})", s)
        if m2:
            y = int(m2.group(1))
            return y
        # try year in parentheses e.g., (2004)
        m3 = re.search(r"\((\d{4})\)", s)
        if m3:
            return int(m3.group(1))
    return None

# apply id extraction
if 'book_id' in df_books.columns:
    df_books['num_id'] = df_books['book_id'].apply(extract_num_id)
else:
    df_books['num_id'] = None

if 'purchase_id' in df_avgs.columns:
    df_avgs['num_id'] = df_avgs['purchase_id'].apply(extract_num_id)
else:
    df_avgs['num_id'] = None

# extract year from details, description, categories, title
fields_to_search = []
if 'details' in df_books.columns:
    fields_to_search.append('details')
if 'description' in df_books.columns:
    fields_to_search.append('description')
if 'categories' in df_books.columns:
    fields_to_search.append('categories')
if 'title' in df_books.columns:
    fields_to_search.append('title')

# function to get year for a row
def get_year_for_row(row):
    vals = [row.get(f) for f in fields_to_search]
    return extract_year_any(vals)

# compute years
df_books['year'] = df_books.apply(get_year_for_row, axis=1)
# compute decade string
df_books['decade'] = df_books['year'].apply(lambda y: f"{(y//10)*10}s" if pd.notnull(y) else None)

# convert avg_rating
df_avgs['avg_rating'] = pd.to_numeric(df_avgs['avg_rating'], errors='coerce')

# merge
df_merged = pd.merge(df_books, df_avgs, on='num_id', how='inner', suffixes=('_book','_avg'))
# keep rows with decade and avg_rating
df_merged = df_merged[df_merged['decade'].notnull() & df_merged['avg_rating'].notnull()]

# group
grp = df_merged.groupby('decade').agg(book_count=('num_id', lambda x: int(x.nunique())),
                                       mean_avg_rating=('avg_rating', 'mean')).reset_index()

# filter >=10
grp_filtered = grp[grp['book_count'] >= 10].copy()

if grp_filtered.empty:
    result = None
else:
    top = grp_filtered.sort_values(['mean_avg_rating','decade'], ascending=[False, True]).iloc[0]
    result = {'decade': top['decade'], 'average_rating': round(float(top['mean_avg_rating']),4), 'book_count': int(top['book_count'])}

# also include some diagnostics if result None
out = {'result': result, 'total_books_with_year': int(df_books['year'].notnull().sum()), 'total_merged_rows': int(len(df_merged)), 'decade_groups': grp.to_dict(orient='records')}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_8TbuovrDdOB1xBpUtttDEP9A': ['review'], 'var_call_14ux0gRqZwo7087az28Kt6PP': ['books_info'], 'var_call_5dwCE4tu8xQa66eB3wyRTBzu': 'file_storage/call_5dwCE4tu8xQa66eB3wyRTBzu.json', 'var_call_V2MudqENPjmroLDcBNOyV1cj': 'file_storage/call_V2MudqENPjmroLDcBNOyV1cj.json', 'var_call_1fQyjP8cKJKxos6iWhcuzwV3': None, 'var_call_SjGHGFBt7k8lLJutROwDBk57': [], 'var_call_dZZ390RWaCPDtIiw2mRxcZTB': {'books_count': 200, 'avgs_count': 200, 'books_sample': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.', 'description': '[]', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'num_id': 1, 'year': None}, {'book_id': 'bookid_2', 'title': 'Notes from a Kidwatcher', 'details': 'This book, published by Heinemann in its first edition on May 20, 1996, is written in English and is available in paperback format, consisting of 316 pages. It has an ISBN-10 of 0435088688 and an ISBN-13 of 978-0435088682. The item weighs 1.05 pounds and its dimensions are 6.03 x 0.67 x 8.95 inches.', 'description': '["About the Author", "SANDRA WILDE, Ph.D., is widely recognized for her expertise in developmental spelling and her advocacy of holistic approaches to spelling and phonics. She is Professor of Curriculum and Instruction at Portland State University in Oregon. She is best known for her work in invented spelling, phonics and miscue analysis. She specializes in showing teachers how kids\' invented spellings and miscues can help us work with them in more sophisticated and learner-centered ways. Looking at what kids do as they read and write is at the heart of Sandra\'s presentations and workshops. She can do lively keynote presentations that highlight the interesting things that we can learn by paying close attention to students\' invented spellings and miscues, as well as workshops of varying lengths that focus on student-centered teaching of spelling and phonics. She has recently begun offering workshops that focus on understanding students\' miscues as a guide to appropriate instruction, p"]', 'categories': '["Books", "Reference", "Words, Language & Grammar"]', 'num_id': 2, 'year': None}, {'book_id': 'bookid_3', 'title': 'Service: A Navy SEAL at War', 'details': 'This book, published by Little, Brown and Company in its first edition on May 8, 2012, is available in English and is bound as a hardcover with a total of 384 pages. It has an ISBN-10 of 9780316185363 and an ISBN-13 of 978-0316185363. The item weighs 1.4 pounds and its dimensions are 6.25 inches in width, 1.55 inches in depth, and 9.55 inches in height.', 'description': '["Review", "Praise for SERVICE\\"An action-packed...reflective saga of contemporary military service.\\"―", "Kirkus Reviews", "\\"Marcus Luttrell, with James D. Hornfischer, has written another emotional story that the reader will not want to put down.\\"―", "American Thinker", "About the Author", "Marcus Luttrell", "became a combat-trained Navy SEAL in 2002 and served in many dangerous Special Operations assignments around the world. He is the author of the", "New York Times", "bestseller", "Lone Survivor", ", and is a popular corporate and organizational speaker. He lives near Houston, Texas.\xa0James D. Hornfischer\xa0is the author of four bestselling books on the U.S. Navy in World War II,", "The Fleet at Flood", "Tide", ",", "Neptune\'s", "Inferno, Ship of Ghosts,", "and", "The Last Stand of the Tin Can Sailors,", "winner of the Samuel Eliot Morison Award. He lives in Austin, Texas."]', 'categories': '["Books", "Biographies & Memoirs", "Leaders & Notable People"]', 'num_id': 3, 'year': None}, {'book_id': 'bookid_4', 'title': 'Monstrous Stories #4: The Day the Mice Stood Still', 'details': 'This book, published by Scholastic Paperbacks in a reprint edition on October 29, 2013, is written in English and consists of 64 pages. It has an ISBN-10 of 0545425573 and an ISBN-13 of 978-0545425575. The reading age is suitable for children between 7 and 10 years old, and it corresponds to a Lexile measure of 590L. The book is appropriate for students in grades 2 through 5. Weighing 1.92 ounces, its dimensions are 5.25 x 0.2 x 7.5 inches.', 'description': '[]', 'categories': '["Books", "Children\'s Books", "Science Fiction & Fantasy"]', 'num_id': 4, 'year': None}, {'book_id': 'bookid_5', 'title': 'Parker & Knight', 'details': 'The book was published on May 18, 2014, and is available in English. It has a file size of 1542 KB and allows for unlimited simultaneous device usage. Text-to-speech functionality is enabled, and it supports screen readers, enhancing accessibility for readers. Enhanced typesetting is also enabled, while the X-Ray feature is not available. Word Wise is enabled to assist with comprehension, and sticky notes can be used on Kindle Scribe. The print length of the book is 233 pages.', 'description': '[]', 'categories': '["Books", "Mystery, Thriller & Suspense", "Thrillers & Suspense"]', 'num_id': 5, 'year': None}, {'book_id': 'bookid_6', 'title': 'Writings from a Black Woman Living in the Land of the "Free": Strength, Power, Resilience', 'details': 'This book, published independently on December 30, 2021, is written in English and consists of 24 pages. It has an ISBN 13 of 979-8528537702 and weighs 3.2 ounces. The dimensions of the book are 7 x 0.06 x 9 inches.', 'description': '[]', 'categories': '["Books", "Arts & Photography", "History & Criticism"]', 'num_id': 6, 'year': None}, {'book_id': 'bookid_7', 'title': "Child Development: A Practitioner's Guide:2nd (Second) edition", 'details': 'The book, published by Guilford in its second edition in January 2004, is also noted as the 8082nd edition from January 1, 1994. It has a remarkably light item weight of just 0.01 ounces.', 'description': '[]', 'categories': '["Books", "Parenting & Relationships", "Parenting"]', 'num_id': 7, 'year': None}, {'book_id': 'bookid_8', 'title': 'Make: Electronics: Learning Through Discovery', 'details': 'This book, published by Make Community, LLC, in its second edition on September 22, 2015, is available in English and spans 352 pages in paperback format. It has an ISBN of 9781680450262 for the 10-digit version and 978-1680450262 for the 13-digit version. The content is suitable for readers aged 11 to 17 years. The book weighs 2.91 pounds and its dimensions are 8 inches in width, 0.5 inches in thickness, and 10 inches in height.', 'description': '["From the Author", "Make: Electronics", "is the book that I wish I had owned when I was a young teenager, struggling to learn the basics of electricity and electronics. My goal is to give readers today an easier learning experience than the one I had to go through. And I want it to be fun.", "About the Author", "Charles Platt is a Contributing Editor and regular columnist for Make magazine, where he writes about electronics. He is the author of the highly successful introductory hands-on book, Make:Electronics, and is writing a sequel to that book in addition to volumes 2 and 3 of the Encyclopedia of Electronic Components. Platt was a Senior Writer for Wired magazine, and has written various computer books. As a prototype designer, he created semi-automated rapid cooling devices with medical applications, and air-deployable equipment for first responders. He was the sole author of four mathematical-graphics software packages, and has been fascinated by electronics since he put together a telephone answering machine from a tape recorder and military-surplus relays at age 15. He lives in a Northern Arizona wilderness area, where he has his own workshop for prototype fabrication and projects that he writes about for Make magazine."]', 'categories': '["Books", "Engineering & Transportation", "Engineering"]', 'num_id': 8, 'year': None}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'details': 'This book, published independently on September 25, 2019, is written in English and spans 367 pages. It is available in paperback format and has an ISBN-10 of 1694621731 and an ISBN-13 of 978-1694621733. The item weighs 1.38 pounds and measures 6 x 0.92 x 9 inches.', 'description': '[]', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'num_id': 9, 'year': None}, {'book_id': 'bookid_10', 'title': 'Four Centuries of American Education', 'details': 'This book, published by WallBuilder Press in its first edition on November 8, 2004, is available in English and comprises 51 pages in paperback format. It has an ISBN-10 of 1932225323 and an ISBN-13 of 978-1932225327, with a total item weight of 3.52 ounces.', 'description': '["About the Author", "David Barton is the founder of WallBuilders, an organization dedicated to presenting America\'s forgotten history and heroes, with an emphasis on our moral, religious, and constitutional heritage. David is author of numerous best-selling works and a national award-winning historian who brings a fresh perspective to history."]', 'categories': '["Books", "Education & Teaching", "Schools & Teaching"]', 'num_id': 10, 'year': None}], 'avgs_sample': [{'purchase_id': 'purchaseid_1', 'avg_rating': '4.0', 'num_id': 1}, {'purchase_id': 'purchaseid_10', 'avg_rating': '4.85', 'num_id': 10}, {'purchase_id': 'purchaseid_100', 'avg_rating': '3.3333333333333335', 'num_id': 100}, {'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'num_id': 101}, {'purchase_id': 'purchaseid_102', 'avg_rating': '3.0', 'num_id': 102}, {'purchase_id': 'purchaseid_103', 'avg_rating': '3.2', 'num_id': 103}, {'purchase_id': 'purchaseid_104', 'avg_rating': '4.333333333333333', 'num_id': 104}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'num_id': 105}, {'purchase_id': 'purchaseid_106', 'avg_rating': '3.1', 'num_id': 106}, {'purchase_id': 'purchaseid_107', 'avg_rating': '4.0', 'num_id': 107}], 'common_num_ids_sample': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]}}

exec(code, env_args)
