code = """import json
import re

# Load UC patents
with open(locals()['var_function-call-3627068258271379600'], 'r') as f:
    uc_records = json.load(f)

uc_pub_numbers = set()
pub_num_pattern = re.compile(r'(?:pub\.?|publication)\s+(?:number|no\.?)\s+([A-Z]{2}-?[0-9]+-?[A-Z0-9]*)', re.IGNORECASE)

for rec in uc_records:
    info = rec['Patents_info']
    match = pub_num_pattern.search(info)
    if match:
        uc_pub_numbers.add(match.group(1))

assignee_patterns = [
    re.compile(r'^(.+?)\s+holds\s+the', re.IGNORECASE),
    re.compile(r'is\s+(?:owned\s+by|assigned\s+to|belonging\s+to|held\s+by)\s+(.+?)(?:\s+and|\s*,)', re.IGNORECASE),
    re.compile(r'held\s+by\s+(.+?),\s+with', re.IGNORECASE)
]

def get_assignee(text):
    for p in assignee_patterns:
        m = p.search(text)
        if m:
            return m.group(1).strip()
    return None

results = []

# Load Chunk 2
with open(locals()['var_function-call-6961723374787660946'], 'r') as f:
    chunk = json.load(f)

for rec in chunk:
    citations = rec.get('citation')
    if not citations or citations == '[]':
        continue
    
    try:
        citations_list = json.loads(citations)
    except:
        continue
        
    found = False
    for cit in citations_list:
        if cit.get('publication_number') in uc_pub_numbers:
            found = True
            break
    
    if found:
        assignee = get_assignee(rec['Patents_info'])
        if assignee and 'UNIV CALIFORNIA' not in assignee and 'UNIVERSITY OF CALIFORNIA' not in assignee:
            cpc_json = rec.get('cpc')
            subclass = None
            if cpc_json:
                try:
                    cpc_list = json.loads(cpc_json)
                    for c in cpc_list:
                        if c.get('first'):
                            code = c.get('code', '')
                            if len(code) >= 4:
                                subclass = code[:4]
                            break
                    if not subclass and cpc_list:
                        code = cpc_list[0].get('code', '')
                        if len(code) >= 4:
                            subclass = code[:4]
                except:
                    pass
            
            if subclass:
                results.append({"assignee": assignee, "subclass": subclass})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12868220818788144791': 'file_storage/function-call-12868220818788144791.json', 'var_function-call-2492118762681271268': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_function-call-18177144468656687824': [{'COUNT(*)': '277813'}], 'var_function-call-6015838364880532085': [{'COUNT(*)': '0'}], 'var_function-call-3627068258271379600': 'file_storage/function-call-3627068258271379600.json', 'var_function-call-12921287316337246279': {'count': 167, 'sample': ['US-10900049-B2', 'AU-7724398-A', 'KR-20200084864-A', 'CN-101584047-A', 'US-2021282642-A1']}, 'var_function-call-1286936377843854032': 'file_storage/function-call-1286936377843854032.json', 'var_function-call-799417787624374824': [{'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0565', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0562', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0566', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/052', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}, {'code': 'Y02E60/10', 'first': False, 'inventive': False, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/028', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/1315', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/021', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B33/00', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M4/1315', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/582', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/1315', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M10/0562', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/028', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0565', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/021', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0566', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/052', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}], 'var_function-call-1360944170723234994': [], 'var_function-call-6961723374787660946': 'file_storage/function-call-6961723374787660946.json'}

exec(code, env_args)
