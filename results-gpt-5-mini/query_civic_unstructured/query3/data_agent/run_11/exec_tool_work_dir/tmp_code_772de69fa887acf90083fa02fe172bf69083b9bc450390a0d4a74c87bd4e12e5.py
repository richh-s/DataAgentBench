code = """import json, re
funding = var_call_xFUYNSWQQe0b7JtiSruERKuM
path = var_call_2ajh9JRnLUZjcgZaBU1zv32y
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

all_text = "\n\n".join(d.get('text','') for d in docs).lower()

def normalize_name(n):
    # remove parenthetical suffixes and extra whitespace
    base = re.sub(r"\s*\([^)]*\)\s*$", "", n)
    return re.sub(r"\s+", " ", base).strip().lower()

status_map = []
results = []
for fr in funding:
    pname = fr.get('Project_Name','')
    psource = fr.get('Funding_Source','')
    amount = fr.get('Amount', None)
    base = normalize_name(pname)
    status = 'not found'
    # try direct substring
    if base and base in all_text:
        # find context around first occurrence
        idx = all_text.find(base)
        start = max(0, idx-200)
        context = all_text[start: idx+200]
    else:
        # fallback: match by keywords - require 2 significant words match
        words = [w for w in re.split(r"\W+", base) if len(w)>3]
        found = False
        for i in range(len(words), 1, -1):
            # try join of first i words
            for j in range(0, max(1, len(words)-i+1)):
                chunk = ' '.join(words[j:j+i])
                if chunk and chunk in all_text:
                    idx = all_text.find(chunk)
                    start = max(0, idx-200)
                    context = all_text[start: idx+200]
                    found = True
                    break
            if found:
                break
        if not found:
            context = ''
    ctx = context.lower()
    # determine status from context
    if any(x in ctx for x in ['construction was completed','notice of completion','complete construction','completed,','completed', 'complete construction:']):
        status = 'completed'
    elif any(x in ctx for x in ['awaiting','awaiting final','awaiting approval','waiting for','not started','identified']):
        status = 'not started'
    elif any(x in ctx for x in ['preliminary design','working with the consultant to finalize the design','finalize the design','complete design','design phase','design is','project is in the preliminary design','begin construction','currently under construction','advertise','begin construction:','project is currently under construction']):
        status = 'design'
    else:
        # if we found any context but no keywords, set not started
        if ctx:
            status = 'not started'
        else:
            status = 'not started'
    # normalize amount to int if possible
    try:
        amt = int(amount)
    except:
        try:
            amt = int(float(amount))
        except:
            amt = None
    results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': amt, 'Status': status})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_2ajh9JRnLUZjcgZaBU1zv32y': 'file_storage/call_2ajh9JRnLUZjcgZaBU1zv32y.json', 'var_call_QLNYso6DCSC7NVUDNVKM3KbR': {'doc_count': 19}, 'var_call_xFUYNSWQQe0b7JtiSruERKuM': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
