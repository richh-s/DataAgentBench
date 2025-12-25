code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-8048486413748627374'], 'r') as f:
    reviews = json.load(f)
with open(locals()['var_function-call-10305899063336439880'], 'r') as f:
    books = json.load(f)

df_reviews = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Normalize IDs
df_reviews['id_num'] = df_reviews['purchase_id'].str.extract(r'(\d+)')
df_books['id_num'] = df_books['book_id'].str.extract(r'(\d+)')

def extract_year(text):
    if not isinstance(text, str): return None
    match = re.search(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},\s+(\d{4})', text)
    if match: return int(match.group(1))
    return None

df_books['year'] = df_books['details'].apply(extract_year)
df_books['year'] = df_books['year'].fillna(df_books['subtitle'].apply(extract_year))
df_books['decade'] = (df_books['year'] // 10) * 10
df_books['decade'] = df_books['decade'].fillna(-1).astype(int).astype(str) + "s"

df_merged = pd.merge(df_reviews, df_books, on='id_num', how='inner')
df_merged['rating'] = df_merged['rating'].astype(float)

# Method 1: Average of all reviews
decade_reviews = df_merged.groupby('decade').agg(
    avg_rating=('rating', 'mean'),
    distinct_books=('book_id', 'nunique')
).reset_index()
filtered_reviews = decade_reviews[(decade_reviews['distinct_books'] >= 10) & (decade_reviews['decade'] != '-1s')]
best_reviews = filtered_reviews.sort_values('avg_rating', ascending=False).iloc[0]

# Method 2: Average of book averages
book_stats = df_merged.groupby(['decade', 'book_id'])['rating'].mean().reset_index()
decade_books = book_stats.groupby('decade').agg(
    avg_of_book_avgs=('rating', 'mean'),
    distinct_books=('book_id', 'count')
).reset_index()
filtered_books = decade_books[(decade_books['distinct_books'] >= 10) & (decade_books['decade'] != '-1s')]
best_books = filtered_books.sort_values('avg_of_book_avgs', ascending=False).iloc[0]

result = {
    "method_1_winner": best_reviews['decade'],
    "method_1_score": best_reviews['avg_rating'],
    "method_2_winner": best_books['decade'],
    "method_2_score": best_books['avg_of_book_avgs']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11980478109906576321': ['books_info'], 'var_function-call-9741073344249609642': 'file_storage/function-call-9741073344249609642.json', 'var_function-call-15691835330281128782': ['review'], 'var_function-call-10425051511888995697': [{'COUNT(*)': '1833'}], 'var_function-call-2377527336151131583': [{'count': '200'}], 'var_function-call-8048486413748627374': 'file_storage/function-call-8048486413748627374.json', 'var_function-call-10305899063336439880': 'file_storage/function-call-10305899063336439880.json', 'var_function-call-5379179217560364536': 'No decade meets the criteria.', 'var_function-call-9562459679862445883': {'decade': '2020s', 'average_rating': 4.663636363636364, 'distinct_books': 21, 'all_stats': [{'decade': '-1s', 'avg_rating': 4.208333333333333, 'distinct_books': 10}, {'decade': '1880s', 'avg_rating': 4.25, 'distinct_books': 1}, {'decade': '1930s', 'avg_rating': 5.0, 'distinct_books': 2}, {'decade': '1940s', 'avg_rating': 5.0, 'distinct_books': 1}, {'decade': '1970s', 'avg_rating': 4.285714285714286, 'distinct_books': 2}, {'decade': '1980s', 'avg_rating': 4.208333333333333, 'distinct_books': 11}, {'decade': '1990s', 'avg_rating': 3.8405797101449277, 'distinct_books': 18}, {'decade': '2000s', 'avg_rating': 4.273684210526316, 'distinct_books': 46}, {'decade': '2010s', 'avg_rating': 4.608591885441528, 'distinct_books': 88}, {'decade': '2020s', 'avg_rating': 4.663636363636364, 'distinct_books': 21}]}}

exec(code, env_args)
