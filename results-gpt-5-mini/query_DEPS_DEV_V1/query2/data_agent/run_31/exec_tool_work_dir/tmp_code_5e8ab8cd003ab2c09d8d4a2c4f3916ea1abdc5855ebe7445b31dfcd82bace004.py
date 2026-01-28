code = """import json,os,re
# load storage variables
pfile = var_call_1uJQtFrSJUUR4MpPwh3LIibr
ppfile = var_call_MSSL9RI53qkcXKHpqb02tgtz
pinfo_file = var_call_RcNmnp6SA6aqtBY7VAvGVMbt

def load(v):
    if isinstance(v, str) and os.path.exists(v):
        return json.load(open(v,'r'))
    return v

pkgs = load(pfile)
projpkg = load(ppfile)
projinfo = load(pinfo_file)

# build set of keys for MIT released packages
pkg_keys = set((x['System'], x['Name'], x['Version']) for x in pkgs)
# map keys to project names
mapping = {}
for row in projpkg:
    key = (row.get('System'), row.get('Name'), row.get('Version'))
    if key in pkg_keys:
        mapping.setdefault(key, []).append(row.get('ProjectName'))
# unique project names associated
projects = set()
for v in mapping.values():
    for pn in v:
        if pn:
            projects.add(pn)

# parse project_info to get fork counts per project
proj_forks = {}
# regexes
repo_re_specific = re.compile(r'The project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
repo_re_any = re.compile(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
forks_re1 = re.compile(r'([0-9,]+)\s+forks')
forked_times_re = re.compile(r'forked\s+([0-9,]+)\s+times')
# iterate rows
for row in projinfo:
    pi = row.get('Project_Information') or ''
    repo = None
    m = repo_re_specific.search(pi)
    if m:
        repo = m.group(1)
    else:
        m2 = repo_re_any.search(pi)
        if m2:
            repo = m2.group(1)
    if not repo:
        continue
    # extract forks
    forks = None
    m3 = forks_re1.search(pi)
    if m3:
        forks = int(m3.group(1).replace(',',''))
    else:
        m4 = forked_times_re.search(pi)
        if m4:
            forks = int(m4.group(1).replace(',',''))
    if forks is None:
        # try look for 'and X forks' pattern
        m5 = re.search(r'and\s+([0-9,]+)\s+forks', pi)
        if m5:
            forks = int(m5.group(1).replace(',',''))
    if forks is None:
        # fallback 0
        forks = 0
    # store max if multiple entries
    if repo in proj_forks:
        proj_forks[repo] = max(proj_forks[repo], forks)
    else:
        proj_forks[repo] = forks

# Now for projects associated with MIT released pkgs, collect forks if available
results = []
for proj in projects:
    # project names in projpkg seem to be like 'owner/repo'
    # sometimes have leading slash; normalize by stripping leading '/'
    norm = proj.lstrip('/')
    if norm in proj_forks:
        results.append({'ProjectName': norm, 'Forks': proj_forks[norm]})
    else:
        # try case where project_info might have different case; try lowercasing keys
        if norm.lower() in (k.lower() for k in proj_forks.keys()):
            # find matching key
            for k,v in proj_forks.items():
                if k.lower() == norm.lower():
                    results.append({'ProjectName': norm, 'Forks': v})
                    break
# sort by forks desc
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)
top5 = results_sorted[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_P4UkSti8t5SZZ1nHGnj0x295': 'file_storage/call_P4UkSti8t5SZZ1nHGnj0x295.json', 'var_call_1uJQtFrSJUUR4MpPwh3LIibr': 'file_storage/call_1uJQtFrSJUUR4MpPwh3LIibr.json', 'var_call_MSSL9RI53qkcXKHpqb02tgtz': 'file_storage/call_MSSL9RI53qkcXKHpqb02tgtz.json', 'var_call_HmAe5yLePs6ubr7XV8rfa1Vc': {'count_project_names': 5284, 'sample_project_names': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0xsalah/tete', '1394/manipula', '1728954833/project-manager', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4catalyzer/theme', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client', 'aaronjwang/redux-websocket', 'abacritt/angularx-social-login', 'abrcdf1023/egroup-material', 'abrcdf1023/egroup-redux', 'abrcdf1023/egroup-utils', 'abuinitski/redux-bundler-async-resources', 'accenture/sfpowerscripts', 'actorapp/react-scroll', 'adamhalasz/uniqid', 'aduth/preact-jsx-runtime', 'adyatlov/behold', 'aeb-labs/graphql-weaver', 'aelbore/esbuild-jest', 'age-bijkaart/cbuf', 'agtenr/typescript-storagefactory', 'agustinramos/react-orgchart', 'aheckmann/mquery', 'aheissenberger/serverless-appsync-offline', 'ahmadnassri/node-har-validator', 'ahmadreza-s/dotlottie-player', 'ahmadreza-s/xmlparser', 'ahomu/grunt-data-uri', 'ahram-dolphin/cli', 'ai/audio-recorder-polyfill', 'ai/browserslist', 'airbnb/babel-plugin-dynamic-import-node', 'airdwing/node-dwing-azure-iot-device-mqtt', 'airdwing/node-dwing-common', 'airtable/blocks', 'akiran/react-slick', 'akserg/ng2-dnd']}, 'var_call_1swWJ2ywflbSAkKsnb1bNCXm': {'projpkg_sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}]}, 'var_call_zw2uqDziPzGk416NuhktNzCJ': 'file_storage/call_zw2uqDziPzGk416NuhktNzCJ.json', 'var_call_RcNmnp6SA6aqtBY7VAvGVMbt': 'file_storage/call_RcNmnp6SA6aqtBY7VAvGVMbt.json'}

exec(code, env_args)
