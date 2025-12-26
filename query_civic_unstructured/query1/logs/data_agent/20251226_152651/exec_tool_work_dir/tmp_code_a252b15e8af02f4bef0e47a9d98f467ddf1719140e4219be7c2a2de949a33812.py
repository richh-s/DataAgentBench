code = """import json
with open(var_call_vD4zEmrG487DkCnRuuc8jrW7, 'r') as f:
    funding_projects = json.load(f)
project_names = set([p['Project_Name'] for p in funding_projects])

with open(var_call_lanOkBXfzRQGOCcSYpVNQvY3, 'r') as f:
    civic_texts = [d['text'] for d in json.load(f)]

# Find projects in the "(Design)" phase and match with funding names
import re
matching_projects = set()
for text in civic_texts:
    lines = text.split('\n')
    in_design_section = False
    for line in lines:
        if re.search(r'Capital Improvement Projects \(Design\)', line):
            in_design_section = True
            continue
        # End section at next header or blank line after section start
        if in_design_section and (re.match(r'^\s*$', line) or re.search(r'Capital Improvement Projects', line)):
            in_design_section = False
        if in_design_section:
            # Look for likely project name line
            m = re.match(r'^([A-Za-z0-9 &\-().]+?)( Updates:|$)', line)
            if m:
                name = m.group(1).strip()
                if name and len(name) > 3:
                    # Fuzzy match with funded project names
                    for fund_name in project_names:
                        # Lowercase for comparison
                        if name.lower() in fund_name.lower():
                            matching_projects.add(fund_name)

result = len(matching_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vD4zEmrG487DkCnRuuc8jrW7': 'file_storage/call_vD4zEmrG487DkCnRuuc8jrW7.json', 'var_call_lanOkBXfzRQGOCcSYpVNQvY3': 'file_storage/call_lanOkBXfzRQGOCcSYpVNQvY3.json'}

exec(code, env_args)
