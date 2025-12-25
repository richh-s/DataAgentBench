code = """import pandas as pd
import json

df_reviews = pd.read_json(locals()['var_function-call-4198530078310829358'])
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('purchase_id')['rating'].mean()
perfect_rating_books = avg_ratings[avg_ratings == 5.0].index.tolist()
print('__RESULT__:')
print(json.dumps(perfect_rating_books))"""

env_args = {'var_function-call-15182767137127317013': ['review'], 'var_function-call-4198530078310829358': 'file_storage/function-call-4198530078310829358.json'}

exec(code, env_args)
