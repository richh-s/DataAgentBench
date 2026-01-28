code = """import json
import re

# Access the results properly
funding_results = locals()['var_functions.query_db:24']

# Load civic documents from file path
civic_docs_path = locals()['var_functions.query_db:4']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Found {len(funding_results)} FEMA-related funding records")
print(f"Found {len(civic_docs)} civic documents to search for statuses")

# Extract project names from funding results
fema_project_names = [record['Project_Name'] for record in funding_results]

# Create a dictionary to store project statuses
project_statuses = {}

# Search for project statuses in the civic documents
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or len(line) < 5:
            continue
            
        # Skip common headers that are not project names
        skip_patterns = ['Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 
                        'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:',
                        'Capital Improvement Projects', 'Disaster Recovery Projects',
                        'Project Schedule:', 'Project Description:', 'Project Updates:']
        
        if any(skip in line for skip in skip_patterns):
            continue
        
        # Look for project names (typically lines that don't end with punctuation)
        # and are followed by status information
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '□', 'c', '(')):
            # Check if next few lines contain status info
            next_text = ' '.join(lines[i+1:i+5])
            
            if any(keyword in next_text for keyword in ['Updates:', 'Status:', 'Project Schedule', 'construction', 'design', 'Complete', 'Advertise']):
                current_project = line
                
                # Determine status based on keywords
                status = 'Unknown'
                if 'under construction' in next_text.lower():
                    status = 'Construction'
                elif 'construction was completed' in next_text.lower() or 'complete construction' in next_text.lower():
                    status = 'Completed'
                elif 'complete design' in next_text.lower() or 'staff is working' in next_text.lower():
                    status = 'Design'
                elif 'advertise:' in next_text.lower() or 'out to bid' in next_text.lower():
                    status = 'Bidding'
                elif 'awaiting' in next_text.lower():
                    status = 'Awaiting Approval'
                elif 'not started' in next_text.lower():
                    status = 'Not Started'
                
                if current_project:
                    project_statuses[current_project] = status

print(f"Extracted {len(project_statuses)} project statuses from documents")

# Match funding records with status information
results = []

for funding in funding_results:
    proj_name = funding['Project_Name']
    status = 'Unknown'
    
    # Try exact match first
    if proj_name in project_statuses:
        status = project_statuses[proj_name]
    else:
        # Try to find base name match
        base_name = proj_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA Project)', '').replace(' (CalJPIA/FEMA Project)', '')
        
        # Look for partial matches
        for extracted_name, extracted_status in project_statuses.items():
            if (base_name.lower() in extracted_name.lower() or 
                extracted_name.lower() in base_name.lower() or
                (len(base_name) > 10 and base_name[:10].lower() in extracted_name.lower())):
                status = extracted_status
                break
    
    results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding['Funding_Source'],
        'Amount': funding['Amount'],
        'Status': status
    })

print(f"\nFound {len(results)} projects with funding and status information")

# Format results for output
output = []
for r in results:
    output.append(f"Project: {r['Project_Name']}")
    output.append(f"  Funding: {r['Funding_Source']}")
    output.append(f"  Amount: ${r['Amount']}")
    output.append(f"  Status: {r['Status']}")
    output.append("")

final_output = "\n".join(output)
print(final_output)

# Also create a summary
summary = f"Total Projects: {len(results)}\n"
summary += f"Total Amount: ${sum(int(r['Amount']) for r in results):,}\n"

status_counts = {}
for r in results:
    status = r['Status']
    status_counts[status] = status_counts.get(status, 0) + 1

summary += "\nStatus Breakdown:\n"
for status, count in status_counts.items():
    summary += f"  {status}: {count}\n"

print("\n" + summary)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
