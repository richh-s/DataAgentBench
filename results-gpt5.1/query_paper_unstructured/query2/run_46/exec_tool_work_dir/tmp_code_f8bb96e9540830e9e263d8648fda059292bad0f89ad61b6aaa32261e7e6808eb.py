code = """import json, statistics, re

# Load citation records for 2018
path = var_call_vU2xuhl0JVlWNL5NjVjHBA9p
with open(path, 'r') as f:
    citations_2018 = json.load(f)

# Load paper docs
path_docs = var_call_LAtIsnB0LU4o1xf9lCJkWV6Y
with open(path_docs, 'r') as f:
    paper_docs = json.load(f)

# Build a mapping from title to source by parsing text for 'Copyright' lines mentioning ACM
source_by_title = {}
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # look for lines with 'Copyright' and 'ACM'
    is_acm = False
    for line in text.split('\n'):
        if 'Copyright' in line and 'ACM' in line:
            is_acm = True
            break
        if 'Permission to make digital or hard copies' in line and 'ACM' in line:
            is_acm = True
            break
    if is_acm:
        source_by_title[title] = 'ACM'

# Collect citation counts for ACM papers cited in 2018
acm_citations = []
for rec in citations_2018:
    title = rec['title']
    if source_by_title.get(title) == 'ACM':
        try:
            c = int(rec['citation_count'])
        except Exception:
            continue
        acm_citations.append(c)

avg_citations = statistics.mean(acm_citations) if acm_citations else None

result = json.dumps({'average_citation_count_acm_2018': avg_citations, 'num_papers': len(acm_citations)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_vU2xuhl0JVlWNL5NjVjHBA9p': 'file_storage/call_vU2xuhl0JVlWNL5NjVjHBA9p.json', 'var_call_LAtIsnB0LU4o1xf9lCJkWV6Y': 'file_storage/call_LAtIsnB0LU4o1xf9lCJkWV6Y.json'}

exec(code, env_args)
