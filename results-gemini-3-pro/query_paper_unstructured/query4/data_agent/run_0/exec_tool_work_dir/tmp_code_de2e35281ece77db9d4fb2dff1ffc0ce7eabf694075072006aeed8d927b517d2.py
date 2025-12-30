code = """import json
import re

file_path = locals()['var_function-call-2371613327861333471']

with open(file_path, 'r') as f:
    papers = json.load(f)

titles_2016_pa = []

# Regex for physical activity
pa_pattern = re.compile(r'physical\s+activity', re.IGNORECASE)

# Regex for year 2016 in header
# Look for 2016 in first 2000 chars.
# Common formats: "CHI '16", "CHI 2016", "September 2016", "Copyright 2016", "© 2016"
year_regex = re.compile(r'(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|ACM|IEEE)[\s\S]{0,30}(?:2016|\'16)|Copyright\s*(?:©)?\s*2016|©\s*2016|\b2016\b', re.IGNORECASE)

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check domain
    if not pa_pattern.search(text):
        continue

    # Check year in header (first 2000 chars)
    header_text = text[:2000]
    
    # Check if 2016 is present in the header text
    # This is a heuristic. A paper published in 2016 will almost certainly mention 2016 in the header/footer of the first page.
    # But a paper in 2017 might cite a 2016 paper in the first page (e.g. in abstract).
    # So looking for specific venue/copyright patterns is better.
    
    is_2016 = False
    if year_regex.search(header_text):
        is_2016 = True
    
    # Double check to avoid false positives from 2017 papers citing 2016
    # If the header also contains 2017 or 2015, we need to be careful.
    # But usually the venue year is prominent.
    # Let's trust the regex for now. If I get many results, I can refine.
    # Another check: exclude if "2017" or "2018" is in the venue string.
    # e.g. "CHI 2017"
    
    if is_2016:
        # Extra check: if "2017" is also in the header and closer to the venue name?
        # Let's assume the presence of "2016" in copyright or venue pattern is sufficient.
        titles_2016_pa.append(filename.replace('.txt', ''))

print("__RESULT__:")
print(json.dumps(titles_2016_pa))"""

env_args = {'var_function-call-10785526798684626706': 'file_storage/function-call-10785526798684626706.json', 'var_function-call-5504457116591251088': 'file_storage/function-call-5504457116591251088.json', 'var_function-call-2371613327861333471': 'file_storage/function-call-2371613327861333471.json'}

exec(code, env_args)
