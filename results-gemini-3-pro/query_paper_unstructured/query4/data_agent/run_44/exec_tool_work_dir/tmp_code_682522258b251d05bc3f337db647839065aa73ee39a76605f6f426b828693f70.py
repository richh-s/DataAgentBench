code = """import json
import re

# Load the paper documents
# The key for the full result is var_function-call-4863138715288248504
file_path = locals()['var_function-call-4863138715288248504']
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 2016 in the first 1000 characters
    header = text[:1000]
    
    # Heuristics for 2016 publication
    is_2016 = False
    
    # 1. Look for Copyright 2016
    if re.search(r'Copyright\s+(?:\u00a9\s*)?2016', header, re.IGNORECASE):
        is_2016 = True
    
    # 2. Look for conference header with 2016 or '16
    # e.g., "CHI '16", "CHI 2016", "UbiComp '16", "September ... 2016"
    elif re.search(r"(?:CHI|UbiComp|CSCW|DIS|IUI|OzCHI|TEI|AH|PervasiveHealth|WWW)\s*(?:'16|2016)", header, re.IGNORECASE):
        is_2016 = True
        
    # 3. Look for "Month ... 2016" in the header
    elif re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December).*?2016', header, re.IGNORECASE):
        is_2016 = True
    
    # Domain Check
    # Look for "physical activity" in the full text (case insensitive)
    # The prompt says "Fields like domain ... may contain multiple values ... matching domains ... use substring/contains"
    has_domain = "physical activity" in text.lower()
    
    if is_2016 and has_domain:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-1438467208148862698': 'file_storage/function-call-1438467208148862698.json', 'var_function-call-987307425493553399': 'file_storage/function-call-987307425493553399.json', 'var_function-call-4863138715288248504': 'file_storage/function-call-4863138715288248504.json'}

exec(code, env_args)
