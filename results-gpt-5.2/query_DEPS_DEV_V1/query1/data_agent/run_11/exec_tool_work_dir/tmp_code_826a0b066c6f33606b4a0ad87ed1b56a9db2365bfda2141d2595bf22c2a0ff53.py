code = """import json, re, pandas as pd

# load mappings
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

# load project_info texts
pii_src = var_call_SK7MNv9s0POjtEmxy7vGqf3a
if isinstance(pii_src, str):
    with open(pii_src, 'r', encoding='utf-8') as f:
        pii = json.load(f)
else:
    pii = pii_src
pii_df = pd.DataFrame(pii)

# extract repo and stars
repo_re = re.compile(r"project(?: named)? ([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
stars_re = re.compile(r"([0-9][0-9,]*) stars")

def parse(text):
    repo = None
    m1 = repo_re.search(text)
    if m1:
        repo = m1.group(1)
    else:
        # alt pattern 'project is hosted on GitHub under the name owner/repo'
        m2 = re.search(r"name ([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", text)
        if m2:
            repo = m2.group(1)
    stars = None
    m3 = stars_re.search(text)
    if m3:
        stars = int(m3.group(1).replace(',',''))
    return repo, stars

parsed = pii_df['Project_Information'].dropna().apply(parse)
pii_df['Repo'] = [r for r,s in parsed]
pii_df['Stars'] = [s for r,s in parsed]
pii_df = pii_df.dropna(subset=['Repo','Stars'])
pii_df = pii_df[['Repo','Stars']].drop_duplicates('Repo')

# join mapping to stars
m2 = m.merge(pii_df, left_on='ProjectName', right_on='Repo', how='inner')
# if multiple repos for same package (shouldn't for latest version), take max stars
pkg = m2.groupby(['Name','Version'], as_index=False).agg({'Stars':'max','ProjectName':'first'})

# top 5
pkg_top = pkg.sort_values('Stars', ascending=False).head(5)

result = pkg_top[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_RIYcCOdoLLu1gxZThVtbsKau': 'file_storage/call_RIYcCOdoLLu1gxZThVtbsKau.json', 'var_call_UJZ6a9Mgixf7T2LuzAWCqzsJ': 'file_storage/call_UJZ6a9Mgixf7T2LuzAWCqzsJ.json', 'var_call_tZL7QyhauLyG7dim23pOYDgf': {'latest_mapped_count': 20899, 'distinct_projects': 6807, 'project_names_sample': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0x6c38/srp', '0x6c38/srt', '0xsalah/tete', '1394/manipula', '1394/model', '1728954833/project-manager', '1hive/dao-list', '1hive/gardens', '1xinternet/drupal-editable', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4x-sas/create-react-app', '634750802/react-typewriter-effect', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', '947418354/boot-style', '9z/npm-package-practice', 'a-ebra/lotide', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client', 'aaronm-2112/tickets-common', 'aaronsisler/packages.generate-react-templates', 'aaronsisler/packages.git-my-files', 'abacritt/angularx-social-login', 'abuinitski/redux-bundler-async-resources', 'actorapp/react-scroll', 'admin-dikesoft/angular-dk-grid-community', 'admin-dikesoft/angular-dk-grid-standard', 'aduth/preact-jsx-runtime', 'adyatlov/behold', 'aeb-labs/graphql-weaver', 'aelbore/esbuild-jest', 'age-bijkaart/cbuf', 'agtenr/typescript-storagefactory', 'agustinramos/react-orgchart', 'aheckmann/mquery', 'aheissenberger/serverless-appsync-offline', 'ahmadreza-s/dotlottie-player', 'ahmadreza-s/xmlparser', 'ahomu/grunt-data-uri', 'ahram-dolphin/cli']}, 'var_call_b97lqWX0sMIXwWWkhqnU7d7X': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_call_NChp669Vjhjkf43UW0diOhGk': [{'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}], 'var_call_B5OrGeL0OI8TBuxZlTzyrOyQ': {'project_count': 6807, 'first_chunk_where': "Project_Information LIKE '%/crislin2046%' OR Project_Information LIKE '%/robpethick%' OR Project_Information LIKE '%0x1ance/soulbound%' OR Project_Information LIKE '%0x1ance/wishport%' OR Project_Information LIKE '%0x6c38/srp%' OR Project_Information LIKE '%0x6c38/srt%' OR Project_Information LIKE '%0xsalah/tete%' OR Project_Information LIKE '%1394/manipula%' OR Project_Information LIKE '%1394/model%' OR Project_Information LIKE '%1728954833/project-manager%' OR Project_Information LIKE '%1hive/dao-list%' OR Project_Information LIKE '%1hive/gardens%' OR Project_Information LIKE '%1xinternet/drupal-editable%' OR Project_Information LIKE '%20lives/scad-js%' OR Project_Information LIKE '%286810/react-native-switch-box%' OR Project_Information LIKE '%431910864/dumi-antd-components%' OR Project_Information LIKE '%4x-sas/create-react-app%' OR Project_Information LIKE '%634750802/react-typewriter-effect%' OR Project_Information LIKE '%6km/minify-css%' OR Project_Information LIKE '%776a0a/dus%"}, 'var_call_SK7MNv9s0POjtEmxy7vGqf3a': 'file_storage/call_SK7MNv9s0POjtEmxy7vGqf3a.json'}

exec(code, env_args)
