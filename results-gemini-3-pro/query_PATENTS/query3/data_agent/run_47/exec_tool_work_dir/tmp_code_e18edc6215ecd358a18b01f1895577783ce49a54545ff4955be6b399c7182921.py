code = """import json
import re

# Load UNIV CALIFORNIA patents info
with open(locals()['var_function-call-4071176841800524273'], 'r') as f:
    uc_patents_data = json.load(f)

# Extract UNIV CALIFORNIA publication numbers
uc_pub_nums = set()
pub_num_pattern = re.compile(r"publication (?:number|no\.|num\.)\s+([A-Za-z0-9\-]+)")

for row in uc_patents_data:
    info = row.get('Patents_info', '')
    match = pub_num_pattern.search(info)
    if match:
        uc_pub_nums.add(match.group(1))

# Load ALL patents data
with open(locals()['var_function-call-14099782207739025782'], 'r') as f:
    all_patents_data = json.load(f)

citing_info = [] # List of (assignee, cpc_subclass)

# Assignee extraction patterns
assignee_patterns = [
    re.compile(r"^(.*?) holds the"),
    re.compile(r"owned by (.*?)(?: and| with|,)"),
    re.compile(r"assigned to (.*?)(?: and| with|,)"),
    re.compile(r"belonging to (.*?)(?: and| with|,)"),
    re.compile(r"held by (.*?)(?: and| with|,)"),
]

def extract_assignee(text):
    for pat in assignee_patterns:
        m = pat.search(text)
        if m:
            return m.group(1).strip()
    # If starts with "In [Country], the application ... is [action] by [Assignee]"
    # Handled by "owned by", "assigned to" etc.
    return None

def extract_cpc_subclass(cpc_json):
    try:
        cpc_list = json.loads(cpc_json)
        if not cpc_list:
            return None
        # Assuming the first one is primary
        # Structure is usually [{"code": "..."}...] or just strings?
        # The prompt says "JSON-like list of Cooperative Patent Classification entries, each with code and metadata."
        # Let's assume dict with "code".
        first_cpc = cpc_list[0]
        if isinstance(first_cpc, dict):
            code = first_cpc.get('code', '')
        elif isinstance(first_cpc, str):
            code = first_cpc
        else:
            return None
        
        # Subclass is first 4 chars (e.g. H01L)
        if len(code) >= 4:
            return code[:4]
    except:
        return None
    return None

for row in all_patents_data:
    info = row.get('Patents_info', '')
    assignee = extract_assignee(info)
    
    if not assignee:
        continue
        
    if "UNIV CALIFORNIA" in assignee:
        continue
        
    citations = row.get('citation', '[]')
    try:
        cited_list = json.loads(citations)
    except:
        continue
        
    cited_nums = set()
    for c in cited_list:
        p_num = c.get('publication_number', '')
        if p_num:
            cited_nums.add(p_num)
            
    # Check intersection
    if not uc_pub_nums.isdisjoint(cited_nums):
        # Found a citation
        cpc_subclass = extract_cpc_subclass(row.get('cpc', '[]'))
        if cpc_subclass:
            citing_info.append({"assignee": assignee, "subclass": cpc_subclass})

# Result
print("__RESULT__:")
print(json.dumps(citing_info))"""

env_args = {'var_function-call-3584651619192785956': 'file_storage/function-call-3584651619192785956.json', 'var_function-call-4071176841800524273': 'file_storage/function-call-4071176841800524273.json', 'var_function-call-11677664063818156311': [{'COUNT(*)': '277813'}], 'var_function-call-14099782207739025782': 'file_storage/function-call-14099782207739025782.json'}

exec(code, env_args)
