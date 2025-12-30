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
        if len(headers) < 20:
            txt_preview = paper.get('text', '')[:150]
            headers.append({'title': title, 'header': txt_preview})

result_data = {
    'matched_count': matched_count,
    'samples': headers
}

print("__RESULT__:")
print(json.dumps(result_data))"""

env_args = {'var_function-call-14258248544266261240': 'file_storage/function-call-14258248544266261240.json', 'var_function-call-14258248544266263107': 'file_storage/function-call-14258248544266263107.json', 'var_function-call-18048887829581669547': 'file_storage/function-call-18048887829581669547.json', 'var_function-call-15377559382259389158': 0, 'var_function-call-8390217922804451433': 'Done'}

exec(code, env_args)
