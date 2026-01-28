code = """import json
import re

# Load the paper documents
with open(locals()['var_function-call-5351248468420054587'], 'r') as f:
    papers = json.load(f)

titles_2016 = []

def get_year(text):
    # Look at the first 1000 characters for context
    header = text[:1000]
    
    # Check for specific conference patterns which are very reliable
    # e.g., "CHI 2016", "UbiComp '16", "Ubicomp 2016", "CSCW '16"
    # Matches: "CHI 2016", "CHI '16", "CHI'16", "CHI 16"
    matches = re.findall(r"(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|OzCHI|TEI|AH|PervasiveHealth|WWW)\s*['\u2019]?\s*(\d{2,4})", header, re.IGNORECASE)
    for m in matches:
        if len(m) == 2:
            y = int("20" + m)
            if y == 2016: return 2016
            if y > 2016: return y # Found a later year
        elif len(m) == 4:
            y = int(m)
            if y == 2016: return 2016
            if y > 2016: return y

    # Check for Copyright 2016
    if re.search(r"Copyright\s+(?:©|\(c\))?\s*2016", header, re.IGNORECASE):
        return 2016
    
    # Check for "Month 2016" or "Month DD-DD, 2016"
    if re.search(r"[A-Z][a-z]+\s+\d{1,2}[–-]?\d{0,2},?\s+2016", header):
        return 2016
        
    # Fallback: look for 2016, but ensure no 2017, 2018 etc in header
    years = re.findall(r"20\d{2}", header)
    years = [int(y) for y in years]
    if 2016 in years:
        # If there is a later year in the header, assume it's the later year (e.g. published 2018, citing 2016)
        if any(y > 2016 for y in years):
            return max(years)
        return 2016
        
    return None

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' in text.lower():
        # Check year
        y = get_year(text)
        if y == 2016:
            titles_2016.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-2934941311290250447': 'file_storage/function-call-2934941311290250447.json', 'var_function-call-2934941311290249234': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-5351248468420054587': 'file_storage/function-call-5351248468420054587.json'}

exec(code, env_args)
