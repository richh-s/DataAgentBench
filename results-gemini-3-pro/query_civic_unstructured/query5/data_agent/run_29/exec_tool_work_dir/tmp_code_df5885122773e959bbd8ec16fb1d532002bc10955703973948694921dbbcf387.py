code = """import json
import pandas as pd

funding_path = locals()['var_function-call-13193485311528156786']
civic_docs_path = locals()['var_function-call-13193485311528154511']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Get all disaster project names from Funding
disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"]
disaster_project_names = []
for row in funding_data:
    if any(kw in row['Project_Name'] for kw in disaster_keywords):
        disaster_project_names.append(row['Project_Name'])

print(f"Disaster projects in Funding: {len(disaster_project_names)}")

# Extract dates for these projects specifically
results = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split(chr(10))
    # We can use the simple find approach for names in the known list
    for proj in disaster_project_names:
        if proj in text:
            # Locate the project block
            # This is heuristic, but if the name is unique, it works.
            # We find the line with the name.
            # Then look forward for "Begin Construction:"
            # We need to find the specific occurrence that is a header (followed by Updates)
            # Or just search near the name.
            
            # Find all occurrences
            idx = -1
            while True:
                idx = text.find(proj, idx+1)
                if idx == -1:
                    break
                
                # Check context (next 500 chars)
                context = text[idx:idx+1000]
                
                # Check for Start Date in context
                start_date = None
                keywords = ["Begin Construction:", "Construction Start:", "Begin construction:"]
                for kw in keywords:
                    if kw in context:
                        parts = context.split(kw)
                        if len(parts) > 1:
                            rem = parts[1].strip()
                            if "  " in rem:
                                start_date = rem.split("  ")[0]
                            else:
                                start_date = rem[:30]
                            start_date = start_date.strip()
                            # Clean garbage
                            if "(cid:" in start_date:
                                start_date = start_date.split("(cid:")[0].strip()
                            break
                
                if start_date:
                    results.append({"Project": proj, "Date": start_date})

# Deduplicate results
unique_results = {}
for r in results:
    if r['Project'] not in unique_results:
        unique_results[r['Project']] = set()
    unique_results[r['Project']].add(r['Date'])

# Check for 2022
started_2022 = []
for proj, dates in unique_results.items():
    for d in dates:
        if "2022" in d:
            started_2022.append(proj)
            break

print("__RESULT__:")
print(json.dumps(started_2022))"""

env_args = {'var_function-call-11217381671134747036': ['Funding'], 'var_function-call-11217381671134747201': ['civic_docs'], 'var_function-call-13193485311528156786': 'file_storage/function-call-13193485311528156786.json', 'var_function-call-13193485311528154511': 'file_storage/function-call-13193485311528154511.json', 'var_function-call-16349189720385277872': 'file_storage/function-call-16349189720385277872.json', 'var_function-call-8983212948348442456': {'total_funding': 495000.0, 'matched_projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)'], 'debug_targets': ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'damaged by the Woolsey Fire.']}, 'var_function-call-7168125031985036471': [{'Project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Date': 'Spring 2022'}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Date': 'April 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Date': 'Spring 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Date': 'Spring 2022'}, {'Project': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Date': 'Fall 2022 (cid:131)'}, {'Project': 'Clover Heights Storm Drain (FEMA Project)', 'Date': 'Summer 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Date': 'Spring 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Date': 'Spring 2022'}, {'Project': 'Clover Heights Storm Drain (FEMA Project)', 'Date': 'Summer 2022'}, {'Project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Date': 'Spring 2022'}, {'Project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Date': 'Spring 2022'}, {'Project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Date': 'Summer 2022'}, {'Project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Date': 'Spring 2022'}, {'Project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Date': 'Summer 2022'}, {'Project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Date': 'Summer 2022'}, {'Project': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Date': 'Fall 2022 (cid:131)'}], 'var_function-call-7168125031985033706': [{'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}]}

exec(code, env_args)
