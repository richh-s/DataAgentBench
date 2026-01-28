code = """import json
import re
import pandas as pd

# Load data files from storage keys
with open(var_call_GFKuGiEUWp4gojAfgOX0vlGM, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_IA052drrJgZbeYVgVDV4ItOX, 'r') as f:
    funding = json.load(f)

# Convert funding to DataFrame
fund_df = pd.DataFrame(funding)
# Ensure Amount numeric
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster-related keywords
keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey']

# Helper to normalize project name
def normalize(name):
    if not isinstance(name, str):
        return ''
    name = re.sub(r"\(.*?\)", "", name)  # remove parentheses content
    return re.sub(r"\s+", " ", name).strip().lower()

# Build documents list with lowercase text
docs = []
for doc in civic_docs:
    text = doc.get('text','') or ''
    filename = doc.get('filename','') or ''
    docs.append({'filename': filename.lower(), 'text': text.lower()})

matches = []

for _, row in fund_df.iterrows():
    pname = row['Project_Name']
    pname_l = (pname or '').lower()
    # Determine if disaster-related
    is_disaster = any(k in pname_l for k in keywords)
    src = str(row.get('Funding_Source','') or '').lower()
    if not is_disaster and any(k in src for k in keywords + ['federal assistance']):
        is_disaster = True
    if not is_disaster:
        continue

    # Determine if started in 2022
    started_2022 = False
    core = normalize(pname)
    if '2022' in pname_l:
        started_2022 = True
    else:
        for d in docs:
            text = d['text']
            if core and core in text:
                # search window around occurrences for '2022'
                for m in re.finditer(re.escape(core), text):
                    start = max(0, m.start()-200)
                    end = min(len(text), m.end()+200)
                    window = text[start:end]
                    if '2022' in window:
                        started_2022 = True
                        break
                if started_2022:
                    break
            # also consider filename date hints
            if d['filename'] and '2022' in d['filename'] and core and core in text:
                started_2022 = True
                break
    if started_2022:
        matches.append({'Project_Name': pname, 'Amount': int(row['Amount'])})

# Sum amounts
total = sum(m['Amount'] for m in matches)

output = {'total_disaster_funding_started_2022': total, 'matched_records': matches}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_WdAUq4FdzXMRWPpkrBvinOIF': ['civic_docs'], 'var_call_wwSjWegAh834UWWjF6AXP8TA': ['Funding'], 'var_call_GFKuGiEUWp4gojAfgOX0vlGM': 'file_storage/call_GFKuGiEUWp4gojAfgOX0vlGM.json', 'var_call_IA052drrJgZbeYVgVDV4ItOX': 'file_storage/call_IA052drrJgZbeYVgVDV4ItOX.json'}

exec(code, env_args)
