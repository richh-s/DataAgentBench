code = """import json, re
from statistics import mean

# Load citations
with open(var_call_Dv0qLBd55QRuURx8AQoPniwM, 'r') as f:
    citations = json.load(f)

# Build a set of titles cited in 2018
cited_titles_2018 = {c['title'] for c in citations}

# Load paper docs
with open(var_call_6fBjV4fvOmzHPjtbTGb0dDLj, 'r') as f:
    docs = json.load(f)

# Helper to detect ACM source from text
def is_acm(text):
    if not isinstance(text, str):
        return False
    return 'copyright' in text.lower() and 'acm' in text[:500].lower()

# Map filename (without .txt) to whether it's ACM
acm_titles = set()
for d in docs:
    fname = d.get('filename','')
    title = fname[:-4] if fname.lower().endswith('.txt') else fname
    if title in cited_titles_2018 and is_acm(d.get('text','')):
        acm_titles.add(title)

# Compute average citation count for ACM papers cited in 2018
counts = [int(c['citation_count']) for c in citations if c['title'] in acm_titles]
avg = mean(counts) if counts else 0

result = avg

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Dv0qLBd55QRuURx8AQoPniwM': 'file_storage/call_Dv0qLBd55QRuURx8AQoPniwM.json', 'var_call_6fBjV4fvOmzHPjtbTGb0dDLj': 'file_storage/call_6fBjV4fvOmzHPjtbTGb0dDLj.json'}

exec(code, env_args)
