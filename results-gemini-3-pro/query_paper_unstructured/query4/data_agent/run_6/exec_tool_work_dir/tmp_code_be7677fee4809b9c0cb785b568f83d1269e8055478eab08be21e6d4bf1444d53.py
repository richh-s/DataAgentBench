code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-5245459546365613242'], 'r') as f:
    paper_docs = json.load(f)
with open(locals()['var_function-call-2821157427682143998'], 'r') as f:
    citations = json.load(f)

# Process papers
matching_papers = []
for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Check year: Look for "2016" in the first 2000 characters
    # This covers the header, copyright line, and conference info usually found at the top.
    header_text = text[:2000]
    is_2016 = '2016' in header_text
    
    # Check domain: "physical activity" in full text (case insensitive)
    is_domain = 'physical activity' in text.lower()
    
    if is_2016 and is_domain:
        matching_papers.append(title)

# Process citations
df_citations = pd.DataFrame(citations)

# Filter citations for matching titles
if not df_citations.empty:
    matched_citations = df_citations[df_citations['title'].isin(matching_papers)].copy()
    
    if not matched_citations.empty:
        # Convert citation_count to int
        matched_citations['citation_count'] = matched_citations['citation_count'].astype(int)
        
        # Group by title and sum citation_count
        result_df = matched_citations.groupby('title')['citation_count'].sum().reset_index()
        
        # Convert to list of dicts
        result = result_df.to_dict(orient='records')
    else:
        result = []
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7041651409828348030': ['paper_docs'], 'var_function-call-5245459546365613242': 'file_storage/function-call-5245459546365613242.json', 'var_function-call-2821157427682143998': 'file_storage/function-call-2821157427682143998.json'}

exec(code, env_args)
