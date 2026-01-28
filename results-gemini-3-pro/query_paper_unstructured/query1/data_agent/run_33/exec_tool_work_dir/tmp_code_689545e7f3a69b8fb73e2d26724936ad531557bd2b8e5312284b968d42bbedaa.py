code = """import json
import pandas as pd
import re

# Load Citations
citations_path = locals()['var_function-call-1373040785545021376']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)
# Convert citation_count to numeric
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Load Paper Docs
docs_path = locals()['var_function-call-6365592025106147893']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)
df_docs = pd.DataFrame(docs_data)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

# Debug: Check if 'food' is in any text
def check_food_simple(text):
    return 'food' in text.lower()

df_docs['has_food_simple'] = df_docs['text'].apply(check_food_simple)
print(f"Papers with 'food' in text: {df_docs['has_food_simple'].sum()}")

# Debug: Check title match
# Take a title from citations and check if it exists in docs
sample_title = df_citations['title'].iloc[0]
print(f"Sample title from citations: {sample_title}")
print(f"Exists in docs: {sample_title in df_docs['title'].values}")

# Re-run the domain logic with the simple check first to see potential
# If simple check > 0, then we can refine.
# I'll use the result of simple check for now to see the max possible citations.
# But I must be careful about false positives.

# Let's try to capture papers where 'food' is in the Title OR Keywords OR Abstract (first 3000 chars)
# Using 'food' in title is safe.
# Using 'food' in keywords is safe.
# Using 'food' in abstract is relatively safe.
def is_food_domain(row):
    text = row['text'].lower()
    title = row['title'].lower()
    
    if 'food' in title:
        return True
    
    # Check first 3000 chars
    head = text[:3000]
    if 'food' in head:
        return True
        
    return False

df_docs['is_food'] = df_docs.apply(is_food_domain, axis=1)
food_count = df_docs['is_food'].sum()
print(f"Papers identified as food domain (Title/Abstract): {food_count}")

food_titles = df_docs[df_docs['is_food']]['title'].unique()
matched_citations = df_citations[df_citations['title'].isin(food_titles)]
total = matched_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total)))"""

env_args = {'var_function-call-4548718859833522719': 'file_storage/function-call-4548718859833522719.json', 'var_function-call-1373040785545021376': 'file_storage/function-call-1373040785545021376.json', 'var_function-call-14795720345132237503': 'file_storage/function-call-14795720345132237503.json', 'var_function-call-6365592025106147893': 'file_storage/function-call-6365592025106147893.json', 'var_function-call-3244531972049241208': 0}

exec(code, env_args)
