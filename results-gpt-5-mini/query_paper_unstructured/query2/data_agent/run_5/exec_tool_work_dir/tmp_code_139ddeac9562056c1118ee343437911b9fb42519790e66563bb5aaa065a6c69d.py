code = """import json, os
# Load query results from storage variables
# var_call_miSkNz8p6p7BDfA93znX6uJl : citations query result (maybe path)
# var_call_sVulWUpU30niks3BaBshOK9e : paper_docs query result (maybe path)

def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = load_var(var_call_miSkNz8p6p7BDfA93znX6uJl)
papers = load_var(var_call_sVulWUpU30niks3BaBshOK9e)

# Build set of titles from papers filenames (strip .txt)
titles = set()
for d in papers:
    fn = d.get('filename')
    if not fn:
        continue
    title = fn
    if title.lower().endswith('.txt'):
        title = title[:-4]
    titles.add(title)

# Filter citations to those whose title is in titles
matched = []
for rec in citations:
    t = rec.get('title')
    if t in titles:
        cc = rec.get('citation_count')
        try:
            cc_num = int(cc)
        except Exception:
            try:
                cc_num = int(float(cc))
            except Exception:
                continue
        matched.append(cc_num)

if len(matched) == 0:
    result = {'average_citation_count': None, 'paper_count': 0, 'total_citations': 0}
else:
    total = sum(matched)
    count = len(matched)
    avg = total / count
    # round to 2 decimal places
    avg_rounded = round(avg, 2)
    result = {'average_citation_count': avg_rounded, 'paper_count': count, 'total_citations': total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_miSkNz8p6p7BDfA93znX6uJl': 'file_storage/call_miSkNz8p6p7BDfA93znX6uJl.json', 'var_call_sVulWUpU30niks3BaBshOK9e': 'file_storage/call_sVulWUpU30niks3BaBshOK9e.json'}

exec(code, env_args)
