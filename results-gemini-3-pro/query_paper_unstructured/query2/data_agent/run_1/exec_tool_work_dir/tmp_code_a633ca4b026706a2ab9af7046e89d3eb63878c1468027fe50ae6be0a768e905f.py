code = """import json

# Load citations result
with open(locals()['var_function-call-1269001259179698706'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs result (using the one from the count query as it might be larger or same)
# Actually, let's use the first one, assuming they are the same if the second one didn't error.
# But better use the most recent one if it might have more data?
# The preview of the second one started with the same doc.
# Let's use the second one just in case.
with open(locals()['var_function-call-3176844419962824888'], 'r') as f:
    paper_docs = json.load(f)

citation_map = {item['title']: item['citation_count'] for item in citations_data}

matched_info = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    if title in citation_map:
        text = doc.get('text', '')
        is_acm = "ACM" in text
        is_ieee = "IEEE" in text
        matched_info.append({
            "title": title,
            "citations": citation_map[title],
            "is_acm": is_acm,
            "is_ieee": is_ieee
        })

print("__RESULT__:")
print(json.dumps(matched_info))"""

env_args = {'var_function-call-1269001259179698706': 'file_storage/function-call-1269001259179698706.json', 'var_function-call-1269001259179697405': 'file_storage/function-call-1269001259179697405.json', 'var_function-call-10709454489142440522': 68.5, 'var_function-call-910537287014842228': {'total_matched_papers_2018': 2, 'acm_count': 2, 'ieee_count': 1, 'pubmed_count': 0, 'acm_and_ieee_overlap': 1}, 'var_function-call-3176844419962824888': 'file_storage/function-call-3176844419962824888.json'}

exec(code, env_args)
