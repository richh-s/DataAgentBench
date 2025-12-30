code = """import json
import pandas as pd
import re

docs_path = locals()['var_function-call-6365592025106147893']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)
df_docs = pd.DataFrame(docs_data)

stats = {}
stats['total_docs'] = len(df_docs)
stats['avg_len'] = df_docs['text'].str.len().mean()

# Check 'food' in full text
def count_food(text):
    return len(re.findall(r'\bfood\b', text, re.IGNORECASE))

df_docs['food_count'] = df_docs['text'].apply(count_food)
stats['docs_with_food'] = int((df_docs['food_count'] > 0).sum())
stats['total_food_occurrences'] = int(df_docs['food_count'].sum())

# Check titles
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)
food_in_title = df_docs[df_docs['title'].str.contains('food', case=False)]
stats['docs_with_food_in_title'] = len(food_in_title)
stats['sample_titles'] = food_in_title['title'].tolist()[:5]

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-4548718859833522719': 'file_storage/function-call-4548718859833522719.json', 'var_function-call-1373040785545021376': 'file_storage/function-call-1373040785545021376.json', 'var_function-call-14795720345132237503': 'file_storage/function-call-14795720345132237503.json', 'var_function-call-6365592025106147893': 'file_storage/function-call-6365592025106147893.json', 'var_function-call-3244531972049241208': 0, 'var_function-call-168795103559867264': 390, 'var_function-call-6799362587997118290': {'total_citations': 0, 'paper_count': 0, 'papers': []}, 'var_function-call-3454208250982241730': {'food': 1}, 'var_function-call-6770306063962517473': 'Done'}

exec(code, env_args)
