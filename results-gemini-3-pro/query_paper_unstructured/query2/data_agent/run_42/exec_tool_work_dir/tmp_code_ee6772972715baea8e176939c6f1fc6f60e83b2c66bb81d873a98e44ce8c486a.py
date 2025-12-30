code = """import json

# Load citations
with open(locals()['var_function-call-7375441648498366517'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-12252996319457097106'], 'r') as f:
    paper_docs_data = json.load(f)

citation_titles = set(item['title'] for item in citations_data)

acm_count = 0
ieee_count = 0
total_cited_docs = 0

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    title = filename[:-4]
    
    if title in citation_titles:
        total_cited_docs += 1
        text = doc.get('text', '')
        header = text[:5000]
        
        if "ACM" in header:
            acm_count += 1
        if "IEEE" in header:
            ieee_count += 1

print("__RESULT__:")
print(json.dumps({"total_cited_docs": total_cited_docs, "acm_count": acm_count, "ieee_count": ieee_count}))"""

env_args = {'var_function-call-7375441648498366517': 'file_storage/function-call-7375441648498366517.json', 'var_function-call-12252996319457097106': 'file_storage/function-call-12252996319457097106.json', 'var_function-call-15387915071709340266': 68.5}

exec(code, env_args)
