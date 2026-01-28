code = """import json
import os

# Load citations
citations_path = locals()['var_function-call-6953046761647739634']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Filter citations for 2018 and create a lookup
# citations is a list of dicts: [{'title': '...', 'citation_count': '...', 'citation_year': ...?}]
# Wait, the query was SELECT title, citation_count FROM Citations WHERE citation_year = 2018
# So I don't need to filter by year again, assuming the query was correct.
# However, the previous tool output preview shows [{'title': '...', 'citation_count': '95'}, ...]
# It doesn't show citation_year because I didn't select it. But I filtered in SQL.
# So all records in `citations` are for 2018.

citation_map = {}
for c in citations:
    # citation_count might be string or int depending on DB driver. Preview showed string "95".
    try:
        count = int(c['citation_count'])
    except ValueError:
        continue # skip invalid
    citation_map[c['title']] = count

# Load papers
papers_path = locals()['var_function-call-4432525266137560286']
# The file might be large. It contains a list of dicts.
with open(papers_path, 'r') as f:
    papers = json.load(f)

acm_citations = []

for p in papers:
    filename = p.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # remove .txt
    
    if title in citation_map:
        text = p.get('text', '')
        # Check for ACM in the first 3000 characters
        header_text = text[:3000]
        if "ACM" in header_text:
            acm_citations.append(citation_map[title])

if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-6953046761647739634': 'file_storage/function-call-6953046761647739634.json', 'var_function-call-6953046761647740005': 'file_storage/function-call-6953046761647740005.json', 'var_function-call-4432525266137560286': 'file_storage/function-call-4432525266137560286.json'}

exec(code, env_args)
