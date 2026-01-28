code = """import json

# Load civic docs and funding data from storage file paths
with open(var_call_QNC7P8mjljZASGfnnZi9S4PP, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_jifqAMOUNn9PorNbe5w6A4Vg, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Check if any document mentions park, completed, and 2022
texts = [d.get('text','') for d in civic_docs]
park_completed_2022_docs = [t for t in texts if 'park' in t.lower() and 'completed' in t.lower() and '2022' in t]

matched_fund_records = []
if park_completed_2022_docs:
    for rec in funding:
        pname = rec.get('Project_Name','')
        if 'park' in pname.lower() or 'playground' in pname.lower():
            matched_fund_records.append(rec)

# Sum amounts
total = 0
matched_details = []
for rec in matched_fund_records:
    amt = rec.get('Amount', 0)
    try:
        val = int(str(amt))
    except:
        try:
            val = int(float(str(amt)))
        except:
            val = 0
    total += val
    matched_details.append({'Project_Name': rec.get('Project_Name',''), 'Amount': val})

if matched_details:
    msg = f"Total funding for park-related projects completed in 2022: ${total}"
else:
    msg = "Total funding for park-related projects completed in 2022: $0"

print("__RESULT__:")
print(json.dumps(msg))"""

env_args = {'var_call_hrawrctsouX7uyMEWqR3rdZM': ['civic_docs'], 'var_call_vr3n5PyiecSjEweMrZb1UBzg': ['Funding'], 'var_call_QNC7P8mjljZASGfnnZi9S4PP': 'file_storage/call_QNC7P8mjljZASGfnnZi9S4PP.json', 'var_call_jifqAMOUNn9PorNbe5w6A4Vg': 'file_storage/call_jifqAMOUNn9PorNbe5w6A4Vg.json'}

exec(code, env_args)
