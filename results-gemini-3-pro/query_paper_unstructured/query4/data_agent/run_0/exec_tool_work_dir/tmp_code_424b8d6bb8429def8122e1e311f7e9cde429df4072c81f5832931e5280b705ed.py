code = """import json
import re

file_path = locals()['var_function-call-2371613327861333471']

with open(file_path, 'r') as f:
    papers = json.load(f)

titles_2016_pa = []

pa_pattern = re.compile(r"physical\s+activity", re.IGNORECASE)
year_regex = re.compile(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|ACM|IEEE)[\s\S]{0,30}(?:2016|'16)|Copyright\s*(?:©)?\s*2016|©\s*2016", re.IGNORECASE)

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    if not pa_pattern.search(text):
        continue

    header_text = text[:2000]
    
    if year_regex.search(header_text):
        titles_2016_pa.append(filename.replace('.txt', ''))

print("__RESULT__:")
print(json.dumps(titles_2016_pa))"""

env_args = {'var_function-call-10785526798684626706': 'file_storage/function-call-10785526798684626706.json', 'var_function-call-5504457116591251088': 'file_storage/function-call-5504457116591251088.json', 'var_function-call-2371613327861333471': 'file_storage/function-call-2371613327861333471.json'}

exec(code, env_args)
