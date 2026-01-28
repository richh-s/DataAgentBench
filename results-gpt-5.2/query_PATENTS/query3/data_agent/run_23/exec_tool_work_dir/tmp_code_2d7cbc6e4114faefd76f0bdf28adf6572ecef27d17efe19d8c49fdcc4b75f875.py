code = """import json
pairs = var_call_6tXpryjDsDPgy7vhuZTorOZ6
# tool result is dict already
pair_list = pairs['sample'][:]
# but need full pairs; re-load from stored? can't. We'll reconstruct by re-running minimal from sample if count=1.
assignee, subclass = pair_list[0]
title = var_call_TRwb4VnUAOSfxEBnmFtvpm8n[0]['titleFull']
answer = f"{assignee}\t{subclass}: {title}"
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_bn8TU9VmVk7pN006TU4zWS7v': ['publicationinfo'], 'var_call_4JOLYly9fdp0lGpLaOI60GYA': ['cpc_definition'], 'var_call_8mi1In3NOVkCaut8K4dmMMBZ': [], 'var_call_DQHDx6XuPUEqnb6zdY4YYVtE': [], 'var_call_hexwFqpBOYPl5UnOP4IVCFVL': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_xNu75D1MsakbKFD0Cw620bkj': 'file_storage/call_xNu75D1MsakbKFD0Cw620bkj.json', 'var_call_ONamGQwhRaqkRKoZST5o9ogf': {'uc_pub_count': 64, 'sample': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2009234210-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6492396-A', 'AU-6535890-A', 'CA-2298540-A1']}, 'var_call_yPQXULut7RwXm1JJmsji0g0Z': 'file_storage/call_yPQXULut7RwXm1JJmsji0g0Z.json', 'var_call_6tXpryjDsDPgy7vhuZTorOZ6': {'pair_count': 1, 'sample': [['ETHICON LLC', 'A61B']]}, 'var_call_TRwb4VnUAOSfxEBnmFtvpm8n': [{'symbol': 'A61B', 'titleFull': 'DIAGNOSIS; SURGERY; IDENTIFICATION'}]}

exec(code, env_args)
