code = """import json, re
from statistics import mean

# Load citation data
path_citations = var_call_1dGpRNO2DkhNAt4CrcgNogyD
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Build set of titles cited in 2018
titles_2018 = {c['title'] for c in citations}

# Load paper docs
path_docs = var_call_Fc07nxdgccs5zWtQME05BLbc
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Helper to detect ACM source
acm_titles = set()
for d in docs:
    text = d.get('text','')
    # Heuristic: look for 'ACM' near copyright/permission lines
    if re.search(r'Copyright\s+\d{4}.*ACM', text, re.IGNORECASE) or 'Association for Computing Machinery' in text:
        # Derive title from filename (strip .txt)
        fn = d.get('filename','')
        if fn.lower().endswith('.txt'):
            title = fn[:-4]
        else:
            title = fn
        if title in titles_2018:
            acm_titles.add(title)

# Compute average citation count for these ACM papers in 2018
acm_citations = [int(c['citation_count']) for c in citations if c['title'] in acm_titles]

avg_citations = mean(acm_citations) if acm_citations else None

res = avg_citations

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_1dGpRNO2DkhNAt4CrcgNogyD': 'file_storage/call_1dGpRNO2DkhNAt4CrcgNogyD.json', 'var_call_Fc07nxdgccs5zWtQME05BLbc': 'file_storage/call_Fc07nxdgccs5zWtQME05BLbc.json'}

exec(code, env_args)
