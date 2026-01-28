code = """import json
import re

with open(locals()['var_function-call-7586214257055398583'], 'r') as f:
    citations = json.load(f)
with open(locals()['var_function-call-16114964338052687681'], 'r') as f:
    paper_docs = json.load(f)
paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

p1 = r"(?<![a-zA-Z])CHI\s?['\u2019]?\s?(20\d{2}|\d{2})"
p2 = r"Conference on Human Factors in Computing Systems"

unmatched_contexts = []

for cit in citations:
    title = cit['title']
    fname = title + ".txt"
    if fname in paper_map:
        text = paper_map[fname]
        header = text[:3000]
        
        m1 = re.search(p1, header)
        m2 = re.search(p2, header, re.IGNORECASE)
        
        if not m1 and not m2:
            # Check if CHI appears
            # searching for "CHI" with word boundaries
            chi_hits = [m.start() for m in re.finditer(r"\bCHI\b", header)]
            if chi_hits:
                # Get context
                contexts = []
                for start in chi_hits:
                    ctx = header[max(0, start-30):min(len(header), start+30)].replace("\n", " ")
                    contexts.append(ctx)
                unmatched_contexts.append({"title": title, "contexts": contexts})

print("__RESULT__:")
print(json.dumps(unmatched_contexts[:10]))"""

env_args = {'var_function-call-7586214257055398583': 'file_storage/function-call-7586214257055398583.json', 'var_function-call-979778011189952116': 'Sundroid: Solar Radiation Awareness with Smartphones', 'var_function-call-8522392465021198661': 'file_storage/function-call-8522392465021198661.json', 'var_function-call-7603458929060210194': 'file_storage/function-call-7603458929060210194.json', 'var_function-call-16114964338052687681': 'file_storage/function-call-16114964338052687681.json', 'var_function-call-11680504835106074828': 114, 'var_function-call-2209278332186281583': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': '16', 'match': 'CHI 2019'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'count': '98', 'match': 'CHI 2018'}]}

exec(code, env_args)
