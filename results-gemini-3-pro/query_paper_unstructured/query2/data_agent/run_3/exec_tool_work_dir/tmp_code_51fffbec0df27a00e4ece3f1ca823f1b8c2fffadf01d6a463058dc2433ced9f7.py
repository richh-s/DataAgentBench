code = """import json

# Load Citations (already filtered for 2018)
citations_file = locals()['var_function-call-6465728011897823689']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load Papers
papers_file = locals()['var_function-call-10268579578650844668']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Build map of ACM papers
# We assume a paper is published by ACM if "ACM" appears in the first 3000 characters
# This covers headers, footers, copyright notices, etc. on the first page.
acm_titles = set()
for p in papers_data:
    text_head = p['text'][:5000] # Check first 5000 chars
    if "ACM" in text_head or "Association for Computing Machinery" in text_head:
        # Extract title
        title = p['filename']
        if title.endswith('.txt'):
            title = title[:-4]
        acm_titles.add(title)

# Filter citations
counts = []
for c in citations_data:
    if c['title'] in acm_titles:
        # c['citation_count'] might be string or int in the JSON result, SQL usually returns int but sometimes tools wrap in str
        # Looking at preview: "citation_count": "95" -> it is a string.
        try:
            cnt = int(c['citation_count'])
            counts.append(cnt)
        except ValueError:
            continue

# Calculate Average
if counts:
    avg = sum(counts) / len(counts)
else:
    avg = 0.0

print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-6465728011897823689': 'file_storage/function-call-6465728011897823689.json', 'var_function-call-10268579578650844668': 'file_storage/function-call-10268579578650844668.json'}

exec(code, env_args)
