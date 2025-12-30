code = """import json
import re

with open(locals()['var_function-call-7459141219968339162'], 'r') as f:
    papers = json.load(f)

debug_info = []
for p in papers:
    text = p['text']
    match = re.search(r'Author Keywords(.*?)(?:ACM Classification|Introduction)', text[:5000], re.IGNORECASE | re.DOTALL)
    if match:
        keywords = match.group(1).strip()
        keywords = keywords.replace(chr(10), ' ').replace(chr(13), ' ')
        debug_info.append({"filename": p['filename'], "keywords": keywords})
        if len(debug_info) > 5:
            break

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-3676184941267040123': 'file_storage/function-call-3676184941267040123.json', 'var_function-call-6873213907714452995': 'file_storage/function-call-6873213907714452995.json', 'var_function-call-17043150740226976793': 'file_storage/function-call-17043150740226976793.json', 'var_function-call-7459141219968339162': 'file_storage/function-call-7459141219968339162.json', 'var_function-call-4763535483607380': {'total_citations': 0, 'papers': []}, 'var_function-call-6447564677428063804': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'snippet': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'snippet': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippet': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}]}

exec(code, env_args)
