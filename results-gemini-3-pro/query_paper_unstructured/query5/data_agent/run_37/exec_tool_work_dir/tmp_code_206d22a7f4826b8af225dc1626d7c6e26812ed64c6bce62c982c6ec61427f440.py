code = """import json
import re

citations_file = locals()['var_function-call-17226783687381058868']
with open(citations_file, 'r') as f:
    citations = json.load(f)

papers_file_1 = locals()['var_function-call-439047016334957359']
papers_file_2 = locals()['var_function-call-6871933481051541043']

with open(papers_file_1, 'r') as f:
    papers1 = json.load(f)

with open(papers_file_2, 'r') as f:
    papers2 = json.load(f)

all_papers = papers1 + papers2
paper_map = {p['filename']: p['text'] for p in all_papers}

total = 0
for c in citations:
    fname = c['title'] + ".txt"
    if fname in paper_map:
        text = paper_map[fname]
        head = text[:3000]
        
        # Check for CHI venue
        is_chi = False
        if "Conference on Human Factors in Computing Systems" in head:
            is_chi = True
        elif re.search(r'\bCHI\b', head):
            is_chi = True
        
        # Double check to avoid false positives (e.g. CHI as part of an acronym that is not the venue?)
        # But \bCHI\b is quite specific in the header.
        
        if is_chi:
            total += int(c['citation_count'])

print(f"Total citations: {total}")
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_function-call-17226783687381058868': 'file_storage/function-call-17226783687381058868.json', 'var_function-call-11445110573427865236': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"], 'var_function-call-12469297253673424923': 'file_storage/function-call-12469297253673424923.json', 'var_function-call-13349597544077869875': 'file_storage/function-call-13349597544077869875.json', 'var_function-call-5125539185123063334': {'count': 5}, 'var_function-call-7904490856032329911': 'file_storage/function-call-7904490856032329911.json', 'var_function-call-15190824524824419371': 0, 'var_function-call-2112808822247239442': 'file_storage/function-call-2112808822247239442.json', 'var_function-call-439047016334957359': 'file_storage/function-call-439047016334957359.json', 'var_function-call-3475495459262312372': 99, 'var_function-call-6871933481051541043': 'file_storage/function-call-6871933481051541043.json'}

exec(code, env_args)
