code = """import json
import re
import pandas as pd

def extract_paper_info(paper_text, filename):
    title = filename.replace(".txt", "")
    year = None
    contribution_type = None

    # Extract year: look for 4-digit numbers starting with 19 or 20 in the first 500 characters
    year_match = re.search(r'\b(19|20)\d{2}\b', paper_text[:500])
    if year_match:
        year = int(year_match.group(0))

    # Extract contribution: check for "empirical" (case-insensitive) anywhere in the text
    if 'empirical' in paper_text.lower():
        contribution_type = 'empirical'

    return {'title': title, 'year': year, 'contribution': contribution_type}

file_path = locals()['var_function-call-17384357217489800854']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_info = []
for doc in paper_docs:
    info = extract_paper_info(doc['text'], doc['filename'])
    papers_info.append(info)

# Filter papers based on year and contribution
filtered_papers = []
for paper in papers_info:
    if paper['year'] is not None and paper['year'] > 2016 and paper['contribution'] == 'empirical':
        filtered_papers.append(paper)

# Convert to DataFrame for easier merging
filtered_papers_df = pd.DataFrame(filtered_papers)

# Load citation data
citation_file_path = locals()['var_function-call-505378774442661286']
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

citations_df = pd.DataFrame(citation_data)
citations_df['total_citation_count'] = citations_df['total_citation_count'].astype(int)


# Merge the two dataframes
merged_df = pd.merge(filtered_papers_df, citations_df, on='title', how='inner')

# Select and format the final output
result = merged_df[['title', 'total_citation_count']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-8876707072609632946': ['Citations', 'sqlite_sequence'], 'var_function-call-9424252978014940020': ['paper_docs'], 'var_function-call-17384357217489800854': 'file_storage/function-call-17384357217489800854.json', 'var_function-call-13031117097295312790': [], 'var_function-call-505378774442661286': 'file_storage/function-call-505378774442661286.json'}

exec(code, env_args)
