code = """import json
import pandas as pd

with open(locals()['var_function-call-15304272311676446797'], 'r') as f:
    paper_docs = json.load(f)

start_markers = ["author keywords", "index terms", "keywords"]
end_markers = ["acm classification", "introduction", "abstract", "general terms", "categories and subject"]

debug_info = []
matches = 0

for doc in paper_docs:
    text = doc.get('text', '').lower()
    
    found_start = -1
    for sm in start_markers:
        idx = text.find(sm)
        if idx != -1:
            found_start = idx
            break
            
    domain_text = ""
    if found_start != -1:
        start_search = found_start + 20 # Skip the marker itself roughly
        best_end = len(text)
        found_end = False
        for em in end_markers:
            idx = text.find(em, start_search)
            if idx != -1 and idx < best_end:
                best_end = idx
                found_end = True
        
        if not found_end:
            best_end = min(len(text), start_search + 500)
            
        domain_text = text[found_start:best_end]
        if "food" in domain_text:
            matches += 1
            
    debug_info.append(domain_text[:100])

print("__RESULT__:")
print(json.dumps({
    "matches_count": matches,
    "first_5_domains": debug_info[:5],
    "total_docs": len(paper_docs)
}))"""

env_args = {'var_function-call-1526931378206999654': 'file_storage/function-call-1526931378206999654.json', 'var_function-call-1526931378207000783': 'file_storage/function-call-1526931378207000783.json', 'var_function-call-15304272311676446797': 'file_storage/function-call-15304272311676446797.json', 'var_function-call-11626738571080925771': 0}

exec(code, env_args)
