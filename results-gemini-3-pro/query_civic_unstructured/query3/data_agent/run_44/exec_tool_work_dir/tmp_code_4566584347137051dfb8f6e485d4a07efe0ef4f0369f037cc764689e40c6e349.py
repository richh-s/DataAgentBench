code = """import json
import pandas as pd
import re

# Keys
key_funding = locals()['var_function-call-12539470358665637498']
key_docs = locals()['var_function-call-12539470358665634517']

# Load Funding
with open(key_funding, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Docs
with open(key_docs, 'r') as f:
    docs_data = json.load(f)

texts = []
for d in docs_data:
    texts.append(d.get('text', ''))
full_text = chr(10).join(texts)

keywords = ['emergency', 'fema']

def get_tokens(s):
    if not s: return set()
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s.lower())
    return set(s.split())

def is_related(text):
    if not text: return False
    t = text.lower()
    return any(k in t for k in keywords)

lines = full_text.split(chr(10))
projects_list = []

section_headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

# Map sections
section_map = {}
for i, line in enumerate(lines):
    l = line.strip()
    for h in section_headers:
        if h in l:
            section_map[i] = h

sorted_sections = sorted(section_map.items())

for i, line in enumerate(lines):
    if "Updates:" in line or "Project Description:" in line:
        j = i - 1
        while j >= 0 and not lines[j].strip():
            j -= 1
        
        if j < 0: continue
        title = lines[j].strip()
        
        p_section = "Unknown"
        last_idx = -1
        for idx, name in sorted_sections:
            if idx < j and idx > last_idx:
                last_idx = idx
                p_section = name
        
        content_lines = []
        for k in range(i, len(lines)):
            if k > i and ("Updates:" in lines[k] or "Project Description:" in lines[k]):
                break
            if any(h in lines[k] for h in section_headers):
                break
            content_lines.append(lines[k])
        
        content = " ".join(content_lines)
        
        status = "not started"
        if "Design" in p_section:
            status = "design"
        elif "Construction" in p_section:
            if "completed" in content.lower():
                status = "completed"
            else:
                status = "construction"
        elif "Not Started" in p_section:
            status = "not started"
            
        projects_list.append({
            'title': title,
            'tokens': get_tokens(title),
            'status': status,
            'content': content
        })

results = []
for _, row in df_funding.iterrows():
    f_name = row['Project_Name']
    f_tokens = get_tokens(f_name)
    
    # Match
    matched_p = None
    best_overlap = 0
    
    for p in projects_list:
        p_tokens = p['tokens']
        if not f_tokens or not p_tokens: continue
        
        # Check subset or high overlap
        common = f_tokens.intersection(p_tokens)
        
        # If funding name is subset of project title (e.g. "Park" in "Park Improvements") -> risky
        # If project title is subset of funding name (e.g. "Park Improvements" in "Park Improvements (FEMA)") -> good
        
        # We want high Jaccard or subset match
        # Let's use strict subset for the Base Name
        # If p_tokens is subset of f_tokens (since f_name might have suffixes)
        # AND len(p_tokens) covers most of f_tokens (excluding suffixes which we removed in get_tokens)
        
        # Actually get_tokens removed (FEMA...), so they should be very similar.
        
        score = len(common) / len(f_tokens.union(p_tokens))
        if score > 0.8: # high match
            matched_p = p
            break
        
        # Also check if p_tokens is subset of f_tokens (or vice versa)
        if p_tokens.issubset(f_tokens) and len(p_tokens) >= len(f_tokens) - 1:
             matched_p = p
             break
        if f_tokens.issubset(p_tokens) and len(f_tokens) >= len(p_tokens) - 1:
             matched_p = p
             break

    related = False
    if is_related(f_name):
        related = True
    if matched_p and (is_related(matched_p['content']) or is_related(matched_p['title'])):
        related = True
        
    if related:
        st = matched_p['status'] if matched_p else "not started"
        results.append({
            "Project_Name": f_name,
            "Funding_Source": row['Funding_Source'],
            "Amount": row['Amount'],
            "Status": st
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3750553953043117850': ['Funding'], 'var_function-call-3750553953043118673': ['civic_docs'], 'var_function-call-12539470358665637498': 'file_storage/function-call-12539470358665637498.json', 'var_function-call-12539470358665634517': 'file_storage/function-call-12539470358665634517.json', 'var_function-call-10065264714784678123': 'file_storage/function-call-10065264714784678123.json', 'var_function-call-9873514450190324949': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'design'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'design'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}]}

exec(code, env_args)
