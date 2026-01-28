code = """import json
import re

# Load citations data for 2018 from the variable
# The result key "var_functions.query_db:4" needs to be accessed properly
citations_data = var_functions_query_db_4

# If it's a string (file path), load the JSON file
if isinstance(citations_data, str):
    citations_file = citations_data
    citations_2018 = []
    with open(citations_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_data

# Load paper documents from the variable
paper_docs_data = var_functions_query_db_5

# If it's a string (file path), load the JSON file
if isinstance(paper_docs_data, str):
    paper_docs_file = paper_docs_data
    paper_docs = []
    with open(paper_docs_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

# Build a set of titles that are ACM papers
acm_titles_set = set()
for doc in paper_docs:
    # Extract title from filename
    filename = doc.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]  # Remove .txt extension
    # Check if text contains ACM
    text = doc.get('text', '')
    if 'ACM' in text:
        # Normalize title for matching
        acm_titles_set.add(title.strip().lower())

# Filter citations for ACM papers and compute average citation count
acm_citations = []
total_citations = 0
for cit in citations_2018:
    cit_title = cit.get('title', '').strip().lower()
    if cit_title in acm_titles_set:
        acm_citations.append(cit)
        total_citations += int(cit.get('citation_count', 0))

avg_citation = total_citations / len(acm_citations) if acm_citations else 0

result = f"The average citation count for papers published by ACM cited in 2018 is {avg_citation:.2f}, based on {len(acm_citations)} ACM papers."

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
