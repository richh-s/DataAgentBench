code = """import json
import re

with open(locals()['var_function-call-7586214257055398583'], 'r') as f:
    citations = json.load(f)

with open(locals()['var_function-call-16114964338052687681'], 'r') as f:
    paper_docs = json.load(f)

paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

def get_venue_match(text):
    header = text[:5000]
    p1 = r"(?<![a-zA-Z])CHI\s?['\u2019]?\s?(20\d{2}|\d{2})"
    p2 = r"Conference on Human Factors in Computing Systems"
    
    m1 = re.search(p1, header)
    if m1:
        return m1.group(0)
    m2 = re.search(p2, header, re.IGNORECASE)
    if m2:
        return m2.group(0)
    return None

matched_info = []
total_citations = 0

for cit in citations:
    title = cit['title']
    fname = title + ".txt"
    if fname in paper_map:
        match = get_venue_match(paper_map[fname])
        if match:
            total_citations += int(cit['citation_count'])
            matched_info.append({"title": title, "count": cit['citation_count'], "match": match})

print(f"Total matched: {len(matched_info)}")
print(f"Total citations: {total_citations}")
print("Matched papers:", json.dumps(matched_info[:5], indent=2))

print("__RESULT__:")
print(json.dumps(matched_info))"""

env_args = {'var_function-call-7586214257055398583': 'file_storage/function-call-7586214257055398583.json', 'var_function-call-979778011189952116': 'Sundroid: Solar Radiation Awareness with Smartphones', 'var_function-call-8522392465021198661': 'file_storage/function-call-8522392465021198661.json', 'var_function-call-7603458929060210194': 'file_storage/function-call-7603458929060210194.json', 'var_function-call-16114964338052687681': 'file_storage/function-call-16114964338052687681.json', 'var_function-call-11680504835106074828': 114}

exec(code, env_args)
