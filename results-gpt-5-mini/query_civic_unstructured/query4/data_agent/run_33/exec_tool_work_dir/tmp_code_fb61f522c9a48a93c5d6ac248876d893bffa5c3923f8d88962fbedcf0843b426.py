code = """import json
import re
import pandas as pd

# Load the civic docs JSON result file (path provided in storage variable)
with open(var_call_XmOcMyV6dDzMk79hkziBnoRT, 'r') as f:
    civic_docs = json.load(f)

with open(var_call_6tLrAYAZs645eaZFYiy7sB7E, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
# Ensure Amount is integer
fund_df['Amount'] = fund_df['Amount'].astype(str).str.replace(',', '').str.strip()
fund_df['Amount'] = fund_df['Amount'].apply(lambda x: int(x) if x and x.isdigit() else int(float(x)) if x else 0)

spring_months = ['march', 'april', 'may']
found_projects = []

undesirable_patterns = [r'^\s*Updates', r'^\s*Project Schedule', r'^\s*Page', r'^\s*Agenda', r'^\s*Item', r'^\s*To:', r'^\s*Subject:', r'^\s*Prepared by', r'^\s*Approved by', r'^\s*Date prepared']
undesirable_re = re.compile('|'.join(undesirable_patterns), re.I)

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        lower = line.lower()
        match = False
        # check for explicit 'Spring 2022'
        if re.search(r'\bspring\b.*2022|2022.*\bspring\b', line, re.I):
            match = True
        # check for month names in Spring with 2022
        if not match and any(m in lower and '2022' in lower for m in spring_months):
            match = True
        # check for patterns like 'Begin Construction: Spring 2022' or similar
        if not match and re.search(r'begin\s+construction\b.*2022|advertise\b.*2022|complete\s+design\b.*2022', line, re.I):
            # ensure that it's in spring months or contains 'spring'
            if re.search(r'\bspring\b', line, re.I) or any(m in lower and '2022' in lower for m in spring_months):
                match = True
        if match:
            # find previous non-empty candidate line up to 8 lines above
            candidate = None
            for j in range(i-1, max(-1, i-9), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                if undesirable_re.search(cand):
                    continue
                # skip short lines
                if len(cand) < 5:
                    continue
                # skip lines that are clearly schedule labels
                if re.search(r'project schedule|updates|estimated schedule|project description', cand, re.I):
                    continue
                candidate = cand
                break
            if candidate:
                # clean candidate
                candidate = re.sub(r'\(cid:[0-9]+\)', '', candidate).strip()
                # sometimes candidate may be like 'Capital Improvement Projects (Design)' - skip if contains 'Capital Improvement'
                if re.search(r'capital improvement|disaster recovery|capital improvement projects', candidate, re.I):
                    # try a bit further up
                    for j in range(j-1, max(-1, i-12), -1):
                        cand2 = lines[j].strip()
                        if not cand2:
                            continue
                        if undesirable_re.search(cand2):
                            continue
                        if len(cand2) < 5:
                            continue
                        if re.search(r'capital improvement', cand2, re.I):
                            continue
                        candidate = cand2
                        break
                if candidate:
                    found_projects.append(candidate)

# Deduplicate preserving order
seen = set()
unique_projects = []
for p in found_projects:
    if p not in seen:
        seen.add(p)
        unique_projects.append(p)

# Now match with funding table
matched = []
total_funding = 0
for p in unique_projects:
    # exact match in funding
    rows = fund_df[fund_df['Project_Name'] == p]
    if not rows.empty:
        amt = int(rows['Amount'].sum())
        matched.append({'Project_Name': p, 'Funding': int(amt)})
        total_funding += int(amt)
    else:
        # try case-insensitive exact
        rows = fund_df[fund_df['Project_Name'].str.lower() == p.lower()]
        if not rows.empty:
            amt = int(rows['Amount'].sum())
            matched.append({'Project_Name': p, 'Funding': int(amt)})
            total_funding += int(amt)
        else:
            # try contains
            rows = fund_df[fund_df['Project_Name'].str.contains(re.escape(p), case=False, na=False)]
            if not rows.empty:
                amt = int(rows['Amount'].sum())
                matched.append({'Project_Name': p, 'Funding': int(amt)})
                total_funding += int(amt)
            else:
                # no funding found, include with 0
                matched.append({'Project_Name': p, 'Funding': 0})

result = {
    'project_count': len(unique_projects),
    'total_funding': int(total_funding),
    'projects': matched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xF9qG9hjLwVG5yPC88s9AZmq': ['civic_docs'], 'var_call_DtKC2JHnfELFsMnXXT60pZhj': ['Funding'], 'var_call_XmOcMyV6dDzMk79hkziBnoRT': 'file_storage/call_XmOcMyV6dDzMk79hkziBnoRT.json', 'var_call_6tLrAYAZs645eaZFYiy7sB7E': 'file_storage/call_6tLrAYAZs645eaZFYiy7sB7E.json'}

exec(code, env_args)
