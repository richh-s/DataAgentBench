code = """import json
import pandas as pd
import re

# Load data
docs_path = locals()['var_function-call-12003933845837938718']
funding_path = locals()['var_function-call-7144794427946386972']

with open(docs_path, 'r') as f:
    docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
# Sort by length descending to match longest names first
project_names = sorted(list(set(funding_df['Project_Name'].unique())), key=len, reverse=True)

found_projects = []

for doc in docs:
    text = doc['text']
    # Normalize text?
    # Iterate through project names and find their position
    # This is a simple parser. A better one would use the structure (headers etc).
    
    # We will try to split the text by project names.
    # But project names might appear multiple times.
    # Let's find all start indices of all project names.
    
    # Create a list of (index, project_name)
    occurrences = []
    for pn in project_names:
        # Simple string find might be enough, but regex is safer for boundaries?
        # Let's use simple find for now, assuming names are distinct enough.
        # But names like "Road Repair" might be substrings of "X Road Repair".
        # Since we sorted by length, we can try to mark regions.
        
        # Actually, let's just use regex with word boundaries if possible, or just exact string match.
        # Names contain special chars like parens. Escape them.
        pattern = re.escape(pn)
        for match in re.finditer(pattern, text, re.IGNORECASE):
            occurrences.append((match.start(), pn))
            
    # Sort occurrences by position
    occurrences.sort(key=lambda x: x[0])
    
    # Now iterate and extract text chunks
    for i in range(len(occurrences)):
        start_idx, name = occurrences[i]
        
        # Determine end index (start of next project or end of text)
        # However, we must be careful not to cut off if the next occurrence is overlapping (which shouldn't happen with valid text flow)
        # or if the next occurrence is just a mention in the description.
        # Usually project sections are sequential.
        
        # Let's assume the section goes until the next project header.
        # But how to distinguish a header from a mention?
        # In the sample, headers were on their own lines or distinct.
        
        # Let's just take the text until the next occurrence in the list.
        if i < len(occurrences) - 1:
            end_idx = occurrences[i+1][0]
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        
        # Check for Spring 2022 in this segment
        # Pattern: "Spring 2022" or "2022-Spring"
        if re.search(r'Spring[,\s-]*2022', segment, re.IGNORECASE) or re.search(r'2022[,\s-]*Spring', segment, re.IGNORECASE):
            # Extract the context
            # Find the line
            lines = segment.split('\n')
            relevant_lines = [line.strip() for line in lines if '2022' in line and 'Spring' in line]
            
            found_projects.append({
                "doc_file": doc['filename'],
                "project": name,
                "context": relevant_lines
            })

print("__RESULT__:")
print(json.dumps(found_projects))"""

env_args = {'var_function-call-7144794427946386357': 'file_storage/function-call-7144794427946386357.json', 'var_function-call-7144794427946386972': 'file_storage/function-call-7144794427946386972.json', 'var_function-call-12003933845837938718': 'file_storage/function-call-12003933845837938718.json', 'var_function-call-16291157491090177624': {'doc_count': 5, 'funding_count': 500, 'matches': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}}

exec(code, env_args)
