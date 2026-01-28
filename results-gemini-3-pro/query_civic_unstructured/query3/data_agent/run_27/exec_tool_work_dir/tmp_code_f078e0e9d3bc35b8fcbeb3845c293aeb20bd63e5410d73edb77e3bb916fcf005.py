code = """import json
import pandas as pd

# Load Funding Data
with open(locals()['var_function-call-2005657449811241247'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open(locals()['var_function-call-2005657449811241560'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = [line.strip() for line in text.splitlines()]
    
    current_status_section = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check Header
        if "Capital Improvement Projects (Design)" in line:
            current_status_section = "design"
            i += 1
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_status_section = "construction"
            i += 1
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status_section = "not started"
            i += 1
            continue
            
        if not line:
            i += 1
            continue
            
        # Check Project Name (lookahead for marker)
        is_project = False
        look_ahead = i + 1
        # Increase lookahead range
        while look_ahead < len(lines) and look_ahead < i + 15:
            if "(cid:190)" in lines[look_ahead]:
                is_project = True
                break
            if lines[look_ahead]:
                break # Non-empty line without marker
            look_ahead += 1
            
        if is_project and current_status_section:
            project_name = line
            
            # Extract Block
            block_lines = []
            j = i + 1
            while j < len(lines):
                curr_line = lines[j]
                
                if "Capital Improvement Projects (" in curr_line:
                    break
                
                # Check for new project
                is_new_proj = False
                if curr_line and "(cid:190)" not in curr_line:
                    la_k = j + 1
                    while la_k < len(lines) and la_k < j + 15:
                        if "(cid:190)" in lines[la_k]:
                            is_new_proj = True
                            break
                        if lines[la_k]:
                            break
                        la_k += 1
                
                if is_new_proj:
                    break
                
                block_lines.append(curr_line)
                j += 1
            
            full_text = " ".join(block_lines)
            
            status = current_status_section
            # Refine status
            if status == "construction":
                if "completed" in full_text.lower() or "notice of completion" in full_text.lower():
                    status = "completed"
            
            extracted_projects.append({
                "Project_Name": project_name,
                "Status": status,
                "Full_Text": full_text
            })
            i = j
        else:
            i += 1

df_civic = pd.DataFrame(extracted_projects)
# Drop duplicates in civic extraction (same project in multiple docs or same doc?)
df_civic = df_civic.drop_duplicates(subset=['Project_Name'])

df_funding = pd.DataFrame(funding_data)
# Ensure clean names
df_funding['Project_Name'] = df_funding['Project_Name'].str.strip()
df_civic['Project_Name'] = df_civic['Project_Name'].str.strip()

# Join
merged = pd.merge(df_funding, df_civic, on="Project_Name", how="inner")

# Filter
def is_related(row):
    txt = (str(row['Project_Name']) + " " + str(row['Full_Text']) + " " + str(row['Funding_Source'])).lower()
    if "emergency" in txt or "fema" in txt:
        return True
    return False

filtered = merged[merged.apply(is_related, axis=1)]

# Select columns
# User asked for: project names, funding sources, amounts, and statuses
result = filtered[['Project_Name', 'Funding_Source', 'Amount', 'Status']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2005657449811241560': 'file_storage/function-call-2005657449811241560.json', 'var_function-call-2005657449811241247': 'file_storage/function-call-2005657449811241247.json', 'var_function-call-15949721559473304236': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}], 'var_function-call-15594219515499924166': [{'Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Status': 'design', 'Next': ''}]}

exec(code, env_args)
