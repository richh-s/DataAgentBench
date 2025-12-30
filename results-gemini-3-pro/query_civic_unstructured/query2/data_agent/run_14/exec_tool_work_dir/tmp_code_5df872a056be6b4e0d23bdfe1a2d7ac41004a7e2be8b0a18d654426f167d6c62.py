code = """import json
import re

funding_path = locals()['var_function-call-13164751492978107468']
civic_path = locals()['var_function-call-9869211362583101527']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

all_text = ""
for d in civic_data:
    all_text += d.get('text', '') + ' '

park_projects = []
for item in funding_data:
    if 'park' in item['Project_Name'].lower() or 'playground' in item['Project_Name'].lower():
        park_projects.append(item['Project_Name'])

debug_snippets = {}

for p_name in park_projects:
    base_name = p_name.split('(')[0].strip()
    matches = [m.start() for m in re.finditer(re.escape(base_name), all_text, re.IGNORECASE)]
    
    p_snippets = []
    for start in matches:
        snip = all_text[start:start+300]
        # remove newlines
        snip = snip.replace('\n', ' ')
        p_snippets.append(snip)
    
    debug_snippets[p_name] = p_snippets

print('__RESULT__:')
print(json.dumps(debug_snippets))"""

env_args = {'var_function-call-13164751492978107468': 'file_storage/function-call-13164751492978107468.json', 'var_function-call-13164751492978107155': 'file_storage/function-call-13164751492978107155.json', 'var_function-call-9869211362583101527': 'file_storage/function-call-9869211362583101527.json', 'var_function-call-4590254566354638505': {'confirmed_projects': [], 'total_funding': 0}, 'var_function-call-11353638954296130998': 'Done', 'var_function-call-13277355279832923139': {'text_length': 63699, 'funding_count': 500, 'target_found_exact': True, 'matches_count': 5, 'snippets': ['Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Street', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff ', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-\n\npost shade structures at Malibu Bluffs Park\n\n(cid:190) Estimated Schedule:\n\n(cid:', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-\n\npost shade structures at Malibu Bluffs Park\n\n(cid:190) Estimated Schedule:\n\n(cid:', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff ']}, 'var_function-call-4194027231121006763': {'confirmed_projects': ['Bluffs Park Shade Structure'], 'total_funding': 21000}}

exec(code, env_args)
