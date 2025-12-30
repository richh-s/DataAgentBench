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

target = "Michael Landon Center Roof Replacement Project"
# search
matches = [m.start() for m in re.finditer(re.escape(target), all_text, re.IGNORECASE)]

snippets = []
for start in matches:
    snippets.append(all_text[start:start+400].replace(chr(10), ' '))

print('__RESULT__:')
print(json.dumps(snippets))"""

env_args = {'var_function-call-13164751492978107468': 'file_storage/function-call-13164751492978107468.json', 'var_function-call-13164751492978107155': 'file_storage/function-call-13164751492978107155.json', 'var_function-call-9869211362583101527': 'file_storage/function-call-9869211362583101527.json', 'var_function-call-4590254566354638505': {'confirmed_projects': [], 'total_funding': 0}, 'var_function-call-11353638954296130998': 'Done', 'var_function-call-13277355279832923139': {'text_length': 63699, 'funding_count': 500, 'target_found_exact': True, 'matches_count': 5, 'snippets': ['Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Street', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff ', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-\n\npost shade structures at Malibu Bluffs Park\n\n(cid:190) Estimated Schedule:\n\n(cid:', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-\n\npost shade structures at Malibu Bluffs Park\n\n(cid:190) Estimated Schedule:\n\n(cid:', 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff ']}, 'var_function-call-4194027231121006763': {'confirmed_projects': ['Bluffs Park Shade Structure'], 'total_funding': 21000}, 'var_function-call-16302065240402989575': 'file_storage/function-call-16302065240402989575.json', 'var_function-call-12379116878183087823': [{'Funding_ID': '78', 'Project_Name': 'Point Dume Decomposed Granite Walkway Repair Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '86000'}, {'Funding_ID': '79', 'Project_Name': 'Point Dume Walkway Repairs', 'Funding_Source': 'International Aid', 'Amount': '59000'}]}

exec(code, env_args)
