code = """import json
import pandas as pd
from collections import defaultdict

# Read funding database results
with open(var_call_eHjXm0iLq7FmCEyod4ch2HCV, 'r') as f:
    funding_data = json.load(f)

funded_projects = set([item['Project_Name'] for item in funding_data])

# Read civic docs database results
with open(var_call_TkreCFhV8ywTnKrAIOEjQ8i6, 'r') as f:
    docs_data = json.load(f)

# Try to find project entries with their status and name (simple extraction from example text)
# We'll focus only on documents that mention "Capital Improvement Projects (Design)" and parse likely project entries
project_names_design = set()
for doc in docs_data:
    text = doc.get('text', '').lower()
    if 'capital improvement projects (design)' in text:
        # simple extraction using lines between "Capital Improvement Projects (Design)" and next header
        # find the part of text
        start_idx = text.find('capital improvement projects (design)')
        if start_idx != -1:
            # take up to next section or reasonable cutoff
            section = text[start_idx:start_idx + 4000]
            # split by lines, loop through and look for likely project descriptions
            for line in section.split('\n'):
                # try to find project names by common format (avoid headers, look for update or schedule)
                if 'updates:' in line or 'project schedule:' in line or 'description:' in line:
                    # get previous line(s)
                    i = section.split('\n').index(line)
                    if i > 0:
                        prev_line = section.split('\n')[i-1].strip()
                        # exclude headers, blank, unrelated lines
                        if prev_line and 'project' in prev_line:
                            # project name is likely in prev_line
                            project_names_design.add(prev_line.title())

# Now, check which of these design-status projects are also in funded_projects
matching_projects = funded_projects.intersection(project_names_design)

# Final count is number of design-status capital projects with funding > $50,000
result = len(matching_projects)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eHjXm0iLq7FmCEyod4ch2HCV': 'file_storage/call_eHjXm0iLq7FmCEyod4ch2HCV.json', 'var_call_TkreCFhV8ywTnKrAIOEjQ8i6': 'file_storage/call_TkreCFhV8ywTnKrAIOEjQ8i6.json'}

exec(code, env_args)
