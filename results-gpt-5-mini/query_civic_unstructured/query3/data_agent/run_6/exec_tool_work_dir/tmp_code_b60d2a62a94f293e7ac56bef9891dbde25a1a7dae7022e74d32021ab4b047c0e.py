code = """import json, os
# Load processed results from previous execute_python stored under var_call_sav05sLYsUhVocITeKBvTyAS
data_var = var_call_sav05sLYsUhVocITeKBvTyAS
if isinstance(data_var, str):
    with open(data_var, 'r') as f:
        records = json.load(f)
else:
    records = data_var

# Filter for projects related to 'fema' or 'emergency'
filtered = []
for r in records:
    pname = str(r.get('Project_Name',''))
    fsrc = str(r.get('Funding_Source',''))
    low = (pname + ' ' + fsrc).lower()
    if 'fema' in low or 'emergency' in low:
        # ensure amount formatting
        amt = r.get('Amount')
        try:
            amt_int = int(amt) if amt is not None else None
        except:
            try:
                amt_int = int(float(amt))
            except:
                amt_int = None
        filtered.append({
            'Project_Name': pname,
            'Funding_Source': fsrc,
            'Amount': amt_int,
            'Status': r.get('Status','unknown')
        })

# Sort by Project_Name
filtered_sorted = sorted(filtered, key=lambda x: x['Project_Name'].lower())

# Build plain-text lines
lines = []
for rec in filtered_sorted:
    amt = rec['Amount']
    amt_str = f"${amt:,}" if isinstance(amt, int) else "Unknown"
    lines.append(f"{rec['Project_Name']} — {rec['Funding_Source']} — {amt_str} — {rec['Status']}")

if not lines:
    answer_text = "No projects related to 'emergency' or 'FEMA' were found."
else:
    answer_text = "\n".join(lines)

# Print according to required format
print("__RESULT__:")
print(json.dumps(answer_text))"""

env_args = {'var_call_igZlSbiLWjIZqU8d0FYKe2z4': 'file_storage/call_igZlSbiLWjIZqU8d0FYKe2z4.json', 'var_call_cQ1zQFelFE9RnIqGqbRuGGrR': 'file_storage/call_cQ1zQFelFE9RnIqGqbRuGGrR.json', 'var_call_sav05sLYsUhVocITeKBvTyAS': 'file_storage/call_sav05sLYsUhVocITeKBvTyAS.json'}

exec(code, env_args)
