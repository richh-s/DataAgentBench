code = """import json

# Get citations data
cit_key = 'var_functions.query_db:2'
cit_data = locals()[cit_key]

if isinstance(cit_data, str) and cit_data.endswith('.json'):
    citations = json.load(open(cit_data))
else:
    citations = cit_data

print('Citations count:', len(citations))
if len(citations) > 0:
    print('Citation keys:', citations[0].keys())

# Get paper docs
paper_key = 'var_functions.query_db:22'
paper_data = locals()[paper_key]

if isinstance(paper_data, str) and paper_data.endswith('.json'):
    paper_docs = json.load(open(paper_data))
else:
    paper_docs = paper_data

print('Papers count:', len(paper_docs))

# Build citation lookup
citation_lookup = {}
for c in citations:
    t = c.get('title', '')
    count = int(c.get('citation_count', 0))
    citation_lookup[t] = citation_lookup.get(t, 0) + count

# Process papers and count food domain citations
food_citations = 0
food_papers = 0

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text_lower = doc.get('text', '').lower()
    
    if 'food' in text_lower or 'eating' in text_lower:
        food_papers += 1
        if title in citation_lookup:
            c_count = citation_lookup[title]
            food_citations += c_count
            print('MATCH:', title[:60], c_count)

print('Total food papers:', food_papers)
print('Total food citations:', food_citations)

result = {'total_citation_count': food_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}}

exec(code, env_args)
