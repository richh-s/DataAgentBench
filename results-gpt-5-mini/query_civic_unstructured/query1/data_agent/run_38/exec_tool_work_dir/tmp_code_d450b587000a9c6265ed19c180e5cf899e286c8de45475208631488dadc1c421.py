code = """import json
import re

# Load stored results from previous tool calls

# var_call_JHnX4q0HQXa5dfcycSQwhe9L and var_call_DlC638WHnZUqSOKzZuMXVzCj are file paths for large results

def load_var(var):
    if isinstance(var, str):
        # try to open as file path
        try:
            with open(var, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            # maybe it's a small JSON string
            try:
                return json.loads(var)
            except Exception:
                return var
    else:
        return var

civic_docs = load_var(var_call_JHnX4q0HQXa5dfcycSQwhe9L)
funding = load_var(var_call_DlC638WHnZUqSOKzZuMXVzCj)

# Helper to clean amount string to int
def to_int_amount(x):
    if x is None:
        return 0
    s = str(x)
    s = re.sub(r"[^0-9.-]", "", s)
    try:
        return int(float(s))
    except Exception:
        return 0

# Extract project names under 'Capital Improvement Projects (Design)'
design_projects = set()
headers_patterns = [r"Capital Improvement Projects \(Design\)", r"Capital Improvement Projects \(Design\):?", r"Capital Improvement Projects \(Design\)\s*"]
stop_patterns = [r"Capital Improvement Projects \(Construction\)", r"Capital Improvement Projects \(Not Started\)", r"Capital Improvement Projects \(Construction\):?", r"Capital Improvement Projects \(Not Started\):?", r"Capital Improvement Projects \(Construction\)", r"Capital Improvement Projects \(Not Started\)", r"Capital Improvement Projects \(Construction\)", r"Capital Improvement Projects \(Not Started\)", r"Capital Improvement Projects \(Construction\)"]
# More generic stops
generic_stops = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Capital Improvement Projects (Construction)"]

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    # search for design header positions
    # case-insensitive
    matches = [m.start() for m in re.finditer(r"Capital Improvement Projects \(Design\)", text, flags=re.IGNORECASE)]
    for start in matches:
        # slice from header end
        sub = text[start:]
        # find end where construction or not started section begins
        end_match = re.search(r"Capital Improvement Projects \((Construction|Not Started)\)", sub, flags=re.IGNORECASE)
        end_idx = end_match.start() if end_match else None
        section = sub if end_idx is None else sub[:end_idx]
        # split into lines and pick candidate project lines
        lines = [ln.strip() for ln in section.splitlines()]
        # skip the header line itself
        if len(lines) > 0:
            # find index of header line
            header_idx = None
            for i,l in enumerate(lines):
                if re.search(r"Capital Improvement Projects \(Design\)", l, flags=re.IGNORECASE):
                    header_idx = i
                    break
            if header_idx is None:
                header_idx = 0
            # collect subsequent lines as project names until a blank or known keywords
            for l in lines[header_idx+1:]:
                if not l:
                    continue
                # stop if we hit known section markers
                if re.search(r"Capital Improvement Projects \((Construction|Not Started)\)", l, flags=re.IGNORECASE):
                    break
                # ignore lines that look like bullets or markers
                if l.lower().startswith('(cid:') or l.lower().startswith('page'):
                    continue
                # ignore lines that are headings like 'Updates:' or 'Project Schedule:'
                if re.search(r"^(updates|project schedule|page|recommended action|discussion):?", l.lower()):
                    continue
                # ignore lines that are sentences (contain ':' or end with '.') but project names may also have punctuation
                # Heuristic: if line contains more than 6 words and contains verbs like 'staff', 'city', treat as paragraph
                words = l.split()
                if len(words) > 6 and any(w.lower() in ('staff','city','project','plans','construction','design','complete','advertise','begin','work','working') for w in words[:6]):
                    continue
                # also ignore lines that start with words like 'Complete Design' etc
                if re.match(r'^(complete|advertise|begin)\b', l.lower()):
                    continue
                # Otherwise, treat as project name candidate
                # Remove trailing punctuation
                candidate = l.strip(':').strip()
                # Avoid lines that are single words like 'Page' or 'Item'
                if len(candidate.split()) < 2:
                    continue
                design_projects.add(candidate)

# Now process funding records into dict summing amounts for exact project names
funding_map = {}
for row in funding:
    pname = row.get('Project_Name')
    amt = to_int_amount(row.get('Amount'))
    if pname in funding_map:
        funding_map[pname] += amt
    else:
        funding_map[pname] = amt

# For each design project, check funding
qualified = []
for proj in sorted(design_projects):
    amt = funding_map.get(proj, 0)
    if amt > 50000:
        qualified.append({'Project_Name': proj, 'Amount': amt})

result = {'count': len(qualified), 'projects': qualified}

import sys
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cPS60iHJJy96p63wJ9oRmb8U': ['civic_docs'], 'var_call_ZHmSGv5JNRwXoGfcDdbRp0sh': ['Funding'], 'var_call_DlC638WHnZUqSOKzZuMXVzCj': 'file_storage/call_DlC638WHnZUqSOKzZuMXVzCj.json', 'var_call_JHnX4q0HQXa5dfcycSQwhe9L': 'file_storage/call_JHnX4q0HQXa5dfcycSQwhe9L.json'}

exec(code, env_args)
