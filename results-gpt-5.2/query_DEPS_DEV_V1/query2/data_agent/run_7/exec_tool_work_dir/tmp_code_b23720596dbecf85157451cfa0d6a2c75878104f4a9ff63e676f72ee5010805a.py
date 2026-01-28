code = """import json, re, pandas as pd

pkg_src = var_call_f6UmnHm9tLgbcTWK5VBMfZzV
ppv_src = var_call_FZ9C0DUWeVO3ERu0JmBuDl5s
pi_src  = var_call_U2j8WjgCLNqYbofEeqERkDrU

def load_records(src):
    if isinstance(src, str):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    return src

pkg = load_records(pkg_src)
ppv = load_records(ppv_src)
pi  = load_records(pi_src)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = set(m['ProjectName'].dropna().drop_duplicates())

pi_df = pd.DataFrame(pi)
pi_df['ProjectName'] = pi_df['ProjectName'].astype(str).str.strip()
pi_df = pi_df[pi_df['ProjectName'].isin(projects)].copy()

# parse forks with two patterns
pat1 = re.compile(r'\b([0-9][0-9,]*)\s+forks\b', re.IGNORECASE)
pat2 = re.compile(r'forks\s+count\s+of\s+([0-9][0-9,]*)', re.IGNORECASE)

def parse_forks(txt):
    if not isinstance(txt, str):
        return None
    m1 = pat1.search(txt)
    if m1:
        return int(m1.group(1).replace(',',''))
    m2 = pat2.search(txt)
    if m2:
        return int(m2.group(1).replace(',',''))
    return None

pi_df['Forks'] = pi_df['Project_Information'].map(parse_forks)

valid = pi_df.dropna(subset=['Forks'])
if valid.empty:
    result = {'parsed': 0, 'total_matching': int(len(pi_df)), 'examples_missing': pi_df['Project_Information'].head(5).tolist()}
else:
    top = valid.groupby('ProjectName', as_index=False)['Forks'].max().sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    result = top.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_f6UmnHm9tLgbcTWK5VBMfZzV': 'file_storage/call_f6UmnHm9tLgbcTWK5VBMfZzV.json', 'var_call_FZ9C0DUWeVO3ERu0JmBuDl5s': 'file_storage/call_FZ9C0DUWeVO3ERu0JmBuDl5s.json', 'var_call_b4vxqe2IjkAeUso3a7dupFw3': 'file_storage/call_b4vxqe2IjkAeUso3a7dupFw3.json', 'var_call_yyGel3uqTKeIgIupFmQdPAWY': [], 'var_call_U2j8WjgCLNqYbofEeqERkDrU': 'file_storage/call_U2j8WjgCLNqYbofEeqERkDrU.json', 'var_call_EOxbVYJe2r0MltQSEsWxjULe': [], 'var_call_ZdeIHn5KFEWpS36xQK8gBG46': [{'cnt': '176170'}], 'var_call_2FyPi0eHYAMlJd2RQrGh56gu': [{'cnt': '591699'}], 'var_call_ihCSkQNdQ8t7LOHZxiEwrEzL': [{'cnt': '770'}], 'var_call_L9GChsLH5wGaZl4Wg2neeWtD': {'matched_pkg_versions': 84002, 'distinct_projects_from_join': 5289, 'project_info_rows_matching_projects': 445, 'sample_projects_from_join': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0xsalah/tete', '1394/manipula', '1728954833/project-manager', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4catalyzer/theme', '4x-sas/create-react-app', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client'], 'sample_project_info_projectnames': ['lberrocal/npm-packages-template', 'leaflet/leaflet.markercluster', 'leandrowd/react-responsive-carousel', 'ledgerproject/keypairoom', 'leecade/react-native-swiper', 'lekoarts/gatsby-themes', 'lenconda/dollie', 'leo-ran/easy-node-reflect', 'leoilab/react-native-analytics-segment-io', 'leviticusmb/sysconsole', 'libertydsnp/parquetjs', 'libertyequalitydata/dynamic-data', 'liivevideo/react-native-web-webrtc', 'lisiadito/checksslcertificate', 'litejs/natural-compare-lite', 'ljharb/define-properties', 'ljharb/has-symbols', 'ljharb/object.assign', 'ln-zap/node-lnd-grpc', 'locize/fluent_conv']}}

exec(code, env_args)
