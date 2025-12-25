code = """import json
import re

with open(locals()['var_function-call-4091625522379035702']) as f:
    info_rows = json.load(f)

res = {}
res['rows_count'] = len(info_rows)
if len(info_rows) > 0:
    text = info_rows[0]['Project_Information']
    res['example_text'] = text
    
    simple_pat = r'[a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+'
    res['simple_matches'] = re.findall(simple_pat, text)

    complex_pat = r'\b(?=[a-zA-Z0-9\-\.]*[a-zA-Z])[a-zA-Z0-9\-\.]+\/(?=[a-zA-Z0-9\-\.]*[a-zA-Z])[a-zA-Z0-9\-\.]+\b'
    res['complex_matches'] = re.findall(complex_pat, text)

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-6485848890492900329': ['packageinfo'], 'var_function-call-6485848890492900454': ['project_info', 'project_packageversion'], 'var_function-call-474351073472527354': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-17329601053264025037': [{'count_star()': '770'}], 'var_function-call-15234202801282220009': [{'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Licenses': '[\n  "EUPL-1.2"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Licenses': '[]'}, {'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Licenses': '[\n  "ISC"\n]'}, {'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Licenses': '[\n  "MIT"\n]'}], 'var_function-call-3894250662162695542': [{'COUNT(*)': '661372'}], 'var_function-call-543603203718078934': [{'COUNT(*)': '176170'}], 'var_function-call-13912716373860961398': [{'count_star()': '597602'}], 'var_function-call-4091625522379036388': 'file_storage/function-call-4091625522379036388.json', 'var_function-call-4091625522379036045': 'file_storage/function-call-4091625522379036045.json', 'var_function-call-4091625522379035702': 'file_storage/function-call-4091625522379035702.json', 'var_function-call-12052291588044334746': [], 'var_function-call-809749469135880200': 'done', 'var_function-call-4428019070161265216': {'valid_pkgs_count': 84744, 'relevant_projects_count': 5430, 'sample_relevant': ['goosedefi/goose-uikit', 'rackt/async-props', 'floatdrop/pinkie', 'dotnetautor/easm', 'dominictarr/crypto-browserify'], 'project_stats_count': 0, 'sample_stats_keys': [], 'sample_parse': [], 'overlap_count': 0}, 'var_function-call-2928250688251336945': 'debug done'}

exec(code, env_args)
