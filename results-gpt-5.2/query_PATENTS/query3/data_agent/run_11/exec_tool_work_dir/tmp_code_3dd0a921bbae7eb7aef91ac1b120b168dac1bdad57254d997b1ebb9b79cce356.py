code = """import re, json
import pandas as pd

rows = var_call_orSJcL9REVmx7crexoGaa75w
texts = [r['Patents_info'] for r in rows]
# infer assignee pattern: likely starts sentence until ' holds' or ' is owned by' or ' is assigned to'
print('__RESULT__:')
print(json.dumps(texts))"""

env_args = {'var_call_YJidZmBvU5MTPVYW57hU6WF7': ['publicationinfo'], 'var_call_LRepTdXnPvuewKZleMJeYEt0': ['cpc_definition'], 'var_call_89qb0KndyOtUX3EZVb5EyOw1': [], 'var_call_EpTAmg0Qd8RR0QwpJzsoYOy4': [], 'var_call_orSJcL9REVmx7crexoGaa75w': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}]}

exec(code, env_args)
