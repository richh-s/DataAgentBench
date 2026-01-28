code = """import json
import pandas as pd
import re

# Load funding data
funding_data = pd.read_json(locals()['var_function-call-8349484065091426871'])
project_names = set(funding_data['Project_Name'].str.strip().tolist())

# Load doc text
with open(locals()['var_function-call-9085321241350089186'], 'r') as f:
    docs = json.load(f)

extracted_projects = []

# Regex for date in filename (MMDDYYYY)
date_pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

def parse_doc_date(filename):
    match = date_pattern.search(filename)
    if match:
        m, d, y = match.groups()
        return pd.to_datetime(f"{y}-{m}-{d}")
    return pd.to_datetime("1900-01-01") # Default if not found

for doc in docs:
    text = doc['text']
    filename = doc.get('filename', '')
    doc_date = parse_doc_date(filename)
    
    lines = text.split('\\n')
    
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        if line_clean in project_names:
            current_project = line_clean
        
        if current_project:
            lower_line = line_clean.lower()
            if "begin construction" in lower_line:
                parts = line_clean.split(':')
                if len(parts) > 1:
                    date_str = parts[-1].strip()
                    extracted_projects.append({
                        "Project_Name": current_project,
                        "st": date_str,
                        "doc_date": doc_date
                    })
                    current_project = None

df_extracted = pd.DataFrame(extracted_projects)

if not df_extracted.empty:
    # Sort by doc_date desc to keep latest info
    df_extracted = df_extracted.sort_values('doc_date', ascending=False)
    # Drop duplicates on Project_Name, keeping first (latest)
    df_latest = df_extracted.drop_duplicates(subset=['Project_Name'], keep='first')
    
    # Filter for Spring 2022
    def is_spring_2022(date_str):
        ds = date_str.lower()
        if "2022" not in ds:
            return False
        if "spring" in ds:
            return True
        # Check months: March, April, May
        if "march" in ds or "april" in ds or "may" in ds:
            return True
        return False

    df_spring_2022 = df_latest[df_latest['st'].apply(is_spring_2022)].copy()

    # Join with Funding
    # Funding data has Project_Name, Amount
    df_merged = df_spring_2022.merge(funding_data, on='Project_Name', how='inner')
    
    result_list = df_merged[['Project_Name', 'st', 'Amount']].to_dict(orient='records')
    
    total_funding = df_merged['Amount'].sum()
    count = len(df_merged)
    
    print("__RESULT__:")
    print(json.dumps({
        "projects": result_list,
        "count": count,
        "total_funding": int(total_funding)
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"projects": [], "count": 0, "total_funding": 0}))"""

env_args = {'var_function-call-3235961165398988678': 'file_storage/function-call-3235961165398988678.json', 'var_function-call-8349484065091426871': 'file_storage/function-call-8349484065091426871.json', 'var_function-call-1088354946493889427': [{'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'st': 'Fall 2023'}, {'Project_Name': 'PCH Median Improvements Project', 'st': 'Fall 2023'}, {'Project_Name': 'Westward Beach Road Repair Project', 'st': 'Fall 2023'}, {'Project_Name': 'Westward Beach Road Drainage Improvements Project', 'st': 'Fall 2023'}, {'Project_Name': 'Clover Heights Storm Drainage Improvements', 'st': 'Fall 2023'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'st': 'Summer 2023'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'st': 'Summer 2023'}, {'Project_Name': 'Permanent Skate Park', 'st': 'Winter 2024'}, {'Project_Name': 'PCH at Trancas Canyon Road Right Turn Lane', 'st': 'Fall 2023'}, {'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'st': 'April 2023'}, {'Project_Name': 'Storm Drain Trash Screens Phase Two', 'st': 'Summer 2023'}, {'Project_Name': 'Marie Canyon Green Streets', 'st': 'Spring 2022'}, {'Project_Name': 'PCH Median Improvements Project', 'st': 'Spring/Summer 2022'}, {'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'st': 'Spring/Summer 2022'}, {'Project_Name': 'Westward Beach Road Improvements Project', 'st': 'Summer/Winter 2022'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'st': 'Fall 2022'}, {'Project_Name': 'Bluffs Park Shade Structure', 'st': 'Spring 2022'}, {'Project_Name': 'Permanent Skate Park', 'st': 'To be determined'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'st': 'April 2022'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'st': 'April 2022'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'st': 'Fall 2022'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'st': 'Fall 2022'}, {'Project_Name': 'Marie Canyon Green Streets', 'st': 'Summer 2021'}, {'Project_Name': 'PCH Median Improvements Project', 'st': 'Fall 2021'}, {'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'st': 'September 2021'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure', 'st': 'Estimated Summer 2021'}, {'Project_Name': 'Westward Beach Road Improvements Project', 'st': 'Fall 2021'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'st': 'March 2022'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'st': 'Summer 2021'}, {'Project_Name': 'Annual Street Maintenance', 'st': 'Summer 2021'}, {'Project_Name': 'Bluffs Park Shade Structure', 'st': 'Fall 2021'}, {'Project_Name': 'Vehicle Protection Devices', 'st': 'Fall 2021'}, {'Project_Name': 'Malibu Road Slope Repairs', 'st': 'Winter 2021'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'st': 'Fall 2021'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'st': 'Summer/Fall 2021'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'st': 'Summer/Fall 2021'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'st': 'Summer 2021'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'st': 'Summer 2022'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Marie Canyon Green Streets', 'st': 'Summer 2021'}, {'Project_Name': 'PCH Median Improvements Project', 'st': 'Fall 2021'}, {'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'st': 'September 2021'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure', 'st': 'Estimated Summer 2021'}, {'Project_Name': 'Westward Beach Road Improvements Project', 'st': 'Fall 2021'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'st': 'March 2022'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'st': 'April 2021'}, {'Project_Name': 'Annual Street Maintenance', 'st': 'Summer 2021'}, {'Project_Name': 'Bluffs Park Shade Structure', 'st': 'Fall 2021'}, {'Project_Name': 'Vehicle Protection Devices', 'st': 'Fall 2021'}, {'Project_Name': 'Malibu Road Slope Repairs', 'st': 'Winter 2021'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'st': 'Fall 2021'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'st': 'Summer 2021'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'st': 'Summer/Fall 2021'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'st': 'Summer/Fall 2021'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'st': 'Summer 2021'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'st': 'Summer 2022'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Marie Canyon Green Streets', 'st': 'Summer 2022'}, {'Project_Name': 'PCH Median Improvements Project', 'st': 'Summer 2022'}, {'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'st': 'Summer 2022'}, {'Project_Name': 'Westward Beach Road Improvements Project', 'st': 'Fall/Winter 2022'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'st': 'Spring 2023'}, {'Project_Name': 'Bluffs Park Shade Structure', 'st': 'Spring 2022'}, {'Project_Name': 'Permanent Skate Park', 'st': 'To be determined'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'st': 'Summer 2022'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'st': 'Summer 2022'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'st': 'Summer 2022'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'st': 'Spring 2022'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'st': 'Fall 2022'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'st': 'Fall 2022'}], 'var_function-call-9085321241350089186': 'file_storage/function-call-9085321241350089186.json'}

exec(code, env_args)
