code = """import json
import re

# Load CPC Definitions
cpc_titles = {}
with open(locals()['var_function-call-12777540766248807963'], 'r') as f:
    cpc_defs = json.load(f)
    for entry in cpc_defs:
        cpc_titles[entry['symbol']] = entry['titleFull']

# Load All Patents
with open(locals()['var_function-call-12777540766248806770'], 'r') as f:
    all_patents = json.load(f)

# Regex for Pub Number
# Examples: "publication number US-11081687-B2", "pub. number US-2022074631-A1", "publication no. US-..."
pub_num_re = re.compile(r"(?:publication|pub\.?)\s+(?:number|no\.)\s+([A-Za-z0-9-]+)", re.IGNORECASE)

# Regex for Assignee
# Examples: "PANASONIC ... holds the", "... is owned by UNIV ...", "... assigned to ...", "belonging to ..."
assignee_re_start = re.compile(r"^(.+?)\s+holds\s+the", re.IGNORECASE)
assignee_re_middle = re.compile(r"(?:owned by|assigned to|belonging to|held by)\s+(.+?)(?:\s+and|\s*,)", re.IGNORECASE)

def extract_assignee(text):
    m = assignee_re_start.match(text)
    if m:
        return m.group(1).strip()
    m = assignee_re_middle.search(text)
    if m:
        return m.group(1).strip()
    return None

def extract_pub_num(text):
    m = pub_num_re.search(text)
    if m:
        return m.group(1).strip()
    return None

# Step 1: Identify UC Patents
uc_pub_nums = set()
uc_patents_info_list = []

for p in all_patents:
    p_info = p.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in p_info: # Check for UC ownership
        # Need to verify if it is indeed the assignee.
        # "UNIV CALIFORNIA holds..." or "assigned to UNIV CALIFORNIA"
        extracted_assignee = extract_assignee(p_info)
        if extracted_assignee and 'UNIV CALIFORNIA' in extracted_assignee:
            pub_num = extract_pub_num(p_info)
            if pub_num:
                uc_pub_nums.add(pub_num)
                uc_patents_info_list.append(p_info)

# Step 2: Find Citing Patents
citing_results = []
seen_citations = set()

for p in all_patents:
    # Check citations
    citations = p.get('citation', '[]')
    if not citations: continue
    try:
        citations_list = json.loads(citations)
    except:
        continue
    
    cites_uc = False
    for cit in citations_list:
        if cit.get('publication_number') in uc_pub_nums:
            cites_uc = True
            break
            
    if cites_uc:
        p_info = p.get('Patents_info', '')
        assignee = extract_assignee(p_info)
        
        # Exclude self-citations
        if assignee and 'UNIV CALIFORNIA' not in assignee:
            # Get Primary CPC Subclass
            cpc_json = p.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_json)
            except:
                cpc_list = []
            
            primary_subclass = None
            if cpc_list:
                # Find first=true
                primary_code = None
                for c in cpc_list:
                    if c.get('first') is True:
                        primary_code = c.get('code')
                        break
                if not primary_code and len(cpc_list) > 0:
                    primary_code = cpc_list[0].get('code')
                
                if primary_code:
                    # Extract subclass (first 4 chars)
                    # e.g. H01M10/0565 -> H01M
                    primary_subclass = primary_code[:4]
            
            if primary_subclass:
                title = cpc_titles.get(primary_subclass, "Title Not Found")
                # Store unique assignee-title pair
                pair = (assignee, title)
                if pair not in seen_citations:
                    citing_results.append(pair)
                    seen_citations.add(pair)

# Step 3: Format output
# The user wants "name of each citing assignee together with the full title of the CPC subclass"
# I will return a list of dictionaries or a formatted string.
# Let's return a list of JSON objects.

output = [{"Assignee": a, "CPC_Subclass_Title": t} for a, t in citing_results]

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-6595341616232824735': ['publicationinfo'], 'var_function-call-6595341616232823242': ['cpc_definition'], 'var_function-call-10533967409685439844': 'file_storage/function-call-10533967409685439844.json', 'var_function-call-10533967409685438467': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}], 'var_function-call-5807521106307905467': [{'count(*)': '277813'}], 'var_function-call-18370542604915769929': 'file_storage/function-call-18370542604915769929.json', 'var_function-call-13488432459981353820': [{'count': '260808'}], 'var_function-call-7584670842812926601': [{'symbol': 'C01B', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}], 'var_function-call-12777540766248806770': 'file_storage/function-call-12777540766248806770.json', 'var_function-call-12777540766248807963': 'file_storage/function-call-12777540766248807963.json'}

exec(code, env_args)
