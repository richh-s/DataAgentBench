code = """import json

# Load citations
file_path_cit = locals()['var_function-call-17666330447833607191']
with open(file_path_cit, 'r') as f:
    citations_list = json.load(f)

# Create citation map: title -> citation_count (convert to int)
citation_map = {c['title']: int(c['citation_count']) for c in citations_list}

# Load paper docs
file_path_docs = locals()['var_function-call-3540073977128497152']
with open(file_path_docs, 'r') as f:
    docs = json.load(f)

# Filter ACM papers
acm_citations = []
for doc in docs:
    title = doc['filename'].replace('.txt', '')
    if title in citation_map:
        text = doc.get('text', '')
        # Check for ACM
        is_acm = False
        if "© ACM" in text:
            is_acm = True
        elif "permissions@acm.org" in text:
            is_acm = True
        elif "Association for Computing Machinery" in text:
            is_acm = True
        elif "Copyright" in text and "ACM" in text:
             is_acm = True
        
        if is_acm:
            acm_citations.append(citation_map[title])

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-17666330447833607191': 'file_storage/function-call-17666330447833607191.json', 'var_function-call-11031819639720739797': 'file_storage/function-call-11031819639720739797.json', 'var_function-call-11580890549591616551': 158, 'var_function-call-15015239705628452412': 'file_storage/function-call-15015239705628452412.json', 'var_function-call-12301809577552988153': 'file_storage/function-call-12301809577552988153.json', 'var_function-call-291982586650051971': 'file_storage/function-call-291982586650051971.json', 'var_function-call-7820464138049076348': 5, 'var_function-call-3540073977128497152': 'file_storage/function-call-3540073977128497152.json'}

exec(code, env_args)
