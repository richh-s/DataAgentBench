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
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    if title in citation_titles:
        matched_count += 1
        if len(headers) < 20:
            headers.append(f"Title: {title}\nHeader: {paper.get('text', '')[:200]}")

print(f"DEBUG: Total papers matched with citations: {matched_count}")
print("DEBUG: Sample Headers:")
for h in headers:
    print(h)
    print("-" * 20)

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-14258248544266261240': 'file_storage/function-call-14258248544266261240.json', 'var_function-call-14258248544266263107': 'file_storage/function-call-14258248544266263107.json', 'var_function-call-18048887829581669547': 'file_storage/function-call-18048887829581669547.json', 'var_function-call-15377559382259389158': 0}

exec(code, env_args)
