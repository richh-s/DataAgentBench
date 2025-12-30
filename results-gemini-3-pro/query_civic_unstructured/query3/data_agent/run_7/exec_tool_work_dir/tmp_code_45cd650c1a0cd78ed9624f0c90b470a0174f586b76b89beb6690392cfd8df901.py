code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-16505334197824858844'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-5478402608851220705'], 'r') as f:
    civic_docs = json.load(f)

# Extract date and sort documents
def get_date(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        d = match.group(1)
        # MMDDYYYY -> YYYYMMDD for sorting
        return d[4:] + d[0:2] + d[2:4]
    return "00000000"

civic_docs.sort(key=lambda x: get_date(x.get('filename', '')), reverse=False) # Oldest to Newest

# Combine text? No, process sequentially to update status
# Actually, if I join them, I lose the ability to know which section belongs to which doc/date?
# Wait, if I join them, I have:
# Doc1 ... Header ... Projects ... Doc2 ... Header ... Projects ...
# The `lines` iteration will encounter headers and update `current_status`.
# So sequential processing of joined text (ordered by date) works naturally, 
# assuming headers are present in each doc.
# Yes, "Capital Improvement Projects (Design)" appears in each doc.
# So if Doc1 has Project A under Design, Project Map gets A=Design.
# Then Doc2 has Project A under Construction, Project Map gets A=Construction.
# This works.

text_list = [doc.get('text', '') for doc in civic_docs]
full_text = chr(10).join(text_list)

# Prepare Project Names
project_names = funding_df['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

# Parsing Text
lines = full_text.split(chr(10))
current_status = 'unknown'
project_map = {} # Name -> {status, context}

status_headers = {
    'Capital Improvement Projects (Design)': 'design',
    'Capital Improvement Projects (Construction)': 'construction_section',
    'Capital Improvement Projects (Not Started)': 'not started'
}

current_project = None
current_project_context = []

def save_current_project():
    if current_project:
        final_status = current_status
        context_str = ' '.join(current_project_context).lower()
        
        if current_status == 'construction_section':
            if 'completed' in context_str or 'notice of completion' in context_str:
                final_status = 'completed'
            else:
                final_status = 'under construction'
        
        # Check topic relevance
        is_relevant_topic = False
        keywords = ['fema', 'emergency', 'fire', 'disaster', 'caloes']
        if any(k in context_str for k in keywords):
            is_relevant_topic = True
            
        # Update map (overwrite with latest status/info)
        # We should preserve 'relevant_topic' if it was ever true? 
        # Or just use the latest context? 
        # Usually topic doesn't change, but context might be smaller in updates.
        # Let's check: if it was relevant before, keep it relevant?
        # But if the project matches by name, we re-evaluate.
        # Let's assume the latest report has the full context or sufficient context.
        
        project_map[current_project] = {
            'status': final_status,
            'relevant_topic': is_relevant_topic
        }

for line in lines:
    clean_line = line.strip()
    if not clean_line:
        continue
        
    # Check for Headers
    is_header = False
    for header, status in status_headers.items():
        if header in clean_line:
            save_current_project()
            current_project = None
            current_project_context = []
            current_status = status
            is_header = True
            break
    if is_header:
        continue

    # Check for Project Name match
    found_project = None
    if current_status != 'unknown':
        for name in project_names:
            if clean_line == name:
                found_project = name
                break
            if name in clean_line and len(clean_line) < len(name) + 10:
                 found_project = name
                 break
    
    if found_project:
        save_current_project()
        current_project = found_project
        current_project_context = []
    else:
        if current_project:
            current_project_context.append(clean_line)

save_current_project()

# Merge and Filter
results = []
for index, row in funding_df.iterrows():
    p_name = row['Project_Name']
    
    # Relevance Check
    name_relevant = 'fema' in p_name.lower() or 'emergency' in p_name.lower()
    
    # Status/Topic from Text
    p_data = project_map.get(p_name)
    
    if p_data:
        status = p_data['status']
        topic_relevant = p_data['relevant_topic']
    else:
        status = 'unknown'
        topic_relevant = False
        
    if (name_relevant or topic_relevant) and status != 'unknown':
        results.append({
            'Project_Name': p_name,
            'Funding_Source': row['Funding_Source'],
            'Amount': row['Amount'],
            'Status': status
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-16505334197824856773': 'file_storage/function-call-16505334197824856773.json', 'var_function-call-16505334197824858844': 'file_storage/function-call-16505334197824858844.json', 'var_function-call-5478402608851220705': 'file_storage/function-call-5478402608851220705.json', 'var_function-call-16425645266247422134': [{'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000', 'Status': 'not started'}, {'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'Status': 'not started'}, {'Project_Name': 'Malibu Road Slope Repairs', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}]}

exec(code, env_args)
