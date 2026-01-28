code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_4qeuULn4ldVjtXVJC5qwtIuw, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_T4qx94sHR0XKvOGNqrXeGexd, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
ff = pd.DataFrame(funding)
if 'Amount' in ff.columns:
    def parse_amount(x):
        try:
            return int(str(x).replace(',', '').strip())
        except:
            try:
                return int(float(str(x)))
            except:
                return 0
    ff['Amount'] = ff['Amount'].apply(parse_amount)
else:
    ff['Amount'] = 0

# Define park-related keywords to filter funding projects
park_keywords = ['park', 'playground', 'bluffs', 'malibu bluffs', 'malibu park', 'legacy park', 'point dume', 'trancas canyon', 'walkway', 'bench', 'benches', 'arbor', 'playground']

# Filter funding rows where Project_Name contains any park keyword
def is_park_project(name):
    if not isinstance(name, str):
        return False
    nl = name.lower()
    for kw in park_keywords:
        if kw in nl:
            return True
    return False

park_fundings = ff[ff['Project_Name'].apply(is_park_project)].to_dict(orient='records')

# Helper to check if project is marked completed in 2022 in civic docs

def project_completed_in_2022(project_name, civic_docs):
    pn = project_name.lower()
    for doc in civic_docs:
        text = doc.get('text','').lower()
        # look for exact project name mention
        idx = text.find(pn)
        if idx != -1:
            window = text[max(0, idx-200): idx+500]
            if 'completed' in window and '2022' in window:
                return True
        # if not found, try keyword-based nearby search
        for kw in ['bluffs park', 'park', 'playground', 'walkway', 'point dume', 'trancas canyon']:
            kidx = text.find(kw)
            if kidx != -1:
                window = text[max(0, kidx-200): kidx+500]
                if 'completed' in window and '2022' in window:
                    # additional check: ensure project_name or parts of it appear nearby or kw is specific enough
                    # check if some token from project_name appears in the window
                    tokens = [t for t in pn.split() if len(t)>3]
                    matched = any(t in window for t in tokens[:4])
                    if matched:
                        return True
                    # allow for generic "Bluffs Park Shade Structure" matching 'bluffs' + 'shade' etc
                    if kw in ['bluffs park','point dume','trancas canyon']:
                        return True
    return False

projects_completed_2022 = []
for rec in park_fundings:
    pname = rec.get('Project_Name','')
    amt = int(rec.get('Amount',0))
    if project_completed_in_2022(pname, civic_docs):
        projects_completed_2022.append({'Project_Name': pname, 'Amount': amt})

# As a fallback, also check for projects that may be park-related but named differently in funding table
# For example, 'Bluffs Park Shade Structure' might be named slightly differently; we already matched that via keywords.

total = sum(p['Amount'] for p in projects_completed_2022)

result = {'total': total, 'projects': projects_completed_2022}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gcJLvKaO5Gvc3U8w2HX0wx8m': ['civic_docs'], 'var_call_T4qx94sHR0XKvOGNqrXeGexd': 'file_storage/call_T4qx94sHR0XKvOGNqrXeGexd.json', 'var_call_AcArUDNAjzLRe1mYou5z2T2n': ['Funding'], 'var_call_4qeuULn4ldVjtXVJC5qwtIuw': 'file_storage/call_4qeuULn4ldVjtXVJC5qwtIuw.json'}

exec(code, env_args)
