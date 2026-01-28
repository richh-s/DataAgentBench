code = """import json
import pandas as pd

with open(var_call_bmIgUAXKjX8yjxSfPgATyeTy, 'r') as f:
    reviews = json.load(f)
with open(var_call_PqDutk8xXQUKu7IuHjYHFlrN, 'r') as f:
    books = json.load(f)

df_r = pd.DataFrame(reviews)
df_b = pd.DataFrame(books)

out = {
    'review_columns': list(df_r.columns),
    'books_columns': list(df_b.columns),
    'review_len': len(df_r),
    'books_len': len(df_b),
    'review_head': df_r.head(3).to_dict(orient='records'),
    'books_head': df_b.head(3).to_dict(orient='records')
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_V4Ay7XT6DZjxMcFI1xYIrbr3': ['review'], 'var_call_xjSOnwYTFge2cGaFGNaZqfAm': ['books_info'], 'var_call_bmIgUAXKjX8yjxSfPgATyeTy': 'file_storage/call_bmIgUAXKjX8yjxSfPgATyeTy.json', 'var_call_PqDutk8xXQUKu7IuHjYHFlrN': 'file_storage/call_PqDutk8xXQUKu7IuHjYHFlrN.json'}

exec(code, env_args)
