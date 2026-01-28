code = """import json
import re
import pandas as pd

def extract_year(text):
    # Search for a four-digit number that is likely a year in the first 200 characters
    match = re.search(r'\b(19|20)\d{2}\b', text[:200])
    if match:
        return int(match.group(0))
    return None

def extract_domain(text):
    if 'physical activity' in text.lower():
        return 'physical activity'
    return None

paper_docs_raw = json.load(open(locals()['var_function-call-13040654951209415358'], 'r'))
papers_extracted_info = []
for doc in paper_docs_raw:
    title = doc['filename'].replace('.txt', '')
    year = extract_year(doc['text'])
    domain = extract_domain(doc['text'])
    if year is not None and domain == 'physical activity':
        papers_extracted_info.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_df = pd.DataFrame([p for p in papers_extracted_info if p['year'] == 2016])

citations_df = pd.DataFrame(json.load(open(locals()['var_function-call-12305578897446280284'], 'r')))
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

merged_df = pd.merge(filtered_papers_df, citations_df, on='title', how='inner')

# Group by title and sum citation counts
result_df = merged_df.groupby('title')['citation_count'].sum().reset_index()

print("__RESULT__:")
print(result_df.to_json(orient='records'))"""

env_args = {'var_function-call-12305578897446280284': 'file_storage/function-call-12305578897446280284.json', 'var_function-call-2531435270866315542': ['paper_docs'], 'var_function-call-13040654951209415358': 'file_storage/function-call-13040654951209415358.json', 'var_function-call-13697098365809760818': [], 'var_function-call-875481124080558574': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': 'physical activity'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': 'physical activity'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': 'physical activity'}]}

exec(code, env_args)
