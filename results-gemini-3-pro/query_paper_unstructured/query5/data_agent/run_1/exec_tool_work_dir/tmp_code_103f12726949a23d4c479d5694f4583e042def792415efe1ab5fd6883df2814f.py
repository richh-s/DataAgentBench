code = """import json
import re

with open(locals()['var_function-call-12437250052302532993'], 'r') as f:
    citations_data = json.load(f)

citations_2020 = {item['title']: int(item['citation_count']) for item in citations_data if int(item['citation_count']) > 0}

with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

matched = []
total = 0

for doc in paper_docs:
    filename = doc['filename']
    title = filename.rsplit('.', 1)[0]
    if title in citations_2020:
        text = doc['text']
        # Broader search
        is_chi = False
        # Look for typical CHI headers
        if re.search(r'CHI\s*[\'’]?\d{2,4}', text[:1000]):
            is_chi = True
        elif "Conference on Human Factors in Computing Systems" in text[:1000]:
            is_chi = True
        elif "CHI Conference" in text[:1000]:
            is_chi = True
        elif re.search(r'\bCHI\b', text[:500]): # Short word in header
             is_chi = True
        
        # If not found in header, maybe check footer or specific phrase
        if not is_chi:
            if "Proc. of CHI" in text or "Proceedings of CHI" in text:
                is_chi = True

        if is_chi:
            c = citations_2020[title]
            total += c
            matched.append(title)

print("__RESULT__:")
print(json.dumps({"total_citations": total, "count": len(matched), "titles": matched[:10]}))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json', 'var_function-call-767057999987748063': 16, 'var_function-call-17271081787061420733': 16}

exec(code, env_args)
