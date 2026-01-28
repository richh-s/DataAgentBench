code = """import json
import string

# Load stored results
with open(var_call_JB6TQEL3z93YnYHK9rnGpkHo, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_qNKgQ52ocQxIOP8yjhn1GgPu, 'r') as f:
    funding_rows = json.load(f)

# Build funding list (ensure amounts are ints)
funding_list = []
for r in funding_rows:
    name = r.get('Project_Name', '')
    amt = r.get('Amount', 0)
    try:
        amt_i = int(str(amt))
    except:
        continue
    if amt_i > 50000:
        funding_list.append({'name': name, 'amount': amt_i})

# helper to normalize text by removing punctuation and lowering
punct_trans = str.maketrans({p: ' ' for p in string.punctuation})

def norm_text(s):
    if not isinstance(s, str):
        return ''
    return s.lower().translate(punct_trans)

# helper to base name (remove parenthetical suffix)
def base_name(s):
    if not isinstance(s, str):
        return ''
    idx = s.find('(')
    if idx != -1:
        return s[:idx].strip()
    return s.strip()

matched_projects = []
seen = set()

for fr in funding_list:
    fname = fr['name']
    bname = base_name(fname).lower()
    if not bname:
        continue
    # normalized base name with punctuation removed
    nb = norm_text(bname)
    found = False
    for doc in civic_docs:
        text = doc.get('text', '')
        if not text:
            continue
        ntext = norm_text(text)
        pos = ntext.find(nb)
        if pos == -1:
            continue
        # if found, check if in Capital Improvement Projects (Design) section
        marker = 'capital improvement projects design'
        mpos = ntext.find(marker)
        in_design_section = False
        if mpos != -1:
            # find end markers
            end_markers = ['capital improvement projects construction', 'capital improvement projects not started']
            endpos = len(ntext)
            for em in end_markers:
                j = ntext.find(em, mpos + len(marker))
                if j != -1 and j < endpos:
                    endpos = j
            if pos >= mpos and pos < endpos:
                in_design_section = True
        # check context window for the word 'design' and 'capital'
        window_radius = 300
        start = max(0, pos - window_radius)
        end = min(len(ntext), pos + len(nb) + window_radius)
        context = ntext[start:end]
        has_design = 'design' in context
        has_capital = 'capital' in context or 'capital improvement' in context
        if in_design_section or (has_design and has_capital) or (has_design and 'project' in context):
            if nb not in seen:
                seen.add(nb)
                matched_projects.append({'project_name': base_name(fname), 'funding_amount': fr['amount']})
            found = True
            break
    # if not found in docs, continue

result = {'count': len(matched_projects), 'matched_projects': [p['project_name'] for p in matched_projects]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_qNKgQ52ocQxIOP8yjhn1GgPu': 'file_storage/call_qNKgQ52ocQxIOP8yjhn1GgPu.json', 'var_call_JB6TQEL3z93YnYHK9rnGpkHo': 'file_storage/call_JB6TQEL3z93YnYHK9rnGpkHo.json'}

exec(code, env_args)
