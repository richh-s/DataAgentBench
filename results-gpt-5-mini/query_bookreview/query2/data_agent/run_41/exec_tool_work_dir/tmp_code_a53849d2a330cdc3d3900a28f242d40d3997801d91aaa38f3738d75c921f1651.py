code = """import json
# Load the books_database query result from the provided storage file path
path = var_call_KgPg7WcafUFyAWr7srkBpqMA
with open(path, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Filter for English-language books by checking 'details' and 'description' and 'categories' for English mentions
import re
eng_books = []
for b in books:
    details = (b.get('details') or '')
    description = (b.get('description') or '')
    categories = (b.get('categories') or '')
    text = ' '.join([details, description, categories])
    if re.search(r'\bEnglish\b', text, flags=re.IGNORECASE) or re.search(r'in English', text, flags=re.IGNORECASE) or re.search(r'available in English', text, flags=re.IGNORECASE):
        eng_books.append({'book_id': b.get('book_id'), 'title': b.get('title')})

# Remove duplicates and ensure valid ids
seen = set()
unique_books = []
for eb in eng_books:
    bid = eb.get('book_id')
    if bid and bid not in seen:
        seen.add(bid)
        unique_books.append(eb)

import json
print("__RESULT__:")
print(json.dumps(unique_books))"""

env_args = {'var_call_KgPg7WcafUFyAWr7srkBpqMA': 'file_storage/call_KgPg7WcafUFyAWr7srkBpqMA.json'}

exec(code, env_args)
