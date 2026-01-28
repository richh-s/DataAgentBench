code = """import json
import re

# Load the paper docs
try:
    with open(locals()['var_function-call-5276622005229675102'], 'r') as f:
        papers = json.load(f)
except Exception as e:
    # If the previous result was empty or failed, papers will be empty
    papers = []

titles = []
relevant_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Check domain "physical activity" (case insensitive)
    # The hint implies we should extract it. Usually searching the text is fine.
    # To be safer, we can check if it's in the first part (keywords) or just present.
    # The prompt implies domain is a property. "Physical activity" is a common phrase.
    if 'physical activity' not in text.lower():
        continue
        
    # Check year 2016
    # Look in the first 1000 characters for the year 2016.
    header = text[:1500]
    
    # Heuristics for publication year:
    # 1. "Copyright 2016" or "© 2016"
    # 2. Conference/Date line: "September ... 2016", "CHI 2016", "CHI '16"
    # 3. Avoid matching citations.
    
    is_2016 = False
    
    # Specific patterns for 2016 publication
    if re.search(r'(?:Copyright|©).{0,20}2016', header, re.IGNORECASE):
        is_2016 = True
    elif re.search(r'\b2016\b', header):
        # If 2016 is in the header, likely the year. 
        # But check if 2015 or 2017 is also there, to avoid confusion (e.g. "Review of 2015 work... presented in 2016")
        # Usually the conference year is prominent.
        # Let's assume presence in first 1000 chars is good enough given the pre-filter.
        is_2016 = True
        
    # Double check it's not a paper from 2015 or 2017 referencing 2016 (unlikely in header)
    # or a 2017 paper citing 2016 work in the intro.
    # If "Copyright 2017" or "Copyright 2015" is found, ignore.
    if re.search(r'(?:Copyright|©).{0,20}(?:2015|2014|2013|2017|2018|2019)', header, re.IGNORECASE):
        # If another year is explicitly the copyright year, it's probably not 2016.
        # But if both appear? e.g. "Copyright 2016... (c) 2015 work" - rare.
        # Let's trust the copyright year if present.
        if not re.search(r'(?:Copyright|©).{0,20}2016', header, re.IGNORECASE):
            is_2016 = False
            
    if is_2016:
        # Extract title from filename
        title = filename.replace('.txt', '')
        titles.append(title)
        relevant_papers.append({'title': title, 'filename': filename})

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-13566097313952112574': 'file_storage/function-call-13566097313952112574.json', 'var_function-call-5276622005229675102': 'file_storage/function-call-5276622005229675102.json'}

exec(code, env_args)
