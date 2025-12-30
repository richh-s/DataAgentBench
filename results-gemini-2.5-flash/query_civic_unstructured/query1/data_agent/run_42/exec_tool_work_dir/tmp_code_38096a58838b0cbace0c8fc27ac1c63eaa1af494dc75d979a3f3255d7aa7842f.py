code = """import pandas as pd
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

# Extract project information from civic documents
projects = []
for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to find Capital Improvement Projects (Design) section
    design_capital_projects_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|\n\nDisaster Recovery Projects|RECOMMENDED ACTION:|$)', text, re.DOTALL)
    
    if design_capital_projects_match:
        design_capital_section = design_capital_projects_match.group(1)
        # Split the section into lines and filter for project names
        lines = design_capital_section.split('\n')
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line and not any(keyword in cleaned_line for keyword in [
                'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Project Description:',
                '(cid:190)', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:',
                'RECOMMENDED ACTION:', 'DISCUSSION:', 'Page ', 'Item', 'Agenda Item #', 'Fiscal Year',
                'City will be issuing a RFQ/P for design services', 'Project is delayed due to the Cultural Resource review',
                'Staff is working with the State Water Board', 'Staff has submitted a request for Federal funding',
                'Project to be discussed during a joint Public Works and Public Safety Commission meeting',
                'City to request proposal from consultant for design services', 'Staff is currently working on the final design plans',
                'Funding agreement is schedule for city council', 'Project is currently under construction',
                'Project is currently out to bid', 'Construction was completed', 'Notice of completion filed',
                'City has submitted an application through Measure R', 'Project is in the preliminary design phase',
                'Preliminary design will determine if signals need to be upgraded',
                'Staff has also prepared a Public Works Quarterly Update flier',
                'This flier will include a variety of Public Works statistics', 'including Projects Under Design',
                'Citizen Request', 'Encroachment Permits Issued', 'and the amount of Development Reviews perfor',
                'City Council awarded the contract', 'Plans are under review by Fish and Wildlife',
                'Army Corp. of Engineers has cleared the project', 'City submitted plans to CalOES for review',
                'Plans and specifications have been completed', 'Awaiting final FEMA/CalOES approval',
                'Field data collection has been completed', 'storm drain inventory has been finalized',
                'Consultant working finalizing a CIP recommendation list', 'Plans and specifications are being finalized by consultant',
                'Staff is working with the consultant to finalize the design plans', 'City submitted plans to Caltrans for review',
                'City working with consultant on the design of the shoulder repairs',
                'Staff is working with the consultant to finalize the design plans',
                'City will work with the design consultant to review design alternatives',
                'City received four (4) construction bids', 'rejected all bids due to a budget shortfall',
                'Staff is working with the consultant to finalize the design plans for this project and will submit to the County for review.'
            ]):
                projects.append({'Project_Name': cleaned_line, 'type': 'capital', 'status': 'design'})

# Create a DataFrame for projects from civic documents
civic_projects_df = pd.DataFrame(projects)

# Merge the two dataframes
merged_df = pd.merge(funding_df, civic_projects_df, on='Project_Name', how='inner')

# Count unique projects
count = merged_df['Project_Name'].nunique()

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_function-call-17014294750015647345': 'file_storage/function-call-17014294750015647345.json', 'var_function-call-7117339431964219411': 'file_storage/function-call-7117339431964219411.json'}

exec(code, env_args)
