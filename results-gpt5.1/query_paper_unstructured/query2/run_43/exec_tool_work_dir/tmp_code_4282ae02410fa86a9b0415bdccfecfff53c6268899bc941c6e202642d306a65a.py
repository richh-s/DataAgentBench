code = """import json
import re

# Load previous results
import_path_citations = var_call_Aqc0yvLzi0hmiuL3UjpZUnGf
import_path_docs = var_call_Bn2rBecjDXR0tetokdk8l8Rz

with open(import_path_citations, 'r') as f:
    citations = json.load(f)
with open(import_path_docs, 'r') as f:
    docs = json.load(f)

# Build mapping from title to source by parsing text for 'Copyright' line
source_by_title = {}
for d in docs:
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = d.get('text','')
    m = re.search(r'Copyright\s+\d{4}\s+\xa9\s+([^\n]+)', text)
    source = None
    if m:
        line = m.group(1)
        if 'ACM' in line:
            source = 'ACM'
        elif 'IEEE' in line:
            source = 'IEEE'
        elif 'PubMed' in line:
            source = 'PubMed'
    # fallback: look for 'Permission to make digital or hard copies' and 'ACM'
    if source is None and 'ACM' in text:
        source = 'ACM'
    if source:
        source_by_title[title] = source

# Filter citation records for ACM papers
counts = []
for c in citations:
    title = c.get('title','')
    source = source_by_title.get(title)
    if source == 'ACM':
        try:
            cnt = int(c.get('citation_count',0))
            counts.append(cnt)
        except Exception:
            pass

avg = sum(counts)/len(counts) if counts else None

result = {"average_citation_count_acm_2018": avg, "num_papers": len(counts)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Aqc0yvLzi0hmiuL3UjpZUnGf': 'file_storage/call_Aqc0yvLzi0hmiuL3UjpZUnGf.json', 'var_call_Bn2rBecjDXR0tetokdk8l8Rz': 'file_storage/call_Bn2rBecjDXR0tetokdk8l8Rz.json'}

exec(code, env_args)
