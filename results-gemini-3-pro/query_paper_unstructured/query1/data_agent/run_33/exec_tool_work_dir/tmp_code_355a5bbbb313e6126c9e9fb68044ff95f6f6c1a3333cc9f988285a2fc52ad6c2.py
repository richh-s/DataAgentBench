code = """import json
import pandas as pd
import re

citations_path = locals()['var_function-call-1373040785545021376']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

docs_path = locals()['var_function-call-6365592025106147893']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)
df_docs = pd.DataFrame(docs_data)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

found_contexts = []

def inspect_food(row):
    text = row['text'].lower()
    title = row['title'].lower()
    
    match = False
    context = ""
    
    if 'food' in title:
        match = True
        context = "TITLE: " + title
    elif 'food' in text[:3000]:
        match = True
        idx = text.find('food')
        start = max(0, idx - 20)
        end = min(len(text), idx + 20)
        context = "TEXT: ..." + text[start:end].replace('\n', ' ') + "..."
        
    if match:
        found_contexts.append(context)
        return True
    return False

df_docs['is_food'] = df_docs.apply(inspect_food, axis=1)
food_count = df_docs['is_food'].sum()
matched_citations = df_citations[df_citations['title'].isin(df_docs[df_docs['is_food']]['title'])]
total_citations = matched_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "count": int(food_count),
    "total_citations": int(total_citations),
    "contexts": found_contexts[:20] 
}))"""

env_args = {'var_function-call-4548718859833522719': 'file_storage/function-call-4548718859833522719.json', 'var_function-call-1373040785545021376': 'file_storage/function-call-1373040785545021376.json', 'var_function-call-14795720345132237503': 'file_storage/function-call-14795720345132237503.json', 'var_function-call-6365592025106147893': 'file_storage/function-call-6365592025106147893.json', 'var_function-call-3244531972049241208': 0, 'var_function-call-168795103559867264': 390, 'var_function-call-6799362587997118290': {'total_citations': 0, 'paper_count': 0, 'papers': []}}

exec(code, env_args)
