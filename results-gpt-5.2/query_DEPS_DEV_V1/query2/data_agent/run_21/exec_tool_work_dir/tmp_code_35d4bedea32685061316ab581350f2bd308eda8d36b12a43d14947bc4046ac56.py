code = """import json, re, pandas as pd

pkg_src = var_call_0pcdKayhxvcrynnDCx115Yfq
if isinstance(pkg_src, str):
    with open(pkg_src, 'r') as f:
        pkg_rows = json.load(f)
else:
    pkg_rows = pkg_src

ppv_src = var_call_TpAs4zLCeG1KAWDDMKpk2cGP
if isinstance(ppv_src, str):
    with open(ppv_src, 'r') as f:
        ppv_rows = json.load(f)
else:
    ppv_rows = ppv_src

pi_src = var_call_CuGasJqqcFtP6qp4SVCjeQvv
if isinstance(pi_src, str):
    with open(pi_src, 'r') as f:
        pi_rows = json.load(f)
else:
    pi_rows = pi_src

pkg_df = pd.DataFrame(pkg_rows)[['System','Name','Version']]
ppv_df = pd.DataFrame(ppv_rows)[['System','Name','Version','ProjectName']]

mapped = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = set(mapped['ProjectName'].dropna().astype(str))

# parse repo and fork count
repo_re = re.compile(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', re.IGNORECASE)
fork_patterns = [
    re.compile(r'\b([0-9][0-9,]*)\s+forks\b', re.IGNORECASE),
    re.compile(r'forks\s+count\s+of\s+([0-9][0-9,]*)', re.IGNORECASE),
    re.compile(r'forked\s+([0-9][0-9,]*)\s+times', re.IGNORECASE),
]

rows = []
for rec in pi_rows:
    text = rec.get('Project_Information') or ''
    mrepo = repo_re.search(text)
    if not mrepo:
        continue
    repo = mrepo.group(1)
    if repo not in projects:
        continue
    forks = None
    for fr in fork_patterns:
        mf = fr.search(text)
        if mf:
            forks = int(mf.group(1).replace(',',''))
            break
    if forks is None:
        continue
    rows.append((repo, forks))

fork_df = pd.DataFrame(rows, columns=['ProjectName','Forks']).groupby('ProjectName', as_index=False)['Forks'].max()

top5 = fork_df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_0pcdKayhxvcrynnDCx115Yfq': 'file_storage/call_0pcdKayhxvcrynnDCx115Yfq.json', 'var_call_TpAs4zLCeG1KAWDDMKpk2cGP': 'file_storage/call_TpAs4zLCeG1KAWDDMKpk2cGP.json', 'var_call_ZkQJIhcOCJJwrTmrGxxid0I6': {'n_pkg_versions': 176998, 'n_mapped_versions': 378738, 'n_projects': 5336, 'sample_query': "SELECT Project_Information FROM project_info WHERE Project_Information LIKE '%/crislin2046%' OR Project_Information LIKE '%/robpethick%' OR Project_Information LIKE '%0x1ance/soulbound%' OR Project_Information LIKE '%0x1ance/wishport%' OR Project_Information LIKE '%0xsalah/tete%' OR Project_Information LIKE '%1394/manipula%' OR Project_Information LIKE '%1728954833/project-manager%' OR Project_Information LIKE '%20lives/scad-js%' OR Project_Information LIKE '%286810/react-native-switch-box%' OR "}, 'var_call_CuGasJqqcFtP6qp4SVCjeQvv': 'file_storage/call_CuGasJqqcFtP6qp4SVCjeQvv.json', 'var_call_vBcBE6UazZCxQBNUvdJtBwD7': [], 'var_call_Vg4bQGAm0lKhd09q2gQXMD4Z': ['The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'], 'var_call_wMFRuAGPgE8z6MVBrtQ6vuvm': [], 'var_call_cAMwDE9DVRQRS7j6CwG5FNTK': {'pi_rows': 770, 'projects': 8059, 'pi_with_repo_in_projects': 0, 'pi_with_forks': 0, 'examples': []}, 'var_call_rRDMpNAZeVhyQzUiy3uTzbQN': {'n_pi_repos': 571, 'n_intersection': 570, 'sample_intersection': ['thinkjs/think-sequelize', 'reactive-extensions/rxjs', 'leviticusmb/sysconsole', 'sindresorhus/decamelize', 'lekoarts/gatsby-themes', 'sindresorhus/slash', 'surnet/graphql-amqp-subscriptions', 'sentrei/dogan', 'stardustapp/javascript-client', 'mikolalysenko/uniq', 'ljharb/define-properties', 'thlorenz/convert-source-map', 'matthiaaas/express-file-routing', 'thebigbrain/dora.js', 'redux-observable/redux-observable', 'legendjaden/aftablecolumn', 'mathiasbynens/unicode-match-property-value-ecmascript', 'the-economist-editorial/component-ad-panel', 'marijnh/moduleserve', 'react-component/dropdown'], 'sample_pi_repos': ['thinkjs/think-sequelize', 'reactive-extensions/rxjs', 'leviticusmb/sysconsole', 'sindresorhus/decamelize', 'lekoarts/gatsby-themes', 'sindresorhus/slash', 'surnet/graphql-amqp-subscriptions', 'sentrei/dogan', 'stardustapp/javascript-client', 'mikolalysenko/uniq']}}

exec(code, env_args)
