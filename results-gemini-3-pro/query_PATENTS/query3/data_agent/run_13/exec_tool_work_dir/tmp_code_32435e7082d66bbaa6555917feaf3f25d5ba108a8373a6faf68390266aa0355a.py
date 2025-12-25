code = """import json
import re

# Load UC Patents Info
uc_file_path = locals()['var_function-call-163982095095483053']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

# Extract UC Publication Numbers
uc_pubs = set()
pat_pattern = re.compile(r"(?:publication|pub\.)\s+(?:number|no\.)\s+([A-Z]{2}-[\w\d-]+)")

for row in uc_data:
    info = row['Patents_info']
    match = pat_pattern.search(info)
    if match:
        uc_pubs.add(match.group(1))

# Load All Patents
all_file_path = locals()['var_function-call-12118947113934152352']
with open(all_file_path, 'r') as f:
    all_data = json.load(f)

results = {} # assignee -> set of cpc_subclasses

# Regex to extract assignee from Patents_info
# Pattern: "Assignee Name holds..." or "In Country, the application ... is owned by Assignee Name and..."
# The patterns in previous output:
# "PANASONIC IP MAN CO LTD holds the US patent application..."
# "In US, the application ... is owned by UNIV CALIFORNIA and..."
# "The JP patent filing ... is assigned to UNIV CALIFORNIA and..."
# "The AU application ... is belonging to UNIV CALIFORNIA and..."
# "Patent filing ... held by UNIV CALIFORNIA..."
# "Patent application ... from KR, owned by UNIV CALIFORNIA, with..."

# This seems complicated to extract perfectly.
# Maybe I can assume the text up to "holds", "is owned by", "is assigned to", "is belonging to" contains the assignee?
# But sometimes "In US, the application ... is owned by Assignee".
# I need to capture the assignee name.
# Let's look at patterns again.
# 1. "^(.*?) holds the"
# 2. "is owned by (.*?) and"
# 3. "is assigned to (.*?) and"
# 4. "is belonging to (.*?) and"
# 5. "held by (.*?), with" or "held by (.*?) and"
# 6. "belonging to (.*?), with"

# Let's try to define a function to extract assignee.

def get_assignee(text):
    text = text.replace('\n', ' ')
    # Case 1: "X holds the..."
    m = re.search(r"^(.*?) holds the ", text)
    if m:
        return m.group(1).strip()
    
    # Case 2: "... is owned by X and" or "... is owned by X, with"
    m = re.search(r"is owned by (.*?) (?:and|with|has)", text)
    if m:
        return m.group(1).strip()
    
    # Case 3: "... is assigned to X and"
    m = re.search(r"is assigned to (.*?) (?:and|with|has)", text)
    if m:
        return m.group(1).strip()
    
    # Case 4: "... is belonging to X and"
    m = re.search(r"is belonging to (.*?) (?:and|with|has)", text)
    if m:
        return m.group(1).strip()
        
    # Case 5: "held by X, with" or "held by X and"
    m = re.search(r"held by (.*?) (?:and|with|,)", text)
    if m:
        return m.group(1).strip()
    
    # Case 6: "belonging to X, with"
    m = re.search(r"belonging to (.*?) (?:and|with|,)", text)
    if m:
        return m.group(1).strip()
        
    return None

def get_subclass(cpc_json_str):
    try:
        cpc_list = json.loads(cpc_json_str)
        if not cpc_list:
            return None
        # Assume first is primary
        primary = cpc_list[0]
        # entry usually has 'code' or similar?
        # Let's check the structure of cpc list items from previous output? 
        # Wait, the previous output didn't show cpc content deeply.
        # But description says "JSON-like list of Cooperative Patent Classification entries, each with code and metadata."
        # I'll check if 'code' key exists.
        if 'code' in primary:
            code = primary['code']
            # Subclass is first 4 chars e.g. H01L
            return code[:4]
    except:
        return None
    return None

citing_assignees = {} # name -> set of subclasses

for row in all_data:
    # Check citations
    try:
        cits = json.loads(row['citation'])
    except:
        continue
        
    cited_uc = False
    for c in cits:
        if c.get('publication_number') in uc_pubs:
            cited_uc = True
            break
            
    if cited_uc:
        assignee = get_assignee(row['Patents_info'])
        if assignee:
            # Clean assignee name
            assignee = assignee.strip()
            # Exclude UNIV CALIFORNIA
            if "UNIV CALIFORNIA" in assignee: # Simple check to exclude variants
                continue
            
            subclass = get_subclass(row['cpc'])
            if subclass:
                if assignee not in citing_assignees:
                    citing_assignees[assignee] = set()
                citing_assignees[assignee].add(subclass)

# Convert sets to lists for JSON serialization
final_result = []
all_subclasses = set()
for k, v in citing_assignees.items():
    final_result.append({"assignee": k, "subclasses": list(v)})
    all_subclasses.update(v)

print("__RESULT__:")
print(json.dumps({"assignees": final_result, "all_subclasses": list(all_subclasses)}))"""

env_args = {'var_function-call-3523691000772885977': 'file_storage/function-call-3523691000772885977.json', 'var_function-call-163982095095483053': 'file_storage/function-call-163982095095483053.json', 'var_function-call-7359064648347536263': ['AU-2898989-A', 'US-2023279470-A1', 'CN-101584047-A', 'US-2020025859-A1', 'US-7745569-B2', 'CN-102584712-A', 'KR-20200041324-A', 'US-2018304537-A1', 'KR-20180041236-A', 'US-2021282642-A1'], 'var_function-call-8038203737880887453': [{'cnt': '277813'}], 'var_function-call-12118947113934152352': 'file_storage/function-call-12118947113934152352.json'}

exec(code, env_args)
