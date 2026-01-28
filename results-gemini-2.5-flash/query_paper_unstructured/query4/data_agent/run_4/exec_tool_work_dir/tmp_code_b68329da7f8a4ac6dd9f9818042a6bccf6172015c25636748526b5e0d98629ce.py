code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-11852784549828080247'], 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year: looking for 4 digits that resemble a year (19XX or 20XX)
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Check for 'physical activity' in the entire text (case-insensitive)
    if year == 2016 and 'physical activity' in text.lower():
        extracted_papers.append({'title': title})


pd_extracted_papers = pd.DataFrame(extracted_papers)

citations = pd.read_json(locals()['var_function-call-9934081816412356413'])
citations['citation_count'] = citations['citation_count'].astype(int)

merged_df = pd.merge(pd_extracted_papers, citations, on='title', how='inner')

result = merged_df.groupby('title')['citation_count'].sum().reset_index().to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-8240804717267947776': ['paper_docs'], 'var_function-call-11852784549828080247': 'file_storage/function-call-11852784549828080247.json', 'var_function-call-3880476428057308976': [], 'var_function-call-375944317011682617': ['Citations', 'sqlite_sequence'], 'var_function-call-9934081816412356413': 'file_storage/function-call-9934081816412356413.json'}

exec(code, env_args)
