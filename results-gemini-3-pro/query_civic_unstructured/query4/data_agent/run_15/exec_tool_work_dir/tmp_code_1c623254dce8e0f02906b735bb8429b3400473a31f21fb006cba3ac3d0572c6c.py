code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-6539417024683493818'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6539417024683493925'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
funding_projects = set(df_funding['Project_Name'].unique())

# Prepare regex for dates
spring_2022_patterns = [
    r"Spring,? 2022",
    r"March,? 2022",
    r"April,? 2022",
    r"May,? 2022"
]
date_pattern = re.compile(r"(" + "|".join(spring_2022_patterns) + ")", re.IGNORECASE)

# Keywords indicating start
start_keywords = ["Begin Construction", "Start Construction", "Construction Start", "Project Start", "Est. Start", "Scheduled Start"]

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    # Normalize text to handle newlines inside sentences if needed, but keeping structure is better.
    # We will look for project blocks.
    
    # Identify project locations
    # We create a list of (position, project_name)
    project_positions = []
    for proj in funding_projects:
        # Simple substring search.
        # Adding some boundary checks might be good, but project names are usually long enough.
        # We search case-insensitive? The names in DB seem Capitalized. Text is mixed.
        # Let's do case-insensitive search.
        start = 0
        while True:
            idx = text.lower().find(proj.lower(), start)
            if idx == -1:
                break
            project_positions.append((idx, proj))
            start = idx + 1
            
    # Sort by position
    project_positions.sort(key=lambda x: x[0])
    
    # Iterate through segments
    for i in range(len(project_positions)):
        pos, proj_name = project_positions[i]
        # End of this segment is start of next project or end of text
        end_pos = project_positions[i+1][0] if i+1 < len(project_positions) else len(text)
        
        # Define segment text
        # Limit segment length to avoid capturing unrelated text if projects are far apart
        segment_len = end_pos - pos
        if segment_len > 5000: # Arbitrary large limit
            segment_len = 5000
        segment = text[pos:pos+segment_len]
        
        # Search for Start/Begin keywords AND Spring 2022 date in this segment
        # We look for: keyword ... date
        # Example: "Begin Construction: Spring 2022"
        # We should ensure the date is associated with the keyword.
        # Let's find all dates in the segment.
        
        for match in date_pattern.finditer(segment):
            date_str = match.group(0)
            date_pos = match.start()
            
            # Check context before the date (e.g., within previous 50 chars)
            context = segment[max(0, date_pos - 100):date_pos]
            
            # Check if any start keyword is in context
            is_start = False
            for kw in start_keywords:
                if kw.lower() in context.lower():
                    is_start = True
                    break
            
            if is_start:
                found_projects.add(proj_name)
                # print(f"Found: {proj_name} -> {date_str} (Context: {context.strip()})")

# Calculate total funding
relevant_projects = df_funding[df_funding['Project_Name'].isin(found_projects)]
total_amount = pd.to_numeric(relevant_projects['Amount']).sum()
count = len(relevant_projects)

print("__RESULT__:")
print(json.dumps({"count": count, "total_amount": total_amount, "projects": list(found_projects)}))"""

env_args = {'var_function-call-2878608132661582587': ['Funding'], 'var_function-call-2878608132661583018': 'file_storage/function-call-2878608132661583018.json', 'var_function-call-6539417024683493818': 'file_storage/function-call-6539417024683493818.json', 'var_function-call-6539417024683493925': 'file_storage/function-call-6539417024683493925.json'}

exec(code, env_args)
