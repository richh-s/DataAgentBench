code = """import json
import pandas as pd
import re
from datetime import datetime

with open(var_call_1FcBgCKDIm7pwEtxeM28e23N, 'r') as f:
    reviews = json.load(f)
with open(var_call_17MEPLWTrGD9QV5OvoSDLmmZ, 'r') as f:
    books = json.load(f)

rev_df = pd.DataFrame(reviews)
books_df = pd.DataFrame(books)

out = {
    'rev_columns': list(rev_df.columns),
    'books_columns': list(books_df.columns),
    'rev_sample_first_row': rev_df.iloc[0].to_dict() if len(rev_df)>0 else None,
    'books_sample_first_row': books_df.iloc[0].to_dict() if len(books_df)>0 else None
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_mVVpJoNT9uzr2PlzsQWzbkqG': ['review'], 'var_call_tRrgSzlaazg8qOSlICKzoF4A': ['books_info'], 'var_call_1FcBgCKDIm7pwEtxeM28e23N': 'file_storage/call_1FcBgCKDIm7pwEtxeM28e23N.json', 'var_call_17MEPLWTrGD9QV5OvoSDLmmZ': 'file_storage/call_17MEPLWTrGD9QV5OvoSDLmmZ.json'}

exec(code, env_args)
