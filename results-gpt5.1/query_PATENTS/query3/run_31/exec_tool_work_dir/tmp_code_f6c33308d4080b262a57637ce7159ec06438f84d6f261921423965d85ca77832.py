code = """import json, pandas as pd

res = json.loads(var_call_qh4spwRr22p6LcM1zi02bgDW)"""

env_args = {'var_call_z5zUfdbxgREZlBt5y72RDQWv': 'file_storage/call_z5zUfdbxgREZlBt5y72RDQWv.json', 'var_call_LVSJmsZNtF22Q84diPB8U8aE': ['cpc_definition'], 'var_call_qh4spwRr22p6LcM1zi02bgDW': {'assignee_cpc_pairs': [{'assignee': 'UNKNOWN', 'cpc_symbol': 'C12N'}, {'assignee': 'UNKNOWN', 'cpc_symbol': 'A61K'}], 'symbols': ['A61K', 'C12N']}, 'var_call_HK4W5CVnrkuRXLKvtTTdmI1T': [{'symbol': 'A61K', 'titleFull': 'PREPARATIONS FOR MEDICAL, DENTAL OR TOILETRY PURPOSES'}, {'symbol': 'C12N', 'titleFull': 'MICROORGANISMS OR ENZYMES; COMPOSITIONS THEREOF; PROPAGATING, PRESERVING, OR MAINTAINING MICROORGANISMS; MUTATION OR GENETIC ENGINEERING; CULTURE MEDIA'}]}

exec(code, env_args)
