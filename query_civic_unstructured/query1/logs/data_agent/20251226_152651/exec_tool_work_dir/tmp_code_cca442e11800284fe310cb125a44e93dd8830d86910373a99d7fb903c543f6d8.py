code = """import json
with open(var_call_vD4zEmrG487DkCnRuuc8jrW7, 'r') as f:
    funding_projects = json.load(f)
project_names = set([p['Project_Name'] for p in funding_projects])

with open(var_call_lanOkBXfzRQGOCcSYpVNQvY3, 'r') as f:
    civic_texts = [d['text'] for d in json.load(f)]

# Find projects mentioned in design phase and match with project_names
import re
matching_projects = set()
for text in civic_texts:
    # Find blocks mentioning status/design
    # Approach: Find all lines with "Capital Improvement Projects (Design)" or similar sections
    # and extract project names within those blocks
    lines = text.split('\n')
    in_design_section = False
    for line in lines:
        if re.search(r'Capital Improvement Projects.*\(Design\)', line):
            in_design_section = True
        elif re.search(r'Capital Improvement Projects', line) and not re.search(r'\(Design\)', line):
            in_design_section = False
        if in_design_section:
            # Attempt to extract the project name (Look for header lines, e.g. "PCH Median Improvements Project")
            m = re.match(r'^([A-Za-z0-9 &()-]+?)( Updates:|$)', line)
            if m:
                name = m.group(1).strip()
                # Fuzzy match for project names in funding_projects
                for fund_name in project_names:
                    # Lowercase for matching, remove extra chars for comparison
                    if name and name.lower() in fund_name.lower():
                        matching_projects.add(fund_name)

# Now, the number of unique projects with funding > $50,000 AND 'design' status is:
result = len(matching_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vD4zEmrG487DkCnRuuc8jrW7': 'file_storage/call_vD4zEmrG487DkCnRuuc8jrW7.json', 'var_call_lanOkBXfzRQGOCcSYpVNQvY3': 'file_storage/call_lanOkBXfzRQGOCcSYpVNQvY3.json'}

exec(code, env_args)
