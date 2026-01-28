code = """import json
import re

# Access file paths
path_docs = locals()['var_function-call-3874891945524290296']
path_funding = locals()['var_function-call-15854994629238298351']

# Load files
with open(path_docs, 'r') as f:
    docs = json.load(f)

with open(path_funding, 'r') as f:
    funding = json.load(f)

# Funding map
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding}
project_names = list(funding_map.keys())

# Regex patterns
# Note: In the python code string, backslashes need to be escaped if inside a string?
# But here I am writing the python code that will be executed.
# I will use raw strings for regex where possible, but be careful with newlines.
start_patterns = [
    r"Begin [Cc]onstruction[:\s]+(.*?)(?:\n|$)",
    r"Construction Start[:\s]+(.*?)(?:\n|$)",
    r"Start Date[:\s]+(.*?)(?:\n|$)",
    r"Work [Bb]egan[:\s]+(.*?)(?:\n|$)"
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
    
    # Pre-compile regex for the project name? No, simpler to string match.
    # Actually, iterate docs.
    
    for doc in docs:
        text = doc['text']
        if proj in text:
            # Find all occurrences
            try:
                # regex escape the project name
                proj_re = re.escape(proj)
                # Find indices
                indices = [m.start() for m in re.finditer(proj_re, text)]
                
                for idx in indices:
                    snippet = text[idx:idx+2000] # Look ahead 2000 chars
                    
                    # Check topics
                    if not is_disaster:
                        for kw in disaster_keywords:
                            if kw.lower() in snippet.lower():
                                is_disaster = True
                                break
                    
                    # Check Start Date
                    for pat in start_patterns:
                        m = re.search(pat, snippet)
                        if m:
                            date_str = m.group(1)
                            if "2022" in date_str:
                                started_2022 = True
                                found_st = date_str
                                
                    # Check past tense phrases
                    if "construction began" in snippet.lower():
                        # Find the phrase and check surrounding text
                        start_phrase_idx = snippet.lower().find("construction began")
                        # Check 50 chars after
                        date_snippet = snippet[start_phrase_idx:start_phrase_idx+60]
                        if "2022" in date_snippet:
                            started_2022 = True
            except Exception as e:
                pass

    if is_disaster and started_2022:
        matches[proj] = funding_map[proj]

total_amount = sum(matches.values())
print("__RESULT__:")
print(json.dumps({"total_funding": total_amount, "projects": list(matches.keys())}))"""

env_args = {'var_function-call-3965553099974352021': ['civic_docs'], 'var_function-call-4642291863643268056': 'file_storage/function-call-4642291863643268056.json', 'var_function-call-15854994629238298351': 'file_storage/function-call-15854994629238298351.json', 'var_function-call-3874891945524290296': 'file_storage/function-call-3874891945524290296.json'}

exec(code, env_args)
