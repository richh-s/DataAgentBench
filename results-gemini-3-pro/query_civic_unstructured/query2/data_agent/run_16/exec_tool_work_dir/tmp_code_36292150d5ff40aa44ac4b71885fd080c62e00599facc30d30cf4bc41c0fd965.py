code = """import json
import re

# Load data
with open(locals()['var_function-call-2466750499459274811'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-3057395287432783199'], 'r') as f:
    civic_docs = json.load(f)

project_names = [r['Project_Name'] for r in funding_data]
# Sort by length descending to match longer names first to avoid partial matches if names are substrings
project_names.sort(key=len, reverse=True)

completed_2022_projects = set()

# Regex patterns for completion in 2022
# "Construction was completed November 2022"
# "Construction was completed, November 2022"
# "Complete Construction: November 2022"
# "Construction completed: 2022"
# We look for "complete" ... "2022" within a short window, and ensure year is 2022.
# We also need to avoid "Complete Design: 2022".
# So we specifically look for construction completion.

completion_patterns = [
    r"construction\s+was\s+completed,?\s+([a-zA-Z]+)?\s?2022",
    r"complete\s+construction:?\s+([a-zA-Z]+)?\s?2022",
    r"construction\s+completed\s+([a-zA-Z]+)?\s?2022"
]

def check_park_related(text):
    text_lower = text.lower()
    keywords = ['park', 'playground', 'recreation']
    return any(k in text_lower for k in keywords)

for doc in civic_docs:
    text = doc['text']
    # Normalize newlines to spaces for easier regex
    # text_flat = text.replace('\n', ' ') 
    # Actually, keep newlines might be useful for separation, but for regex matching across lines it's easier to flat.
    # But let's keep text as is and matches can handle whitespace.
    
    # We iterate project names and find them in text
    for pname in project_names:
        # Use regex escape for pname
        pname_esc = re.escape(pname)
        # Find all occurrences
        for match in re.finditer(pname_esc, text, re.IGNORECASE):
            # Extract a context window after the match
            start = match.end()
            # Look ahead until the next double newline or some reasonable limit (e.g. 500 chars)
            # or until the next project name (which is hard to know without finding all first)
            # Let's just take next 1000 chars.
            context = text[start:start+1000]
            
            # Check if park related (in name or context)
            # Actually, "park-related" check should probably be on the Project Name or the context.
            # If Project Name contains "Park", it's park related.
            is_park = check_park_related(pname) or check_park_related(context)
            
            if is_park:
                # Check status
                # Look for completion in 2022 in the context
                is_completed_2022 = False
                for pat in completion_patterns:
                    if re.search(pat, context, re.IGNORECASE):
                        is_completed_2022 = True
                        break
                
                if is_completed_2022:
                    completed_2022_projects.add(pname)

# Now calculate funding
total_funding = 0
matching_funding_records = []

for r in funding_data:
    if r['Project_Name'] in completed_2022_projects:
        total_funding += int(r['Amount'])
        matching_funding_records.append(r)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": list(completed_2022_projects)}))"""

env_args = {'var_function-call-2466750499459274811': 'file_storage/function-call-2466750499459274811.json', 'var_function-call-2466750499459274820': 'file_storage/function-call-2466750499459274820.json', 'var_function-call-3057395287432783199': 'file_storage/function-call-3057395287432783199.json'}

exec(code, env_args)
