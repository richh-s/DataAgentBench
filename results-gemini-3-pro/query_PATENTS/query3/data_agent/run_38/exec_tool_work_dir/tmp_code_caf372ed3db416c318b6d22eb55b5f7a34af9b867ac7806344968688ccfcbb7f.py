code = """import json
import re

# Load UC patents info
uc_file_path = locals()['var_function-call-8137744820168532470']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

uc_pub_nums = set()
pub_num_pattern = re.compile(r'(?:publication|pub\.|publication\s+no\.)\s+(?:number\s+)?([A-Z0-9-]+)', re.IGNORECASE)

def extract_pub_num(info_str):
    m = pub_num_pattern.search(info_str)
    if m:
        return m.group(1)
    return None

def extract_assignee(info_str):
    # Heuristic: "X holds the...", "In US, the application ... is owned by X and...", "Application ... from US, owned by X, with..."
    # Pattern 1: "^(.*?) holds the"
    # Pattern 2: "is owned by (.*?) and"
    # Pattern 3: "is held by (.*?) and"
    # Pattern 4: "is assigned to (.*?) and"
    # Pattern 5: "belonging to (.*?) and"
    # Pattern 6: "owned by (.*?), with"
    # Pattern 7: "held by (.*?), with"
    # Pattern 8: "assigned to (.*?), with"
    # Pattern 9: "belonging to (.*?), with"
    
    patterns = [
        r'^(.*?) holds the',
        r'is owned by (.*?) and',
        r'is held by (.*?) and',
        r'is assigned to (.*?) and',
        r'is belonging to (.*?) and',
        r'owned by (.*?), with',
        r'held by (.*?), with',
        r'assigned to (.*?), with',
        r'belonging to (.*?), with'
    ]
    
    for pat in patterns:
        m = re.search(pat, info_str)
        if m:
            return m.group(1).strip()
    return "UNKNOWN"

for row in uc_data:
    pn = extract_pub_num(row['Patents_info'])
    if pn:
        uc_pub_nums.add(pn)

print(f"Found {len(uc_pub_nums)} UC patents.")

# Load all patents
all_file_path = locals()['var_function-call-16893693537298639860']
with open(all_file_path, 'r') as f:
    all_data = json.load(f)

citing_records = []
needed_subclasses = set()

for row in all_data:
    p_info = row.get('Patents_info', '')
    assignee = extract_assignee(p_info)
    
    # Check if assignee is UC (exclude)
    # Be careful with variations: "UNIV CALIFORNIA", "THE REGENTS...", "UNIVERSITY OF CALIFORNIA"
    if "UNIV CALIFORNIA" in assignee or "UNIVERSITY OF CALIFORNIA" in assignee:
        continue
    
    citations = row.get('citation', '[]')
    try:
        citations_list = json.loads(citations)
    except:
        citations_list = []
        
    cites_uc = False
    for cit in citations_list:
        if cit.get('publication_number') in uc_pub_nums:
            cites_uc = True
            break
            
    if cites_uc:
        # Get CPC
        cpc_str = row.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
        except:
            cpc_list = []
        
        if cpc_list:
            # Assuming first is primary
            # CPC object structure? The description says "JSON-like list... each with code"
            # Let's inspect one if needed, but usually it has 'code'
            first_cpc = cpc_list[0]
            if isinstance(first_cpc, dict):
                code = first_cpc.get('code', '')
            elif isinstance(first_cpc, str):
                code = first_cpc # sometimes simple list of strings
            else:
                code = ''
            
            # Extract subclass (first 4 chars, e.g. H01L)
            if len(code) >= 4:
                subclass = code[:4]
                citing_records.append({
                    "assignee": assignee,
                    "subclass": subclass
                })
                needed_subclasses.add(subclass)

print("__RESULT__:")
print(json.dumps({"records": citing_records, "subclasses": list(needed_subclasses)}))"""

env_args = {'var_function-call-1948186479364963139': 'file_storage/function-call-1948186479364963139.json', 'var_function-call-1480699074357668368': [{'count(*)': '277813'}], 'var_function-call-5067680842395544481': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'Application (no. US-77231501-A) from US, owned by CALIFORNIA INST OF TECHN, with publication no. US-6559125-B1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'The US application (number US-202016813462-A) is held by CALIFORNIA INST OF TECHN and has publication no. US-11226538-B2.'}, {'Patents_info': 'CALIFORNIA INST OF TECHN holds the US patent application (number US-201815983019-A), with publication number US-10746600-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'In US, the application (number US-201715617385-A) is held by PACIFIC BIOSCIENCES CALIFORNIA INC and has pub. number US-2017343479-A1.'}, {'Patents_info': 'The IL application (number IL-9133089-A) is held by CALIFORNIA BIOTECHNOLOGY INC and has publication number IL-91330-A0.'}], 'var_function-call-8137744820168532470': 'file_storage/function-call-8137744820168532470.json', 'var_function-call-16893693537298639860': 'file_storage/function-call-16893693537298639860.json'}

exec(code, env_args)
