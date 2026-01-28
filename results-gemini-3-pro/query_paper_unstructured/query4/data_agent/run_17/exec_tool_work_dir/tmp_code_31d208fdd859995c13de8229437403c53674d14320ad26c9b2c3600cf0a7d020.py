code = """import json
import pandas as pd
import re

# Access variables from locals()
citations_file = locals()['var_function-call-1625396781395039115']
papers_file = locals()['var_function-call-3120307728303997294']

# Load citations
with open(citations_file, 'r') as f:
    citations_data = json.load(f)
df_citations = pd.DataFrame(citations_data)

# Aggregate citations by title
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
df_citations_agg = df_citations.groupby('title')['citation_count'].sum().reset_index()

# Load papers
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

filtered_papers = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract year
    # Look for 2016 in the first 1000 chars. 
    # Also considering "CHI '16" or similar patterns just in case 2016 is not explicit.
    # But usually full year is present in copyright or header.
    header = text[:1000]
    if re.search(r'\b2016\b', header):
        year = 2016
    else:
        year = None
        
    # Extract domain
    # Check for 'physical activity' in text (case insensitive)
    if 'physical activity' in text.lower():
        domain_match = True
    else:
        domain_match = False
        
    if year == 2016 and domain_match:
        # Clean title
        title = filename.replace('.txt', '')
        filtered_papers.append(title)

# Join with citations
# Filter aggregated citations where title is in filtered_papers
result_df = df_citations_agg[df_citations_agg['title'].isin(filtered_papers)]

# Convert to list of dicts
final_result = result_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-14316968101871802559': ['paper_docs'], 'var_function-call-14316968101871802262': ['Citations', 'sqlite_sequence'], 'var_function-call-637640979100223299': 'file_storage/function-call-637640979100223299.json', 'var_function-call-1625396781395039115': 'file_storage/function-call-1625396781395039115.json', 'var_function-call-3120307728303997294': 'file_storage/function-call-3120307728303997294.json'}

exec(code, env_args)
