code = """import json

# Load results from previous tool calls (file paths provided in var_call_8MKnJCANw3bgV7DD6eEy3AZ4 and var_call_P44gbxWE0hqFtue0i58uGKlV)
with open(var_call_8MKnJCANw3bgV7DD6eEy3AZ4, 'r', encoding='utf-8') as f:
    acm_files = json.load(f)
with open(var_call_P44gbxWE0hqFtue0i58uGKlV, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build set of titles from ACM papers (filename without .txt)
acm_titles = set()
for rec in acm_files:
    fn = rec.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    acm_titles.add(title)

# Filter citation records for 2018 to only those whose title is in ACM titles
counts = []
matched_titles = []
for rec in citations:
    title = rec.get('title', '')
    c = rec.get('citation_count', 0)
    try:
        count = int(c)
    except:
        try:
            count = int(float(c))
        except:
            count = 0
    if title in acm_titles:
        counts.append(count)
        matched_titles.append(title)

if len(counts) == 0:
    avg = None
else:
    avg = sum(counts) / len(counts)

result = {
    'average_citation_count': avg,
    'paper_count': len(counts)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_umamt8XAW4bnui7A2aWlW6PZ': ['paper_docs'], 'var_call_5sifspgoDPzyQdGuA8cN4Zw2': ['Citations', 'sqlite_sequence'], 'var_call_8MKnJCANw3bgV7DD6eEy3AZ4': 'file_storage/call_8MKnJCANw3bgV7DD6eEy3AZ4.json', 'var_call_P44gbxWE0hqFtue0i58uGKlV': 'file_storage/call_P44gbxWE0hqFtue0i58uGKlV.json'}

exec(code, env_args)
