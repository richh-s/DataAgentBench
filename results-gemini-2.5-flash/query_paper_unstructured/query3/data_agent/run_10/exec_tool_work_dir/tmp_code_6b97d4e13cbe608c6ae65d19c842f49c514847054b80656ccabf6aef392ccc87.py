code = """import pandas as pd
import json
import re

citation_data_path = locals()['var_function-call-991468019746900088']
paper_docs_data_path = locals()['var_function-call-15516009526492749506']

with open(citation_data_path, 'r') as f:
    citations = json.load(f)
df_citations = pd.DataFrame(citations)
df_citations['total_citation_count'] = pd.to_numeric(df_citations['total_citation_count'])

with open(paper_docs_data_path, 'r') as f:
    paper_docs = json.load(f)
df_papers = pd.DataFrame(paper_docs)

def extract_paper_info(text, filename):
    title = filename.replace('.txt', '')
    year = None
    contribution_type = []

    # Extract year
    # Look for 4-digit years or 2-digit years following an apostrophe (e.g., '15)
    years_found = re.findall(r"\b(?:19|20)\d{2}\b|\'\d{2}", text[:1000])
    # Convert 'YY to 20YY
    years_processed = []
    for y in years_found:
        if y.startswith("'"):
            years_processed.append(2000 + int(y[1:]))
        else:
            years_processed.append(int(y))
    
    if years_processed:
        # Assuming the earliest year found in the beginning of the paper is the publication year
        year = min(years_processed)

    # Extract contribution type
    if 'empirical' in text.lower():
        contribution_type.append('empirical')

    return title, year, contribution_type

df_papers[['title', 'year', 'contribution']] = df_papers.apply(
    lambda row: pd.Series(extract_paper_info(row['text'], row['filename'])),
    axis=1
)

# Filter for papers with 'empirical' contribution and published after 2016
filtered_papers = df_papers[
    df_papers['contribution'].apply(lambda x: 'empirical' in x) &
    (df_papers['year'] > 2016)
]

# Merge with citation data
final_result = pd.merge(filtered_papers, df_citations, on='title', how='inner')

# Select and format the required columns
output = final_result[['title', 'total_citation_count']].to_json(orient='records')

print('__RESULT__:')
print(output)"""

env_args = {'var_function-call-991468019746900088': 'file_storage/function-call-991468019746900088.json', 'var_function-call-15516009526492749506': 'file_storage/function-call-15516009526492749506.json'}

exec(code, env_args)
