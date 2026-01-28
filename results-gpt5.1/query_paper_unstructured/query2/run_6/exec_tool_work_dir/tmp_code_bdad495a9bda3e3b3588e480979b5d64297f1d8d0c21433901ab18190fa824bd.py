code = """import json, statistics, re

# Load citations data for 2018
with open(var_call_zyNrT0DpCRmonlBsJF4eM5Kk, 'r') as f:
    citations_2018 = json.load(f)

# Build a quick lookup of titles cited in 2018 (set)
titles_2018 = {rec['title'] for rec in citations_2018}

# Load paper docs
with open(var_call_NiLUAPCX7h5nKpOBr8oeprlW, 'r') as f:
    paper_docs = json.load(f)

# Helper to infer source from text
def infer_source(text):
    # Look for ACM or IEEE near copyright/permission lines
    text_upper = text.upper()
    if 'COPYRIGHT' in text_upper and 'ACM' in text_upper:
        return 'ACM'
    if 'ASSOCIATION FOR COMPUTING MACHINERY' in text_upper:
        return 'ACM'
    if 'IEEE' in text_upper:
        return 'IEEE'
    if 'PUBMED' in text_upper:
        return 'PubMed'
    return None

# Map title -> source
title_to_source = {}
for doc in paper_docs:
    filename = doc.get('filename','')
    title = re.sub(r"\.txt$","", filename)
    if title in titles_2018:
        source = infer_source(doc.get('text',''))
        title_to_source[title] = source

# Filter citations to only ACM-sourced papers
acm_citations = [int(rec['citation_count']) for rec in citations_2018 if title_to_source.get(rec['title']) == 'ACM']

if acm_citations:
    avg_citations = statistics.mean(acm_citations)
else:
    avg_citations = None

result = json.dumps({'average_citation_count_acm_2018': avg_citations})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_zyNrT0DpCRmonlBsJF4eM5Kk': 'file_storage/call_zyNrT0DpCRmonlBsJF4eM5Kk.json', 'var_call_NiLUAPCX7h5nKpOBr8oeprlW': 'file_storage/call_NiLUAPCX7h5nKpOBr8oeprlW.json'}

exec(code, env_args)
