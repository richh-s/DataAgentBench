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
print(f"Total papers loaded: {len(all_papers)}")

paper_map = {p['filename']: p['text'] for p in all_papers}

total_citations = 0
chi_papers_count = 0
missing_papers = 0

for c in citations:
    title = c['title']
    filename = title + ".txt"
    if filename in paper_map:
        text = paper_map[filename]
        header = text[:2000]
        
        is_chi = False
        # Regex for CHI followed by year or space. match single quote or right single quote
        if re.search(r'CHI\s*[\'\u2019]?\d{2,4}', header, re.IGNORECASE):
            is_chi = True
        elif "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        elif re.search(r'\bCHI\b', header):
             is_chi = True
             
        if is_chi:
            total_citations += int(c['citation_count'])
            chi_papers_count += 1
    else:
        missing_papers += 1

print(f"Matched papers: {len(citations) - missing_papers}")
print(f"CHI papers found: {chi_papers_count}")
print(f"Total citations for CHI papers: {total_citations}")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-17226783687381058868': 'file_storage/function-call-17226783687381058868.json', 'var_function-call-11445110573427865236': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"], 'var_function-call-12469297253673424923': 'file_storage/function-call-12469297253673424923.json', 'var_function-call-13349597544077869875': 'file_storage/function-call-13349597544077869875.json', 'var_function-call-5125539185123063334': {'count': 5}, 'var_function-call-7904490856032329911': 'file_storage/function-call-7904490856032329911.json', 'var_function-call-15190824524824419371': 0, 'var_function-call-2112808822247239442': 'file_storage/function-call-2112808822247239442.json', 'var_function-call-439047016334957359': 'file_storage/function-call-439047016334957359.json', 'var_function-call-3475495459262312372': 99, 'var_function-call-6871933481051541043': 'file_storage/function-call-6871933481051541043.json'}

exec(code, env_args)
