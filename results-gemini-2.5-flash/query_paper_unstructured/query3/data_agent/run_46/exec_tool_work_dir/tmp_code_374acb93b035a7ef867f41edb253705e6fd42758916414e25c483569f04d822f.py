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
    
    # Extract year (looking for 4-digit numbers, usually near copyright or venue info in the first 2000 chars)
    # Corrected the regex by removing the problematic single quote.
    year_match = re.search(r"(?:[Cc]opyright|\n\n[A-Z]{3,}\s\d{2})\s*(\d{4})", text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    # Check for 'empirical' contribution
    is_empirical = 'empirical' in text.lower()
    
    if year and is_empirical:
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
