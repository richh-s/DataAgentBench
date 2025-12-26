code = """import json

# We have extracted project names, funding sources, and amounts.
# Now, let's check the statuses for these emergency warning projects from the civic documents (from the large file var_call_Ffyfx7ZGn5pCidDjfLLmz02A)

# Load the list of relevant project names
related_projects = json.loads('''{"Project_Name": "Birdview Avenue Improvements (FEMA/CalOES Project)", "Funding_Source": "Research Institution Funding", "Amount": 14000}, {"Project_Name": "Clover Heights Storm Drain (FEMA Project)", "Funding_Source": "Local NGO Fund", "Amount": 21000}, {"Project_Name": "Corral Canyon Culvert Repairs (FEMA Project)", "Funding_Source": "Municipal Fund", "Amount": 43000}, {"Project_Name": "Corral Canyon Culvert Repairs (FEMA/CalOES Project)", "Funding_Source": "Taxpayer Contribution", "Amount": 15000}, {"Project_Name": "Corral Canyon Road Bridge Repairs (FEMA Project)", "Funding_Source": "Local Business Support", "Amount": 25000}, {"Project_Name": "Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)", "Funding_Source": "Cultural Heritage Grant", "Amount": 58000}, {"Project_Name": "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)", "Funding_Source": "Private Sponsor", "Amount": 94000}, {"Project_Name": "Guardrail Replacement Citywide (FEMA Project)", "Funding_Source": "Impact Investment Fund", "Amount": 22000}, {"Project_Name": "Guardrail Replacement Citywide (FEMA/CalOES Project)", "Funding_Source": "Development Bank Loan", "Amount": 45000}, {"Project_Name": "Latigo Canyon Road Culvert Repairs (FEMA Project)", "Funding_Source": "Federal Assistance", "Amount": 36000}, {"Project_Name": "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)", "Funding_Source": "National Foundation Fund", "Amount": 44000}, {"Project_Name": "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)", "Funding_Source": "Municipal Fund", "Amount": 91000}, {"Project_Name": "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)", "Funding_Source": "Community Fund", "Amount": 78000}, {"Project_Name": "Outdoor Warning Signs", "Funding_Source": "Urban Renewal Fund", "Amount": 92000}, {"Project_Name": "Outdoor Warning Sirens", "Funding_Source": "Social Impact Investment", "Amount": 28000}, {"Project_Name": "Outdoor Warning Sirens (FEMA Project)", "Funding_Source": "Environmental Grant", "Amount": 27000}, {"Project_Name": "Outdoor Warning Sirens (FEMA)", "Funding_Source": "State Development Grant", "Amount": 81000}, {"Project_Name": "Outdoor Warning Sirens - Design (FEMA Project)", "Funding_Source": "Local Business Support", "Amount": 43000}, {"Project_Name": "Outdoor Warningn Sirens - Design (FEMA Project)", "Funding_Source": "Technology Innovation Fund", "Amount": 84000}, {"Project_Name": "PCH Overhead Warning Signs", "Funding_Source": "International Organization Grant", "Amount": 73000}, {"Project_Name": "Storm Drain Master Plan (FEMA Project)", "Funding_Source": "Environmental Grant", "Amount": 80000}, {"Project_Name": "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)", "Funding_Source": "Infrastructure Bond", "Amount": 44000}, {"Project_Name": "Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)", "Funding_Source": "Infrastructure Bond", "Amount": 92000}''')

# Load full civic document list from large file
with open(var_call_Ffyfx7ZGn5pCidDjfLLmz02A, 'r') as f:
    civic_docs = json.load(f)

def extract_status_details(text, project_names):
    """
    For each project in project_names, extract its status from the civic document text.
    Very simple method: look for the project name (or keywords), and extract a sentence nearby mentioning status keywords.
    """
    import re
    status_keywords = ['status', 'phase', 'completed', 'under construction', 'out to bid', 'not started', 'pending', 'delayed', 'final design', 'design', 'preliminary', 'approval', 'advertise', 'update', 'in progress', 'scheduled']
    results = {}
    text_lower = text.lower()
    for proj in project_names:
        name = proj['Project_Name'].lower()[:50] # Use start of name for matching
        # Find a spot in text
        idx = text_lower.find(name[:25]) # Short match
        status_found = None
        if idx >= 0:
            clipped_text = text_lower[max(0, idx-200):idx+400]
            for word in status_keywords:
                if word in clipped_text:
                    # Extract the sentence around the word
                    sentences = re.split(r'[.!?\n]', clipped_text)
                    for sent in sentences:
                        if word in sent:
                            status_found = sent.strip().replace('\n',' ').replace('  ',' ')
                            break
            results[proj['Project_Name']] = status_found
        else:
            results[proj['Project_Name']] = None
    return results

# Gather status info for all related projects by scanning all docs
project_names = related_projects
status_info = {}

for doc in civic_docs:
    doc_status = extract_status_details(doc['text'], project_names)
    # Keep non-None status findings
    for proj, stat in doc_status.items():
        if stat and (proj not in status_info or not status_info[proj]):
            status_info[proj] = stat

# Merge with funding info and produce a summary
output = []
for proj in related_projects:
    name = proj['Project_Name']
    summary = {
        'Project_Name': name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status_info.get(name, None)
    }
    output.append(summary)

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_Ffyfx7ZGn5pCidDjfLLmz02A': 'file_storage/call_Ffyfx7ZGn5pCidDjfLLmz02A.json', 'var_call_GO4HIhWh7vCBIxRVSvSCEhKp': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': '73000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_Cs7aw9Xhh0O5agXoD65xbLXP': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': 73000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)
