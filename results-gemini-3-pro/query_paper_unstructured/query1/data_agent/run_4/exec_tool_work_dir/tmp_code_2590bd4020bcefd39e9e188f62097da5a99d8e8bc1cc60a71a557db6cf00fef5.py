code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-343981584432704958'], 'r') as f:
    papers = json.load(f)
with open(locals()['var_function-call-6501009897595543018'], 'r') as f:
    citations = json.load(f)

# Convert to DataFrame
df_papers = pd.DataFrame(papers)
df_citations = pd.DataFrame(citations)

# Preprocess citations
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Helper to identify domain
def is_food_domain(row):
    filename = row.get('filename', '')
    text = row.get('text', '')
    if not text:
        return False
    
    # 1. Check Title
    title = filename.replace('.txt', '')
    if 'food' in title.lower():
        return True
    
    # 2. Check Keywords
    # Look for "Author Keywords" or "Keywords" or "Index Terms"
    # We will look for the section and take a chunk of text.
    text_lower = text.lower()
    
    # Find all occurrences of "keywords" to be safe (e.g. "Author Keywords", "ACM Classification Keywords")
    # We want to check if 'food' appears in the lines immediately following "keywords"
    
    keyword_indices = [m.start() for m in re.finditer(r'keywords', text_lower)]
    
    for idx in keyword_indices:
        # Extract a window, say 500 chars
        window = text_lower[idx:idx+500]
        # We need to be careful not to match "food" in the main text if it's far away.
        # But usually keywords are at the start.
        # Let's check if 'food' is in this window.
        if 'food' in window:
             return True

    return False

# Filter papers
food_papers = []
for p in papers:
    if is_food_domain(p):
        title = p['filename'].replace('.txt', '')
        food_papers.append(title)

# Filter citations
# The titles in citations match the filenames without .txt
# We want citations for these papers.
# Note: Citations table has multiple entries per paper (one for each year).
# We want the *total* citation count for these papers.

# Filter citations where title is in food_papers
food_citations = df_citations[df_citations['title'].isin(food_papers)]

total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-4282369109293305518': ['paper_docs'], 'var_function-call-17210862545939823160': 'file_storage/function-call-17210862545939823160.json', 'var_function-call-6501009897595543018': 'file_storage/function-call-6501009897595543018.json', 'var_function-call-343981584432704958': 'file_storage/function-call-343981584432704958.json'}

exec(code, env_args)
