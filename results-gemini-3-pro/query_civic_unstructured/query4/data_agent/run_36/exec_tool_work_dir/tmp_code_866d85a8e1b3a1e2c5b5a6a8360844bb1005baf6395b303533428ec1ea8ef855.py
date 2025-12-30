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
project_names = df_funding['Project_Name'].unique().tolist()
# Sort project names by length descending
project_names.sort(key=len, reverse=True)

# Define Spring 2022 patterns
spring_2022_patterns = [
    r'Spring\s*2022',
    r'March\s*2022',
    r'April\s*2022',
    r'May\s*2022',
    r'2022\s*Spring',
    r'03/\d{2}/2022',
    r'04/\d{2}/2022',
    r'05/\d{2}/2022'
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
    'Start'
]

def is_start_date(text_segment, date_match_span):
    start_index = max(0, date_match_span[0] - 150) # Increased context window
    preceding_text = text_segment[start_index:date_match_span[0]].lower()
    
    # Check if "Complete" appears right before (e.g. "Complete Design: Spring 2022")
    # We want to avoid cases where "Spring 2022" is the completion date.
    
    # Split preceding text by lines to focus on the immediate line
    lines = preceding_text.split('\n')
    relevant_line = lines[-1] if lines else preceding_text
    
    # If the relevant line is too short, include previous line?
    if len(relevant_line) < 10 and len(lines) > 1:
        relevant_line = lines[-2] + " " + lines[-1]
        
    for indicator in start_indicators:
        if indicator.lower() in relevant_line:
            # Check for negative indicators in the same relevant line
            if "complete" in relevant_line or "finish" in relevant_line:
                # E.g. "Complete Design; Begin Construction" -> Good
                # "Complete Construction" -> Bad
                # Check position
                ind_pos = relevant_line.find(indicator.lower())
                comp_pos = -1
                if "complete" in relevant_line: comp_pos = relevant_line.find("complete")
                if "finish" in relevant_line: comp_pos = max(comp_pos, relevant_line.find("finish"))
                
                # If "Complete" is before "Begin", it might be "Complete Design, Begin Construction" -> OK
                # If "Complete" is after "Begin" ? Unlikely.
                # If "Begin" is part of "Begin Construction", we are good.
                pass
            return True
            
    # Also check if the line *starts* with "Start:" or "Begin:"
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
            end_pos = start_pos + 2000 # Look ahead
            context = text[start_pos:end_pos]
            
            date_matches = list(spring_2022_regex.finditer(context))
            
            for dm in date_matches:
                if is_start_date(context, dm.span()):
                    found_projects.add(proj)
                    break
            
            if proj in found_projects:
                break

matched_df = df_funding[df_funding['Project_Name'].isin(found_projects)]
total_funding = matched_df['Amount'].astype(float).sum()
count = len(matched_df)

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total_funding, 'projects': list(matched_df['Project_Name'].unique())}))"""

env_args = {'var_function-call-898378015105959722': 'file_storage/function-call-898378015105959722.json', 'var_function-call-898378015105961733': ['Funding'], 'var_function-call-16470054379603944391': 'file_storage/function-call-16470054379603944391.json', 'var_function-call-16470054379603946372': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-15751791052793352313': 'file_storage/function-call-15751791052793352313.json', 'var_function-call-15751791052793352304': 'file_storage/function-call-15751791052793352304.json'}

exec(code, env_args)
