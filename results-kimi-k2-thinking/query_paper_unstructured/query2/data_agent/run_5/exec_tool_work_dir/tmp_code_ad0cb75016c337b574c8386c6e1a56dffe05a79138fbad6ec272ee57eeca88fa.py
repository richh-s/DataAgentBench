code = """import json
import re

# Load citations data for 2018
citations_file = var_functions.query_db_4
citations_2018 = []
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load paper documents
paper_docs_file = var_functions.query_db_5
paper_docs = []
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

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

avg_citation = total_citations / len(acm_citations) if acm_citations else None

result = {
    "average_citation_count": avg_citation,
    "num_acm_papers_cited_in_2018": len(acm_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
