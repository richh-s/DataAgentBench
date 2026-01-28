code = """import json
import re

citations_file = locals()['var_function-call-17226783687381058868']
papers_file = locals()['var_function-call-7904490856032329911']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

# Create a lookup for papers by filename
paper_map = {p['filename']: p['text'] for p in papers}

total_citations = 0
chi_papers_count = 0
missing_papers = 0

for c in citations:
    title = c['title']
    filename = title + ".txt"
    if filename in paper_map:
        text = paper_map[filename]
        # Check for CHI venue
        # Heuristic: Look for "CHI" in the first 1000 characters or "Conference on Human Factors in Computing Systems"
        # The preview showed "UBICOMP '15..." at the very beginning.
        # So I will check the first 500 characters.
        header = text[:1000]
        
        # Regex for CHI year or CHI conference
        # CHI usually appears as "CHI 'XX" or "CHI 20XX" or "Proceedings of the ... CHI"
        # Or just "CHI" in the header line.
        
        is_chi = False
        if re.search(r'\bCHI\b', header):
            is_chi = True
        elif "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
            
        if is_chi:
            total_citations += int(c['citation_count'])
            chi_papers_count += 1
    else:
        missing_papers += 1

print(f"Processed {len(citations)} citations.")
print(f"Matched papers: {len(citations) - missing_papers}")
print(f"CHI papers found: {chi_papers_count}")
print(f"Total citations for CHI papers: {total_citations}")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-17226783687381058868': 'file_storage/function-call-17226783687381058868.json', 'var_function-call-11445110573427865236': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"], 'var_function-call-12469297253673424923': 'file_storage/function-call-12469297253673424923.json', 'var_function-call-13349597544077869875': 'file_storage/function-call-13349597544077869875.json', 'var_function-call-5125539185123063334': {'count': 5}, 'var_function-call-7904490856032329911': 'file_storage/function-call-7904490856032329911.json'}

exec(code, env_args)
