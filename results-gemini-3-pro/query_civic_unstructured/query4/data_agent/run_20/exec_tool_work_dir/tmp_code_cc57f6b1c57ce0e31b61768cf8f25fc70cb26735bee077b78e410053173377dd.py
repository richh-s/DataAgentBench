code = """import json
import re

# Load data
with open(locals()['var_function-call-8460811092792669481'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-8460811092792670416'], 'r') as f:
    civic_docs = json.load(f)

# Funding map
funding_map = {item['Project_Name'].strip(): int(item['Amount']) for item in funding_data}
funding_names = list(funding_map.keys())
funding_names.sort(key=len, reverse=True)

debug_list = []

def check_date(d):
    d = d.lower()
    if '2022' not in d: return False
    if 'spring' in d: return True
    if 'march' in d or 'april' in d or 'may' in d: return True
    if '03/' in d or '04/' in d or '05/' in d: return True
    if '-03' in d or '-04' in d or '-05' in d: return True
    return False

for doc in civic_docs:
    text = doc['text']
    
    pattern = "Begin Construction\\s*[:]\\s*([^\\n]+)"
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    
    for m in matches:
        date_str = m.group(1).strip()
        if check_date(date_str):
            best_name = None
            best_idx = -1
            
            search_limit = max(0, m.start() - 5000)
            search_text = text[search_limit:m.start()]
            
            for name in funding_names:
                idx = search_text.rfind(name)
                if idx != -1:
                    abs_idx = search_limit + idx
                    if abs_idx > best_idx:
                        best_idx = abs_idx
                        best_name = name
            
            if best_name:
                debug_list.append({"project": best_name, "date": date_str})

print("__RESULT__:")
print(json.dumps(debug_list))"""

env_args = {'var_function-call-15438762544756245875': 'file_storage/function-call-15438762544756245875.json', 'var_function-call-15438762544756246872': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-8460811092792669481': 'file_storage/function-call-8460811092792669481.json', 'var_function-call-8460811092792670416': 'file_storage/function-call-8460811092792670416.json', 'var_function-call-8912619866491154738': {'count': 12, 'total_funding': 621000, 'projects': ['Marie Canyon Green Streets', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Bluffs Park Shade Structure', 'PCH Signal Synchronization System Improvements Project', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'PCH Median Improvements Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)']}}

exec(code, env_args)
