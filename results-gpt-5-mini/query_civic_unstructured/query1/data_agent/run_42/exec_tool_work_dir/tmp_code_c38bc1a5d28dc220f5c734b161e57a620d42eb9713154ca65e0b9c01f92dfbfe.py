code = """import json, re

# Load results from previous tool calls stored in files
with open(var_call_2fT1eOIBqHwk4SP7blH2OZs8, 'r') as f:
    funding_records = json.load(f)
with open(var_call_kgGbjsawYRuEoq22ztIB5F46, 'r') as f:
    civic_docs = json.load(f)

# Extract 'Capital Improvement Projects (Design)' sections from civic documents
design_projects = []
pattern = re.compile(r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Capital Improvement Projects \(Construction\)|$)", re.DOTALL | re.IGNORECASE)
for doc in civic_docs:
    text = doc.get('text','')
    for m in pattern.finditer(text):
        section = m.group(1)
        # Split into lines and pick candidate project name lines
        for line in section.splitlines():
            s = line.strip()
            if not s:
                continue
            # Skip lines that look like metadata or headings
            if s.startswith('(') or s.endswith(':'):
                continue
            low = s.lower()
            if any(keyword in low for keyword in ['updates', 'project schedule', 'page', 'agenda', 'recommended action', 'discussion', 'item', 'approved by', 'prepared by', 'date prepared', 'meeting date']):
                continue
            # Likely a project name
            design_projects.append(s)

# Deduplicate and clean
def normalize_name(s):
    s = s or ''
    s = re.sub(r"\s*\([^)]*\)", "", s)  # remove parenthetical content
    s = re.sub(r"[^A-Za-z0-9& ]+", " ", s)  # remove punctuation except &
    s = s.lower()
    s = re.sub(r"\s+", " ", s).strip()
    return s

design_projects = [d for d in design_projects]
# Normalize and unique
norm_design = {normalize_name(d): d for d in design_projects}

# Process funding records with Amount > 50000 (ensure numeric)
funding_names = set()
for r in funding_records:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_num = int(str(amt).replace(',', '').strip())
    except:
        try:
            amt_num = int(float(amt))
        except:
            continue
    if amt_num > 50000:
        funding_names.add(normalize_name(name))

# Count how many design projects have funding > 50000
matched = []
for nd, orig in norm_design.items():
    if nd in funding_names:
        matched.append(orig)

count = len(matched)

# Prepare output
output = {
    'count': count,
    'matched_projects': matched
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_2fT1eOIBqHwk4SP7blH2OZs8': 'file_storage/call_2fT1eOIBqHwk4SP7blH2OZs8.json', 'var_call_kgGbjsawYRuEoq22ztIB5F46': 'file_storage/call_kgGbjsawYRuEoq22ztIB5F46.json'}

exec(code, env_args)
