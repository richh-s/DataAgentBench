code = """import json
import re

file_path = locals()['var_function-call-18099153275120727410']
with open(file_path, 'r') as f:
    papers = json.load(f)

for p in papers:
    print('='*20)
    print('Title:', p['filename'])
    text = p['text']
    
    lines = text.split('\n')
    found_contrib = False
    for line in lines:
        if 'contribution' in line.lower():
            print('COORD contribution:', line.strip()[:100])
            found_contrib = True
    
    if not found_contrib:
        print('No contribution keyword found in lines.')

    match = re.search(r'Copyright (20\d{2})', text)
    if match:
        print('Year (Copyright):', match.group(1))
    else:
        match = re.search(r"'\d{2}", text)
        if match:
            print('Year (Conf):', match.group(0))
        else:
            print('Year not found')

    if 'empirical' in text.lower():
        print('Contains empirical: Yes')
    else:
        print('Contains empirical: No')"""

env_args = {'var_function-call-10449789667232023992': ['paper_docs'], 'var_function-call-10449789667232022543': 'file_storage/function-call-10449789667232022543.json', 'var_function-call-10449789667232025190': 'file_storage/function-call-10449789667232025190.json', 'var_function-call-18099153275120727410': 'file_storage/function-call-18099153275120727410.json'}

exec(code, env_args)
