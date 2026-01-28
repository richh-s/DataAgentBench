code = """import json, re

# Load data from previous tool results stored as file paths
with open(var_call_apVXBIziHB2S37dj0884dIbm, 'r') as f:
    citations = json.load(f)
with open(var_call_qBw4mKr8liYBbia9C9Up9ePq, 'r') as f:
    docs = json.load(f)

# Build mapping from title (filename without .txt) to text
doc_map = {}
for d in docs:
    fn = d.get('filename', '')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    doc_map[title] = d.get('text', '')

# Prepare pattern to detect CHI venue mentions
chi_pattern = re.compile(r"\bCHI\b", re.I)

chi_papers = []
total = 0

for entry in citations:
    title = entry.get('title')
    # normalize citation_count to int
    cc_raw = entry.get('citation_count', 0)
    try:
        cc = int(cc_raw)
    except:
        try:
            cc = int(float(cc_raw))
        except:
            cc = 0
    # find corresponding doc
    text = doc_map.get(title)
    if text:
        text_upper = text.upper()
        if chi_pattern.search(text) or 'SIGCHI' in text_upper:
            chi_papers.append({'title': title, 'citation_count': cc})
            total += cc

# Sort papers by citation_count descending
chi_papers.sort(key=lambda x: x['citation_count'], reverse=True)

result = {'papers': chi_papers, 'total_citations_2020': total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_apVXBIziHB2S37dj0884dIbm': 'file_storage/call_apVXBIziHB2S37dj0884dIbm.json', 'var_call_qBw4mKr8liYBbia9C9Up9ePq': 'file_storage/call_qBw4mKr8liYBbia9C9Up9ePq.json'}

exec(code, env_args)
