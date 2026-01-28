code = """import json, re

path = var_call_9RVtcJOgzfif5Kwn7XVkpCk3
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def parse_assignee(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r"owned by ([^\.]+?) and has", patents_info, flags=re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"assigned to ([^\.]+?) and has", patents_info, flags=re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"holds the [A-Z]{2} patent filing.*?owned by ([^\.]+)", patents_info, flags=re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"^([^,\.]+) holds", patents_info, flags=re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"assignee(?:_harmonized)?\s*[:=]\s*([^\.]+)", patents_info, flags=re.I)
    if m:
        return m.group(1).strip()
    return None

assignees=set()
for r in recs:
    a=parse_assignee(r.get('Patents_info',''))
    if a:
        assignees.add(a)

print('__RESULT__:')
print(json.dumps(sorted(assignees)))"""

env_args = {'var_call_lcjFhTyKzuPLwaCmwJdrVTp8': ['publicationinfo'], 'var_call_PFaRcpbJzb9CLkv748uaflfN': ['cpc_definition'], 'var_call_9RVtcJOgzfif5Kwn7XVkpCk3': 'file_storage/call_9RVtcJOgzfif5Kwn7XVkpCk3.json', 'var_call_LA4NsfAziLYM7YgDV3NQnJWs': [{'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'A61K'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'A61L'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'A61P'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'C07D'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'C07K'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'C08J'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'C08L'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'C12Q'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'F25B'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cpc_subclass': 'G01V'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication no', 'cpc_subclass': 'C08B'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication no', 'cpc_subclass': 'C08L'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication no', 'cpc_subclass': 'C12N'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication no', 'cpc_subclass': 'G01N'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication no', 'cpc_subclass': 'H01L'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication no', 'cpc_subclass': 'H03H'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication no', 'cpc_subclass': 'H04J'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication no', 'cpc_subclass': 'H04L'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number EP-2210307-A4', 'cpc_subclass': 'H01M'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number JP-2009260386-A', 'cpc_subclass': 'C30B'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number JP-2009260386-A', 'cpc_subclass': 'H01L'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11072681-B2', 'cpc_subclass': 'C07H'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11072681-B2', 'cpc_subclass': 'C08G'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'cpc_subclass': 'C12Q'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-2004115131-A1', 'cpc_subclass': 'G01N'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-2021039104-A1', 'cpc_subclass': 'B01L'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number WO-2014152660-A1', 'cpc_subclass': 'G01N'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number WO-2019067860-A1', 'cpc_subclass': 'A61K'}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number WO-2019067860-A1', 'cpc_subclass': 'A61P'}, {'citing_assignee': 'UNIV CALIFORNIA, with pub', 'cpc_subclass': 'B25J'}, {'citing_assignee': 'UNIV CALIFORNIA, with pub', 'cpc_subclass': 'C07D'}, {'citing_assignee': 'UNIV CALIFORNIA, with pub', 'cpc_subclass': 'C07K'}, {'citing_assignee': 'UNIV CALIFORNIA, with pub', 'cpc_subclass': 'G01R'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication no', 'cpc_subclass': 'A61B'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication no', 'cpc_subclass': 'A61K'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication no', 'cpc_subclass': 'A61N'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication no', 'cpc_subclass': 'H04L'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication number CN-103687626-A', 'cpc_subclass': 'A61K'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication number CN-103687626-A', 'cpc_subclass': 'C12N'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication number US-11014955-B2', 'cpc_subclass': 'C07H'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication number WO-2018067976-A1', 'cpc_subclass': 'B01L'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication number WO-2018067976-A1', 'cpc_subclass': 'G01N'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication number WO-2019173834-A1', 'cpc_subclass': 'A61K'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication number WO-2019173834-A1', 'cpc_subclass': 'A61L'}, {'citing_assignee': 'UNIV CALIFORNIA, with publication number WO-2023239670-A1', 'cpc_subclass': 'A61N'}]}

exec(code, env_args)
