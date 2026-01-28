code = """import json

citations_path = locals()['var_function-call-13908298438428433880']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# check for 0s
zeros = 0
for item in citations_data:
    if int(item['citation_count']) == 0:
        zeros += 1
print(f"Zeros in citation data: {zeros}")

# Recalculate everything
citation_map = {item['title']: int(item['citation_count']) for item in citations_data if int(item['citation_count']) > 0}

papers_path = locals()['var_function-call-13272072186750426102']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

acm_counts = []

for p in papers_data:
    title = p['filename'].replace('.txt', '')
    if title not in citation_map:
        continue
    
    text_head = p['text'][:5000]
    
    # Logic from before
    is_acm = False
    if "Association for Computing Machinery" in text_head:
        is_acm = True
    elif "ACM" in text_head:
        if "Copyright" in text_head or "Permission" in text_head or "Classification Keywords" in text_head:
            is_acm = True
            
    # Check IEEE
    if "IEEE" in text_head and "©" in text_head:
         # simple heuristic, if IEEE is present with copyright symbol, it's likely IEEE
         # But need to be careful not to exclude ACM papers that mention IEEE.
         # However, usually the copyright line is unique.
         # If "Copyright ... ACM" is present, it's ACM.
         if "Copyright" in text_head and "ACM" in text_head:
             is_acm = True
         elif "Copyright" in text_head and "IEEE" in text_head:
             is_acm = False # It's IEEE

    if is_acm:
        acm_counts.append(citation_map[title])

if not acm_counts:
    res = 0
else:
    res = sum(acm_counts) / len(acm_counts)

print(f"Sum: {sum(acm_counts)}")
print(f"Count: {len(acm_counts)}")
print(f"Avg: {res}")
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-13908298438428433880': 'file_storage/function-call-13908298438428433880.json', 'var_function-call-13908298438428430929': 'file_storage/function-call-13908298438428430929.json', 'var_function-call-17064019482965131703': 'file_storage/function-call-17064019482965131703.json', 'var_function-call-13272072186750426102': 'file_storage/function-call-13272072186750426102.json', 'var_function-call-5520325511212738459': 68.5, 'var_function-call-15154583783909403440': 50.0, 'var_function-call-13439012975967068817': 68.5}

exec(code, env_args)
