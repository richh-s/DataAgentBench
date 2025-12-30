code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-11339180666459361146'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-11339180666459360437'], 'r') as f:
    civic_docs_data = json.load(f)

# Normalize project names for matching
# The text has "cid" codes, so we might need to be careful.
# But Project Names usually appear as headers.

# Prepare a set of known project names to help extraction
known_projects = set(funding_df['Project_Name'].str.lower().str.strip().tolist())

matched_projects = set()

# Terms indicating Start
start_terms = ["begin construction", "start construction", "construction begin", "construction start", "project start", "start date", "begins"]
# Terms indicating Spring 2022
# "Spring 2022", "March 2022", "April 2022", "May 2022", "03/2022", "04/2022", "05/2022"
spring_2022_terms = ["spring 2022", "spring, 2022", "march 2022", "april 2022", "may 2022", "march, 2022", "april, 2022", "may, 2022"]

# Helper to check line
def check_line_for_start(line):
    line_lower = line.lower()
    # Check if any spring 2022 term is in the line
    has_spring = any(term in line_lower for term in spring_2022_terms)
    if not has_spring:
        return False
    # Check if it indicates a start
    # "Advertise" might be considered start of procurement, but usually "Start" means physical start or project initiation.
    # However, for some projects "Advertise" is the first step listed.
    # Let's stick to "Begin" or "Start" or "Construction" if it says "Construction: Spring 2022"
    if any(term in line_lower for term in start_terms):
        return True
    return False

# We need to associate lines with projects.
# We will iterate through lines. If a line matches a known project name (roughly), we set current_project.
# Then we scan subsequent lines for dates.

# Create a normalized map for easier lookup
# But text headers might not be exact. e.g. "2022 Morning View..." matches "2022 Morning View Resurfacing & Storm Drain Improvements"
# Let's try to match lines to project names.

found_details = []

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check if line is a project name
        # We check if the line is in our known_projects set (fuzzy or exact)
        # normalize line
        line_norm = line_clean.lower().strip()
        
        # Exact match check
        if line_norm in known_projects:
            current_project = line_clean # Use the text's version or the funding version? Let's verify.
            # Find the funding version
            # But line_clean might have formatting.
            # Let's map back to funding name
            # We need the exact funding name to join later.
            for name in funding_df['Project_Name']:
                if name.lower().strip() == line_norm:
                    current_project = name
                    break
        else:
            # Check if it starts with a known project name (sometimes text has trailing chars)
            # or if a known project name is contained in the line? 
            # Be careful of false positives. Project names are usually distinctive.
            # Let's check if any funding project name is a substring of the line, 
            # AND the line isn't too long (like a sentence mentioning the project).
            # Project headers are usually short.
            if len(line_norm) < 100:
                for name in funding_df['Project_Name']:
                    name_norm = name.lower().strip()
                    if name_norm == line_norm:
                        current_project = name
                        break
        
        if current_project:
            # Check for schedule info
            if check_line_for_start(line_clean):
                matched_projects.add(current_project)
                found_details.append((current_project, line_clean))

# Output the findings
print("__RESULT__:")
print(json.dumps(list(matched_projects)))"""

env_args = {'var_function-call-2238045295135148005': ['civic_docs'], 'var_function-call-2238045295135146372': 'file_storage/function-call-2238045295135146372.json', 'var_function-call-2238045295135148835': ['Funding'], 'var_function-call-2238045295135147202': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11339180666459360437': 'file_storage/function-call-11339180666459360437.json', 'var_function-call-11339180666459361146': 'file_storage/function-call-11339180666459361146.json'}

exec(code, env_args)
