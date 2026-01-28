code = """import json

# Load citations
with open(locals()['var_function-call-14258248544266261240'], 'r') as f:
    citations_data = json.load(f)

citation_titles = set(entry['title'] for entry in citations_data)

# Load paper documents
with open(locals()['var_function-call-18048887829581669547'], 'r') as f:
    papers_data = json.load(f)

matched_count = 0
headers = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    if title in citation_titles:
        matched_count += 1
        if len(headers) < 10:
            # use repr to avoid syntax issues with special chars
            txt_preview = paper.get('text', '')[:100]
            headers.append((title, txt_preview))

print('DEBUG MATCH COUNT:', matched_count)
for t, h in headers:
    print('TITLE:', t)
    print('HEADER:', repr(h))
    print('---')

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-14258248544266261240': 'file_storage/function-call-14258248544266261240.json', 'var_function-call-14258248544266263107': 'file_storage/function-call-14258248544266263107.json', 'var_function-call-18048887829581669547': 'file_storage/function-call-18048887829581669547.json', 'var_function-call-15377559382259389158': 0}

exec(code, env_args)
