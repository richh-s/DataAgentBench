code = """import json
import re

# Load citations data for 2018
citations_data = var_functions_query_db_4
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_data

# Load paper documents
paper_docs_data = var_functions_query_db_5
if isinstance(paper_docs_data, str):
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

# Build a set of titles that are ACM papers
acm_titles_set = set()
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        text = doc.get('text', '')
        if 'ACM' in text:
            acm_titles_set.add(title.strip().lower())

# Filter citations for ACM papers and compute average citation count
acm_citations = []
total_citations = 0
for cit in citations_2018:
    cit_title = cit.get('title', '').strip().lower()
    if cit_title in acm_titles_set:
        acm_citations.append(cit)
        total_citations += int(cit.get('citation_count', 0))

if acm_citations:
    avg_citation = total_citations / len(acm_citations)
    result = f"The average citation count for papers published by ACM cited in 2018 is {avg_citation:.2f}, based on {len(acm_citations)} ACM papers."
else:
    result = "No ACM papers were found in the citation data for 2018."

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
