code = """import json
import pandas as pd
import re

# Load Citations
citations_path = locals()['var_function-call-1373040785545021376']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Load Paper Docs
docs_path = locals()['var_function-call-5170324898158576945']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)
df_docs = pd.DataFrame(docs_data)

# Extract title from filename
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

def is_food_domain(row):
    text = row['text']
    title = row['title'].lower()
    
    # Check Title
    if 'food' in title:
        return True
    
    # Check first 3000 chars (Header/Abstract/Keywords)
    # We look for word boundary 'food' or 'foods'
    head_text = text[:3000].lower()
    if re.search(r'\bfoods?\b', head_text):
        return True
        
    return False

df_docs['is_food'] = df_docs.apply(is_food_domain, axis=1)

food_papers = df_docs[df_docs['is_food']]
food_titles = food_papers['title'].unique()

# Filter citations
matched_citations = df_citations[df_citations['title'].isin(food_titles)]
total_citations = int(matched_citations['citation_count'].sum())

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-4548718859833522719': 'file_storage/function-call-4548718859833522719.json', 'var_function-call-1373040785545021376': 'file_storage/function-call-1373040785545021376.json', 'var_function-call-14795720345132237503': 'file_storage/function-call-14795720345132237503.json', 'var_function-call-6365592025106147893': 'file_storage/function-call-6365592025106147893.json', 'var_function-call-3244531972049241208': 0, 'var_function-call-168795103559867264': 390, 'var_function-call-6799362587997118290': {'total_citations': 0, 'paper_count': 0, 'papers': []}, 'var_function-call-3454208250982241730': {'food': 1}, 'var_function-call-6770306063962517473': 'Done', 'var_function-call-13166130446865522156': {'total_docs': 5, 'avg_len': 66867.0, 'docs_with_food': 0, 'total_food_occurrences': 0, 'docs_with_food_in_title': 0, 'sample_titles': []}, 'var_function-call-5170324898158576945': 'file_storage/function-call-5170324898158576945.json'}

exec(code, env_args)
