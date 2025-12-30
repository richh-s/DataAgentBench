code = """import json

# Load citations
file_path_cit = locals()['var_function-call-17666330447833607191']
with open(file_path_cit, 'r') as f:
    citations_list = json.load(f)

citation_map = {c['title']: int(c['citation_count']) for c in citations_list}

# Load paper docs
file_path_docs = locals()['var_function-call-3540073977128497152']
with open(file_path_docs, 'r') as f:
    docs = json.load(f)

acm_citations = []
total_found = 0
for doc in docs:
    title = doc['filename'].replace('.txt', '')
    if title in citation_map:
        total_found += 1
        text = doc.get('text', '')
        # Check for ACM
        is_acm = False
        # Strict checks
        if "permissions@acm.org" in text:
            is_acm = True
        elif "© ACM" in text:
            is_acm = True
        elif "Association for Computing Machinery" in text:
             # Check if it's in the header/footer area? 
             # Or just trust it.
             is_acm = True
        
        # Check "Copyright" and "ACM" proximity?
        # A simple "Copyright" ... "ACM" check might be too loose if "ACM" is far away.
        # But let's assume if the strict checks fail, we might look for "Copyright 20.. ACM"
        
        if not is_acm and "Copyright" in text and "ACM" in text:
            # Let's see if they are somewhat close.
            # This is hard without regex or detailed parsing.
            # But the previous run used this loose check.
            is_acm = True

        if is_acm:
            acm_citations.append(citation_map[title])

print("__RESULT__:")
print(json.dumps({"total_cited_papers": len(citation_map), "papers_found_in_docs": total_found, "acm_papers_count": len(acm_citations), "avg": sum(acm_citations)/len(acm_citations) if acm_citations else 0}))"""

env_args = {'var_function-call-17666330447833607191': 'file_storage/function-call-17666330447833607191.json', 'var_function-call-11031819639720739797': 'file_storage/function-call-11031819639720739797.json', 'var_function-call-11580890549591616551': 158, 'var_function-call-15015239705628452412': 'file_storage/function-call-15015239705628452412.json', 'var_function-call-12301809577552988153': 'file_storage/function-call-12301809577552988153.json', 'var_function-call-291982586650051971': 'file_storage/function-call-291982586650051971.json', 'var_function-call-7820464138049076348': 5, 'var_function-call-3540073977128497152': 'file_storage/function-call-3540073977128497152.json', 'var_function-call-16924924423564672170': 60.092592592592595}

exec(code, env_args)
