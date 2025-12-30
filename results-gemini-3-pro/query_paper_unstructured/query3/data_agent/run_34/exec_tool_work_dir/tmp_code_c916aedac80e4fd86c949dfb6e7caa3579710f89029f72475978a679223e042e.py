code = """import json
import re
import pandas as pd

# Load Citations
citation_file = locals()['var_function-call-3193368456383189036']
with open(citation_file, 'r') as f:
    citations_list = json.load(f)

# Convert to dict: title -> total_citations
# Handle potential string/int issues
citation_map = {}
for item in citations_list:
    try:
        count = int(item['total_citations'])
    except:
        count = 0
    citation_map[item['title']] = count

# Load Papers
papers_file = locals()['var_function-call-13531993563476914468']
with open(papers_file, 'r') as f:
    papers = json.load(f)

results = []

for paper in papers:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    text = paper.get('text', '')
    
    # Extract Year from first 2000 chars
    # We assume the publication year appears early in the text (e.g. header)
    header_text = text[:3000]
    
    # Find years 2017-2029
    years = re.findall(r'\b(20(?:1[7-9]|2[0-9]))\b', header_text)
    
    if not years:
        continue
    
    # Heuristic: The publication year is likely the first one mentioned in the context of conference/copyright.
    # We'll take the first year found that is > 2016.
    pub_year = None
    for y in years:
        if int(y) > 2016:
            pub_year = int(y)
            break
            
    if not pub_year:
        continue
        
    # Check "empirical"
    if 'empirical' not in text.lower():
        continue
        
    # Get citations
    # If title not in map, citation count is 0 (or maybe we shouldn't include it? I'll include with 0)
    # But usually joining implies intersection. I'll include it if it matches the paper criteria.
    count = citation_map.get(title, 0)
    
    results.append({"title": title, "citation_count": count})

# Sort by citation count desc for better presentation
results.sort(key=lambda x: x['citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-224810883549294860': 'file_storage/function-call-224810883549294860.json', 'var_function-call-9456626268790233779': ['paper_docs'], 'var_function-call-16636765420084793523': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-3193368456383189036': 'file_storage/function-call-3193368456383189036.json', 'var_function-call-13531993563476914468': 'file_storage/function-call-13531993563476914468.json'}

exec(code, env_args)
