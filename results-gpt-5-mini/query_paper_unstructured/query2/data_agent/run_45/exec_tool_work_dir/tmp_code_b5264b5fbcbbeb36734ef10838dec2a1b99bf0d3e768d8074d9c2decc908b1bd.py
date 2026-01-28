code = """import json
import math

# Load the large query results from storage files
with open(var_call_FJ2wbF1DU5DTIi9CCpvoS2Up, 'r') as f:
    citations = json.load(f)
with open(var_call_rN8zHDXWX29817x2ic2kWnrC, 'r') as f:
    acm_docs = json.load(f)

# Extract ACM paper titles from filenames by removing .txt
acm_titles = set()
for d in acm_docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        acm_titles.add(fn[:-4])
    else:
        acm_titles.add(fn)

# Filter citations for citation_year=2018 was already applied in the SQL query
# Now select only those whose title is in acm_titles
matched = []
for rec in citations:
    title = rec.get('title')
    if title in acm_titles:
        # clean citation_count
        cc = rec.get('citation_count')
        try:
            cc_int = int(cc)
        except Exception:
            # try stripping non-digits
            s = ''.join(ch for ch in str(cc) if ch.isdigit())
            cc_int = int(s) if s else 0
        matched.append({'title': title, 'citation_count': cc_int})

count = len(matched)
if count > 0:
    total = sum(x['citation_count'] for x in matched)
    average = total / count
    # round to 4 decimal places for clarity
    average = round(average, 4)
else:
    average = None

result = {'average_citation_count': average, 'paper_count': count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3EeV2PRQsKJ39nylNcMJQcFQ': ['paper_docs'], 'var_call_FJ2wbF1DU5DTIi9CCpvoS2Up': 'file_storage/call_FJ2wbF1DU5DTIi9CCpvoS2Up.json', 'var_call_rN8zHDXWX29817x2ic2kWnrC': 'file_storage/call_rN8zHDXWX29817x2ic2kWnrC.json'}

exec(code, env_args)
