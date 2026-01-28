code = """import json, re
p = var_call_wImwkSyb52z6GhaPMqPSk2rh
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)
funding = var_call_Wlgp12VUKqh9IND6xpl3l483

def norm(s):
    return re.sub(r'[^a-z0-9]+',' ', s.lower()).strip()

completed = set()
# search by funding project names occurrence near 'completed' and '2022'
for doc in docs:
    text = doc.get('text','')
    low = text.lower()
    for rec in funding:
        name = rec['Project_Name']
        name_short = re.sub(r'\s*\(.*?\)','', name)
        name_short = re.sub(r'\bproject\b','', name_short, flags=re.I).strip()
        variants = [name, name_short]
        found_flag = False
        for var in variants:
            if not var or len(var) < 3:
                continue
            idx = low.find(var.lower())
            if idx != -1:
                start = max(0, idx-200)
                end = min(len(text), idx+len(var)+200)
                window = text[start:end]
                if re.search(r'completed', window, re.I) and re.search(r'2022', window):
                    completed.add(name)
                    found_flag = True
                    break
        if found_flag:
            continue
    # general park patterns
    for m in re.finditer(r'([A-Z][A-Za-z0-9 &\-]{0,80}Park(?: [A-Za-z0-9 &\-]*)?)', text):
        span = m.span()
        start = max(0, span[0]-200)
        end = min(len(text), span[1]+200)
        window = text[start:end]
        if re.search(r'completed', window, re.I) and re.search(r'2022', window):
            name = m.group(1).strip()
            completed.add(name)

# now match funding records
matched = []
total = 0
for rec in funding:
    pname = rec['Project_Name']
    np = norm(pname)
    matched_flag = False
    for c in completed:
        if not c:
            continue
        nc = norm(c)
        # if normalized names overlap or one contains the other
        if nc and (nc in np or np in nc):
            matched_flag = True
            break
    if matched_flag:
        try:
            amt = int(rec['Amount'])
        except:
            try:
                amt = int(float(rec['Amount']))
            except:
                amt = 0
        total += amt
        matched.append(pname)

out = {"completed_projects": sorted(list(completed)), "matched_funding_projects": matched, "total_funding": total}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_wImwkSyb52z6GhaPMqPSk2rh': 'file_storage/call_wImwkSyb52z6GhaPMqPSk2rh.json', 'var_call_QIxgPloYIKXLSebWZMiRw7nK': [], 'var_call_Wlgp12VUKqh9IND6xpl3l483': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}]}

exec(code, env_args)
