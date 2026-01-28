code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-1526931378206999654'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-15304272311676446797'], 'r') as f:
    paper_docs = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce').fillna(0).astype(int)

paper_list = []
# Regex pattern
pattern_str = r"Author Keywords\s*[:\n\r]*(.*?)(?=\n\s*(?:ACM Classification|INTRODUCTION|Introduction|General Terms|Categories and Subject|ABSTRACT))"

for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    text = doc.get('text', '')
    
    # Use re.DOTALL | re.IGNORECASE
    match = re.search(pattern_str, text, re.DOTALL | re.IGNORECASE)
    
    domain_text = ""
    if match:
        domain_text = match.group(1).strip()
    
    paper_list.append({
        'title': title,
        'domain_text': domain_text.lower()
    })

df_papers = pd.DataFrame(paper_list)

# Filter for 'food' domain
food_papers = df_papers[df_papers['domain_text'].str.contains('food', na=False)]

# Join with citations
merged = pd.merge(food_papers, df_citations, on='title', how='inner')

total_citations = merged['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-1526931378206999654': 'file_storage/function-call-1526931378206999654.json', 'var_function-call-1526931378207000783': 'file_storage/function-call-1526931378207000783.json', 'var_function-call-15304272311676446797': 'file_storage/function-call-15304272311676446797.json'}

exec(code, env_args)
