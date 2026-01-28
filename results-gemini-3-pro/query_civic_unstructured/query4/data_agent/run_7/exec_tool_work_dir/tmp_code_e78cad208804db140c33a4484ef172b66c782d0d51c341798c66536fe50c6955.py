code = """import json
import pandas as pd

# Files
funding_path = locals()['var_function-call-11339180666459361146']
docs_path = locals()['var_function-call-11339180666459360437']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Funding lookup
funding_df = pd.DataFrame(funding_data)
# Create a set of lowercased stripped names for matching
project_map = {} # normalized -> original
for name in funding_df['Project_Name']:
    project_map[name.lower().strip()] = name

matched_projects = set()

start_keywords = ["begin", "start", "advertise", "award", "construction"] # "Construction: Spring 2022"
spring_keywords = ["spring 2022", "spring, 2022", "march 2022", "april 2022", "may 2022"]

# Check each doc
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        line_lower = line_clean.lower()
        
        # Check if line is a project name
        if line_lower in project_map:
            current_project = project_map[line_lower]
        
        # If inside a project section, check for dates
        if current_project:
            # Check for Spring 2022
            # Also handle "March, 2022" etc if needed, but sticking to list
            is_spring = False
            for sk in spring_keywords:
                if sk in line_lower:
                    is_spring = True
                    break
            
            if is_spring:
                # Check for start context
                # "Begin Construction: Spring 2022"
                # "Start: Spring 2022"
                # "Project Schedule: ... Spring 2022" -> Too vague?
                # "Advertise: Spring 2022" -> Acceptable start?
                # "Estimated Schedule: Complete Design: Spring 2022" -> No.
                
                # Check strict start keywords
                is_start = False
                if "begin" in line_lower: is_start = True
                elif "start" in line_lower: is_start = True
                elif "advertise" in line_lower: is_start = True
                elif "award" in line_lower: is_start = True
                # If "Construction: Spring 2022" without "Begin"?
                # "Construction: Spring 2022" usually means construction phase.
                # If "Complete Construction: Spring 2022" -> No.
                elif "construction" in line_lower and "complete" not in line_lower and "finish" not in line_lower:
                    is_start = True
                
                if is_start:
                    matched_projects.add(current_project)

# Calculate totals
final_projects = list(matched_projects)
total_amount = funding_df[funding_df['Project_Name'].isin(final_projects)]['Amount'].astype(int).sum()

print("__RESULT__:")
print(json.dumps({
    "count": len(final_projects),
    "total_funding": int(total_amount),
    "projects": final_projects
}))"""

env_args = {'var_function-call-2238045295135148005': ['civic_docs'], 'var_function-call-2238045295135146372': 'file_storage/function-call-2238045295135146372.json', 'var_function-call-2238045295135148835': ['Funding'], 'var_function-call-2238045295135147202': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11339180666459360437': 'file_storage/function-call-11339180666459360437.json', 'var_function-call-11339180666459361146': 'file_storage/function-call-11339180666459361146.json', 'var_function-call-12135098682891406353': 'file_storage/function-call-11339180666459361146.json'}

exec(code, env_args)
