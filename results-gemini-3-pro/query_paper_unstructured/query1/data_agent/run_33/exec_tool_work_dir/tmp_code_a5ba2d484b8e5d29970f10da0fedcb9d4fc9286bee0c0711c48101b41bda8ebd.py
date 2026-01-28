code = """import json
import pandas as pd
import re

docs_path = locals()['var_function-call-6365592025106147893']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)
df_docs = pd.DataFrame(docs_data)

print(f"Total docs: {len(df_docs)}")
print(f"Avg text length: {df_docs['text'].str.len().mean()}")

# Check 'food' in full text
def count_food(text):
    return len(re.findall(r'\bfood\b', text, re.IGNORECASE))

df_docs['food_count'] = df_docs['text'].apply(count_food)
print(f"Docs with 'food' word: {(df_docs['food_count'] > 0).sum()}")
print(f"Total 'food' occurrences: {df_docs['food_count'].sum()}")

# Check titles
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
food_in_title = df_docs[df_docs['title'].str.contains('food', case=False)]
print(f"Docs with 'food' in title: {len(food_in_title)}")
print(f"Titles with 'food': {food_in_title['title'].tolist()[:5]}")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-4548718859833522719': 'file_storage/function-call-4548718859833522719.json', 'var_function-call-1373040785545021376': 'file_storage/function-call-1373040785545021376.json', 'var_function-call-14795720345132237503': 'file_storage/function-call-14795720345132237503.json', 'var_function-call-6365592025106147893': 'file_storage/function-call-6365592025106147893.json', 'var_function-call-3244531972049241208': 0, 'var_function-call-168795103559867264': 390, 'var_function-call-6799362587997118290': {'total_citations': 0, 'paper_count': 0, 'papers': []}, 'var_function-call-3454208250982241730': {'food': 1}}

exec(code, env_args)
