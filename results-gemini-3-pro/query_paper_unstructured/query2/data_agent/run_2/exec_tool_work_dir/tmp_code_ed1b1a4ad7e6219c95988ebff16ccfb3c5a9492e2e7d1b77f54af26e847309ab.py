code = """import json

citations_path = locals()['var_function-call-13908298438428433880']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citation_map = {item['title']: int(item['citation_count']) for item in citations_data}

papers_path = locals()['var_function-call-13272072186750426102']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

acm_citations = []
ieee_citations = []
debug_titles = []

for p in papers_data:
    title = p['filename'].replace('.txt', '')
    if title not in citation_map:
        continue
        
    text_head = p['text'][:5000] # First page roughly
    
    # Check for ACM
    # Look for "ACM" in close proximity to "Copyright" or "Permission"
    # Or "Association for Computing Machinery"
    is_acm = False
    if "Association for Computing Machinery" in text_head:
        is_acm = True
    elif "ACM" in text_head:
        # Check if it's likely the publisher line
        if "Copyright" in text_head or "Permission" in text_head:
            # This is a bit loose, as "Copyright" could be anywhere.
            # But usually in the header/footer of first page.
            is_acm = True
        elif "ACM Classification Keywords" in text_head:
            is_acm = True
    
    # Check for IEEE
    is_ieee = False
    if "IEEE" in text_head:
        if "Copyright" in text_head or "Permission" in text_head:
             # Heuristic
             pass
        # IEEE papers often say "IEEE" in the header or footer
        # "978-1-.../10/$26.00 ©2010 IEEE"
        if "©" in text_head and "IEEE" in text_head:
            is_ieee = True
        if "©" in text_head and "ieee" in text_head.lower():
            is_ieee = True
            
    # Resolution
    if is_acm and not is_ieee:
        acm_citations.append(citation_map[title])
        debug_titles.append(title)
    elif is_ieee and not is_acm:
        ieee_citations.append(citation_map[title])
    elif is_acm and is_ieee:
        # Ambiguous, check which one appears in copyright line?
        # This is rare.
        # Let's assume if it has ACM keywords, it's ACM.
        acm_citations.append(citation_map[title]) 

print(f"ACM papers: {len(acm_citations)}")
print(f"IEEE papers: {len(ieee_citations)}")
if acm_citations:
    print(f"Avg ACM: {sum(acm_citations)/len(acm_citations)}")
else:
    print("Avg ACM: 0")

print("__RESULT__:")
print(json.dumps(sum(acm_citations)/len(acm_citations) if acm_citations else 0))"""

env_args = {'var_function-call-13908298438428433880': 'file_storage/function-call-13908298438428433880.json', 'var_function-call-13908298438428430929': 'file_storage/function-call-13908298438428430929.json', 'var_function-call-17064019482965131703': 'file_storage/function-call-17064019482965131703.json', 'var_function-call-13272072186750426102': 'file_storage/function-call-13272072186750426102.json', 'var_function-call-5520325511212738459': 68.5, 'var_function-call-15154583783909403440': 50.0}

exec(code, env_args)
