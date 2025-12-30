code = """import json
import re
import pandas as pd

# Load previous results
civic_docs = json.load(open('var_function-call-15751791052793352313.json'))
funding_data = json.load(open('var_function-call-15751791052793352304.json'))

df_funding = pd.DataFrame(funding_data)
project_names = df_funding['Project_Name'].unique().tolist()
# Sort project names by length descending to match longest first (though exact match is better)
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

# Helper to check if a date string is preceded by a start indicator
def is_start_date(text_segment, date_match_span):
    # Look at text before the date
    start_index = max(0, date_match_span[0] - 100)
    preceding_text = text_segment[start_index:date_match_span[0]].lower()
    
    # Check for start indicators
    for indicator in start_indicators:
        if indicator.lower() in preceding_text:
            # Check for negation or "Complete"
            # e.g. "Complete Design" should not match if we just matched "Spring 2022"
            # But "Begin Construction" is good.
            # We need to be careful not to match "Complete Design: Spring 2022" if "Design" is not "Construction"
            
            # Let's check if "Complete" or "Finish" is closer to the date than the start indicator
            # Find last index of indicator
            ind_idx = preceding_text.rfind(indicator.lower())
            
            # Check if "complete" or "finish" appears after the indicator
            segment_after_indicator = preceding_text[ind_idx+len(indicator):]
            if "complete" in segment_after_indicator or "finish" in segment_after_indicator or "end" in segment_after_indicator:
                continue # Likely "Complete ... Start ..." ? unlikely in this short window.
                # Actually, "Complete Design" might be the label.
                # If the line is "Complete Design: Spring 2022", "Begin" is not there.
                # If the line is "Begin Construction: Spring 2022", "Begin" is there.
            
            return True
    return False

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    # Normalize text?
    # Replace some common artifacts
    text = text.replace('(cid:190)', '-').replace('(cid:131)', '*')
    
    # Find projects in text
    # We scan the text for project names.
    # Since names can be substrings of each other, we iterate through sorted names.
    # To avoid double counting overlapping names in the same position, we could track indices.
    # But simpler: just find if a project name exists, and look at its context.
    
    for proj in project_names:
        # Search for project name
        # We assume project name appears as a header or distinct entity
        # Using simple string find might be enough, but let's try regex to ensure boundary?
        # Names might have punctuation.
        
        matches = list(re.finditer(re.escape(proj), text, re.IGNORECASE))
        for match in matches:
            # Get a context window after the match
            # Let's say 500 characters or until the next double newline?
            # The sample shows "Project Schedule" follows.
            
            start_pos = match.end()
            end_pos = start_pos + 1000 # Look ahead 1000 chars
            context = text[start_pos:end_pos]
            
            # Truncate context if another project name appears? 
            # This is expensive to check all.
            # Let's just rely on the proximity of the date.
            
            # Search for Spring 2022 dates in context
            date_matches = list(spring_2022_regex.finditer(context))
            
            for dm in date_matches:
                if is_start_date(context, dm.span()):
                    found_projects.add(proj)
                    break # Found a start date for this project in this doc
            
            if proj in found_projects:
                break # Move to next project

# Join with funding
matched_df = df_funding[df_funding['Project_Name'].isin(found_projects)]
total_funding = matched_df['Amount'].astype(float).sum()
count = len(matched_df)

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total_funding, 'projects': list(matched_df['Project_Name'].unique())}))"""

env_args = {'var_function-call-898378015105959722': 'file_storage/function-call-898378015105959722.json', 'var_function-call-898378015105961733': ['Funding'], 'var_function-call-16470054379603944391': 'file_storage/function-call-16470054379603944391.json', 'var_function-call-16470054379603946372': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-15751791052793352313': 'file_storage/function-call-15751791052793352313.json', 'var_function-call-15751791052793352304': 'file_storage/function-call-15751791052793352304.json'}

exec(code, env_args)
