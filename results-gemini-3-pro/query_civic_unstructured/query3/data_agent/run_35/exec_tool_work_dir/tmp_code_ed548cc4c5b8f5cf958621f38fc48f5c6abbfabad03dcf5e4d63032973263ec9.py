code = """import json
import re
import pandas as pd

funding_path = locals()['var_function-call-7750960758477245626']
docs_path = locals()['var_function-call-3106554336237263291']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

def clean_name(name):
    name = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA|FEMA/CalOES).*?\)$', '', name)
    name = re.sub(r'\s*\((?:FEMA|CalOES)\)$', '', name)
    return name.strip()

df_funding['Base_Name'] = df_funding['Project_Name'].apply(clean_name)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

extracted = []

for doc in civic_docs:
    lines = [l.strip() for l in doc['text'].splitlines() if l.strip()]
    
    current_status = 'unknown'
    current_project_name = None
    current_project_text = []
    
    def save_project(name, text_lines, status):
        if not name: return
        full_text = ' '.join(text_lines)
        st = status
        if st == 'construction' and ('Construction was completed' in full_text or 'Notice of completion' in full_text):
            st = 'completed'
        
        base = clean_name(name)
        txt_lower = (name + ' ' + full_text).lower()
        is_rel = 'emergency' in txt_lower or 'fema' in txt_lower
        extracted.append({'Base_Name': base, 'status': st, 'is_rel': is_rel})

    i = 0
    while i < len(lines):
        line = lines[i]
        
        is_header = False
        new_status = None
        if "Capital Improvement Projects" in line:
            if "(Design)" in line: new_status = "design"
            elif "(Construction)" in line: new_status = "construction"
            elif "(Not Started)" in line: new_status = "not started"
            if new_status: is_header = True
        
        if is_header:
            save_project(current_project_name, current_project_text, current_status)
            current_project_name = None
            current_project_text = []
            current_status = new_status
            i += 1
            continue
            
        is_new_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if next_line.startswith('(cid:190)'):
                is_new_project = True
        
        if is_new_project:
            save_project(current_project_name, current_project_text, current_status)
            current_project_name = line
            current_project_text = []
            i += 1
            continue
            
        if current_project_name:
            current_project_text.append(line)
        
        i += 1
    
    save_project(current_project_name, current_project_text, current_status)

df_ext = pd.DataFrame(extracted)
merged = pd.merge(df_funding, df_ext, on='Base_Name', how='inner')
final = merged[merged['is_rel'] | merged['Project_Name'].str.contains('FEMA|emergency', case=False, regex=True)]
final = final[['Project_Name', 'Funding_Source', 'Amount', 'status']].drop_duplicates()

print('__RESULT__:')
print(final.to_json(orient='records'))"""

env_args = {'var_function-call-10239882962867119811': ['civic_docs'], 'var_function-call-10239882962867121006': ['Funding'], 'var_function-call-7750960758477245626': 'file_storage/function-call-7750960758477245626.json', 'var_function-call-7750960758477242945': 'file_storage/function-call-7750960758477242945.json', 'var_function-call-3106554336237263291': 'file_storage/function-call-3106554336237263291.json', 'var_function-call-9490853399771812395': [{'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000', 'status': 'unknown'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'status': 'unknown'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'status': 'unknown'}], 'var_function-call-16601428091099697315': [{'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000', 'status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'status': 'unknown'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000', 'status': 'unknown'}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000', 'status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'status': 'unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements', 'Funding_Source': 'Non-profit Organization Grant', 'Amount': '34000', 'status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000', 'status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'status': 'unknown'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000', 'status': 'unknown'}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000', 'status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'status': 'unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'status': 'unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000', 'status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'status': 'unknown'}, {'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Social Impact Investment', 'Amount': '77000', 'status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Social Impact Investment', 'Amount': '77000', 'status': 'unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'status': 'design'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000', 'status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000', 'status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'status': 'not started'}]}

exec(code, env_args)
