code = """import json
import re

with open(locals()['var_function-call-3133197345042129806'], 'r') as f:
    papers = json.load(f)

debug_info = []

for p in papers[:5]:
    text = p.get('text', '')
    title = p.get('filename', '')
    header = text[:500]
    
    # Check for any year in 2000s
    all_years = re.findall(r'20[0-9]{2}', header)
    
    is_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        "title": title,
        "header_preview": header.replace('\n', ' ')[:100],
        "found_years": all_years,
        "is_empirical": is_empirical
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-968771099639512082': 'file_storage/function-call-968771099639512082.json', 'var_function-call-10025871425113369306': 'file_storage/function-call-10025871425113369306.json', 'var_function-call-3133197345042129806': 'file_storage/function-call-3133197345042129806.json', 'var_function-call-14920944781988559493': []}

exec(code, env_args)
