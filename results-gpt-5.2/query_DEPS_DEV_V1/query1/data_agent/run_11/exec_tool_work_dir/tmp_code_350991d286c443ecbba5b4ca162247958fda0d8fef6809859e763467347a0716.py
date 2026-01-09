code = """import json, re, pandas as pd

pi_src = var_call_RIYcCOdoLLu1gxZThVtbsKau
if isinstance(pi_src, str):
    with open(pi_src, 'r', encoding='utf-8') as f:
        pi = json.load(f)
else:
    pi = pi_src
ppv_src = var_call_UJZ6a9Mgixf7T2LuzAWCqzsJ
if isinstance(ppv_src, str):
    with open(ppv_src, 'r', encoding='utf-8') as f:
        ppv = json.load(f)
else:
    ppv = ppv_src

pi_df = pd.DataFrame(pi)
ppv_df = pd.DataFrame(ppv)

pi_df['UpstreamPublishedAt'] = pd.to_numeric(pi_df['UpstreamPublishedAt'], errors='coerce')
pi_latest = pi_df.sort_values(['Name','UpstreamPublishedAt','Version']).groupby('Name', as_index=False).tail(1)
pi_latest = pi_latest[['System','Name','Version','UpstreamPublishedAt']]

m = pi_latest.merge(ppv_df, on=['System','Name','Version'], how='inner')
m = m.dropna(subset=['ProjectName'])

project_list = sorted(m['ProjectName'].unique().tolist())

# create LIKE patterns to query stars; we'll query in chunks with OR
chunks = [project_list[i:i+200] for i in range(0, len(project_list), 200)]
patterns = []
for ch in chunks[:3]:
    ors = ' OR '.join(["Project_Information LIKE '%{}%'".format(p.replace("'","''")) for p in ch])
    patterns.append(ors)

out = {'project_count': len(project_list), 'first_chunk_where': patterns[0][:1000]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_RIYcCOdoLLu1gxZThVtbsKau': 'file_storage/call_RIYcCOdoLLu1gxZThVtbsKau.json', 'var_call_UJZ6a9Mgixf7T2LuzAWCqzsJ': 'file_storage/call_UJZ6a9Mgixf7T2LuzAWCqzsJ.json', 'var_call_tZL7QyhauLyG7dim23pOYDgf': {'latest_mapped_count': 20899, 'distinct_projects': 6807, 'project_names_sample': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0x6c38/srp', '0x6c38/srt', '0xsalah/tete', '1394/manipula', '1394/model', '1728954833/project-manager', '1hive/dao-list', '1hive/gardens', '1xinternet/drupal-editable', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4x-sas/create-react-app', '634750802/react-typewriter-effect', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', '947418354/boot-style', '9z/npm-package-practice', 'a-ebra/lotide', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client', 'aaronm-2112/tickets-common', 'aaronsisler/packages.generate-react-templates', 'aaronsisler/packages.git-my-files', 'abacritt/angularx-social-login', 'abuinitski/redux-bundler-async-resources', 'actorapp/react-scroll', 'admin-dikesoft/angular-dk-grid-community', 'admin-dikesoft/angular-dk-grid-standard', 'aduth/preact-jsx-runtime', 'adyatlov/behold', 'aeb-labs/graphql-weaver', 'aelbore/esbuild-jest', 'age-bijkaart/cbuf', 'agtenr/typescript-storagefactory', 'agustinramos/react-orgchart', 'aheckmann/mquery', 'aheissenberger/serverless-appsync-offline', 'ahmadreza-s/dotlottie-player', 'ahmadreza-s/xmlparser', 'ahomu/grunt-data-uri', 'ahram-dolphin/cli']}, 'var_call_b97lqWX0sMIXwWWkhqnU7d7X': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_call_NChp669Vjhjkf43UW0diOhGk': [{'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}]}

exec(code, env_args)
