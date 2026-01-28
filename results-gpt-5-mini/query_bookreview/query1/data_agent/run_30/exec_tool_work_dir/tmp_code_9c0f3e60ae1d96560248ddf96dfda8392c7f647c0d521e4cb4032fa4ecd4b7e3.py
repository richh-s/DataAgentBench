code = """import json
with open(var_call_v4Qs3F5BbtONXcuyiUrFTqZk, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_MzN91tOr8xrMKRPLFMLDuBal, 'r', encoding='utf-8') as f:
    books = json.load(f)

# collect info
info = {
    'reviews_columns': list(reviews[0].keys()) if isinstance(reviews, list) and len(reviews)>0 else [],
    'books_columns': list(books[0].keys()) if isinstance(books, list) and len(books)>0 else [],
    'reviews_sample0': reviews[0] if isinstance(reviews, list) and len(reviews)>0 else None,
    'books_sample0': books[0] if isinstance(books, list) and len(books)>0 else None,
    'reviews_len': len(reviews) if isinstance(reviews, list) else None,
    'books_len': len(books) if isinstance(books, list) else None
}
print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_call_YLjPOkHQrNjMcLg8AQ0CN4zU': ['review'], 'var_call_PCJA205YfJGXnXYCx0XEM9Ol': ['books_info'], 'var_call_v4Qs3F5BbtONXcuyiUrFTqZk': 'file_storage/call_v4Qs3F5BbtONXcuyiUrFTqZk.json', 'var_call_MzN91tOr8xrMKRPLFMLDuBal': 'file_storage/call_MzN91tOr8xrMKRPLFMLDuBal.json'}

exec(code, env_args)
