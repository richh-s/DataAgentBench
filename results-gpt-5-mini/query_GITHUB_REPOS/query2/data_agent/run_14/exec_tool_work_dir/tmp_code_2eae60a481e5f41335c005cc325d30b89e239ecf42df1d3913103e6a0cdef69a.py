code = """import json, re
with open(var_call_wiXK2dUnX8Nkr7ByfryAiyjH, 'r') as f:
    data = json.load(f)

records = []
for r in data:
    path = r.get('sample_path', '') or ''
    if not isinstance(path, str) or not path.lower().endswith('.swift'):
        continue
    desc = (r.get('repo_data_description') or '')
    desc_l = desc.lower()
    # consider non-binary if the description explicitly contains 'non-binary'
    if 'non-binary' not in desc_l:
        continue
    # find a number of times copied
    m = re.search(r"(\d+)\s*times", desc_l)
    if m:
        copies = int(m.group(1))
    else:
        # fallback: any number in description
        nums = re.findall(r"(\d+)", desc_l)
        copies = int(nums[-1]) if nums else 1
    records.append({'id': r.get('id'), 'sample_repo_name': r.get('sample_repo_name'), 'copies': copies, 'sample_path': r.get('sample_path')})

# Aggregate unique ids
id_to_repos = {}
id_to_copies = {}
for rec in records:
    _id = rec['id']
    if not _id:
        continue
    id_to_copies[_id] = max(id_to_copies.get(_id, 0), rec['copies'])
    id_to_repos.setdefault(_id, set()).add(rec['sample_repo_name'])

if id_to_copies:
    max_copies = max(id_to_copies.values())
    max_ids = [k for k,v in id_to_copies.items() if v==max_copies]
else:
    max_copies = 0
    max_ids = []

result = {'max_copies': max_copies, 'max_ids': max_ids, 'id_to_repos_sample': {k: sorted(list(v)) for k,v in id_to_repos.items() if k in max_ids}}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_4Lli0VwvimK3yhNbFzPxIx3w': [], 'var_call_IkcQkgcHm1L1a1uYPlBViuPg': ['commits', 'contents', 'files'], 'var_call_wiXK2dUnX8Nkr7ByfryAiyjH': 'file_storage/call_wiXK2dUnX8Nkr7ByfryAiyjH.json', 'var_call_9VQhqtQnbmz0F3KCW9Ac9Yyj': {'max_copies': 0, 'ids': [], 'candidate_sample_repos': []}, 'var_call_ihGPQCT0HWuEv3eQoftRROXR': {'total_records_in_result': 100, 'first_20_paths': ['5- Shared-CoreData/SharedKit/Record.swift', 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'BusyNavigationBar/Example/AppDelegate.swift', 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'fixed/01682-swift-parser-parsedecl.swift', 'crashes-duplicates/15025-swift-sourcemanager-getmessage.swift', 'crashes-duplicates/18368-swift-sourcemanager-getmessage.swift', 'fixed/01847-std-function-func-swift-type-subst.swift', 'crashes-duplicates/08505-swift-typechecker-conformstoprotocol.swift', 'fixed/00118-swift-dependentgenerictyperesolver-resolvegenerictypeparamtype.swift', 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'crashes-duplicates/15704-no-stacktrace.swift', 'crashes-duplicates/04574-swift-sourcemanager-getmessage.swift', 'crashes-duplicates/02484-swift-sourcemanager-getmessage.swift'], 'count_swift': 100, 'count_nonbinary': 0, 'count_both': 0}}

exec(code, env_args)
