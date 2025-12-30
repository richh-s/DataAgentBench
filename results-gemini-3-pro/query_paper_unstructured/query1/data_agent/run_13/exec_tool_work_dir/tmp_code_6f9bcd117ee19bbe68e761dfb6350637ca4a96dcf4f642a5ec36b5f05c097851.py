code = """import json
import pandas as pd

with open(locals()['var_function-call-1526931378206999654'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-15304272311676446797'], 'r') as f:
    paper_docs = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce').fillna(0).astype(int)

paper_list = []
start_marker = "author keywords"
end_markers = ["acm classification", "introduction", "abstract", "general terms", "categories and subject"]

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = doc.get('text', '').lower()
    
    domain_text = ""
    start_idx = text.find(start_marker)
    if start_idx != -1:
        # Check end markers
        best_end_idx = len(text)
        found_end = False
        for m in end_markers:
            idx = text.find(m, start_idx)
            if idx != -1 and idx < best_end_idx:
                best_end_idx = idx
                found_end = True
        
        # If no end marker found close by, maybe take next 500 chars
        if not found_end:
             best_end_idx = start_idx + 500
             
        domain_text = text[start_idx:best_end_idx]
    
    paper_list.append({
        'title': title,
        'domain_text': domain_text
    })

df_papers = pd.DataFrame(paper_list)

# Filter for 'food' domain
food_papers = df_papers[df_papers['domain_text'].str.contains('food', na=False)]

merged = pd.merge(food_papers, df_citations, on='title', how='inner')
total_citations = merged['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-1526931378206999654': 'file_storage/function-call-1526931378206999654.json', 'var_function-call-1526931378207000783': 'file_storage/function-call-1526931378207000783.json', 'var_function-call-15304272311676446797': 'file_storage/function-call-15304272311676446797.json'}

exec(code, env_args)
