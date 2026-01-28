code = """import json
import re
import pandas as pd

# Load the full paper_docs data
with open(locals()['var_function-call-11852784549828080247'], 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    # Extract year: looking for 4 digits that resemble a year (19XX or 20XX)
    # We'll look for multiple year patterns as sometimes the year is at the beginning or in a specific format
    year_matches = re.findall(r'(19|20)\d{2}', text)
    if year_matches:
        # Assuming the first four-digit number found is the publication year
        # Often, the first year mentioned is the publication year in academic papers
        year = int(year_matches[0])

    # Check if 'physical activity' is present in the text (case-insensitive) to determine the domain
    is_physical_activity_domain = 'physical activity' in text.lower()

    # Filter for papers published in 2016 and in the 'physical activity' domain
    if year == 2016 and is_physical_activity_domain:
        extracted_papers.append({'title': title})

pd_extracted_papers = pd.DataFrame(extracted_papers)

# Load citations data
citations = pd.read_json(locals()['var_function-call-9934081816412356413'])
citations['citation_count'] = citations['citation_count'].astype(int)

final_result = []
# Only proceed with merging if there are extracted papers
if not pd_extracted_papers.empty:
    merged_df = pd.merge(pd_extracted_papers, citations, on='title', how='inner')
    
    # Only proceed with grouping if the merged DataFrame is not empty
    if not merged_df.empty:
        grouped_citations = merged_df.groupby('title')['citation_count'].sum().reset_index()
        final_result = grouped_citations.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-8240804717267947776': ['paper_docs'], 'var_function-call-11852784549828080247': 'file_storage/function-call-11852784549828080247.json', 'var_function-call-3880476428057308976': [], 'var_function-call-375944317011682617': ['Citations', 'sqlite_sequence'], 'var_function-call-9934081816412356413': 'file_storage/function-call-9934081816412356413.json'}

exec(code, env_args)
