code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-2661118915962742960'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2661118915962742543'], 'r') as f:
    funding_data = json.load(f)
    
funding_df = pd.DataFrame(funding_data)
# Convert Amount to numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Filter for park related projects in Funding
# Hint: "park" in topic. Since we don't have topic yet, we use Project_Name for "Park".
# Also "Playground" could be park related.
# Let's start with "Park" and "Playground" in Project_Name.
def is_park_project(name):
    name = name.lower()
    return 'park' in name or 'playground' in name

park_projects_df = funding_df[funding_df['Project_Name'].apply(is_park_project)]
park_project_names = park_projects_df['Project_Name'].unique().tolist()

print(f"Candidate Park Projects: {len(park_project_names)}")
print(park_project_names)

completed_2022_projects = set()

# Normalize text for easier searching
# We will search for each project name in the docs.
# If found, we look at the subsequent text.

for doc in civic_docs:
    text = doc['text']
    # Iterate over all candidate projects
    for proj_name in park_project_names:
        # Find matches of project name
        # Use re.escape to handle special chars in name
        pattern = re.escape(proj_name)
        # We want to find the project name as a header roughly. 
        # But simple search is safer.
        matches = [m.start() for m in re.finditer(pattern, text, re.IGNORECASE)]
        
        for start_idx in matches:
            # Look at the text following the project name (e.g. next 500 chars)
            # Find the end of this project section. Usually sections end with another project name or double newline?
            # Let's just take 500 chars.
            snippet = text[start_idx:start_idx+600]
            
            # Check for completion in 2022
            # Patterns:
            # 1. "Construction was completed" ... "2022"
            # 2. "Complete Construction:" ... "2022"
            # 3. "Construction completed" ... "2022"
            
            # We must convert snippet to lower for case-insensitive check
            snippet_lower = snippet.lower()
            
            # Check for completion keywords
            if 'construction' in snippet_lower and ('completed' in snippet_lower or 'complete' in snippet_lower):
                # Check if "2022" is present
                if '2022' in snippet_lower:
                    # Now we need to be careful. 
                    # "Complete Construction: Summer 2023" (contains 'construction', 'complete') - NO
                    # "Construction was completed November 2022" - YES
                    
                    # Regex to verify 2022 is the year of completion
                    # Look for "completed ... 2022" or "complete construction ... 2022"
                    # Allow for month/season in between
                    
                    # P1: construction (was)? completed,? (in)? (month/season)? 2022
                    # P2: complete construction:? (month/season)? 2022
                    
                    # Regex
                    # \b matches word boundary
                    # We want to match: (construction|complete).*?2022
                    # But we want to ensure no other year comes before 2022 in that span?
                    # Or just check specific phrases.
                    
                    p1 = re.search(r'construction\s+(was\s+)?completed.*?2022', snippet_lower, re.DOTALL)
                    p2 = re.search(r'complete\s+construction.*?2022', snippet_lower, re.DOTALL)
                    
                    if p1 or p2:
                        # One more check: make sure "design" isn't the thing being completed 
                        # (though we looked for "construction" keyword specifically).
                        # p1 looks for "construction ... completed". p2 looks for "complete construction".
                        # These should be safe from "complete design".
                        
                        # Check false positive: "Complete Construction: Summer 2023. Updated 2022."
                        # If the snippet has 2022 but it's not the year.
                        # The regex ensures 2022 follows the completion phrase.
                        # But what if "Complete Construction: 2023. Report date 2022."?
                        # The regex `.*?` is greedy or non-greedy? `.*?` is non-greedy.
                        # It will match the closest 2022.
                        # If "Complete Construction: 2023" appears, it won't match 2022 immediately unless 2022 is first.
                        # Wait. If text is "Complete Construction: 2023. (Updated 2022)", the regex `.*?2022` will match spanning across 2023.
                        # I should limit the distance or ensure no other year (202x) is in between.
                        
                        # Let's extract the date string found.
                        # Helper to validate match
                        def is_valid_match(match, text_segment):
                            span = text_segment[match.start():match.end()]
                            # If there is a 202x (where x!=2) in the span, it might be the actual date.
                            # e.g. "Complete Construction: 2023 ... 2022"
                            # We want 2022 to be the date.
                            years = re.findall(r'202\d', span)
                            if len(years) > 0 and years[0] != '2022':
                                return False
                            return True

                        valid = False
                        if p1 and is_valid_match(p1, snippet_lower): valid = True
                        if p2 and is_valid_match(p2, snippet_lower): valid = True
                        
                        if valid:
                            completed_2022_projects.add(proj_name)

print("Identified Projects:")
print(list(completed_2022_projects))

# Calculate total funding
total_funding = funding_df[funding_df['Project_Name'].isin(completed_2022_projects)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"total_funding": int(total_funding), "projects": list(completed_2022_projects)}))"""

env_args = {'var_function-call-2661118915962742960': 'file_storage/function-call-2661118915962742960.json', 'var_function-call-2661118915962742543': 'file_storage/function-call-2661118915962742543.json'}

exec(code, env_args)
