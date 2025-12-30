code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3769111620830882253'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-3769111620830881668'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
project_names = funding_df['Project_Name'].unique().tolist()
# Sort by length descending to match longer names first (to avoid partial matches if any)
project_names.sort(key=len, reverse=True)

matches = []

# Keywords for start
start_keywords = ["Begin Construction", "Start", "Commence", "Mobilization"]
date_patterns = [
    r"Spring 2022", r"Spring, 2022",
    r"March 2022", r"April 2022", r"May 2022",
    r"March, 2022", r"April, 2022", r"May, 2022",
    r"03/\d{2}/2022", r"04/\d{2}/2022", r"05/\d{2}/2022"
]

for doc in civic_docs:
    text = doc['text']
    # Find all project positions
    positions = []
    for name in project_names:
        # Use simple string find, assuming names are unique enough and case sensitive
        # Or better, regex with boundary? Names might have special chars.
        # Let's just use string find for now.
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1:
                break
            positions.append((idx, name))
            start = idx + len(name)
    
    positions.sort()
    
    # Process sections
    for i in range(len(positions)):
        start_idx, name = positions[i]
        # End is next project start or end of text
        if i < len(positions) - 1:
            end_idx = positions[i+1][0]
        else:
            end_idx = len(text)
        
        section_text = text[start_idx:end_idx]
        
        # Check for dates in this section
        found_date = False
        context = ""
        
        for pat in date_patterns:
            if re.search(pat, section_text, re.IGNORECASE):
                # Found a date. Now check if it's a start date.
                # Extract the line containing the date
                lines = section_text.split('\n')
                for line in lines:
                    if re.search(pat, line, re.IGNORECASE):
                        # Check if line indicates start
                        # Relaxed check: just check if line contains "Begin Construction" or similar
                        # Or if the date is associated with "Schedule"
                        matches.append({
                            "Project": name,
                            "Line": line.strip(),
                            "Filename": doc['filename']
                        })

print("__RESULT__:")
print(json.dumps(matches, indent=2))"""

env_args = {'var_function-call-3769111620830882253': 'file_storage/function-call-3769111620830882253.json', 'var_function-call-3769111620830881668': 'file_storage/function-call-3769111620830881668.json'}

exec(code, env_args)
