code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-6539417024683493818'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6539417024683493925'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Ensure Amount is numeric
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])
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
    
    # Identify project locations
    project_positions = []
    for proj in funding_projects:
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
        end_pos = project_positions[i+1][0] if i+1 < len(project_positions) else len(text)
        
        segment_len = end_pos - pos
        # Heuristic: Project sections are usually not huge. 
        # But let's check up to 2000 chars or next project.
        if segment_len > 3000: 
            segment_len = 3000
        segment = text[pos:pos+segment_len]
        
        # Look for dates
        for match in date_pattern.finditer(segment):
            date_pos = match.start()
            
            # Context window before date
            context = segment[max(0, date_pos - 100):date_pos]
            
            # Check keywords
            is_start = False
            for kw in start_keywords:
                if kw.lower() in context.lower():
                    is_start = True
                    break
            
            if is_start:
                found_projects.add(proj_name)

# Calculate total funding
relevant_projects = df_funding[df_funding['Project_Name'].isin(found_projects)]
total_amount = int(relevant_projects['Amount'].sum()) # Convert to standard int
count = int(len(relevant_projects)) # Convert to standard int

print("__RESULT__:")
print(json.dumps({"count": count, "total_amount": total_amount, "projects": list(found_projects)}))"""

env_args = {'var_function-call-2878608132661582587': ['Funding'], 'var_function-call-2878608132661583018': 'file_storage/function-call-2878608132661583018.json', 'var_function-call-6539417024683493818': 'file_storage/function-call-6539417024683493818.json', 'var_function-call-6539417024683493925': 'file_storage/function-call-6539417024683493925.json'}

exec(code, env_args)
