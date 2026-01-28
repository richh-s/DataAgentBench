code = """import json
import re

# Load data
with open(locals()['var_function-call-17971925795973344162'], 'r') as f:
    docs = json.load(f)

with open(locals()['var_function-call-17971925795973342135'], 'r') as f:
    citations = json.load(f)

food_titles = []
debug_info = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # robust extraction
    # find start
    start_idx = -1
    for kw_header in ["Author Keywords", "Keywords", "Index Terms"]:
        idx = text.find(kw_header)
        if idx != -1:
            start_idx = idx
            break
    
    if start_idx != -1:
        # scan forward for next double newline or "ACM Classification"
        subtext = text[start_idx:]
        # find end
        end_idx = subtext.find('\n\n')
        if end_idx == -1:
            end_idx = len(subtext)
            
        # Also check for next section header like "INTRODUCTION" or "ACM Classification" to be safe
        # Often headers are ALL CAPS or specific phrases
        
        keywords_block = subtext[:end_idx].lower()
        
        if 'food' in keywords_block:
            food_titles.append(title)
            if len(debug_info) < 5:
                debug_info.append({"title": title, "keywords": keywords_block})

# Calculate citations
total_citations = 0
for cit in citations:
    if cit['title'] in food_titles:
        try:
            total_citations += int(cit['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps({"food_titles": food_titles, "total_citations": total_citations, "debug": debug_info}))"""

env_args = {'var_function-call-8748244462217434689': ['paper_docs'], 'var_function-call-8748244462217434842': ['Citations', 'sqlite_sequence'], 'var_function-call-10817664668211665430': 'file_storage/function-call-10817664668211665430.json', 'var_function-call-4112176734939169200': 'file_storage/function-call-4112176734939169200.json', 'var_function-call-17971925795973344162': 'file_storage/function-call-17971925795973344162.json', 'var_function-call-17971925795973342135': 'file_storage/function-call-17971925795973342135.json'}

exec(code, env_args)
