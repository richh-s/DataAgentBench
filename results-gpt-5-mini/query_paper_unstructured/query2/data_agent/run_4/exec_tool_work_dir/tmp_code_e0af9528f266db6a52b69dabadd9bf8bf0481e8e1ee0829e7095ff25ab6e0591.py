code = """import json
import math

# Load data from previous tool call results (file paths provided in variables)
with open(var_call_8XYU59SmifdXyJhWletqgtiA, 'r') as f:
    citations = json.load(f)
with open(var_call_Dsdvmyx7tVnG2UjZCdCj7LDL, 'r') as f:
    acm_files = json.load(f)

# Build set of ACM paper titles (filename without .txt)
acm_titles = set()
for doc in acm_files:
    fn = doc.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    acm_titles.add(title)

# Filter citations for citation_year 2018 already done in query; now match titles to ACM titles
matched_counts = []
for rec in citations:
    title = rec.get('title')
    cc = rec.get('citation_count')
    if title in acm_titles:
        try:
            num = int(cc)
            matched_counts.append(num)
        except Exception:
            # skip non-integer citation counts
            pass

if len(matched_counts) > 0:
    avg = sum(matched_counts) / len(matched_counts)
    avg_rounded = round(avg, 4)
else:
    avg_rounded = None

result = {
    'average_citation_count': avg_rounded,
    'matched_paper_count': len(matched_counts)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8XYU59SmifdXyJhWletqgtiA': 'file_storage/call_8XYU59SmifdXyJhWletqgtiA.json', 'var_call_Dsdvmyx7tVnG2UjZCdCj7LDL': 'file_storage/call_Dsdvmyx7tVnG2UjZCdCj7LDL.json'}

exec(code, env_args)
