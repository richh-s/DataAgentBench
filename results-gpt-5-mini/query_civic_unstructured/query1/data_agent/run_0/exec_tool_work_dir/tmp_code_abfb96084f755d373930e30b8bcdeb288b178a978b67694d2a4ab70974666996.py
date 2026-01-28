code = """import json
import string

def load_var(v):
    if isinstance(v, str):
        try:
            with open(v, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return v
    return v

funding = load_var(var_call_SdeIzpwHWXTGbiSgCGNZzY8M)
docs = load_var(var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV)

# Build combined design section text
design_texts = []
for doc in docs:
    text = doc.get('text', '')
    lower = text.lower()
    marker = 'capital improvement projects (design)'
    idx = lower.find(marker)
    if idx == -1:
        continue
    # find end markers
    end1 = lower.find('capital improvement projects (construction)', idx+1)
    end2 = lower.find('capital improvement projects (not started)', idx+1)
    ends = [p for p in (end1, end2) if p != -1]
    end = min(ends) if ends else None
    section = text[idx + len(marker): end] if end else text[idx + len(marker):]
    design_texts.append(section)

combined = '\n'.join(design_texts).lower()

# normalize function to remove punctuation and extra spaces
trans = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

def normalize(s):
    return ' '.join(s.lower().translate(trans).split())

norm_combined = normalize(combined)

# Check each funding project with Amount > 50000 (these were in funding list)
count = 0
matched_projects = []
for rec in funding:
    pname = rec.get('Project_Name', '').strip()
    if not pname:
        continue
    np = normalize(pname)
    if not np:
        continue
    # also try removing parenthetical suffixes
    p_no_paren = pname.split('(')[0].strip()
    np2 = normalize(p_no_paren)
    # match if normalized project name string appears in combined design text
    if np in norm_combined or np2 in norm_combined:
        count += 1
        matched_projects.append(pname)

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_SdeIzpwHWXTGbiSgCGNZzY8M': 'file_storage/call_SdeIzpwHWXTGbiSgCGNZzY8M.json', 'var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV': 'file_storage/call_fJ8zcOtfuMJb3QVTDXZxf5ZV.json'}

exec(code, env_args)
