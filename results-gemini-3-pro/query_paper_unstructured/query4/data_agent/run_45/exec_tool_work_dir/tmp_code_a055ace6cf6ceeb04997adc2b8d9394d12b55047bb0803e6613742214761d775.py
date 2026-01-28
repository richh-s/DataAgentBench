code = """import json
import re

file_path = locals()['var_function-call-1805963749802490353']
with open(file_path, 'r') as f:
    papers = json.load(f)

filtered_titles = []
venue_pattern = re.compile(r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).{0,50}2016", re.IGNORECASE)
copyright_pattern = re.compile(r"(Copyright|©).{0,50}2016", re.IGNORECASE)
domain_pattern = re.compile(r"physical activity", re.IGNORECASE)

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    if domain_pattern.search(filename) or domain_pattern.search(text[:3000]):
        header = text[:1000]
        is_2016 = False
        if venue_pattern.search(header) or copyright_pattern.search(header):
            is_2016 = True
        
        if is_2016:
            title = filename.rsplit('.', 1)[0]
            filtered_titles.append(title)

print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-13658712290201137078': 'file_storage/function-call-13658712290201137078.json', 'var_function-call-1805963749802490353': 'file_storage/function-call-1805963749802490353.json'}

exec(code, env_args)
