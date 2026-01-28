code = """import json

# Load the two tool results which may be either lists or file paths
pdocs_var = var_call_GbuaTr5ohZU6CckypqvaSnbr
cites_var = var_call_ziZJf93MNCSRgtn202EhbrzI

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to JSON
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

paper_docs = load_var(pdocs_var)
citations = load_var(cites_var)

# Build set of titles for papers whose text contains 'ACM' (we queried that)
acm_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    title = title.strip()
    if title:
        acm_titles.add(title)

# Filter citation records for 2018 (these records are already for 2018)
sum_cites = 0
count = 0
for rec in citations:
    title = rec.get('title')
    if title in acm_titles:
        try:
            cc = int(rec.get('citation_count', 0))
        except:
            try:
                cc = int(float(rec.get('citation_count', 0)))
            except:
                cc = 0
        sum_cites += cc
        count += 1

if count > 0:
    avg = sum_cites / count
    avg_rounded = round(avg, 2)
else:
    avg_rounded = None

output = {'average_citation_count': avg_rounded, 'paper_count': count}

print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print('" + json.dumps(output) + "')")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_GbuaTr5ohZU6CckypqvaSnbr': 'file_storage/call_GbuaTr5ohZU6CckypqvaSnbr.json', 'var_call_ziZJf93MNCSRgtn202EhbrzI': 'file_storage/call_ziZJf93MNCSRgtn202EhbrzI.json'}

exec(code, env_args)
