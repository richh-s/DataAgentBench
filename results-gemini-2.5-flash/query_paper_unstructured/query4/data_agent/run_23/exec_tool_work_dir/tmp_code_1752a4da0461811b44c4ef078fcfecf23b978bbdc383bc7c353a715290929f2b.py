code = """import pandas as pd
import json
import re

# Load the full result from the JSON file for paper_docs
file_path_papers = locals()['var_function-call-13583694419194179142']
with open(file_path_papers, 'r') as f:
    paper_docs = json.load(f)

df_papers = pd.DataFrame(paper_docs)

# Extract title from filename
df_papers['title'] = df_papers['filename'].apply(lambda x: x.replace('.txt', ''))

# Function to extract year and domain from text
def extract_info(text):
    year = None
    # Try to extract a four-digit number that looks like a year
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_match:
        year = int(year_match.group(0))

    domain = []
    # Use substring matching for 'physical activity' within the entire text (case-insensitive)
    if re.search(r'(?i)physical activity', text):
        domain.append('physical activity')

    return year, domain

df_papers[['year', 'domain']] = df_papers['text'].apply(lambda x: pd.Series(extract_info(x)))

# Filter for papers published in 2016 and in the 'physical activity' domain
filtered_papers = df_papers[(df_papers['year'] == 2016) & (df_papers['domain'].apply(lambda x: 'physical activity' in [d.lower() for d in x] if x else False))]

# Select only title and year from the filtered papers to avoid large intermediate results
filtered_papers_for_merge = filtered_papers[['title', 'year']].copy()

# Load the full result from the JSON file for citations
file_path_citations = locals()['var_function-call-9615023223999036809']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)

# Ensure 'citation_count' is numeric
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Join the filtered papers with citation data
merged_df = pd.merge(filtered_papers_for_merge, df_citations, on='title', how='inner')

# Group by title and sum the citation count
total_citations = merged_df.groupby('title')['citation_count'].sum().reset_index()

result = total_citations.to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-12002833206080555708': ['paper_docs'], 'var_function-call-13583694419194179142': 'file_storage/function-call-13583694419194179142.json', 'var_function-call-12214905290348426633': [], 'var_function-call-9615023223999036809': 'file_storage/function-call-9615023223999036809.json', 'var_function-call-12622661220469309068': [], 'var_function-call-204629567651961434': [], 'var_function-call-9341337320625884206': 'file_storage/function-call-9341337320625884206.json'}

exec(code, env_args)
