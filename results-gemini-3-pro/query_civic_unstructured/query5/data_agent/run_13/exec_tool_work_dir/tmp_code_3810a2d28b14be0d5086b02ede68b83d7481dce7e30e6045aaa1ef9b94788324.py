code = """import json
import re

# Load files
with open('var_function-call-3874891945524290296.json') as f:
    docs = json.load(f)

with open('var_function-call-15854994629238298351.json') as f:
    funding = json.load(f)

# Funding map
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding}
project_names = list(funding_map.keys())

# Regex patterns
start_patterns = [
    re.compile(r"Begin [Cc]onstruction[:\s]+(.*?)(?:\n|$)"),
    re.compile(r"Construction Start[:\s]+(.*?)(?:\n|$)"),
    re.compile(r"Start Date[:\s]+(.*?)(?:\n|$)"),
    re.compile(r"Work [Bb]egan[:\s]+(.*?)(?:\n|$)")
]

disaster_suffixes = ["(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)", "(FEMA)", "(CalOES)", "(CalJPIA)", "Disaster Recovery"]
disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Fire", "Disaster", "Emergency"]

matches = {}

for proj in project_names:
    is_disaster = False
    started_2022 = False
    
    # Check suffix
    for s in disaster_suffixes:
        if s.lower() in proj.lower():
            is_disaster = True
            break
            
    # Search in docs
    found_st = None
    
    for doc in docs:
        text = doc['text']
        if proj in text:
            # Find all occurrences
            # We look at a window after the project name
            indices = [m.start() for m in re.finditer(re.escape(proj), text)]
            for idx in indices:
                snippet = text[idx:idx+2000] # Look ahead 2000 chars
                
                # Check topics if not yet disaster
                if not is_disaster:
                    for kw in disaster_keywords:
                        if kw.lower() in snippet.lower():
                            # Be careful not to match generic text. 
                            # Usually keywords appear in "Topic: ..." or description.
                            # Given the hint, we assume presence in the project block is sufficient.
                            is_disaster = True
                            break
                
                # Check Start Date
                for pat in start_patterns:
                    m = pat.search(snippet)
                    if m:
                        date_str = m.group(1)
                        if "2022" in date_str:
                            started_2022 = True
                            found_st = date_str
                            
                # Also check "updates" section for past tense starts
                # "Construction began in January 2022"
                if "construction began" in snippet.lower():
                    # extract simplified date
                    sub_idx = snippet.lower().find("construction began")
                    sub_snippet = snippet[sub_idx:sub_idx+50]
                    if "2022" in sub_snippet:
                        started_2022 = True
                        found_st = sub_snippet

    if is_disaster and started_2022:
        matches[proj] = funding_map[proj]

total_amount = sum(matches.values())
print("__RESULT__:")
print(json.dumps({"total_funding": total_amount, "projects": list(matches.keys())}))"""

env_args = {'var_function-call-3965553099974352021': ['civic_docs'], 'var_function-call-4642291863643268056': 'file_storage/function-call-4642291863643268056.json', 'var_function-call-15854994629238298351': 'file_storage/function-call-15854994629238298351.json', 'var_function-call-3874891945524290296': 'file_storage/function-call-3874891945524290296.json'}

exec(code, env_args)
