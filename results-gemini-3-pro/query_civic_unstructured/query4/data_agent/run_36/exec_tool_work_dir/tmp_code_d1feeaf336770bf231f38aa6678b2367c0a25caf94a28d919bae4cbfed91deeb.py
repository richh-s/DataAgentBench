code = """import json
import re
import pandas as pd

# Access file paths from local variables
path_civic = locals()['var_function-call-15751791052793352313']
path_funding = locals()['var_function-call-15751791052793352304']

# Load data
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

with open(path_funding, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Ensure Amount is numeric
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'], errors='coerce').fillna(0)

project_names = df_funding['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

# Define Spring 2022 patterns - escaping backslashes for JSON transport
spring_2022_patterns = [
    r'Spring\\s*2022',
    r'March\\s*2022',
    r'April\\s*2022',
    r'May\\s*2022',
    r'2022\\s*Spring',
    r'03/\\d{2}/2022',
    r'04/\\d{2}/2022',
    r'05/\\d{2}/2022'
]
spring_2022_regex = re.compile('|'.join(spring_2022_patterns), re.IGNORECASE)

start_indicators = [
    'Begin Construction',
    'Start Construction',
    'Construction Start',
    'Construction Begin',
    'Date Started',
    'Started',
    'Begins',
    'Begin',
    'Start',
    'Advertise' # Adding Advertise as potential start if Construction is not mentioned or implied
]

def is_start_date(text_segment, date_match_span):
    start_index = max(0, date_match_span[0] - 150)
    preceding_text = text_segment[start_index:date_match_span[0]].lower()
    
    lines = preceding_text.split('\n')
    relevant_line = lines[-1] if lines else preceding_text
    if len(relevant_line) < 10 and len(lines) > 1:
        relevant_line = lines[-2] + " " + lines[-1]
        
    for indicator in start_indicators:
        if indicator.lower() in relevant_line:
            # Check for negative indicators
            if "complete" in relevant_line or "finish" in relevant_line:
                 # Logic to distinguish "Complete Design" vs "Complete Construction"
                 # If "Construction" is in indicator ("Begin Construction"), we are safer.
                 # If indicator is just "Begin" or "Start", and "Complete" is there?
                 # e.g. "Complete Design; Start Construction" -> OK.
                 # e.g. "Project Complete" -> Not OK.
                 if "construction" in indicator.lower():
                     return True
                 # If "Advertise" -> OK (as start of procurement)
                 if "advertise" in indicator.lower():
                     return True
                 
                 # Ambiguous case: "Complete Design" (contains no indicator unless we matched "Start"?)
                 # If relevant_line is "Complete Design: Spring 2022", "Begin" is NOT in it.
                 # So we wouldn't be in this block unless "Begin" or "Start" is also there.
                 pass
            return True
            
    if relevant_line.strip().startswith("Start") or relevant_line.strip().startswith("Begin"):
        return True
        
    return False

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    text = text.replace('(cid:190)', '-').replace('(cid:131)', '*')
    
    for proj in project_names:
        # Search for project name
        matches = list(re.finditer(re.escape(proj), text, re.IGNORECASE))
        for match in matches:
            start_pos = match.end()
            end_pos = start_pos + 1000
            context = text[start_pos:end_pos]
            
            date_matches = list(spring_2022_regex.finditer(context))
            
            for dm in date_matches:
                if is_start_date(context, dm.span()):
                    found_projects.add(proj)
                    break
            
            if proj in found_projects:
                break

matched_df = df_funding[df_funding['Project_Name'].isin(found_projects)]
total_funding = matched_df['Amount'].sum()
count = len(matched_df)

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total_funding, 'projects': list(matched_df['Project_Name'].unique())}))"""

env_args = {'var_function-call-898378015105959722': 'file_storage/function-call-898378015105959722.json', 'var_function-call-898378015105961733': ['Funding'], 'var_function-call-16470054379603944391': 'file_storage/function-call-16470054379603944391.json', 'var_function-call-16470054379603946372': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-15751791052793352313': 'file_storage/function-call-15751791052793352313.json', 'var_function-call-15751791052793352304': 'file_storage/function-call-15751791052793352304.json'}

exec(code, env_args)
