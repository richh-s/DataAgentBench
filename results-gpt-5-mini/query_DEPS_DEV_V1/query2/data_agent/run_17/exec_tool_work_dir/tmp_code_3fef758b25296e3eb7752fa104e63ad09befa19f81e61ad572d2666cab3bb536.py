code = """import json, re
pkg_path = var_call_oy7rkcqUhosdoleV1S5dixVk
ppv_path = var_call_I9REvBUjaV8FcUHZHINzvScE
proj_info_path = var_call_EkXd752NRanRt05GIewLqfZS
with open(pkg_path, 'r') as f:
    pkgs = json.load(f)
with open(ppv_path, 'r') as f:
    ppv = json.load(f)
with open(proj_info_path, 'r') as f:
    proj_info = json.load(f)
# Build set of (System,Name,Version) from pkgs
pkg_set = set((r.get('System'), r.get('Name'), r.get('Version')) for r in pkgs)
# Map ppv tuples to ProjectName for those in pkg_set
matched_projects = {}
for r in ppv:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    if key in pkg_set:
        proj = r.get('ProjectName')
        matched_projects.setdefault(proj, []).append({'System': r.get('System'), 'Name': r.get('Name'), 'Version': r.get('Version')})
# Parse proj_info to extract repo and forks robustly
repo_forks = {}
repo_pattern = re.compile(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)')
forks_pattern = re.compile(r'([0-9][0-9,]*)\s+forks', re.IGNORECASE)
for r in proj_info:
    text = r.get('Project_Information','')
    repos = repo_pattern.findall(text)
    forks_matches = forks_pattern.findall(text)
    if not repos or not forks_matches:
        continue
    # choose repo: prefer first repo-like token that contains at least one letter and not startswith 'The' etc.
    repo = None
    for rp in repos:
        if '/' in rp:
            repo = rp
            break
    if repo is None:
        continue
    forks_str = forks_matches[-1]
    try:
        forks = int(forks_str.replace(',',''))
    except Exception:
        continue
    repo_forks[repo] = forks
# Now for each matched project, get forks if available
results = []
for proj, pklist in matched_projects.items():
    if proj in repo_forks:
        results.append({'project': proj, 'forks': repo_forks[proj], 'matched_package_count': len(pklist)})
# Sort by forks desc and take top 5
results_sorted = sorted(results, key=lambda x: x['forks'], reverse=True)[:5]
print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_DVz30QS38OPrjRQdXuHLEkI5': ['packageinfo'], 'var_call_ADQ91SZxih62Z859qz1fgKUp': ['project_info', 'project_packageversion'], 'var_call_oy7rkcqUhosdoleV1S5dixVk': 'file_storage/call_oy7rkcqUhosdoleV1S5dixVk.json', 'var_call_S7VM1YWlDVqhFnG8TysEIgvV': {'num_rows': 176998, 'unique_names': 10486, 'unique_pairs': 85158}, 'var_call_I9REvBUjaV8FcUHZHINzvScE': 'file_storage/call_I9REvBUjaV8FcUHZHINzvScE.json', 'var_call_wVNb1WzE2pfGjziOg9zRdVXT': {'total_rows': 591699, 'unique_mappings': 321836}, 'var_call_EkXd752NRanRt05GIewLqfZS': 'file_storage/call_EkXd752NRanRt05GIewLqfZS.json', 'var_call_wGsnUMloMbxxyCPEYYVIV5IV': {'total_extracted': 276, 'top20': [{'repo': 'leaflet/leaflet', 'open_issues': 521, 'stars': 38715, 'forks': 5782, 'text': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'repo': 'react-native-elements/react-native-elements', 'open_issues': 116, 'stars': 24814, 'forks': 4623, 'text': 'The project react-native-elements/react-native-elements is a GitHub repository that currently has 116 open issues, 24,814 stars, and 4,623 forks, making it a popular choice for developers looking to enhance their React Native applications.'}, {'repo': 'microsoft/monaco-editor', 'open_issues': 385, 'stars': 36025, 'forks': 3407, 'text': 'The project microsoft/monaco-editor is hosted on GitHub and currently has 385 open issues, 36,025 stars, and 3,407 forks.'}, {'repo': 'quilljs/quill', 'open_issues': 321, 'stars': 42407, 'forks': 3318, 'text': 'The project quilljs/quill is hosted on GitHub and currently has 321 open issues, 42,407 stars, and 3,318 forks.'}, {'repo': 'react-native-community/react-native-webview', 'open_issues': 87, 'stars': 6345, 'forks': 2962, 'text': 'The project react-native-community/react-native-webview is hosted on GitHub and currently has 87 open issues, 6345 stars, and 2962 forks.'}, {'repo': 'rjsf-team/react-jsonschema-form', 'open_issues': 284, 'stars': 13923, 'forks': 2170, 'text': 'The project rjsf-team/react-jsonschema-form is hosted on GitHub and currently has 284 open issues, 13,923 stars, and 2,170 forks, making it a popular choice among developers for handling JSON schema forms.'}, {'repo': 'tmpvar/jsdom', 'open_issues': 479, 'stars': 19356, 'forks': 1668, 'text': 'The project tmpvar/jsdom is hosted on GitHub, where it currently has 479 open issues, 19,356 stars, and 1,668 forks, making it a popular choice among developers looking to work with a JavaScript environment that simulates a web browser.'}, {'repo': 'sass/node-sass', 'open_issues': 189, 'stars': 8498, 'forks': 1326, 'text': 'The project sass/node-sass on GitHub currently has 189 open issues, 8498 stars, and 1326 forks, making it a popular choice among developers for managing stylesheets with Sass.'}, {'repo': 'react-native-community/react-native-tab-view', 'open_issues': 47, 'stars': 5137, 'forks': 1073, 'text': 'The project react-native-community/react-native-tab-view on GitHub is a popular repository that currently has 47 open issues, 5,137 stars, and 1,073 forks.'}, {'repo': 'mbrn/material-table', 'open_issues': 23, 'stars': 3464, 'forks': 1035, 'text': 'The project mbrn/material-table is hosted on GitHub and currently has 23 open issues, 3464 stars, and 1035 forks, making it a popular choice among developers looking for a material design data table solution.'}, {'repo': 'mjmlio/mjml', 'open_issues': 75, 'stars': 15829, 'forks': 937, 'text': 'The project mjmlio/mjml on GitHub is a popular repository that currently has 75 open issues, 15,829 stars, and 937 forks.'}, {'repo': 'mapbox/node-sqlite3', 'open_issues': 139, 'stars': 5917, 'forks': 805, 'text': 'The project mapbox/node-sqlite3 on GitHub currently has 139 open issues, 5917 stars, and 805 forks, making it a popular choice for developers looking to integrate SQLite3 with Node.js.'}, {'repo': 'react-icons/react-icons', 'open_issues': 198, 'stars': 11295, 'forks': 730, 'text': 'The project react-icons/react-icons on GitHub is a popular repository that currently has 198 open issues, 11,295 stars, and 730 forks.'}, {'repo': 'supasate/connected-react-router', 'open_issues': 174, 'stars': 4737, 'forks': 605, 'text': 'The project supasate/connected-react-router is hosted on GitHub and currently has 174 open issues, 4737 stars, and 605 forks, making it a notable resource for developers interested in integrating React Router with Redux.'}, {'repo': 'securingsincity/react-ace', 'open_issues': 202, 'stars': 4005, 'forks': 603, 'text': 'The project securingsincity/react-ace on GitHub currently has 202 open issues, 4005 stars, and 603 forks, making it a notable repository in the community.'}, {'repo': 'lekoarts/gatsby-themes', 'open_issues': 11, 'stars': 1836, 'forks': 568, 'text': 'The project lekoarts/gatsby-themes on GitHub currently has 11 open issues, 1836 stars, and 568 forks, making it a popular choice among developers looking for Gatsby themes.'}, {'repo': 'naoufal/react-native-touch-id', 'open_issues': 118, 'stars': 1461, 'forks': 484, 'text': 'The project naoufal/react-native-touch-id on GitHub has 118 open issues, 1461 stars, and 484 forks, making it a noteworthy resource for developers interested in implementing touch ID functionality in React Native applications.'}, {'repo': 'mikemcl/big.js', 'open_issues': 8, 'stars': 4519, 'forks': 419, 'text': 'The GitHub project mikemcl/big.js is a popular library that currently has 8 open issues, 4519 stars, and 419 forks.'}, {'repo': 'salesforce/lwc', 'open_issues': 364, 'stars': 1595, 'forks': 386, 'text': 'The project salesforce/lwc on GitHub currently has 364 open issues, 1595 stars, and 386 forks, making it a popular resource for developers interested in Lightning Web Components.'}, {'repo': 'spite/three.meshline', 'open_issues': 77, 'stars': 2030, 'forks': 375, 'text': 'The project spite/three.meshline on GitHub has 77 open issues, 2030 stars, and 375 forks, making it a notable repository in the community.'}]}}

exec(code, env_args)
