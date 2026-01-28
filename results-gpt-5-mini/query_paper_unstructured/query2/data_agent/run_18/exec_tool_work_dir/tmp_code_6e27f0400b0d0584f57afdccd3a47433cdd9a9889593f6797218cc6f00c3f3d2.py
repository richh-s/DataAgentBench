code = """import json, statistics

# Load data from previous tool calls; variables are provided in the environment
# var_call_obqeqRc1ZIU04e5Xf5am4w4R and var_call_phJuZ6fnXTcCyj1xMHm7iEUn may be file paths (strings) or lists

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to JSON
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = load_var(var_call_obqeqRc1ZIU04e5Xf5am4w4R)
paper_docs = load_var(var_call_phJuZ6fnXTcCyj1xMHm7iEUn)

# Build set of titles from paper_docs filenames (strip .txt)
acm_titles = set()
for d in paper_docs:
    fn = d.get('filename')
    if not fn:
        continue
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    acm_titles.add(title)

# Filter citations for titles that are in ACM paper titles
counts = []
matched_titles = []
for rec in citations:
    t = rec.get('title')
    cc = rec.get('citation_count')
    if t in acm_titles:
        try:
            cnt = int(cc)
        except Exception:
            try:
                cnt = int(float(cc))
            except Exception:
                continue
        counts.append(cnt)
        matched_titles.append(t)

if counts:
    avg = sum(counts)/len(counts)
    # round to 3 decimals
    avg_rounded = round(avg, 3)
else:
    avg_rounded = None

result = {'average_citation_count': avg_rounded, 'matched_papers_count': len(counts)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bxE2M6VnrNdmZidJ1vjgNg1P': ['paper_docs'], 'var_call_obqeqRc1ZIU04e5Xf5am4w4R': 'file_storage/call_obqeqRc1ZIU04e5Xf5am4w4R.json', 'var_call_phJuZ6fnXTcCyj1xMHm7iEUn': 'file_storage/call_phJuZ6fnXTcCyj1xMHm7iEUn.json'}

exec(code, env_args)
