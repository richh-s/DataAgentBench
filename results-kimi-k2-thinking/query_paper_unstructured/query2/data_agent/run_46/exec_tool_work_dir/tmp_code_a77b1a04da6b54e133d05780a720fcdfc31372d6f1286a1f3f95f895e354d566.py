code = """import json

# Access the citations data for 2018 from stored variables
citations_2018 = locals()['var_functions.query_db:0']

# Access the paper documents data from stored variables
paper_docs = locals()['var_functions.query_db:2']

# Check if these are file paths (strings) or actual data
if isinstance(citations_2018, str) and citations_2018.endswith('.json'):
    with open(citations_2018, 'r') as f:
        citations_2018 = json.load(f)

if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

# Process data
print('Number of citations in 2018: ' + str(len(citations_2018)))
print('Number of paper documents: ' + str(len(paper_docs)))

# Create title to document mapping
title_to_doc = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename:
        # Remove .txt extension to get title
        title = filename.replace('.txt', '')
        title_to_doc[title] = doc

# Check first few mappings
sample_titles = list(title_to_doc.keys())[:3]
print('Sample titles from documents:')
for t in sample_titles:
    print('  ' + t)

# Check if citation titles match
matched = 0
unmatched = 0
for citation in citations_2018[:10]:
    cit_title = citation.get('title', '')
    if cit_title in title_to_doc:
        matched += 1
        print('MATCHED: ' + cit_title[:50])
    else:
        unmatched += 1
        print('UNMATCHED: ' + cit_title[:50])

print('Matched: ' + str(matched) + ', Unmatched: ' + str(unmatched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
