code = """import json
import re

# Load UC patent info to get IDs again (or reuse if I could, but here I re-process for safety)
with open(locals()['var_function-call-10411442442073960916'], 'r') as f:
    uc_data = json.load(f)

uc_ids = set()
regex_pub = re.compile(r'(?:publication number|pub\. number|publication no\.)\s+([A-Za-z0-9\-]+)')
for row in uc_data:
    info = row.get('Patents_info', '')
    match = regex_pub.search(info)
    if match:
        uc_ids.add(match.group(1))

# Load all patents with citations
with open(locals()['var_function-call-12616504005831289557'], 'r') as f:
    all_patents = json.load(f)

matches = []
# Regex for assignee extraction
assignee_patterns = [
    re.compile(r'^(.+?) holds the'),
    re.compile(r'is owned by (.+?) (?:and|with)'),
    re.compile(r'is assigned to (.+?) (?:and|with)'),
    re.compile(r'is belonging to (.+?) (?:and|with)'),
    re.compile(r'held by (.+?), with'),
    re.compile(r'belonging to (.+?), with'),
    re.compile(r'assigned to (.+?), with'),
    re.compile(r'owned by (.+?), with')
]

cpc_subclasses = set()

results = []

for row in all_patents:
    citation_str = row.get('citation', '[]')
    try:
        citations = json.loads(citation_str)
    except:
        continue
    
    # Check if cites UC
    cites_uc = False
    for cit in citations:
        if cit.get('publication_number') in uc_ids:
            cites_uc = True
            break
    
    if cites_uc:
        # Extract Assignee
        info = row.get('Patents_info', '')
        assignee = None
        for pat in assignee_patterns:
            m = pat.search(info)
            if m:
                assignee = m.group(1).strip()
                break
        
        if not assignee:
            # Fallback or skip? Let's check if we can get it.
            # Maybe just clean the sentence?
            pass
        
        # Check if Assignee is UC (exclude)
        if assignee and "UNIV CALIFORNIA" not in assignee.upper() and "UNIVERSITY OF CALIFORNIA" not in assignee.upper():
            # Extract CPC
            cpc_str = row.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_str)
                if cpc_list and len(cpc_list) > 0:
                    primary_cpc = cpc_list[0].get('code', '')
                    # Subclass: first 4 chars e.g. H01M
                    if len(primary_cpc) >= 4:
                        subclass = primary_cpc[:4]
                        cpc_subclasses.add(subclass)
                        results.append({"assignee": assignee, "subclass": subclass})
            except:
                pass

print(f"Found {len(results)} matching records.")
print("__RESULT__:")
print(json.dumps({"subclasses": list(cpc_subclasses), "matches": results}))"""

env_args = {'var_function-call-15056912119011397630': 'file_storage/function-call-15056912119011397630.json', 'var_function-call-10236890153849732121': [{'COUNT(*)': '277813'}], 'var_function-call-10411442442073960916': 'file_storage/function-call-10411442442073960916.json', 'var_function-call-11213800036221116732': ['US-7745569-B2', 'TW-201925402-A', 'BR-9610580-A', 'AU-6535890-A', 'US-10337029-B2', 'BR-112021021092-A8', 'WO-2012162563-A2', 'US-2017145219-A1', 'CA-3027364-A1', 'HK-1250569-A1'], 'var_function-call-12616504005831289557': 'file_storage/function-call-12616504005831289557.json'}

exec(code, env_args)
