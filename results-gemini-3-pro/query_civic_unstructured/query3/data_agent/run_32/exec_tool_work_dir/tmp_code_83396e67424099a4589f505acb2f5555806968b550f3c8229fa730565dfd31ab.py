code = """import json
import sqlite3
import pandas as pd
import re

# Load previous results
funding_file = locals()['var_function-call-5036986330958495032']
civic_docs_file = locals()['var_function-call-5036986330958492415']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

full_text = chr(10).join([doc['text'] for doc in civic_docs_data])
lines = full_text.splitlines()

funding_df = pd.DataFrame(funding_data)
results = []
keywords = ['emergency', 'FEMA']

# Map lines to sections
sections = []
current_section = None

# Regex for detecting headers
# Matches: "Capital Improvement Projects (Design)", "Disaster Projects (Completed)", etc.
header_pattern = re.compile(r'(Capital Improvement|Disaster) Projects \((.*?)\)', re.IGNORECASE)

for line in lines:
    l_strip = line.strip()
    match = header_pattern.search(l_strip)
    if match:
        status_raw = match.group(2).lower()
        if 'design' in status_raw:
            current_section = 'design'
        elif 'construction' in status_raw:
            current_section = 'construction'
        elif 'completed' in status_raw:
            current_section = 'completed'
        elif 'not started' in status_raw:
            current_section = 'not started'
        else:
            # Fallback for unknown status in parens?
            current_section = status_raw
    sections.append(current_section)

# Search for projects
for index, row in funding_df.iterrows():
    proj_name = row['Project_Name']
    
    found_idx = -1
    # precise matching
    for i, line in enumerate(lines):
        if proj_name.lower() in line.lower():
            if len(line.strip()) < len(proj_name) + 20:
                found_idx = i
                break
    
    # Fallback: clean name
    if found_idx == -1:
        clean_name = re.sub(r'\s*\(.*?\)', '', proj_name)
        if clean_name and len(clean_name) > 5:
            for i, line in enumerate(lines):
                if clean_name.lower() in line.lower():
                    if len(line.strip()) < len(clean_name) + 20:
                        found_idx = i
                        break
    
    if found_idx != -1:
        section_status = sections[found_idx]
        
        # Extract block
        block_text = []
        for j in range(found_idx, len(lines)):
            l = lines[j].strip()
            # Stop at next section header
            if header_pattern.search(l) and j != found_idx:
                break
            
            # Stop at likely next project
            if j > found_idx and len(block_text) > 0:
                is_bullet = l.startswith('(cid:') or l.startswith('Updates:') or l.startswith('Project Schedule:')
                is_page = 'Page ' in l or 'Agenda Item' in l or l == ''
                if not is_bullet and not is_page:
                    break
            
            block_text.append(lines[j])
        
        full_block = chr(10).join(block_text)
        
        # Check relevance
        is_relevant = False
        for kw in keywords:
            if kw.lower() in proj_name.lower() or kw.lower() in full_block.lower():
                is_relevant = True
                break
        
        if is_relevant:
            final_status = section_status
            
            # Refine status if 'construction'
            if section_status == 'construction':
                if 'completed' in full_block.lower() or 'notice of completion' in full_block.lower():
                    final_status = 'completed'
                elif 'under construction' in full_block.lower():
                    final_status = 'under construction' # Keep descriptive or map to 'design'/'completed'? 
                    # User prompt: "Projects have three statuses: 'design', 'completed', 'not started'".
                    # If I must conform:
                    # 'under construction' is neither. But closer to 'design' (active)?
                    # Or maybe I should output 'design' if active?
                    # Let's output 'under construction' to be safe/accurate, 
                    # or 'design' if strictness is required.
                    # Given the examples in the hint, I will output 'design' for active construction 
                    # ONLY IF I am forced. But I am not. I will output 'under construction'.
                    # WAIT. The user says "Projects have three statuses...". This implies these are the legal values.
                    # I should map 'construction' to one of them.
                    # Construction is "Post-Design".
                    # Is it "Completed"? No.
                    # Is it "Not Started"? No.
                    # Is it "Design"? No.
                    # Maybe "design" -> "In Progress" in the user's mind?
                    # Let's look at "Bluffs Park Shade Structure". Status: Completed.
                    # "Malibu Road Slope Repairs". Status: Construction.
                    # I'll stick to 'construction' if I can't map it to 'completed'.
                    pass
            
            results.append({
                'Project_Name': proj_name,
                'Funding_Source': row['Funding_Source'],
                'Amount': row['Amount'],
                'Status': final_status
            })

# Remove duplicates (if same project found multiple times due to multiple docs or multiple matches)
# We use a dict keyed by Project Name to keep distinct
unique_results = {}
for r in results:
    unique_results[r['Project_Name']] = r

final_list = list(unique_results.values())

print('__RESULT__:')
print(json.dumps(final_list))"""

env_args = {'var_function-call-11141337925117404384': ['civic_docs'], 'var_function-call-11141337925117405097': ['Funding'], 'var_function-call-3665847163097728255': 'file_storage/function-call-3665847163097728255.json', 'var_function-call-3665847163097727678': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-5036986330958495032': 'file_storage/function-call-5036986330958495032.json', 'var_function-call-5036986330958492415': 'file_storage/function-call-5036986330958492415.json', 'var_function-call-7781814033299394491': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}], 'var_function-call-15801149106909399056': ['Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvement Projects and Disaster Recovery Projects.', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'variety of Public Works statistics, including Projects Under Design, Citizen Request,', 'Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvements Projects and Disaster Recovery Projects.', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Completed)', 'Disaster Projects (Design)', 'Disaster Projects (Construction)', 'Disaster Projects (Completed)', 'Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvements Projects and Disaster Recovery Projects.', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Completed)', 'Capital Improvement Projects (Not Started)', 'Disaster Projects (Design)', 'Disaster Projects (Construction)', 'Disaster Projects (Completed)', 'Disaster Projects (Not Started)', 'Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvements Projects and Disaster Recovery Projects.', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Projects (Design)', 'Disaster Projects (Construction)', 'Disaster Projects (Completed)', 'Disaster Projects (Not Started)', 'Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvements Projects and Disaster Recovery Projects.', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Completed)', 'Disaster Projects (Design)', 'Disaster Projects (Construction)', 'Disaster Projects (Completed)']}

exec(code, env_args)
