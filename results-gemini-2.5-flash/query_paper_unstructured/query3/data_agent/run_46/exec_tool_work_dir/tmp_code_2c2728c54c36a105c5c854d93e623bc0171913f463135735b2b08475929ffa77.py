code = """import pandas as pd
import re
import json

# Load citation data
with open(locals()['var_function-call-7430864031196320342'], 'r') as f:
    citation_data = json.load(f)
citations_df = pd.DataFrame(citation_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'], errors='coerce')
citations_agg = citations_df.groupby('title')['citation_count'].sum().reset_index()
citations_agg.rename(columns={'citation_count': 'total_citation_count'}, inplace=True)

# Load paper documents
with open(locals()['var_function-call-15035999036959111997'], 'r') as f:
    paper_docs_data = json.load(f)

extracted_papers = []
for doc in paper_docs_data:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract all 4-digit numbers in the first 2000 characters and filter for plausible years
    all_years = [int(y) for y in re.findall(r'\b\d{4}\b', text[:2000]) if 1950 <= int(y) <= 2024]
    year = max(all_years) if all_years else None # Take the maximum year if multiple are found
    
    # Check for 'empirical' contribution (case-insensitive)
    is_empirical = 'empirical' in text.lower()
    
    if year is not None and is_empirical:
        extracted_papers.append({'title': title, 'year': year, 'contribution': 'empirical'})

papers_df = pd.DataFrame(extracted_papers)

# Filter papers published after 2016
filtered_papers_df = papers_df[papers_df['year'] > 2016]

# Merge with citation data
final_result_df = pd.merge(filtered_papers_df, citations_agg, on='title', how='inner')

# Select and format the desired columns
final_output = final_result_df[['title', 'total_citation_count']]
print('__RESULT__:')
print(final_output.to_json(orient='records'))"""

env_args = {'var_function-call-7430864031196320342': 'file_storage/function-call-7430864031196320342.json', 'var_function-call-15035999036959111997': 'file_storage/function-call-15035999036959111997.json'}

exec(code, env_args)
