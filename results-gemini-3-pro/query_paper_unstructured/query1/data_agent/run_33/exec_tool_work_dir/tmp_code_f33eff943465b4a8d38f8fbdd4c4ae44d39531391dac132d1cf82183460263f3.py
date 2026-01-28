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

def is_food_domain(row):
    text = row['text'].lower()
    title = row['title'].lower()
    
    # Check Title
    if 'food' in title:
        return True
    
    # Check Header/Abstract (first 3000 chars) for distinct word "food" or "foods"
    head = text[:3000]
    if re.search(r'\bfoods?\b', head):
        return True
        
    return False

df_docs['is_food'] = df_docs.apply(is_food_domain, axis=1)
food_papers = df_docs[df_docs['is_food']]
food_titles = food_papers['title'].unique()

# Get citations for these papers
matched_citations = df_citations[df_citations['title'].isin(food_titles)]
grouped = matched_citations.groupby('title')['citation_count'].sum().reset_index()

# Prepare result to inspect
result_info = {
    "total_citations": int(matched_citations['citation_count'].sum()),
    "paper_count": int(len(food_titles)),
    "papers": grouped.to_dict(orient='records')
}

print("__RESULT__:")
print(json.dumps(result_info))"""

env_args = {'var_function-call-4548718859833522719': 'file_storage/function-call-4548718859833522719.json', 'var_function-call-1373040785545021376': 'file_storage/function-call-1373040785545021376.json', 'var_function-call-14795720345132237503': 'file_storage/function-call-14795720345132237503.json', 'var_function-call-6365592025106147893': 'file_storage/function-call-6365592025106147893.json', 'var_function-call-3244531972049241208': 0, 'var_function-call-168795103559867264': 390}

exec(code, env_args)
