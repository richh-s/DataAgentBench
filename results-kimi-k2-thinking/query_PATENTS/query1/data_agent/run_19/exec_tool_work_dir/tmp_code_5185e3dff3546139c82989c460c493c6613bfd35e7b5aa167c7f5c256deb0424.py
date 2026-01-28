code = """import json
import pandas as pd

# Let's reconsider what level 5 CPC codes look like
# From CPC definition, level 5 should be subgroups, which have format like A01H1/02
# The full code includes the class and main group, not just the subgroup part

# Read the counts data
df_counts = pd.read_csv('/tmp/level5_counts.csv')
print('Total unique codes:', df_counts['level5_code'].nunique())
print('Sample codes:', df_counts['level5_code'].unique()[:20])

# Check the structure of CPC codes
# Level 5 subgroup codes should have format: [Section][Class][Subclass]/[Group][/Subgroup]
# For level 5, we want actual subgroups (not main groups ending in /00)

# The format is typically: A61K45/06 or similar
# Before slash: A61K45 (section A, class 61, subclass K, main group 45)
# After slash: 06 (subgroup)

# So level 5 codes ARE the full code including the subgroup number
# Let's query the CPC database to understand the levels better

# Based on the query result, level 5 codes are like "A01H", "A01F" etc.
# But those are actually subclass codes (level 3), not subgroups

# Let me check what level actual subgroups like "A61K45/06" are
print('')
print('Codes ending in /00 (main groups):', len(df_counts[df_counts['level5_code'].str.endswith('/00', na=False)]))
print('Codes with / but not /00 (subgroups):', len(df_counts[~df_counts['level5_code'].str.endswith('/00', na=False) & df_counts['level5_code'].str.contains('/', na=False)]))

print('')
print('Sample main groups:', df_counts[df_counts['level5_code'].str.endswith('/00', na=False)]['level5_code'].unique()[:10])
print('Sample subgroups:', df_counts[~df_counts['level5_code'].str.endswith('/00', na=False) & df_counts['level5_code'].str.contains('/', na=False)]['level5_code'].unique()[:10])

print('__RESULT__:')
print(json.dumps({
    'total_codes': int(df_counts['level5_code'].nunique()),
    'main_groups': int(len(df_counts[df_counts['level5_code'].str.endswith('/00', na=False)]['level5_code'].unique())),
    'subgroups': int(len(df_counts[~df_counts['level5_code'].str.endswith('/00', na=False) & df_counts['level5_code'].str.contains('/', na=False)]['level5_code'].unique()))
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'status': 'parsed', 'count': 2681388, 'sample': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}]}, 'var_functions.execute_python:16': {'level5_records': 2533616, 'year_range': '1837-2024', 'unique_codes': 168648, 'combinations': 875100}, 'var_functions.execute_python:22': ['A61K45/06', 'A61K2039/505', 'Y02P70/50', 'A61K9/0019', 'H04W72/23', 'A61P25/28', 'Y02T10/7072', 'H04L5/0053', 'Y02E60/50', 'H04W72/0446', 'H04L67/12', 'A61P31/04', 'A61P35/02', 'A61K31/519', 'C22C38/02', 'A61K31/506', 'H04W24/10', 'C22C38/04', 'C07D413/14', 'A61K47/10', 'A61K31/5377', 'H04W72/0453', 'A61K9/08', 'G10L15/22', 'A61K9/0014', 'Y02T90/14', 'A61P1/16', 'H01M4/366', 'H04L67/02', 'A61K9/0053', 'G06Q10/10', 'A61P31/12', 'A61K39/3955', 'G06T2207/10016', 'H04W4/029', 'H01L33/62', 'H04W76/14', 'C09D7/61', 'H04L9/3247', 'C22C38/001', 'C07K2317/21', 'A61K2039/545', 'G06Q10/087', 'C12N1/20', 'G06F21/32', 'A61Q19/08', 'G06F3/013', 'H04W48/16', 'C07D403/14', 'G16H40/63', 'C07K2319/30', 'C12Q2600/156', 'H01L24/16', 'H04W16/14', 'H01M4/62', 'H01L27/124', 'A61K9/2054', 'C12N9/22', 'A61B5/055', 'C12N2310/14', 'G06Q30/02', 'A61K47/02', 'C07K16/28', 'H01L29/66795', 'H01L25/50', 'G06F3/0679', 'G01N2800/52', 'G05B15/02', 'H01L29/66545', 'H04W72/20', 'H04N7/18', 'A61K47/12', 'A61P35/04', 'H01Q1/38', 'C07D495/04', 'A61K8/9789', 'H04L63/08', 'C12Q1/6883', 'H04L5/0044', 'A61K47/36', 'G06N3/063', 'H04W56/001', 'G06F8/65', 'C21D8/0226', 'A61K31/713', 'G06N7/01', 'A61K31/198', 'H04L63/1416', 'B22F10/28', 'A61K31/573', 'C09D7/63', 'H01L21/78', 'H04L67/34', 'G06Q40/04', 'H04L63/1425', 'C07D498/04', 'H10K59/12', 'C12N15/85', 'H04W72/02', 'H01G4/30'], 'var_functions.query_db:24': [{'symbol': 'H04L5/0053', 'level': '9.0'}, {'symbol': 'H04L67/12', 'level': '9.0'}, {'symbol': 'H04W72/23', 'level': '9.0'}, {'symbol': 'Y02E60/50', 'level': '9.0'}, {'symbol': 'Y02T10/7072', 'level': '9.0'}, {'symbol': 'A61K47/10', 'level': '10.0'}, {'symbol': 'H04W72/0446', 'level': '10.0'}, {'symbol': 'A61K2039/505', 'level': '8.0'}, {'symbol': 'A61K45/06', 'level': '8.0'}, {'symbol': 'H04W24/10', 'level': '8.0'}, {'symbol': 'Y02P70/50', 'level': '8.0'}, {'symbol': 'C07D413/14', 'level': '8.0'}, {'symbol': 'A61K9/0019', 'level': '9.0'}, {'symbol': 'A61K31/506', 'level': '12.0'}, {'symbol': 'A61K31/519', 'level': '12.0'}, {'symbol': 'A61P25/28', 'level': '8.0'}, {'symbol': 'A61P31/04', 'level': '8.0'}, {'symbol': 'A61P35/02', 'level': '8.0'}, {'symbol': 'C22C38/04', 'level': '8.0'}, {'symbol': 'C22C38/02', 'level': '8.0'}], 'var_functions.query_db:26': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A21D', 'level': '5.0'}, {'symbol': 'A21C', 'level': '5.0'}, {'symbol': 'A21B', 'level': '5.0'}, {'symbol': 'A22B', 'level': '5.0'}, {'symbol': 'A22C', 'level': '5.0'}, {'symbol': 'A23P', 'level': '5.0'}, {'symbol': 'A23C', 'level': '5.0'}, {'symbol': 'A23K', 'level': '5.0'}, {'symbol': 'A23L', 'level': '5.0'}, {'symbol': 'A23N', 'level': '5.0'}, {'symbol': 'A23V', 'level': '5.0'}, {'symbol': 'A23F', 'level': '5.0'}, {'symbol': 'A23G', 'level': '5.0'}, {'symbol': 'A23B', 'level': '5.0'}, {'symbol': 'A23D', 'level': '5.0'}, {'symbol': 'A24C', 'level': '5.0'}, {'symbol': 'B21L', 'level': '5.0'}, {'symbol': 'A24D', 'level': '5.0'}, {'symbol': 'A24F', 'level': '5.0'}, {'symbol': 'A24B', 'level': '5.0'}, {'symbol': 'A41F', 'level': '5.0'}, {'symbol': 'A41G', 'level': '5.0'}, {'symbol': 'A41B', 'level': '5.0'}, {'symbol': 'A47F', 'level': '5.0'}, {'symbol': 'A41D', 'level': '5.0'}, {'symbol': 'A41C', 'level': '5.0'}, {'symbol': 'A41H', 'level': '5.0'}, {'symbol': 'A42B', 'level': '5.0'}, {'symbol': 'A42C', 'level': '5.0'}, {'symbol': 'A43B', 'level': '5.0'}, {'symbol': 'A43C', 'level': '5.0'}, {'symbol': 'A43D', 'level': '5.0'}, {'symbol': 'A44D', 'level': '5.0'}, {'symbol': 'A44B', 'level': '5.0'}, {'symbol': 'A44C', 'level': '5.0'}, {'symbol': 'A45F', 'level': '5.0'}, {'symbol': 'A45C', 'level': '5.0'}]}

exec(code, env_args)
