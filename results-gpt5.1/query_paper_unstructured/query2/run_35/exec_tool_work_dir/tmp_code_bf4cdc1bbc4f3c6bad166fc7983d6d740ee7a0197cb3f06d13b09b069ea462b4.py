code = """import json
import re

# Load full citations result
with open(var_call_HUuDAWoPpFcpGRsBOhUgF43Y, 'r') as f:
    citations = json.load(f)

# Build a mapping from title to source extracted from text (ACM or not)
acm_titles = set()
for doc in var_call_OjIrb6vE2Epul199hrQH7Ssl:
    text = doc.get('text', '')
    # Heuristic: if 'Permission to make digital or hard copies' and 'ACM' near copyright, mark as ACM
    if 'Permission  to  make  digital  or  hard  copies' in text and 'ACM' in text[:5000]:
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        acm_titles.add(title)

# Filter citations for ACM titles
acm_citations_2018 = [int(rec['citation_count']) for rec in citations if rec['title'] in acm_titles]

if acm_citations_2018:
    avg_citations = sum(acm_citations_2018) / len(acm_citations_2018)
else:
    avg_citations = None

result = avg_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HUuDAWoPpFcpGRsBOhUgF43Y': 'file_storage/call_HUuDAWoPpFcpGRsBOhUgF43Y.json', 'var_call_eGWI3bjJTXm0JnpfGMbjV4Pf': ['paper_docs'], 'var_call_OjIrb6vE2Epul199hrQH7Ssl': 'file_storage/call_OjIrb6vE2Epul199hrQH7Ssl.json'}

exec(code, env_args)
