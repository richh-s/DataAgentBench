code = """import json
import re

with open(locals()['var_function-call-7586214257055398583'], 'r') as f:
    citations = json.load(f)
with open(locals()['var_function-call-16114964338052687681'], 'r') as f:
    paper_docs = json.load(f)
paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

p1 = r"(?<![a-zA-Z])CHI\s?['\u2019]?\s?(20\d{2}|\d{2})"
p2 = r"Conference on Human Factors in Computing Systems"
p3 = r"CHI\s+Conference"

matched_titles = set()
total_citations = 0

debug_list = []

for cit in citations:
    title = cit['title']
    fname = title + ".txt"
    if fname in paper_map:
        text = paper_map[fname][:5000] # Check first 5000 chars
        
        m1 = re.search(p1, text)
        m2 = re.search(p2, text, re.IGNORECASE)
        m3 = re.search(p3, text, re.IGNORECASE)
        
        is_match = False
        match_reason = ""
        
        if m1:
            is_match = True
            match_reason = "p1: " + m1.group(0)
        elif m2:
            is_match = True
            match_reason = "p2: " + m2.group(0)
        elif m3:
            # Check if it is NordiCHI or OzCHI
            # p3 matches "CHI Conference". NordiCHI Conference?
            # Check prefix
            idx = m3.start()
            prefix = text[max(0, idx-10):idx]
            if "Nordi" in prefix or "Oz" in prefix:
                pass
            else:
                is_match = True
                match_reason = "p3: " + m3.group(0)
        
        if is_match:
            matched_titles.add(title)
            total_citations += int(cit['citation_count'])
            debug_list.append({"title": title, "reason": match_reason, "citations": cit['citation_count']})

print(f"Matched {len(matched_titles)} papers.")
print(f"Total citations: {total_citations}")
print("__RESULT__:")
print(json.dumps(debug_list))"""

env_args = {'var_function-call-7586214257055398583': 'file_storage/function-call-7586214257055398583.json', 'var_function-call-979778011189952116': 'Sundroid: Solar Radiation Awareness with Smartphones', 'var_function-call-8522392465021198661': 'file_storage/function-call-8522392465021198661.json', 'var_function-call-7603458929060210194': 'file_storage/function-call-7603458929060210194.json', 'var_function-call-16114964338052687681': 'file_storage/function-call-16114964338052687681.json', 'var_function-call-11680504835106074828': 114, 'var_function-call-2209278332186281583': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': '16', 'match': 'CHI 2019'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'count': '98', 'match': 'CHI 2018'}], 'var_function-call-4321253950318469626': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}]}

exec(code, env_args)
