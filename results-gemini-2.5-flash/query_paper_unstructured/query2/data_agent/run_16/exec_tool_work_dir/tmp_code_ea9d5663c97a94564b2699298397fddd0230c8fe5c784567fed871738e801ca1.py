code = """import json
import pandas as pd

with open(locals()['var_function-call-2733262756667275774'], 'r') as f:
    paper_docs = json.load(f)

paper_data = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    source = "Unknown"
    if "ACM" in text:
        source = "ACM"
    elif "IEEE" in text:
        source = "IEEE"
    elif "PubMed" in text:
        source = "PubMed"
    paper_data.append({'title': title, 'source': source})

acm_papers_df = pd.DataFrame(paper_data)
acm_papers_filtered_df = acm_papers_df[acm_papers_df['source'] == 'ACM']

with open(locals()['var_function-call-16151639989344602586'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

merged_df = pd.merge(citations_df, acm_papers_filtered_df, on='title', how='inner')
average_citation_count = merged_df['citation_count'].mean()

print("__RESULT__:")
print(json.dumps(average_citation_count))"""

env_args = {'var_function-call-16151639989344602586': 'file_storage/function-call-16151639989344602586.json', 'var_function-call-2733262756667275774': 'file_storage/function-call-2733262756667275774.json'}

exec(code, env_args)
