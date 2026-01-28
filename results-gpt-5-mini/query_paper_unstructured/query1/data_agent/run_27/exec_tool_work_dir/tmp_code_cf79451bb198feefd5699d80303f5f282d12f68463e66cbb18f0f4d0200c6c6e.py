code = """import json
import pandas as pd
import re

# Load the Mongo query result (paper documents)
try:
    if isinstance(var_call_uuXWjcam3C6b8ECzpApjHLdL, str):
        with open(var_call_uuXWjcam3C6b8ECzpApjHLdL, 'r', encoding='utf-8') as f:
            docs = json.load(f)
    else:
        docs = var_call_uuXWjcam3C6b8ECzpApjHLdL
except Exception as e:
    docs = []

# Load the SQLite query result (citations)
try:
    if isinstance(var_call_EwaVdyGrOxCF52kxtnhU70xp, str):
        with open(var_call_EwaVdyGrOxCF52kxtnhU70xp, 'r', encoding='utf-8') as f:
            citations = json.load(f)
    else:
        citations = var_call_EwaVdyGrOxCF52kxtnhU70xp
except Exception as e:
    citations = []

# Create DataFrames
docs_df = pd.DataFrame(docs)
cit_df = pd.DataFrame(citations)

# Ensure necessary columns
if 'filename' not in docs_df.columns:
    docs_df['filename'] = None
if 'text' not in docs_df.columns:
    docs_df['text'] = ''

# Extract title from filename
def filename_to_title(fn):
    if not isinstance(fn, str):
        return fn
    return fn[:-4] if fn.lower().endswith('.txt') else fn

docs_df['title'] = docs_df['filename'].apply(filename_to_title)

# Identify papers in the 'food' domain by matching the word 'food' in text (case-insensitive)
# Use word boundary to reduce false matches
mask_food = docs_df['text'].fillna('').str.contains(r'\bfood\b', case=False, regex=True)
food_titles = docs_df.loc[mask_food, 'title'].dropna().unique().tolist()

# Prepare citations dataframe
if 'title' not in cit_df.columns:
    cit_df['title'] = None
if 'citation_count' not in cit_df.columns:
    cit_df['citation_count'] = 0

# Convert citation_count to numeric
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# Filter citations for titles in food_titles
cit_food = cit_df[cit_df['title'].isin(food_titles)]

# Sum total citations
total_citations = int(cit_food['citation_count'].sum())

# Also compute number of papers matched and number of citation records
num_papers = len(food_titles)
num_citation_records = len(cit_food)

import json as _json
output = {
    'domain': 'food',
    'total_citations': total_citations,
    'paper_count': num_papers,
    'citation_records_count': num_citation_records
}

print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_Fx1gRCw8fJBp5LpkcDphSJwQ': ['paper_docs'], 'var_call_uuXWjcam3C6b8ECzpApjHLdL': 'file_storage/call_uuXWjcam3C6b8ECzpApjHLdL.json', 'var_call_EwaVdyGrOxCF52kxtnhU70xp': 'file_storage/call_EwaVdyGrOxCF52kxtnhU70xp.json'}

exec(code, env_args)
