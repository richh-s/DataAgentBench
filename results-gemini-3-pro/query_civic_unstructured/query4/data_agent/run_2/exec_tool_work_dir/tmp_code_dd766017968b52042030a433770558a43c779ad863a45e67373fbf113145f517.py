code = """import json
import re

# Load data
with open(locals()['var_function-call-18189666317777667959'], 'r') as f:
    funding_list = json.load(f)

with open(locals()['var_function-call-9598999800864405820'], 'r') as f:
    civic_docs = json.load(f)

# Map Project Name to Amount
project_funding = {}
for item in funding_list:
    name = item.get('Project_Name')
    try:
        amount = float(item.get('Amount', 0))
    except:
        amount = 0
    if name:
        project_funding[name] = amount

project_names = list(project_funding.keys())
project_names.sort(key=len, reverse=True)

started_projects = set()

# Regex for Spring 2022 (March, April, May)
# Patterns: Spring 2022, 2022 Spring, March 2022, April 2022, May 2022
# 2022-03, 2022-04, 2022-05
date_regex = re.compile(r"(Spring\s*,?\s*2022|2022\s*[\-]?\s*Spring|March\s*,?\s*2022|April\s*,?\s*2022|May\s*,?\s*2022|2022\s*[\-]\s*0?3|2022\s*[\-]\s*0?4|2022\s*[\-]\s*0?5)", re.IGNORECASE)

start_indicators = ["Begin Construction", "Construction Start", "Start Date", "Commence", "Construction Expected"]
exclude_indicators = ["Complete Design", "Advertise", "Bid", "Completion", "End", "Final Design", "Complete Construction"]

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    # Find matches
    matches = []
    for pname in project_names:
        idx = text.find(pname)
        while idx != -1:
            matches.append((idx, pname))
            idx = text.find(pname, idx + 1)
            
    matches.sort(key=lambda x: x[0])
    
    # Filter nested matches
    final_matches = []
    last_end = -1
    for start, name in matches:
        end = start + len(name)
        if start >= last_end:
            final_matches.append((start, name))
            last_end = end

    # Analyze segments
    for i in range(len(final_matches)):
        start, name = final_matches[i]
        if i < len(final_matches) - 1:
            segment = text[start:final_matches[i+1][0]]
        else:
            segment = text[start:]
            
        # Search for date in segment
        for dm in date_regex.finditer(segment):
            d_start = dm.start()
            # Look at context before date
            # Get previous line or 100 chars
            context = segment[max(0, d_start - 100):d_start]
            
            # Check for indicators
            # Find the position of the last indicator
            last_start_ind = -1
            for ind in start_indicators:
                ind_match = list(re.finditer(re.escape(ind), context, re.IGNORECASE))
                if ind_match:
                    last_start_ind = max(last_start_ind, ind_match[-1].start())
            
            last_exclude_ind = -1
            for ind in exclude_indicators:
                ind_match = list(re.finditer(re.escape(ind), context, re.IGNORECASE))
                if ind_match:
                    last_exclude_ind = max(last_exclude_ind, ind_match[-1].start())
            
            # Logic: 
            # If we have a start indicator, and it is CLOSER to the date than any exclude indicator (or no exclude indicator)
            # Then it's a match.
            # Example: "Complete Design: Fall 2021. Begin Construction: Spring 2022"
            # Context for Spring 2022: "...Complete Design: Fall 2021. Begin Construction: "
            # "Complete Design" is at index X. "Begin Construction" is at index Y. Y > X.
            # So "Begin Construction" is closer.
            
            if last_start_ind != -1:
                if last_start_ind > last_exclude_ind:
                    started_projects.add(name)
                    # print(f"MATCH: {name} -> {dm.group()} (Context: {context[last_start_ind:]})")

# Calculate total funding
total_funding = 0
count = 0
for name in started_projects:
    total_funding += project_funding.get(name, 0)
    count += 1

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(started_projects)}))"""

env_args = {'var_function-call-18189666317777669424': 'file_storage/function-call-18189666317777669424.json', 'var_function-call-18189666317777667959': 'file_storage/function-call-18189666317777667959.json', 'var_function-call-9598999800864405820': 'file_storage/function-call-9598999800864405820.json'}

exec(code, env_args)
