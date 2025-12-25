code = """import json

# Load data
with open(locals()['var_function-call-4091625522379036388']) as f:
    package_rows = json.load(f) # packageinfo
with open(locals()['var_function-call-4091625522379036045']) as f:
    mapping_rows = json.load(f) # project_packageversion
with open(locals()['var_function-call-4091625522379035702']) as f:
    info_rows = json.load(f) # project_info

debug = {}

# 1. Valid pkgs
valid_pkg_keys = set()
for r in package_rows:
    valid_pkg_keys.add((r['Name'], r['Version']))

# 2. Relevant projects
relevant_projects = set()
for r in mapping_rows:
    if (r['Name'], r['Version']) in valid_pkg_keys:
        relevant_projects.add(r['ProjectName'])
        
debug['relevant_projects_sample'] = list(relevant_projects)[:10]

# 3. Parsed info
parsed_projects = []
for row in info_rows:
    text = row['Project_Information']
    # Just extracting names for debug
    import re
    m = re.search(r'\b([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+)\b', text)
    if m:
        parsed_projects.append(m.group(1))

debug['parsed_projects_sample'] = parsed_projects[:10]

# Check overlap
intersection = relevant_projects.intersection(set(parsed_projects))
debug['intersection_count'] = len(intersection)
debug['intersection_sample'] = list(intersection)[:10]

print('__RESULT__:')
print(json.dumps(debug))"""

env_args = {'var_function-call-6485848890492900329': ['packageinfo'], 'var_function-call-6485848890492900454': ['project_info', 'project_packageversion'], 'var_function-call-474351073472527354': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-17329601053264025037': [{'count_star()': '770'}], 'var_function-call-15234202801282220009': [{'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Licenses': '[\n  "EUPL-1.2"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Licenses': '[\n  "ISC"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Licenses': '[\n  "MIT"\n]'}], 'var_function-call-3894250662162695542': [{'COUNT(*)': '661372'}], 'var_function-call-543603203718078934': [{'COUNT(*)': '176170'}], 'var_function-call-13912716373860961398': [{'count_star()': '597602'}], 'var_function-call-4091625522379036388': 'file_storage/function-call-4091625522379036388.json', 'var_function-call-4091625522379036045': 'file_storage/function-call-4091625522379036045.json', 'var_function-call-4091625522379035702': 'file_storage/function-call-4091625522379035702.json', 'var_function-call-12052291588044334746': [], 'var_function-call-809749469135880200': 'done', 'var_function-call-4428019070161265216': {'valid_pkgs_count': 84744, 'relevant_projects_count': 5430, 'sample_relevant': ['goosedefi/goose-uikit', 'rackt/async-props', 'floatdrop/pinkie', 'dotnetautor/easm', 'dominictarr/crypto-browserify'], 'project_stats_count': 0, 'sample_stats_keys': [], 'sample_parse': [], 'overlap_count': 0}, 'var_function-call-2928250688251336945': 'debug done', 'var_function-call-11631268150816156068': {'rows_count': 770, 'example_text': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'simple_matches': ['lberrocal/npm-packages-template'], 'complex_matches': []}, 'var_function-call-18071086887894786939': []}

exec(code, env_args)
