code = """import json
import pandas as pd

# Load citation data
with open(locals()['var_function-call-18120137010689517392'], 'r') as f:
    citations_data = json.load(f)

# Load paper data
with open(locals()['var_function-call-18120137010689516403'], 'r') as f:
    papers_data = json.load(f)

# Convert citations to a dict for easy lookup: title -> total_citations
citation_map = {item['title']: int(item['total_citations']) for item in citations_data}

results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
        
    # Check Year: 2016
    # Heuristic: Check first 2000 chars for "2016". 
    # Also many papers have the year in the header like "CHI 2016" or "UbiComp '16".
    # But looking for "2016" in the top section is a strong signal for publication year 
    # vs a citation year which usually appears in the bibliography at the end or in brackets.
    # However, a paper published in 2016 might cite 2016 papers. 
    # But usually the venue date is at the top.
    
    # Let's check if '2016' is in the first 1000 characters.
    if '2016' in text[:1000]:
        is_2016 = True
    else:
        is_2016 = False
        
    # Check Domain: 'physical activity'
    if 'physical activity' in text.lower():
        is_domain = True
    else:
        is_domain = False
        
    if is_2016 and is_domain:
        # Get citation count
        total_citations = citation_map.get(title, 0)
        results.append({
            "title": title,
            "total_citations": total_citations
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12537067908498854148': ['paper_docs'], 'var_function-call-12537067908498856339': ['Citations', 'sqlite_sequence'], 'var_function-call-18120137010689517392': 'file_storage/function-call-18120137010689517392.json', 'var_function-call-18120137010689516403': 'file_storage/function-call-18120137010689516403.json'}

exec(code, env_args)
