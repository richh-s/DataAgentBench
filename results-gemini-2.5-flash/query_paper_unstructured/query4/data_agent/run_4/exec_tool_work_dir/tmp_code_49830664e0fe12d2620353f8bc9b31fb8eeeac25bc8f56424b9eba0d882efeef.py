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

    # Extract year: search for a 4-digit number that could be a year in the text
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Extract domain using 'domain:' keyword or by checking the entire text
    domain_from_text = None
    domain_keyword_match = re.search(r'(?i)domain:([^\n]+)', text)
    if domain_keyword_match:
        domain_from_text = domain_keyword_match.group(1).strip()
    elif 'physical activity' in text.lower():
        domain_from_text = 'physical activity' # Default to physical activity if found in text but no explicit domain field

    if year == 2016 and domain_from_text and 'physical activity' in domain_from_text.lower():
        extracted_papers.append({'title': title})


pd_extracted_papers = pd.DataFrame(extracted_papers)

citations = pd.read_json(locals()['var_function-call-9934081816412356413'])
citations['citation_count'] = citations['citation_count'].astype(int)

if not pd_extracted_papers.empty:
    merged_df = pd.merge(pd_extracted_papers, citations, on='title', how='inner')
    result = merged_df.groupby('title')['citation_count'].sum().reset_index().to_json(orient='records')
else:
    result = json.dumps([])

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-8240804717267947776': ['paper_docs'], 'var_function-call-11852784549828080247': 'file_storage/function-call-11852784549828080247.json', 'var_function-call-3880476428057308976': [], 'var_function-call-375944317011682617': ['Citations', 'sqlite_sequence'], 'var_function-call-9934081816412356413': 'file_storage/function-call-9934081816412356413.json'}

exec(code, env_args)
