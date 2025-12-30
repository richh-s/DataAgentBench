code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-4654103334756958724'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-4654103334756962095'], 'r') as f:
    funding_data = json.load(f)

# Helper to normalize strings
def normalize(s):
    return s.strip().lower()

# Extract projects from text
projects = []

for doc in civic_docs:
    text = doc['text']
    # The text contains multiple projects.
    # We look for patterns like: "Project Name\n\n(cid:190) Updates"
    # Regex to find project starts
    # We look for a line that is followed by a line starting with (cid:190) Updates or (cid:190) Project Description
    # We will use re.finditer to get all occurrences
    
    # Pattern: a non-empty line (Project Name), followed by optional newlines, followed by (cid:190) (Updates|Project Description)
    pattern = re.compile(r'(?P<name>[^\n]+)\n+(?=\(cid:190\) (?:Updates|Project Description|Project Updates))')
    
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        p_name = match.group('name').strip()
        start_idx = match.start()
        
        # End index is the start of the next match, or end of text
        if i < len(matches) - 1:
            end_idx = matches[i+1].start()
        else:
            end_idx = len(text)
            
        p_text = text[start_idx:end_idx]
        
        # Analyze p_text for status and date
        # Check for completion in 2022
        # Phrases: "Construction was completed [Date]", "Complete Construction: [Date]", "Notice of completion filed [Date]"
        
        is_completed_2022 = False
        
        # Regex for completion dates
        # "completed[, ]+([A-Za-z]+ \d{4})"
        # "Complete Construction: ([A-Za-z]+ \d{4})"
        
        completion_patterns = [
            r'Construction was completed,? ([A-Za-z]+ \d{4})',
            r'Complete Construction: ([A-Za-z]+ \d{4})',
            r'Notice of completion filed,? ([A-Za-z]+ \d{4})' # This might be later than completion
        ]
        
        found_dates = []
        for cp in completion_patterns:
            dates = re.findall(cp, p_text, re.IGNORECASE)
            found_dates.extend(dates)
            
        # Check if any date is in 2022
        for date_str in found_dates:
            if '2022' in date_str:
                # Double check context?
                # "Construction was completed November 2022" -> YES
                # "Complete Construction: Summer 2022" -> YES
                # "Notice of completion filed January 2023" -> If this is the only date, it might mean completion was earlier.
                # But let's look at the text snippet in the preview:
                # "Construction was completed November 2022. Notice of completion filed January 2023"
                # Here, completion is 2022.
                
                # If we find a 2022 completion date, we mark it.
                # However, if we find "Complete Construction: Summer 2023", that overrides?
                # We should look for PAST tense for completed.
                # "Construction was completed" is strong.
                # "Complete Construction:" might be future schedule.
                
                # Let's verify the phrase.
                # If "Construction was completed ... 2022", it's done in 2022.
                if 'completed' in p_text.lower() and '2022' in date_str:
                     is_completed_2022 = True
                # If "Complete Construction: ... 2022" and it's under "Updates" or "Construction" section?
                # The preview shows "Capital Improvement Projects (Construction)"
                # But "Bluffs Park Shade Structure" says "Updates: Construction was completed November 2022".
                # So looking for "Construction was completed" is good.
                pass
        
        # Refined Logic:
        # Check if text says "Construction was completed" AND that sentence/phrase contains "2022".
        # Or "Complete Construction: [Month] 2022" (if it was completed then).
        # Actually, "Complete Construction: April 2023" is a target date.
        # "Construction was completed November 2022" is a fact.
        
        if re.search(r'Construction was completed,? [A-Za-z]+ 2022', p_text, re.IGNORECASE):
            is_completed_2022 = True
        elif re.search(r'Complete Construction: [A-Za-z]+ 2022', p_text, re.IGNORECASE):
             # This might be a target date. If the project is listed under "Not Started" or "Design", it's a target.
             # If "Construction", it might be target.
             # Only if it says "was completed" we are sure.
             # But let's check the section header?
             # The header "Capital Improvement Projects (Construction)" applies to multiple projects?
             # Yes.
             # But "Bluffs Park Shade Structure" is under "Construction" (maybe? in the preview it's hard to tell indentation).
             # Wait, "Bluffs Park Shade Structure" is followed by "Updates: Construction was completed...".
             # So it is completed.
             
             # Let's rely on "Construction was completed" for now.
             pass
        
        # Also check for "Notice of completion filed ... 2022"?
        
        if is_completed_2022:
            projects.append({'name': p_name, 'text': p_text})

# Now filter for park related and sum funding
total_funding = 0
park_keywords = ['park', 'playground', 'recreation'] # Add more if needed

matched_projects = []

for p in projects:
    name = p['name']
    
    # Check if park related
    is_park = False
    if any(k in name.lower() for k in park_keywords):
        is_park = True
    
    if is_park:
        # Find funding
        # We need exact match or close match
        found_fund = False
        for fund in funding_data:
            if fund['Project_Name'].strip().lower() == name.strip().lower():
                total_funding += fund['Amount']
                matched_projects.append((name, fund['Amount']))
                found_fund = True
                break
        if not found_fund:
            # Try fuzzy match or substring?
            # The names in the preview matched exactly "Bluffs Park Shade Structure".
            pass

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-4654103334756958724': 'file_storage/function-call-4654103334756958724.json', 'var_function-call-4654103334756962095': 'file_storage/function-call-4654103334756962095.json'}

exec(code, env_args)
