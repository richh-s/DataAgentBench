code = """import json
import re

# Load data
with open(locals()['var_function-call-13069126616893175602'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2392722741691488193'], 'r') as f:
    civic_docs = json.load(f)

# Extract unique project names and funding map
project_names = set()
project_funding = {} # Project_Name -> Total Amount

for record in funding_data:
    p_name = record['Project_Name']
    amount = int(record['Amount'])
    project_names.add(p_name)
    if p_name in project_funding:
        project_funding[p_name] += amount
    else:
        project_funding[p_name] = amount

# Sort project names by length desc to ensure longest match
sorted_p_names = sorted(list(project_names), key=len, reverse=True)

target_months = ['march', 'april', 'may']
target_season = 'spring'
target_year = '2022'

started_projects = set()

for doc in civic_docs:
    text = doc['text']
    # Find all project positions
    # We want to find (start_index, project_name)
    # Since names can overlap, we search carefully. 
    # But text is large, so simple find might be slow if many projects. 
    # Actually, 100 projects is small.
    
    found_projects = []
    for p_name in sorted_p_names:
        # Escape regex special chars in project name
        escaped_name = re.escape(p_name)
        # Look for project name. 
        # Note: Project name usually appears as a header or followed by newline
        # But let's just find all occurrences for now.
        for match in re.finditer(escaped_name, text, re.IGNORECASE):
            found_projects.append((match.start(), p_name))
            
    # Sort by position
    found_projects.sort(key=lambda x: x[0])
    
    # Process segments
    for i in range(len(found_projects)):
        start_idx, p_name = found_projects[i]
        
        # Determine end of segment (start of next project or reasonable limit)
        if i < len(found_projects) - 1:
            end_idx = found_projects[i+1][0]
        else:
            end_idx = len(text)
        
        # Limit segment size to avoid reading too much unrelated text 
        # (e.g. if next project is far away)
        # But usually they are close in a list. 
        # Let's cap at 2000 chars.
        segment = text[start_idx:min(end_idx, start_idx + 2000)]
        
        # Look for start date patterns in segment
        # Patterns:
        # Begin Construction: <date>
        # Construction Start: <date>
        # Start Date: <date>
        # Construction to begin: <date>
        
        date_patterns = [
            r"Begin [Cc]onstruction:?\s*([A-Za-z0-9\s,]+)",
            r"Construction [Ss]tart:?\s*([A-Za-z0-9\s,]+)",
            r"[Ss]tart [Dd]ate:?\s*([A-Za-z0-9\s,]+)",
            r"Construction to begin:?\s*([A-Za-z0-9\s,]+)",
            r"Construction expected to begin:?\s*([A-Za-z0-9\s,]+)"
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, segment)
            if match:
                date_str = match.group(1).lower()
                # Check for target date
                # "Spring 2022", "March 2022", "April 2022", "May 2022"
                # "Spring, 2022"
                
                # Check year
                if target_year in date_str:
                    # Check month/season
                    if target_season in date_str:
                        started_projects.add(p_name)
                        break
                    for month in target_months:
                        if month in date_str:
                            started_projects.add(p_name)
                            break
        
        if p_name in started_projects:
            continue

# Calculate results
total_amount = 0
for p in started_projects:
    total_amount += project_funding.get(p, 0)

print("__RESULT__:")
print(json.dumps({
    "count": len(started_projects),
    "total_funding": total_amount,
    "projects": list(started_projects)
}))"""

env_args = {'var_function-call-11013100090032240627': ['Funding'], 'var_function-call-11013100090032239808': ['civic_docs'], 'var_function-call-13069126616893175602': 'file_storage/function-call-13069126616893175602.json', 'var_function-call-13069126616893177209': 'file_storage/function-call-13069126616893177209.json', 'var_function-call-2392722741691488193': 'file_storage/function-call-2392722741691488193.json'}

exec(code, env_args)
