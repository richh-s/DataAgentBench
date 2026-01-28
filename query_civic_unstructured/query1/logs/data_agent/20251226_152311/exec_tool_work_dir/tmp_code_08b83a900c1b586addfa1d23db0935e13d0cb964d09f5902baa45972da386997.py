code = """import json
import pandas as pd
# Load funding projects with Amount > 50000
with open(var_call_NWPE1FVL5DPnVPDBsz8XhNCF, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic docs containing project descriptions
with open(var_call_MWNXnclc3CApthjDZTY4QP5D, 'r') as f:
    civic_docs = json.load(f)

# Project names from funding
funded_projects = set(funding_df['Project_Name'])

# We'll search each document's text for projects with 'design' status and type 'capital'.
import re
capital_design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '').lower()
    # Find blocks with likely project info
    # Extract project status, type, name when status = design and type = capital
    # Heuristic: lines with project name, followed by 'design' and 'capital' keywords nearby
    for line in text.split('\n'):
        if 'design' in line and 'capital' in line:
            # Try to extract project name heuristically (words before 'design' in line)
            match = re.match(r'(.*?)\s*(?:\(|-|:)?.*design.*capital.*', line)
            if match:
                pname = match.group(1).strip()
                if pname:
                    capital_design_projects.add(pname.title())
    # More robust: look for lines that mention 'design' and then get prev line as project name
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        if ('design' in line) and ('capital' in line):
            if idx > 0:
                pname = lines[idx-1].strip()
                if pname:
                    capital_design_projects.add(pname.title())
        # Also, look for pattern: '<project name> (Design)' or 'Design:'
        des_match = re.match(r'(.*)\s*\(design\)', line)
        if des_match:
            pname = des_match.group(1).strip()
            if pname:
                capital_design_projects.add(pname.title())
        des_match2 = re.match(r'design:\s*(.*)', line)
        if des_match2:
            pname = des_match2.group(1).strip()
            if pname:
                capital_design_projects.add(pname.title())

# Now, filter funded projects to those both funded (>50K) and detected as capital-design
relevant_projects = funded_projects.intersection(capital_design_projects)
result = len(relevant_projects)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NWPE1FVL5DPnVPDBsz8XhNCF': 'file_storage/call_NWPE1FVL5DPnVPDBsz8XhNCF.json', 'var_call_MWNXnclc3CApthjDZTY4QP5D': 'file_storage/call_MWNXnclc3CApthjDZTY4QP5D.json'}

exec(code, env_args)
