code = """import json, re, pandas as pd

# load packageinfo MIT+release rows
pkg_path = var_call_5AaHCvj832RS9bSP5oXuFQcn
ppv_path = var_call_hPxn32hOJM2bzCnYUeQO9L1Z
pi_path = var_call_R5k3rCNJYAOPRqTsQePUQGj0

def load_json(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

pkg = load_json(pkg_path)
ppv = load_json(ppv_path)
pi = load_json(pi_path)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

# inner join on System, Name, Version
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# unique projects
projects = merged[['ProjectName']].dropna().drop_duplicates()

# parse forks from Project_Information and extract project name
fork_re = re.compile(r"\b([0-9][0-9,]*)\s+forks?\b", re.IGNORECASE)
name_re = re.compile(r"\bproject\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

def parse_pi(text):
    if not isinstance(text, str):
        return None, None
    mname = name_re.search(text)
    pname = mname.group(1) if mname else None
    mf = fork_re.search(text)
    forks = int(mf.group(1).replace(',','')) if mf else None
    return pname, forks

pi_rows = []
for r in pi:
    pname, forks = parse_pi(r.get('Project_Information'))
    if pname and forks is not None:
        pi_rows.append({'ProjectName': pname, 'Forks': forks})

pi_df = pd.DataFrame(pi_rows).drop_duplicates(subset=['ProjectName'], keep='last')

proj_with_forks = projects.merge(pi_df, on='ProjectName', how='inner')

top5 = proj_with_forks.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_48blh3OiKH1U7DVSUbTE6AwC': [{'table_name': 'project_info'}, {'table_name': 'project_packageversion'}], 'var_call_OE0Gb7o4FqEoNYGHnOBcZxSm': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_call_LBYO4sqHTLDxkeX6iHIylX63': [{'cid': '0', 'name': 'System', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Name', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Version', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Licenses', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Links', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Advisories', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'VersionInfo', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Hashes', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'DependenciesProcessed', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'DependencyError', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'UpstreamPublishedAt', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'Registries', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'SLSAProvenance', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'UpstreamIdentifiers', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'Purl', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_call_5AaHCvj832RS9bSP5oXuFQcn': 'file_storage/call_5AaHCvj832RS9bSP5oXuFQcn.json', 'var_call_hPxn32hOJM2bzCnYUeQO9L1Z': 'file_storage/call_hPxn32hOJM2bzCnYUeQO9L1Z.json', 'var_call_R5k3rCNJYAOPRqTsQePUQGj0': 'file_storage/call_R5k3rCNJYAOPRqTsQePUQGj0.json'}

exec(code, env_args)
