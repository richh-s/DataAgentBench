code = """import json, re, pandas as pd

def load_json(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

pkg_df = pd.DataFrame(load_json(var_call_5AaHCvj832RS9bSP5oXuFQcn))
ppv_df = pd.DataFrame(load_json(var_call_hPxn32hOJM2bzCnYUeQO9L1Z))
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects_df = merged[['ProjectName']].dropna().drop_duplicates()

pi = load_json(var_call_R5k3rCNJYAOPRqTsQePUQGj0)

name_patterns = [
    re.compile(r"project\s+(?:is\s+hosted\s+on\s+GitHub\s+under\s+the\s+name|under\s+the\s+name)\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", re.I),
    re.compile(r"project\s+(?:on\s+GitHub,\s+named\s+|named\s+)\s*([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", re.I),
    re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", re.I)
]

fork_patterns = [
    re.compile(r"\b([0-9][0-9,]*)\s+forks?\b", re.I),
    re.compile(r"forks?\s+count\s+of\s+([0-9][0-9,]*)", re.I),
    re.compile(r"forked\s+([0-9][0-9,]*)\s+times", re.I)
]

def extract_pi(t):
    if not isinstance(t, str):
        return None, None
    pname = None
    for p in name_patterns:
        m = p.search(t)
        if m:
            pname = m.group(1)
            break
    if not pname:
        return None, None
    forks = None
    for p in fork_patterns:
        m = p.search(t)
        if m:
            forks = int(m.group(1).replace(',',''))
            break
    return pname, forks

pi_rows=[]
for r in pi:
    pname, forks = extract_pi(r.get('Project_Information'))
    if pname and forks is not None:
        pi_rows.append({'ProjectName': pname, 'Forks': forks})

pi_df = pd.DataFrame(pi_rows)
pi_df = pi_df.sort_values('Forks', ascending=False).drop_duplicates('ProjectName', keep='first')

proj_with_forks = projects_df.merge(pi_df, on='ProjectName', how='inner')

top5 = proj_with_forks.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_48blh3OiKH1U7DVSUbTE6AwC': [{'table_name': 'project_info'}, {'table_name': 'project_packageversion'}], 'var_call_OE0Gb7o4FqEoNYGHnOBcZxSm': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_call_LBYO4sqHTLDxkeX6iHIylX63': [{'cid': '0', 'name': 'System', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Name', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Version', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Licenses', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Links', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Advisories', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'VersionInfo', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Hashes', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'DependenciesProcessed', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'DependencyError', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'UpstreamPublishedAt', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'Registries', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'SLSAProvenance', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'UpstreamIdentifiers', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'Purl', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_call_5AaHCvj832RS9bSP5oXuFQcn': 'file_storage/call_5AaHCvj832RS9bSP5oXuFQcn.json', 'var_call_hPxn32hOJM2bzCnYUeQO9L1Z': 'file_storage/call_hPxn32hOJM2bzCnYUeQO9L1Z.json', 'var_call_R5k3rCNJYAOPRqTsQePUQGj0': 'file_storage/call_R5k3rCNJYAOPRqTsQePUQGj0.json', 'var_call_o6ANLC342qG5j66M4gtHKJeD': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_ftliDhqTVpSwqEgaxaqSXheT': {'merged_columns': ['System', 'Name', 'Version', 'Licenses', 'VersionInfo', 'ProjectType', 'ProjectName'], 'merged_shape': [378738, 7], 'projects_cols': ['System', 'Name', 'Version', 'Licenses', 'VersionInfo', 'ProjectType', 'ProjectName']}, 'var_call_1kQ0n88JDEyZAtYxFX10ZSjy': {'projects_df_cols': ['ProjectName'], 'projects_df_head': [{'ProjectName': 'discue/ui-components'}, {'ProjectName': 'dvcol/web-extension-utils'}, {'ProjectName': 'dlesage25/eclipse-cli'}], 'pi_df_cols': [], 'pi_df_head': []}, 'var_call_3o4zJPRAOQpAvbnSO2NSMqDr': {'sample_forks_count': ['The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.', 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.', 'The project on GitHub, named leonardparisi/easy-express-server, currently has an open issues count of 0, a stars count of 0, and a forks count of 0.'], 'first_matches': []}, 'var_call_wnKBADLgbvvdhQVLQ8t6uMkK': {'pi_rows_len': 0, 'pi_df_cols': [], 'pi_df_head': []}, 'var_call_g9mOx3zMg5EpuF1tAvaTt9lG': {'matches_found': 10, 'examples': [{'name': 'leaflet/leaflet.markercluster', 'forks': '988', 'text': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'name': 'learnfrontend-dc/product-cart', 'forks': '12', 'text': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'name': 'leebyron/testcheck-js', 'forks': '58,', 'text': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'name': 'legendjaden/aftablecolumn', 'forks': '29', 'text': 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.'}, {'name': 'leo-ran/easy-node-server', 'forks': '0', 'text': 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.'}, {'name': 'leviticusmb/sysconsole', 'forks': '0', 'text': 'The project leviticusmb/sysconsole is hosted on GITHUB and currently has an open issues count of 0, stars count of 0, and forks count of 0.'}, {'name': 'lfujiwara/dnausp-core', 'forks': '1', 'text': 'The project lfujiwara/dnausp-core is hosted on GITHUB and currently has an open issues count of 0, a stars count of 0, and a forks count of 1.'}, {'name': 'linkshare/service-container', 'forks': '9', 'text': 'The GitHub project named linkshare/service-container has an open issues count of 2, a stars count of 26, and a forks count of 9.'}, {'name': 'ljharb/object-keys', 'forks': '15', 'text': 'The GitHub project named ljharb/object-keys has an open issues count of 0, indicating that there are currently no outstanding problems to address. It has garnered a stars count of '}, {'name': 'ln-zap/node-lnd-grpc', 'forks': '16', 'text': 'The project ln-zap/node-lnd-grpc on GitHub currently has 16 open issues, has received 41 stars, and has been forked 16 times.'}]}}

exec(code, env_args)
