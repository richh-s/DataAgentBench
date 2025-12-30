code = """import json
import re
import pandas as pd

# Load Funding Data
with open(locals()['var_function-call-9061716743711808369'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open(locals()['var_function-call-12561724733303725061'], 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

def get_base_name(name):
    name = re.sub(r'\s*\(FEMA.*?\)', '', name)
    name = re.sub(r'\s*\(CalOES.*?\)', '', name)
    name = re.sub(r'\s*\(CalJPIA.*?\)', '', name)
    name = re.sub(r'\s*\(FEMA\)', '', name)
    return name.strip()

funding_df['base_name'] = funding_df['Project_Name'].apply(get_base_name)
unique_base_names = [n for n in funding_df['base_name'].unique() 
                     if n.lower() not in ['discussion', 'agenda', 'item', 'subject', 'report']]

project_details = {} # base_name -> {start_year, is_disaster_text}

for doc in civic_docs:
    text = doc.get('text', '')
    text = " ".join(text.splitlines())
    
    # Find all project positions
    positions = []
    for bn in unique_base_names:
        # Regex to ensure we match whole words if possible? 
        # But project names are long phrases. Literal match is usually fine.
        pattern = re.escape(bn)
        for match in re.finditer(pattern, text):
            positions.append({'pos': match.start(), 'name': bn})
            
    # Sort by position
    positions.sort(key=lambda x: x['pos'])
    
    # Iterate and extract segments
    for i in range(len(positions)):
        curr = positions[i]
        start_pos = curr['pos']
        # End pos is start of next project or end of text
        if i < len(positions) - 1:
            end_pos = positions[i+1]['pos']
        else:
            end_pos = len(text)
            
        # Extract segment
        # We start looking *after* the name? 
        # Actually the name is at start_pos. We want the text AFTER the name.
        segment_start = start_pos + len(curr['name'])
        segment = text[segment_start : end_pos]
        
        # Limit segment length to avoid huge blocks if names are far apart?
        # Say 2000 chars is fine now that we stop at next project.
        if len(segment) > 3000:
            segment = segment[:3000]
            
        # Analyze segment
        start_year = None
        date_match = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9, ]+)', segment)
        if date_match:
            date_str = date_match.group(1)
            y_match = re.search(r'20\d{2}', date_str)
            if y_match:
                start_year = int(y_match.group(0))
        
        is_disaster_text = False
        keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey Fire', 'Disaster', 'Emergency']
        for kw in keywords:
            if kw.lower() in segment.lower():
                is_disaster_text = True
                break
                
        # Store info
        bn = curr['name']
        if bn not in project_details:
             project_details[bn] = {'start_year': start_year, 'is_disaster_text': is_disaster_text}
        else:
            if start_year:
                project_details[bn]['start_year'] = start_year
            if is_disaster_text:
                project_details[bn]['is_disaster_text'] = True

total_funding = 0
debug_list = []

for _, row in funding_df.iterrows():
    base_name = row['base_name']
    if base_name.lower() in ['discussion', 'agenda', 'item', 'subject', 'report']:
        continue
        
    amount = row['Amount']
    orig_name = row['Project_Name']
    
    is_disaster_name = any(x in orig_name for x in ['FEMA', 'CalOES', 'CalJPIA'])
    
    details = project_details.get(base_name, {})
    is_disaster_text = details.get('is_disaster_text', False)
    start_year = details.get('start_year')
    
    is_disaster = is_disaster_name or is_disaster_text
    
    if is_disaster and start_year == 2022:
        total_funding += amount
        debug_list.append({'Project': orig_name, 'Amount': amount, 'Year': start_year})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'debug': debug_list}))"""

env_args = {'var_function-call-836211722748550531': ['civic_docs'], 'var_function-call-836211722748548546': ['Funding'], 'var_function-call-9061716743711809176': 'file_storage/function-call-9061716743711809176.json', 'var_function-call-9061716743711808369': 'file_storage/function-call-9061716743711808369.json', 'var_function-call-12561724733303725061': 'file_storage/function-call-12561724733303725061.json', 'var_function-call-12831751692515772825': {'total_funding': 1785000, 'debug': [{'Project': '2021 Annual Street Maintenance', 'Amount': 24000, 'Year': 2022}, {'Project': 'Annual Street Maintenance', 'Amount': 23000, 'Year': 2022}, {'Project': 'Birdview Avenue Improvements', 'Amount': 79000, 'Year': 2022}, {'Project': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': 85000, 'Year': 2022}, {'Project': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': 14000, 'Year': 2022}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': 87000, 'Year': 2022}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': 81000, 'Year': 2022}, {'Project': 'Civic Center Stormwater Diversion Structure', 'Amount': 64000, 'Year': 2022}, {'Project': 'Civic Center Way Improvements', 'Amount': 37000, 'Year': 2022}, {'Project': 'Corral Canyon Culvert Repairs', 'Amount': 54000, 'Year': 2022}, {'Project': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': 43000, 'Year': 2022}, {'Project': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': 15000, 'Year': 2022}, {'Project': 'Corral Canyon Road Bridge Repairs', 'Amount': 68000, 'Year': 2022}, {'Project': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': 25000, 'Year': 2022}, {'Project': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': 58000, 'Year': 2022}, {'Project': 'Encinal Canyon Road Drainage Improvements', 'Amount': 34000, 'Year': 2022}, {'Project': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': 18000, 'Year': 2022}, {'Project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': 94000, 'Year': 2022}, {'Project': 'Guardrail Replacement Citywide', 'Amount': 39000, 'Year': 2022}, {'Project': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': 22000, 'Year': 2022}, {'Project': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': 45000, 'Year': 2022}, {'Project': 'Latigo Canyon Road Culvert Repairs', 'Amount': 57000, 'Year': 2022}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': 36000, 'Year': 2022}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': 44000, 'Year': 2022}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Amount': 19000, 'Year': 2022}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': 91000, 'Year': 2022}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': 78000, 'Year': 2022}, {'Project': 'Malibu Park Drainage Improvements', 'Amount': 17000, 'Year': 2022}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': 78000, 'Year': 2022}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': 44000, 'Year': 2022}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': 92000, 'Year': 2022}, {'Project': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': 68000, 'Year': 2022}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': 43000, 'Year': 2022}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': 32000, 'Year': 2022}, {'Project': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': 77000, 'Year': 2022}]}}

exec(code, env_args)
