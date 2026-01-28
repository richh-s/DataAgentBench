code = """import json, re, pandas as pd

# Load the funding records JSON from storage file path
with open(var_call_V5tPW2YmUA5d53igvDX358wY, 'r') as f:
    funding = json.load(f)

# Load civic docs
with open(var_call_qZCZflz698EG5IY7DVwKGCSV, 'r') as f:
    civic_docs = json.load(f)

# Convert funding to DataFrame
df_f = pd.DataFrame(funding)
# Ensure Amount numeric
df_f['Amount'] = df_f['Amount'].astype(int)

# Identify disaster-related funding rows by name patterns
pattern_disaster = re.compile(r'FEMA|CALOES|CalOES|CalJPIA|FEMA/CalOES|FEMA\\)|FEMA\b|FEMA/CalOES|Disaster|Fire|Woolsey', re.IGNORECASE)

# Normalize project names for matching: create base name without parentheses suffix
def base_name(name):
    return re.sub(r"\s*\(.*?\)\s*$", "", name).strip()

civic_texts = [d.get('text','').lower() for d in civic_docs]

results = []

for _, row in df_f.iterrows():
    pname = row['Project_Name']
    if pattern_disaster.search(pname):
        base = base_name(pname).lower()
        found_in_docs = False
        started_2022 = False
        matched_contexts = []
        # search each civic doc for base name
        for text in civic_texts:
            if base in text:
                found_in_docs = True
                # find all occurrences and check nearby context for 2022
                for m in re.finditer(re.escape(base), text):
                    start = m.start()
                    # context window
                    window_start = max(0, start-500)
                    window_end = min(len(text), m.end()+500)
                    window = text[window_start:window_end]
                    # Search for year 2022 in window and also schedule keywords near year
                    if '2022' in window:
                        # further ensure it's in a schedule-like context: look for Begin, Start, Construction, Complete, Advertise within +/-100 chars
                        sched_window = text[max(0, start-200):min(len(text), m.end()+200)]
                        if re.search(r'begin|start|construction|complete|adverti|project schedule|project is currently under construction', sched_window, re.IGNORECASE) or re.search(r'\b2022\b', sched_window):
                            started_2022 = True
                            matched_contexts.append(window)
        results.append({
            'Project_Name': pname,
            'Base_Name': base,
            'Amount': int(row['Amount']),
            'Found_In_Docs': found_in_docs,
            'Started_2022': started_2022,
            'Matched_Contexts_Count': len(matched_contexts)
        })

# Also consider projects that might be disaster-related by topic keywords in civic docs but not labeled in funding table with FEMA etc.
# For simplicity, we limit to funding rows with disaster patterns as above.

# Sum amounts for those marked Started_2022
total = sum(r['Amount'] for r in results if r['Started_2022'])

output = {'total_funding_started_2022': total, 'details': results}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Px1SCEumI3Sg4B0yBj6rqeaG': ['civic_docs'], 'var_call_rFMLtbhBpfactT6c9D21zrXM': ['Funding'], 'var_call_qZCZflz698EG5IY7DVwKGCSV': 'file_storage/call_qZCZflz698EG5IY7DVwKGCSV.json', 'var_call_V5tPW2YmUA5d53igvDX358wY': 'file_storage/call_V5tPW2YmUA5d53igvDX358wY.json'}

exec(code, env_args)
