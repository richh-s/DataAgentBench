code = """import json, re, pandas as pd

# Load full aggregated ratings
with open(var_call_mgfSX46ObKYM4mOmZXAfXos3, 'r') as f:
    ratings = json.load(f)

# Load full books details
with open(var_call_OeIYAdjEAjl6ViLF28q38qny, 'r') as f:
    books = json.load(f)

ratings_df = pd.DataFrame(ratings)
books_df = pd.DataFrame(books)

# Extract publication year from details using regex
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    if not isinstance(text, str):
        return None
    # Look for typical "on Month Day, Year" or just years; take earliest year as publication
    years = [int(y) for y in year_pattern.findall(text)]
    # year_pattern with groups returns tuples like ('19','99'), fix that

print('__RESULT__:')
print(json.dumps('debug'))"""

env_args = {'var_call_OeIYAdjEAjl6ViLF28q38qny': 'file_storage/call_OeIYAdjEAjl6ViLF28q38qny.json', 'var_call_JKhOa6zEdwuQxOzgdcsepzS1': [{'book_id': 'bookid_1', 'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_call_1DkIiC3fIN7InZJ9bl6JHStt': ['review'], 'var_call_mgfSX46ObKYM4mOmZXAfXos3': 'file_storage/call_mgfSX46ObKYM4mOmZXAfXos3.json'}

exec(code, env_args)
