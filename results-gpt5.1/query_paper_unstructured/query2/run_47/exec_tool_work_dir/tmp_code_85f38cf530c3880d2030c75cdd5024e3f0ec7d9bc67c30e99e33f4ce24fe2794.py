code = """import json, re

# Load full citations result
path = var_call_S7z9w3BrERVsGPrcnjI454c1
with open(path, 'r') as f:
    citations = json.load(f)

# Build a set of titles cited in 2018
cited_titles_2018 = {rec['title'] for rec in citations}

# Load full paper docs result
path_docs = var_call_4JydZyY1BVYpeqHKZpkc3LHp
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Regex to detect ACM in text (publisher/source)
acm_pattern = re.compile(r"\bACM\b", re.IGNORECASE)

# Map filename (without .txt) to whether it's ACM
acm_titles = set()
for doc in docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    if acm_pattern.search(text):
        acm_titles.add(title)

# Filter citations to those whose titles are ACM papers
acm_citations_2018 = [rec for rec in citations if rec['title'] in acm_titles]

# Compute average citation_count
if acm_citations_2018:
    counts = [int(rec['citation_count']) for rec in acm_citations_2018]
    avg = sum(counts) / len(counts)
else:
    avg = None

result = avg

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_S7z9w3BrERVsGPrcnjI454c1': 'file_storage/call_S7z9w3BrERVsGPrcnjI454c1.json', 'var_call_4JydZyY1BVYpeqHKZpkc3LHp': 'file_storage/call_4JydZyY1BVYpeqHKZpkc3LHp.json'}

exec(code, env_args)
