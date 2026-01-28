code = """import json
import statistics

# Load full citations data from file
with open(var_call_QWHQ82Emz8zubmoQldSpPFDO, 'r') as f:
    citations = json.load(f)

# Load full paper docs data from file
with open(var_call_lgjYEzSB3OooNmluBYJdSb1C, 'r') as f:
    docs = json.load(f)

# Build a mapping from title to whether the paper is ACM (source == 'ACM')
acm_titles = set()
for doc in docs:
    text = doc.get('text', '')
    # Heuristic: if 'ACM' appears near copyright/permission lines, treat as ACM source
    if 'Copyright' in text and 'ACM' in text:
        # title is filename without .txt
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        acm_titles.add(title)

# Collect citation counts for ACM papers cited in 2018
acm_citation_counts = []
for row in citations:
    title = row.get('title')
    if title in acm_titles:
        try:
            count = int(row.get('citation_count'))
        except (TypeError, ValueError):
            continue
        acm_citation_counts.append(count)

if acm_citation_counts:
    avg_citations = statistics.mean(acm_citation_counts)
else:
    avg_citations = None

result = json.dumps(avg_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_QWHQ82Emz8zubmoQldSpPFDO': 'file_storage/call_QWHQ82Emz8zubmoQldSpPFDO.json', 'var_call_lgjYEzSB3OooNmluBYJdSb1C': 'file_storage/call_lgjYEzSB3OooNmluBYJdSb1C.json'}

exec(code, env_args)
