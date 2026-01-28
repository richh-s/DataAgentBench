code = """import json
import re

# Load data
with open(locals()['var_function-call-8460811092792670416'], 'r') as f:
    civic_docs = json.load(f)

# Sort by filename to find latest
civic_docs.sort(key=lambda x: x['filename'])
latest_doc = civic_docs[-1]
text = latest_doc['text']

candidates = [
    "Marie Canyon Green Streets",
    "PCH Median Improvements Project",
    "PCH Signal Synchronization System Improvements Project",
    "Bluffs Park Shade Structure",
    "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)",
    "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)",
    "Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)",
    "Latigo Canyon Road Culvert Repairs (FEMA Project)",
    "Civic Center Water Treatment Facility Phase 2",
    "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)",
    "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)"
]

snippets = {}
for c in candidates:
    # Find approximate location
    # Simplify name for search? "Broad Beach Road Water Quality Infrastructure Repairs"
    # The text uses "Broad Beach Road Water Quality Repair" (shorter).
    # "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)" matches?
    # I'll search for the first part of the name.
    
    # Actually, let's just search for the name as is from the candidate list (which came from Funding).
    # If not found, try shorter.
    
    idx = text.find(c)
    if idx == -1:
        # Try finding by substring (first 20 chars)
        short_name = c[:20]
        idx = text.find(short_name)
    
    if idx != -1:
        snippets[c] = text[idx:idx+500]
    else:
        snippets[c] = "NOT FOUND in latest doc"

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-15438762544756245875': 'file_storage/function-call-15438762544756245875.json', 'var_function-call-15438762544756246872': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-8460811092792669481': 'file_storage/function-call-8460811092792669481.json', 'var_function-call-8460811092792670416': 'file_storage/function-call-8460811092792670416.json', 'var_function-call-8912619866491154738': {'count': 12, 'total_funding': 621000, 'projects': ['Marie Canyon Green Streets', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Bluffs Park Shade Structure', 'PCH Signal Synchronization System Improvements Project', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'PCH Median Improvements Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)']}, 'var_function-call-17250558490267323785': [{'project': 'Marie Canyon Green Streets', 'date': 'Spring 2022'}, {'project': 'PCH Median Improvements Project', 'date': 'Spring/Summer 2022'}, {'project': 'PCH Signal Synchronization System Improvements Project', 'date': 'Spring/Summer 2022'}, {'project': 'Bluffs Park Shade Structure', 'date': 'Spring 2022'}, {'project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'date': 'Spring 2022'}, {'project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'date': 'April 2022'}, {'project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'date': 'Spring 2022'}, {'project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'date': 'Spring 2022'}, {'project': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'date': 'April 2022'}, {'project': 'Civic Center Water Treatment Facility Phase 2', 'date': 'March 2022'}, {'project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'date': 'Spring 2022'}, {'project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'date': 'Spring 2022'}, {'project': 'Civic Center Water Treatment Facility Phase 2', 'date': 'March 2022'}, {'project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'date': 'Spring 2022'}, {'project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'date': 'Spring 2022'}, {'project': 'Bluffs Park Shade Structure', 'date': 'Spring 2022'}, {'project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'date': 'Spring 2022'}, {'project': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'date': 'Spring 2022'}], 'var_function-call-16129373147438483197': ['The design has\n\nstarted and is anticipated to be completed by the Spring of 2022.', '(cid:190) Updates:\n\n(cid:131) The design has started and is anticipated to be completed by the Spring\n\nof 2022.']}

exec(code, env_args)
