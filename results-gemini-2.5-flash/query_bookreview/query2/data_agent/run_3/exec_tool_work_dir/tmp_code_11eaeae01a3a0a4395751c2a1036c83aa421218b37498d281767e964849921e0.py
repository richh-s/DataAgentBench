code = """import pandas as pd
import json

with open(locals()['var_function-call-4348341325577532400'], 'r') as f:
    books_info_data = json.load(f)

books_info_df = pd.DataFrame(books_info_data)

book_ids = books_info_df['book_id'].tolist()

query_parts = []
for i in range(0, len(book_ids), 999):
    chunk = book_ids[i:i+999]
    formatted_chunk = [f"'{book_id}'" for book_id in chunk]
    query_parts.append(f"purchase_id IN ({', '.join(formatted_chunk)})")

full_query_condition = " OR ".join(query_parts)

print("__RESULT__:")
print(json.dumps(full_query_condition))"""

env_args = {'var_function-call-6658667449938364956': ['review'], 'var_function-call-16917640181901645325': ['books_info'], 'var_function-call-4348341325577532400': 'file_storage/function-call-4348341325577532400.json'}

exec(code, env_args)
