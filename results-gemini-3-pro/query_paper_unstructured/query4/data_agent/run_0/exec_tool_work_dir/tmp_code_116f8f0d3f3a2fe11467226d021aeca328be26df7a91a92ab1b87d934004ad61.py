code = """import json
import re

# Load the paper docs from the file stored in the previous step
# The key is var_function-call-2371613327861333471
file_path = locals()['var_function-call-2371613327861333471']

with open(file_path, 'r') as f:
    papers = json.load(f)

titles_2016_pa = []

# Regex for year 2016 in the header/metadata area (first 3000 chars)
year_pattern = re.compile(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\s\S]{0,50}2016|2016[\s\S]{0,50}(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*|Copyright[\s\S]{0,50}2016|©[\s\S]{0,50}2016|ACM 2016|IEEE 2016|\b2016\b', re.IGNORECASE)

# Regex for physical activity
pa_pattern = re.compile(r'physical\s+activity', re.IGNORECASE)

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check domain
    # Hint: "values may be part of a list". "substring/contains matching".
    # I'll check if "physical activity" appears in the text. 
    # To be safer, maybe restricting to the first part or looking for "Keywords"?
    # But the instruction says "Each document contains full text... extract... domain".
    # And hint says "substring matching".
    # I'll check if "physical activity" is in the text.
    if not pa_pattern.search(text):
        continue

    # Check year
    # Look in the first 3000 characters for 2016 in a context that suggests publication date.
    header_text = text[:3000]
    # Simple check: if 2016 is in the header, it's likely the pub year.
    # But references usually appear at the end. 
    # Citations in text might look like [12] or (Smith 2016).
    # Headers usually look like "CHI '16", "Ubicomp '16", "Copyright 2016".
    # Let's refine the year check.
    
    match = False
    # Check for specific venue patterns in header
    # Venues: CHI, Ubicomp, CSCW, DIS, PervasiveHealth, WWW, IUI, OzCHI, TEI, AH
    # Year: 2016
    if re.search(r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[\s\S]{0,20}(2016|\'16)', header_text, re.IGNORECASE):
        match = True
    elif re.search(r'Copyright\s*(©)?\s*2016', header_text, re.IGNORECASE):
        match = True
    elif re.search(r'©\s*2016', header_text):
        match = True
    elif re.search(r'June 2016|July 2016|August 2016|September 2016|October 2016|November 2016|December 2016|January 2016|February 2016|March 2016|April 2016|May 2016', header_text, re.IGNORECASE):
        match = True
    
    if match:
        # Extract title
        title = filename.replace('.txt', '')
        titles_2016_pa.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016_pa))"""

env_args = {'var_function-call-10785526798684626706': 'file_storage/function-call-10785526798684626706.json', 'var_function-call-5504457116591251088': 'file_storage/function-call-5504457116591251088.json', 'var_function-call-2371613327861333471': 'file_storage/function-call-2371613327861333471.json'}

exec(code, env_args)
