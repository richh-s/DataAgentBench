code = """import re, json
from collections import defaultdict

# Load funding data (already JSON-serializable list)
funding_records = var_call_aWXHrDQQUf81FCBRaRJ7h8IJ

# Build a lookup of project names with funding > 50000
funding_projects = {rec['Project_Name'] for rec in funding_records if int(rec['Amount']) > 50000}

# Load civic docs text; if it's a filepath string, open it
civic_data = var_call_Qs94OMR5gYtC2IDDwUZOajyx
if isinstance(civic_data, str):
    import pathlib, json as _json
    civic_data = _json.load(open(civic_data, 'r'))

texts = [d['text'] for d in civic_data]
full_text = '\n'.join(texts)

# Heuristic parsing: find sections under "Capital Improvement Projects (Design)" and similar markers
# We'll extract project lines from the Design section only

# Normalize spaces
norm_text = re.sub(r'\r', '', full_text)

# Find "Capital Improvement Projects (Design)" section
design_sections = []
for m in re.finditer(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects|$)', norm_text, flags=re.S):
    design_sections.append(m.group(1))

design_projects = set()
for sec in design_sections:
    # Split into lines and look for lines that look like project names: non-empty, not starting with bullets or parentheses, and not generic words
    for line in sec.split('\n'):
        line = line.strip()
        if not line:
            continue
        # Filter out obvious non-project lines
        if any(line.startswith(prefix) for prefix in ('Updates', 'Project', 'Estimated', 'Advertise', 'Begin', 'Complete', 'City ', 'Staff ', 'Page ', 'Agenda Item', '(')):
            continue
        # Heuristic: treat lines with at least 2 words and containing a capital letter as project names
        if len(line.split()) >= 2 and re.search(r'[A-Z]', line):
            design_projects.add(line)

# Also look for project lists where status words appear inline, e.g., "(Design)" after project name
for m in re.finditer(r'\n([^\n]+?)\s*\(Design\)', norm_text):
    name = m.group(1).strip()
    if len(name.split()) >= 2:
        design_projects.add(name)

# Now cross-reference with funding projects and filter to type 'capital'.
# Heuristic: assume any project mentioned in Capital Improvement Projects sections is capital.
capital_design_with_funding = {name for name in design_projects if name in funding_projects}

result_count = len(capital_design_with_funding)

print('__RESULT__:')
print(json.dumps(result_count))"""

env_args = {'var_call_aWXHrDQQUf81FCBRaRJ7h8IJ': 'file_storage/call_aWXHrDQQUf81FCBRaRJ7h8IJ.json', 'var_call_Qs94OMR5gYtC2IDDwUZOajyx': 'file_storage/call_Qs94OMR5gYtC2IDDwUZOajyx.json'}

exec(code, env_args)
