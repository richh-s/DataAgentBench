code = """import json
# Read the previous result
with open(var_call_6zkugduQQuZpetqCjeyZQVw4, 'r') as f:
    data = json.load(f)

# We want to produce a cleaned, unique list
out = []
seen = set()
for r in data:
    name = r.get('Project_Name')
    fs = r.get('Funding_Source')
    amt = r.get('Amount')
    st = r.get('Status')
    # normalize status values
    if st is None:
        stnorm = None
    else:
        stl = st.lower()
        if 'design' in stl:
            stnorm = 'design'
        elif 'complete' in stl:
            stnorm = 'completed'
        elif 'under construction' in stl:
            stnorm = 'under construction'
        else:
            stnorm = st
    key = (name, fs, amt, stnorm)
    if key in seen:
        continue
    seen.add(key)
    out.append({'Project_Name': name, 'Funding_Source': fs, 'Amount': amt, 'Status': stnorm})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5oztQ1h43QJsRueRDMVuuaAK': 'file_storage/call_5oztQ1h43QJsRueRDMVuuaAK.json', 'var_call_saeTDqEPUE7OFPW1yq9NfDlk': 'file_storage/call_saeTDqEPUE7OFPW1yq9NfDlk.json', 'var_call_6zkugduQQuZpetqCjeyZQVw4': [{'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000, 'Status': None}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000, 'Status': None}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': None}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': None}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': None}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': None}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000, 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000, 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'design'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'design'}, {'Project_Name': 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'Funding_Source': 'Research Institution Funding', 'Amount': 84000, 'Status': None}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000, 'Status': 'completed'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000, 'Status': 'completed'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'completed'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'completed'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'completed'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'completed'}, {'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': 73000, 'Status': 'completed'}]}

exec(code, env_args)
