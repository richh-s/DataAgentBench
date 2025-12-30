code = """import json

# Load citations
citations_file = locals()['var_function-call-9715954784429857973']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Create a lookup for citation counts of 2018
citation_map = {}
for item in citations_data:
    title = item['title']
    try:
        count = int(item['citation_count'])
        citation_map[title] = count
    except ValueError:
        pass

# Load papers
papers_file = locals()['var_function-call-14503802819118445045']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

acm_citation_counts = []
titles_found = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # remove .txt
    
    if title in citation_map:
        text = paper.get('text', '')
        # Check for ACM in the first 5000 characters to detect publisher
        header = text[:5000]
        if "ACM" in header:
            acm_citation_counts.append(citation_map[title])
            titles_found.append(title)

if not acm_citation_counts:
    result = 0.0
else:
    result = sum(acm_citation_counts) / len(acm_citation_counts)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9715954784429857973': 'file_storage/function-call-9715954784429857973.json', 'var_function-call-10423341774805533385': 'file_storage/function-call-10423341774805533385.json', 'var_function-call-14503802819118445045': 'file_storage/function-call-14503802819118445045.json'}

exec(code, env_args)
