code = """import json

# Load citations result
with open(locals()['var_function-call-1269001259179698706'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs result
with open(locals()['var_function-call-1269001259179697405'], 'r') as f:
    paper_docs = json.load(f)

citation_map = {item['title']: item['citation_count'] for item in citations_data}

acm_count = 0
ieee_count = 0
pubmed_count = 0
both_count = 0
total_matched = 0

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    if title in citation_map:
        text = doc.get('text', '')
        is_acm = "ACM" in text
        is_ieee = "IEEE" in text
        is_pubmed = "PubMed" in text
        
        if is_acm: acm_count += 1
        if is_ieee: ieee_count += 1
        if is_pubmed: pubmed_count += 1
        if is_acm and is_ieee: both_count += 1
        total_matched += 1

print("__RESULT__:")
print(json.dumps({
    "total_matched_papers_2018": total_matched,
    "acm_count": acm_count,
    "ieee_count": ieee_count,
    "pubmed_count": pubmed_count,
    "acm_and_ieee_overlap": both_count
}))"""

env_args = {'var_function-call-1269001259179698706': 'file_storage/function-call-1269001259179698706.json', 'var_function-call-1269001259179697405': 'file_storage/function-call-1269001259179697405.json', 'var_function-call-10709454489142440522': 68.5}

exec(code, env_args)
