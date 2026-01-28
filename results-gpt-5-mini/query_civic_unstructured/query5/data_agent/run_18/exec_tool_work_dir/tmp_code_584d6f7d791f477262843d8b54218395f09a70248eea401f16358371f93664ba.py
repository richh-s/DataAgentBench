code = """import json, re

# Load data from storage file paths
with open(var_call_YS26z9RmPiwh9URIcyLFwcMU, 'r') as f:
    funding = json.load(f)
with open(var_call_CuWWMHKQbQV54zgtnv13awLt, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and project names
for r in funding:
    # convert Amount to int
    try:
        r['Amount'] = int(r['Amount'])
    except:
        r['Amount'] = 0
    r['Project_Name_norm'] = r['Project_Name'].strip()

# Disaster-related keywords
keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'caloes', 'fema/caloes']

candidates = []
for r in funding:
    name_lower = r['Project_Name_norm'].lower()
    if any(k in name_lower for k in keywords):
        candidates.append(r)

# Helper to produce base name without parenthesis content
def base_name(name):
    return re.sub(r"\s*\(.*?\)", "", name).strip()

# Search civic docs for evidence of starting in 2022
results = []
for r in candidates:
    pname = r['Project_Name_norm']
    bname = base_name(pname)
    found_2022 = False
    evidence_texts = []
    pattern_list = [re.escape(pname), re.escape(bname)]
    # also try shorter tokens
    tokens = [t for t in re.split(r"[\-–,:]", bname) if len(t.strip())>4]
    for t in tokens:
        pattern_list.append(re.escape(t.strip()))
    for doc in civic_docs:
        text = doc.get('text','')
        text_low = text.lower()
        for pat in pattern_list:
            if re.search(pat, text, re.IGNORECASE):
                # find all matches and inspect surrounding context
                for m in re.finditer(pat, text, re.IGNORECASE):
                    start = max(0, m.start()-300)
                    end = min(len(text), m.end()+300)
                    window = text[start:end]
                    win_low = window.lower()
                    # check for '2022' in window and presence of start/completion keywords
                    if '2022' in win_low:
                        # check for start-related keywords
                        if any(k in win_low for k in ['begin', 'start', 'advertise', 'construction was completed', 'complete construction', 'complete design', 'construction was completed','complete construction','advertise:','begin construction','begin construction:','complete construction:','advertise:','begin construction']) or '2022' in win_low:
                            found_2022 = True
                            evidence_texts.append(window)
                            break
                if found_2022:
                    break
        if found_2022:
            break
    results.append({
        'Project_Name': pname,
        'Base_Name': bname,
        'Amount': r['Amount'],
        'Started_in_2022': found_2022,
        'Evidence_Count': len(evidence_texts),
        'Evidence_Snippets': evidence_texts[:3]
    })

# Sum amounts for those started_in_2022
total = sum(r['Amount'] for r in results if r['Started_in_2022'])

output = {'total_funding': total, 'currency': 'USD', 'projects': [r for r in results if r['Started_in_2022']]}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_eDlcBPVAHojmCpmT3kgYYERw': ['civic_docs'], 'var_call_37PrqiPgWW2wdgicaRoAlM4D': ['Funding'], 'var_call_YS26z9RmPiwh9URIcyLFwcMU': 'file_storage/call_YS26z9RmPiwh9URIcyLFwcMU.json', 'var_call_CuWWMHKQbQV54zgtnv13awLt': 'file_storage/call_CuWWMHKQbQV54zgtnv13awLt.json'}

exec(code, env_args)
