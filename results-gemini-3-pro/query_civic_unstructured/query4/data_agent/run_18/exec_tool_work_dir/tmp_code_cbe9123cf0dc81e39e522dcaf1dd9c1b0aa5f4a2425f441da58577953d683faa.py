code = """import json
import re

# Access file paths
funding_path = locals()['var_function-call-8816954503851875086']
civic_docs_path = locals()['var_function-call-11062513582446324049']

with open(funding_path) as f:
    funding_data = json.load(f)
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

full_text = chr(10).join([doc['text'] for doc in civic_docs])
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower()
    if "spring 2022" in date_str or "spring, 2022" in date_str:
        return True
    if "spring of 2022" in date_str:
        return True
    if "2022" in date_str:
        if any(m in date_str for m in ["march", "april", "may"]):
            return True
    return False

def get_start_date(project_name, text):
    # Enforce roughly full line match
    # (?m) enables multiline. ^ and $ match start/end of line.
    # We allow some whitespace.
    # Note: Regex characters in project_name need escaping.
    escaped_name = re.escape(project_name)
    pattern = r"(?m)^\s*" + escaped_name + r"\s*$"
    
    matches = [m.start() for m in re.finditer(pattern, text)]
    
    start_dates = []
    
    # Validation keywords
    valid_keywords = ["Updates", "Project Schedule", "Estimated Schedule", "Project Description", "Status", "Schedule"]
    
    date_patterns = [
        r"Begin [Cc]onstruction:?\s*([A-Za-z0-9, ]+)",
        r"Start [Dd]ate:?\s*([A-Za-z0-9, ]+)",
        r"Construction [Ss]tart:?\s*([A-Za-z0-9, ]+)",
        r"Construction to begin:?\s*([A-Za-z0-9, ]+)",
    ]
    
    for start_idx in matches:
        # Check context
        chunk = text[start_idx:start_idx+1000]
        
        # Validate it's a project section
        # Check if any keyword appears in the first 300 chars (headers usually close)
        # Actually, "Updates:" is usually the first thing.
        if not any(k in chunk[:400] for k in valid_keywords):
            continue
            
        for pat in date_patterns:
            m = re.search(pat, chunk)
            if m:
                raw_date = m.group(1).split(chr(10))[0].strip()
                start_dates.append(raw_date)
                
    return start_dates

projects_started_spring_2022 = []

for project_name, amount in funding_map.items():
    dates = get_start_date(project_name, full_text)
    
    # Check dates
    valid_dates = [d for d in dates if is_spring_2022(d)]
    
    if valid_dates:
        projects_started_spring_2022.append({
            "Project_Name": project_name,
            "Amount": amount,
            "Dates_Found": valid_dates
        })

count = len(projects_started_spring_2022)
total_funding = sum(p['Amount'] for p in projects_started_spring_2022)

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "total_funding": total_funding,
    "projects": projects_started_spring_2022
}))"""

env_args = {'var_function-call-13891692615433348012': 'file_storage/function-call-13891692615433348012.json', 'var_function-call-8816954503851875086': 'file_storage/function-call-8816954503851875086.json', 'var_function-call-11062513582446324049': 'file_storage/function-call-11062513582446324049.json', 'var_function-call-2552348695982729751': {'count': 20, 'total_funding': 1105000, 'projects': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': 24000, 'Dates_Found': ['Spring 2022', 'Spring 2022']}, {'Project_Name': 'Annual Street Maintenance', 'Amount': 23000, 'Dates_Found': ['Spring 2022', 'Spring 2022']}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': 21000, 'Dates_Found': ['Spring 2022', 'Spring 2022']}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': 87000, 'Dates_Found': ['Spring 2022', 'Spring 2022']}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': 81000, 'Dates_Found': ['Spring 2022', 'Spring 2022']}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Amount': 45000, 'Dates_Found': ['March 2022', 'March 2022']}, {'Project_Name': 'Discussion', 'Amount': 80000, 'Dates_Found': ['Spring 2022']}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 34000, 'Dates_Found': ['Spring 2022', 'Spring 2022']}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': 94000, 'Dates_Found': ['Spring 2022', 'Spring 2022']}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Amount': 57000, 'Dates_Found': ['April 2022', 'Spring 2022', 'Spring 2022', 'Spring 2022']}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': 36000, 'Dates_Found': ['April 2022', 'Spring 2022']}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': 44000, 'Dates_Found': ['Spring 2022', 'Spring 2022']}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Amount': 19000, 'Dates_Found': ['April 2022', 'Spring 2022', 'Spring 2022']}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': 91000, 'Dates_Found': ['April 2022', 'Spring 2022', 'Spring 2022']}, {'Project_Name': 'Marie Canyon Green Streets', 'Amount': 50000, 'Dates_Found': ['Spring 2022']}, {'Project_Name': 'Recommended Action', 'Amount': 86000, 'Dates_Found': ['Spring 2022']}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': 78000, 'Dates_Found': ['Spring 2022']}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': 44000, 'Dates_Found': ['Spring 2022']}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': 68000, 'Dates_Found': ['Spring 2022']}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': 43000, 'Dates_Found': ['Spring 2022']}]}}

exec(code, env_args)
