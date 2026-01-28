code = """import json, re
with open(var_call_HrC8RRaITuE7rMfCQQq0jjdd, 'r', encoding='utf-8') as f:
    books = json.load(f)

sample = []
for rec in books[:20]:
    details = rec.get('details')
    matches = re.findall(r"\b(\d{4})\b", str(details))
    sample.append({'book_id': rec.get('book_id'), 'details_preview': (details[:200] if details else None), 'year_matches': matches})

res = {'sample': sample, 'total_records': len(books)}
print('__RESULT__:')
import json
print(json.dumps(res))"""

env_args = {'var_call_YWZpvWKF1QbXS0qUsFALVbSm': ['books_info'], 'var_call_i05rlnL0fLX8K3aiJP4gekvf': ['review'], 'var_call_HrC8RRaITuE7rMfCQQq0jjdd': 'file_storage/call_HrC8RRaITuE7rMfCQQq0jjdd.json', 'var_call_DORTvLmFhd2KKB1furIDd2XD': 'file_storage/call_DORTvLmFhd2KKB1furIDd2XD.json', 'var_call_fGwlWs1gvftkop7S9HmxTK3M': {'decade': None, 'average_rating': None, 'book_count': 0}, 'var_call_pcaSdbEpFyLYuRbUubFOM63j': {'total_books_in_books_db': 200, 'books_with_extracted_year': 0, 'unique_books_in_reviews': 200, 'unique_books_in_merged': 200, 'decade_counts_sample': {'<NA>s': 200}, 'decade_stats_top': [{'decade': '<NA>s', 'book_count': 200, 'avg_rating': 4.397539314308705}]}}

exec(code, env_args)
