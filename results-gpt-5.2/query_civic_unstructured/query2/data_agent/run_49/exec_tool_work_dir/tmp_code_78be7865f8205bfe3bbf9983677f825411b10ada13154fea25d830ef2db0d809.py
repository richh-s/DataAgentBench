code = """import json, re
from pathlib import Path

def load_docs(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        return json.loads(Path(maybe_path_or_list).read_text())
    return maybe_path_or_list

docs = load_docs(var_call_f6nLGQzT9j7mybou2uxQzV9K)

# Extract lines that look like project headings and their update lines
park_completed_2022 = set()
for d in docs:
    text = d.get('text','')
    # Find project blocks by heading pattern: line with words (not bullet) followed by blank line and 'Updates:'
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln or len(ln) < 4: 
            continue
        # candidate project name line: no colon, not starting with '(' or 'Page' etc.
        if ':' in ln: 
            continue
        if ln.lower().startswith(('page','agenda','public works','capital improvement','storm drain','discussion','to','prepared','approved','date prepared','meeting date','subject','recommended action')):
            continue
        # check nearby for Updates mentioning completed and 2022, and park keyword in project name
        if 'park' not in ln.lower():
            continue
        window = ' '.join(lines[i:i+20]).lower()
        if 'construction was completed' in window and '2022' in window:
            park_completed_2022.add(ln)

result = sorted(park_completed_2022)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Bja7pTARe75CA9pOmcxUGDvJ': ['Funding'], 'var_call_h8hClp5qJNJCMUWLpOEnlc88': ['civic_docs'], 'var_call_ioD2RgS2AHr6dPkZgxhwGBDO': [], 'var_call_f6nLGQzT9j7mybou2uxQzV9K': 'file_storage/call_f6nLGQzT9j7mybou2uxQzV9K.json'}

exec(code, env_args)
