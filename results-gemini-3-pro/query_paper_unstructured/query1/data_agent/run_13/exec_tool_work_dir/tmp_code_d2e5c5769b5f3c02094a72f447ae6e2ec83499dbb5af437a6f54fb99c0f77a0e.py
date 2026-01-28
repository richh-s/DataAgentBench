code = """import json
import pandas as pd
import re

# Load citations
with open(locals()['var_function-call-1526931378206999654'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-15304272311676446797'], 'r') as f:
    paper_docs = json.load(f)

# Create Citations DataFrame
df_citations = pd.DataFrame(citations_data)
# Convert citation_count to int
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce').fillna(0).astype(int)

# Extract domain and create Paper DataFrame
paper_list = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    text = doc.get('text', '')
    
    # Extract Author Keywords
    # Pattern: "Author Keywords" followed by text until "ACM Classification" or "INTRODUCTION" or "General Terms"
    # We use re.DOTALL to match newlines
    match = re.search(r"Author Keywords\s*[:\n\r]*(.*?)(?=\n\s*(?:ACM Classification|INTRODUCTION|Introduction|General Terms|Categories and Subject|ABSTRACT))", text, re.DOTALL | re.IGNORECASE)
    
    domain_text = ""
    if match:
        domain_text = match.group(1).strip()
    else:
        # Fallback: Maybe keywords are at the end? Or just search in the first 2000 chars?
        # But let's trust the structure for now.
        # If no keywords found, domain_text is empty.
        pass
        
    paper_list.append({
        'title': title,
        'domain_text': domain_text.lower()
    })

df_papers = pd.DataFrame(paper_list)

# Filter for 'food' domain
# Hint says: "Common domains include: 'food'... values may be part of a list"
# So we check if 'food' is in domain_text
food_papers = df_papers[df_papers['domain_text'].str.contains('food', na=False)]

# Join with citations
# Citations table has multiple rows per paper (one for each year).
# We need to sum citation_count for each paper first?
# Or just inner join and sum the column.
# Let's inner join.
merged = pd.merge(food_papers, df_citations, on='title', how='inner')

total_citations = merged['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-1526931378206999654': 'file_storage/function-call-1526931378206999654.json', 'var_function-call-1526931378207000783': 'file_storage/function-call-1526931378207000783.json', 'var_function-call-15304272311676446797': 'file_storage/function-call-15304272311676446797.json'}

exec(code, env_args)
