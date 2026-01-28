code = """import json
# Load the MongoDB query result stored in a file path variable
p = var_call_tsvwQGwqYQamcPNiDCUWMjwf
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# Extract filenames, strip .txt
titles = []
for d in docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        titles.append(fn[:-4])
    else:
        titles.append(fn)
# Deduplicate
titles = sorted(list(dict.fromkeys(titles)))
import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_tLa43TtWacLVmw6hQCvEOaoS': ['paper_docs'], 'var_call_tsvwQGwqYQamcPNiDCUWMjwf': 'file_storage/call_tsvwQGwqYQamcPNiDCUWMjwf.json'}

exec(code, env_args)
