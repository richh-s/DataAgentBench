code = """'''
import pandas as pd
import json
import re

# Load the funding data
with open(locals()['var_function-call-17014294750015647345'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Load the civic docs data
with open(locals()['var_function-call-7117339431964219411'], 'r') as f:
    civic_docs_data = json.load(f)

projects = []
for doc in civic_docs_data:
    text = doc['text']
    
    lines = text.split('\n')
    
    in_design_section = False
    
    # Keywords that signal the end of the current section
    section_end_triggers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects"
    ]

    # Keywords likely to be found in non-project lines within the section
    exclude_keywords_snippets = [
        "Updates:", "Project Schedule:", "Estimated Schedule:", "Project Description:", "(cid:190)", "Page ",
        "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "Subject:", "RECOMMENDED ACTION:",
        "DISCUSSION:", "Fiscal Year", "RFQ/P", "delayed", "Staff is working", "Federal funding",
        "Commission meeting", "request proposal", "final design plans", "Funding agreement",
        "under construction", "out to bid", "Construction was completed", "Notice of completion filed",
        "application through Measure R", "preliminary design phase", "preliminary design will determine",
        "Public Works Quarterly Update flier", "Public Works statistics", "Projects Under Design",
        "Citizen Request", "Encroachment Permits Issued", "Development Reviews",
        "awarded the contract", "Plans are under review", "Army Corp. of Engineers", "submitted plans to CalOES",
        "Plans and specifications have been completed", "Awaiting final FEMA/CalOES approval",
        "Field data collection has been completed", "storm drain inventory", "Consultant working finalizing",
        "Plans and specifications are being finalized", "submitted plans to Caltrans",
        "working with consultant on the design", "submit to the County for review",
        "review design alternatives", "received four (4) construction bids", "rejected all bids",
        "budget shortfall"
    ]

    for line in lines:
        cleaned_line = line.strip()
        
        if "Capital Improvement Projects (Design)" in cleaned_line:
            in_design_section = True
            continue
        
        if in_design_section:
            if any(trigger in cleaned_line for trigger in section_end_triggers):
                in_design_section = False
                continue
            
            # Heuristic to identify project names:
            # - Not empty
            # - Starts with an uppercase letter or a digit
            # - Contains more than one word
            # - Does not contain any of the exclude keywords snippets
            if cleaned_line and (cleaned_line[0].isupper() or cleaned_line[0].isdigit()) and \
               len(cleaned_line.split()) > 1 and not any(snippet in cleaned_line for snippet in exclude_keywords_snippets):
                projects.append({'Project_Name': cleaned_line, 'type': 'capital', 'status': 'design'})

# Create a DataFrame for projects from civic documents
civic_projects_df = pd.DataFrame(projects)

# Merge the two dataframes
merged_df = pd.merge(funding_df, civic_projects_df, on='Project_Name', how='inner')

# Count unique projects
count = merged_df['Project_Name'].nunique()

print('__RESULT__:')
print(json.dumps(count))
'''"""

env_args = {'var_function-call-17014294750015647345': 'file_storage/function-call-17014294750015647345.json', 'var_function-call-7117339431964219411': 'file_storage/function-call-7117339431964219411.json'}

exec(code, env_args)
