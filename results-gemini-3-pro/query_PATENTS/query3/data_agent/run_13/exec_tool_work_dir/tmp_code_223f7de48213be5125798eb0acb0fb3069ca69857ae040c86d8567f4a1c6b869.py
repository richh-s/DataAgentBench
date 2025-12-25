code = """import json
import re

# Load UC Patents Info
uc_file_path = locals()['var_function-call-163982095095483053']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

# Extract UC Publication Numbers
uc_pubs = set()
# pattern: (?:publication|pub\.)\s+(?:number|no\.)\s+([A-Z]{2}-[\w\d-]+)
pat_pattern = re.compile('(?:publication|pub\\.)\\s+(?:number|no\\.)\\s+([A-Z]{2}-[\\w\\d-]+)')

for row in uc_data:
    info = row['Patents_info']
    match = pat_pattern.search(info)
    if match:
        uc_pubs.add(match.group(1))

# Load All Patents
all_file_path = locals()['var_function-call-12118947113934152352']
with open(all_file_path, 'r') as f:
    all_data = json.load(f)

citing_assignees = {} 

# Regexes for assignee
re_holds = re.compile('^(.*?) holds the ')
re_owned = re.compile('is owned by (.*?) (?:and|with|has)')
re_assigned = re.compile('is assigned to (.*?) (?:and|with|has)')
re_belonging = re.compile('is belonging to (.*?) (?:and|with|has)')
re_held = re.compile('held by (.*?) (?:and|with|,)')
re_belonging_start = re.compile('belonging to (.*?) (?:and|with|,)')

def get_assignee(text):
    text = text.replace('\n', ' ')
    m = re_holds.search(text)
    if m: return m.group(1).strip()
    m = re_owned.search(text)
    if m: return m.group(1).strip()
    m = re_assigned.search(text)
    if m: return m.group(1).strip()
    m = re_belonging.search(text)
    if m: return m.group(1).strip()
    m = re_held.search(text)
    if m: return m.group(1).strip()
    m = re_belonging_start.search(text)
    if m: return m.group(1).strip()
    return None

def get_subclasses(cpc_json_str):
    try:
        cpc_list = json.loads(cpc_json_str)
        if not cpc_list:
            return []
        codes = set()
        primaries = [x for x in cpc_list if x.get('first') == True]
        if not primaries:
            primaries = [cpc_list[0]]
            
        for p in primaries:
            if 'code' in p:
                codes.add(p['code'][:4])
        return list(codes)
    except:
        return []

for row in all_data:
    try:
        cits_str = row['citation']
        cits = json.loads(cits_str)
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
            assignee = assignee.strip()
            if 'UNIV CALIFORNIA' in assignee:
                continue
            
            subclasses = get_subclasses(row['cpc'])
            if subclasses:
                if assignee not in citing_assignees:
                    citing_assignees[assignee] = set()
                for s in subclasses:
                    citing_assignees[assignee].add(s)

final_result = []
all_subclasses_set = set()
for k, v in citing_assignees.items():
    final_result.append({'assignee': k, 'subclasses': list(v)})
    all_subclasses_set.update(v)

print('__RESULT__:')
print(json.dumps({'assignees': final_result, 'all_subclasses': list(all_subclasses_set)}))"""

env_args = {'var_function-call-3523691000772885977': 'file_storage/function-call-3523691000772885977.json', 'var_function-call-163982095095483053': 'file_storage/function-call-163982095095483053.json', 'var_function-call-7359064648347536263': ['AU-2898989-A', 'US-2023279470-A1', 'CN-101584047-A', 'US-2020025859-A1', 'US-7745569-B2', 'CN-102584712-A', 'KR-20200041324-A', 'US-2018304537-A1', 'KR-20180041236-A', 'US-2021282642-A1'], 'var_function-call-8038203737880887453': [{'cnt': '277813'}], 'var_function-call-12118947113934152352': 'file_storage/function-call-12118947113934152352.json', 'var_function-call-18096850190734713902': [{'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0565', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0562', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0566', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/052', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}, {'code': 'Y02E60/10', 'first': False, 'inventive': False, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/028', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/1315', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/021', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B33/00', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M4/1315', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/582', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B35/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M4/525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01P2002/76', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/1315', 'first': True, 'inventive': True, 'tree': []}, {'code': 'H01M10/0562', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/028', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M4/505', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0565', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M2004/021', 'first': False, 'inventive': False, 'tree': []}, {'code': 'H01M10/0525', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/0566', 'first': False, 'inventive': True, 'tree': []}, {'code': 'H01M10/052', 'first': False, 'inventive': True, 'tree': []}, {'code': 'C01G45/006', 'first': False, 'inventive': True, 'tree': []}]}

exec(code, env_args)
