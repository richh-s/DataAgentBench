code = """import json, pandas as pd, re

# Load citations totals per title
path = var_call_KK6nAHClQkjNpBe5k1V6qTTW
with open(path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# Use a heuristics list of food-domain titles based on common food-tracking paper titles present in dataset
food_title_keywords = [
    'Food', 'Nutrition', 'Diet', 'Eating', 'Meal', 'Calorie', 'Journaling', 'Journalers', 'Dietitians', 'Chocolate'
]
pat = re.compile(r'(' + '|'.join([re.escape(k) for k in food_title_keywords]) + r')', re.IGNORECASE)

food_df = df_cit[df_cit['title'].str.contains(pat, na=False)].copy()

# Sum total citations
ans = int(food_df['total_citations'].sum())

print('__RESULT__:')
print(json.dumps({'total_citation_count_food_domain_estimate': ans, 'matched_titles_count': int(len(food_df))}))"""

env_args = {'var_call_KK6nAHClQkjNpBe5k1V6qTTW': 'file_storage/call_KK6nAHClQkjNpBe5k1V6qTTW.json', 'var_call_aai80U9Gok8KMYtRUxJQn6YG': [], 'var_call_JdybeP3055DKDx74tXklRb9s': 'file_storage/call_JdybeP3055DKDx74tXklRb9s.json'}

exec(code, env_args)
