code = """import json

# Load civic docs from provided file path variable
civic_path = var_call_0GxLFGimWWtyZ5EaoIHD7wLd
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Funding disaster subset is already a list variable
funding_disaster = var_call_ea85tKtXX7OrXJ0RVlXbPtMc

# Combine civic docs text into one lowercase string
parts = []
for d in civic_docs:
    t = d.get('text', '')
    if t:
        parts.append(t.lower())
full_text = '\n'.join(parts)

# Helper to parse amount
def to_int(x):
    s = str(x)
    digits = ''.join(ch for ch in s if ch.isdigit())
    return int(digits) if digits else 0

selected = []
for r in funding_disaster:
    name = r.get('Project_Name', '')
    name_norm = name.lower()
    amt = to_int(r.get('Amount', 0))
    # check if project name itself contains 2022
    name_has_2022 = '2022' in name_norm
    # search occurrences in full_text
    found_2022_near = False
    start = 0
    while True:
        idx = full_text.find(name_norm, start)
        if idx == -1:
            break
        wstart = max(0, idx-300)
        wend = min(len(full_text), idx+300)
        snippet = full_text[wstart:wend]
        if '2022' in snippet:
            found_2022_near = True
            break
        start = idx + 1
    started_2022 = name_has_2022 or found_2022_near
    if started_2022:
        selected.append({'Project_Name': name, 'Amount': amt})

total = sum(p['Amount'] for p in selected)
out = {'total_funding': total, 'count_projects': len(selected), 'projects': selected}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zOxJAXyiUvuRoRPWatEiq5lx': 'file_storage/call_zOxJAXyiUvuRoRPWatEiq5lx.json', 'var_call_0GxLFGimWWtyZ5EaoIHD7wLd': 'file_storage/call_0GxLFGimWWtyZ5EaoIHD7wLd.json', 'var_call_fWleDfLyPaPnAG17iseqd9Gk': {'test': True}, 'var_call_ea85tKtXX7OrXJ0RVlXbPtMc': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_call_Hk11LDCMWp9Xv0ho4ndZ3l27': [['var_call_zOx', 'str'], ['var_call_0Gx', 'str'], ['var_call_ea8', 'list']], 'var_call_0GQnjacg23ejCVxDSddrLa5x': {'total_funding': 0, 'count_projects': 0, 'projects': []}}

exec(code, env_args)
