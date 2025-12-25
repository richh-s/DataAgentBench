code = """import json
import re

# Load UNIV CAL patents
with open(locals()['var_function-call-4429695443543594421'], 'r') as f:
    univ_cal_data = json.load(f)

target_pub_nums = set()
pub_num_pattern = re.compile(r"publication (?:number|no\.)\s+([A-Z]{2}-[\w\d-]+)")

for item in univ_cal_data:
    info = item.get('Patents_info', '')
    match = pub_num_pattern.search(info)
    if match:
        target_pub_nums.add(match.group(1))

# Load Citing patents
with open(locals()['var_function-call-13044141528385214206'], 'r') as f:
    citing_data = json.load(f)

citing_results = []
# Regex for assignee extraction
assignee_patterns = [
    re.compile(r"^(.*?) holds"),
    re.compile(r"is (?:owned|assigned|held|belonging) (?:to|by) (.*?) (?:and|,)"),
    re.compile(r"held by (.*?),")
]

unique_subclasses = set()

for item in citing_data:
    info = item.get('Patents_info', '')
    
    # Extract Assignee
    assignee = None
    for pat in assignee_patterns:
        m = pat.search(info)
        if m:
            assignee = m.group(1).strip()
            break
            
    if not assignee:
        continue
        
    # Check if assignee is UNIV CALIFORNIA (just in case query missed some or to be sure)
    if "UNIV CALIFORNIA" in assignee:
        continue

    # Check Citations
    citations_str = item.get('citation', '[]')
    try:
        citations = json.loads(citations_str)
    except:
        continue
        
    cited_target = False
    for cit in citations:
        p_num = cit.get('publication_number', '')
        if p_num in target_pub_nums:
            cited_target = True
            break
            
    if cited_target:
        # Extract Primary CPC Subclass
        cpc_str = item.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
        except:
            cpc_list = []
            
        if cpc_list:
            # Assume first is primary
            primary_cpc = cpc_list[0]
            code = primary_cpc.get('code', '')
            # Subclass is first 4 chars?
            # Example: H01M10/0568 -> H01M
            if len(code) >= 4:
                subclass = code[:4]
                unique_subclasses.add(subclass)
                citing_results.append({
                    "assignee": assignee,
                    "subclass": subclass
                })

print("__RESULT__:")
print(json.dumps({
    "subclasses": list(unique_subclasses),
    "citing_info": citing_results
}))"""

env_args = {'var_function-call-1365127592045500777': 'file_storage/function-call-1365127592045500777.json', 'var_function-call-4429695443543594421': 'file_storage/function-call-4429695443543594421.json', 'var_function-call-13044141528385214206': 'file_storage/function-call-13044141528385214206.json'}

exec(code, env_args)
