code = """import json
import re

# Load data
with open(locals()['var_function-call-10489614112549282405'], 'r') as f:
    books = json.load(f)

print("__RESULT__:")
sample = books[0]
details = sample.get('details', '')
years = re.findall(r'\b(19\d{2}|20\d{2})\b', details)
print(json.dumps({
    "sample_book": sample,
    "details": details,
    "years_found": years,
    "type_details": str(type(details))
}))"""

env_args = {'var_function-call-4644691029107538022': 'file_storage/function-call-4644691029107538022.json', 'var_function-call-16058013232113512935': ['review'], 'var_function-call-2272556202224259319': [{'COUNT(*)': '1833'}], 'var_function-call-15315810567359206872': [{'count': '200'}], 'var_function-call-12909927237427682117': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}], 'var_function-call-5847662609626649812': 'file_storage/function-call-5847662609626649812.json', 'var_function-call-10489614112549282405': 'file_storage/function-call-10489614112549282405.json', 'var_function-call-1543764841573784033': [], 'var_function-call-2513143424708080617': {'result': [], 'debug': {'books_count': 0, 'total_books_raw': 200, 'book_ids_example': [1, 2, 3, 4, 5], 'reviews_count': 1833, 'total_reviews_raw': 1833, 'review_ids_example': [1, 2, 3, 4, 5]}}}

exec(code, env_args)
