code = """import json, re
with open(var_call_TUvJXKQeqJ37mMHR2spm3ift,'r',encoding='utf-8') as f:
    books = json.load(f)
with open(var_call_Nx0j5IGC14Xr8U35jHcX9nVS,'r',encoding='utf-8') as f:
    reviews = json.load(f)

# show first 20 books details
sample_books = []
for b in books[:20]:
    sample_books.append({'book_id': b.get('book_id'), 'details': b.get('details')})

# test regex on first 20 details
pattern = re.compile(r"\b(1[5-9]\d{2}|20\d{2})\b")
regex_results = []
for b in books[:20]:
    d = b.get('details')
    matches = pattern.findall(d if isinstance(d,str) else '')
    regex_results.append({'book_id': b.get('book_id'), 'matches': matches})

out = {'sample_books': sample_books, 'regex_results': regex_results, 'num_books': len(books), 'num_reviews': len(reviews)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_25XrTT1v8MA76LlhO9Ah0Qpu': ['review'], 'var_call_CaaMHIphba5mhsgrjOW70AAl': ['books_info'], 'var_call_ahSeu74lplrW2uWVFYFbYKof': 'file_storage/call_ahSeu74lplrW2uWVFYFbYKof.json', 'var_call_t8s9j3CLGS3oQRddFrBguw0a': 'file_storage/call_t8s9j3CLGS3oQRddFrBguw0a.json', 'var_call_AnPCoO6KSaGRcg5jGKCGL4Nx': None, 'var_call_o2VX8jZXpeJ7U4MZ3xWm2fnA': [], 'var_call_TUvJXKQeqJ37mMHR2spm3ift': 'file_storage/call_TUvJXKQeqJ37mMHR2spm3ift.json', 'var_call_Nx0j5IGC14Xr8U35jHcX9nVS': 'file_storage/call_Nx0j5IGC14Xr8U35jHcX9nVS.json', 'var_call_O5RsHGoXv8ot6FPveUYIK5TK': {'books_count': 200, 'reviews_count': 1833, 'merged_rows': 1833, 'rows_with_details': 1833, 'rows_without_details': 0, 'rows_with_year': 0, 'unique_books_with_year': 0, 'decade_stats': [], 'valid_decades': [], 'best_decade': None}}

exec(code, env_args)
