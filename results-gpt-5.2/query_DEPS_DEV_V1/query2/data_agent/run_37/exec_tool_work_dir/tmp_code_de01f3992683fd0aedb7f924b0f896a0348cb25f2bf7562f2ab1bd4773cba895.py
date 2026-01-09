code = """import json, re

def load_json(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

pi = load_json(var_call_R5k3rCNJYAOPRqTsQePUQGj0)
texts = [r.get('Project_Information') for r in pi if isinstance(r.get('Project_Information'), str)]

# sample where 'forks count of' appears
sample = []
for t in texts:
    if 'forks count' in t and 'project ' in t:
        sample.append(t)
        if len(sample) >= 5:
            break

# try regex that handles 'forks count of 988' etc
name_re = re.compile(r"\bproject\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
fork1 = re.compile(r"\b([0-9][0-9,]*)\s+forks?\b", re.I)
fork2 = re.compile(r"forks?\s+count\s+of\s+([0-9][0-9,]*)", re.I)

matches = []
for t in texts[:2000]:
    mname = name_re.search(t)
    if not mname:
        continue
    mf = fork1.search(t) or fork2.search(t)
    if mf:
        matches.append({'text': t[:200], 'name': mname.group(1), 'forks': mf.group(1)})
        if len(matches) >= 5:
            break

print('__RESULT__:')
print(json.dumps({'sample_forks_count': sample, 'first_matches': matches}))"""

env_args = {'var_call_48blh3OiKH1U7DVSUbTE6AwC': [{'table_name': 'project_info'}, {'table_name': 'project_packageversion'}], 'var_call_OE0Gb7o4FqEoNYGHnOBcZxSm': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_call_LBYO4sqHTLDxkeX6iHIylX63': [{'cid': '0', 'name': 'System', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Name', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Version', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Licenses', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Links', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Advisories', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'VersionInfo', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Hashes', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'DependenciesProcessed', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'DependencyError', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'UpstreamPublishedAt', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'Registries', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'SLSAProvenance', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'UpstreamIdentifiers', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'Purl', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_call_5AaHCvj832RS9bSP5oXuFQcn': 'file_storage/call_5AaHCvj832RS9bSP5oXuFQcn.json', 'var_call_hPxn32hOJM2bzCnYUeQO9L1Z': 'file_storage/call_hPxn32hOJM2bzCnYUeQO9L1Z.json', 'var_call_R5k3rCNJYAOPRqTsQePUQGj0': 'file_storage/call_R5k3rCNJYAOPRqTsQePUQGj0.json', 'var_call_o6ANLC342qG5j66M4gtHKJeD': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_ftliDhqTVpSwqEgaxaqSXheT': {'merged_columns': ['System', 'Name', 'Version', 'Licenses', 'VersionInfo', 'ProjectType', 'ProjectName'], 'merged_shape': [378738, 7], 'projects_cols': ['System', 'Name', 'Version', 'Licenses', 'VersionInfo', 'ProjectType', 'ProjectName']}, 'var_call_1kQ0n88JDEyZAtYxFX10ZSjy': {'projects_df_cols': ['ProjectName'], 'projects_df_head': [{'ProjectName': 'discue/ui-components'}, {'ProjectName': 'dvcol/web-extension-utils'}, {'ProjectName': 'dlesage25/eclipse-cli'}], 'pi_df_cols': [], 'pi_df_head': []}}

exec(code, env_args)
