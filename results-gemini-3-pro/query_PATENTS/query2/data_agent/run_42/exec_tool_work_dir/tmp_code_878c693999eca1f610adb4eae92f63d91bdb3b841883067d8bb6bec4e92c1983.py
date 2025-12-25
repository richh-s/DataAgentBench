code = """import json
import pandas as pd
from datetime import datetime

file_path = locals()['var_function-call-8210490788658783622']
with open(file_path, 'r') as f:
    records = json.load(f)

def parse_date(date_str):
    if not date_str:
        return None
    clean = date_str.replace('dated ', '').replace('on ', '').replace('of ', '').replace(',', '').strip()
    for suffix in ['st', 'nd', 'rd', 'th']:
        clean = clean.replace(suffix, '')
    formats = [
        "%d %B %Y", "%B %d %Y", "%Y %B %d", 
        "%d %b %Y", "%b %d %Y", "%Y %b %d"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(clean, fmt)
        except ValueError:
            continue
    return None

filtered_data = []
for r in records:
    # Grant Date filter
    g_date = parse_date(r['grant_date'])
    if not g_date:
        continue
    # H2 2019
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue
    
    # Filing Year
    f_date = parse_date(r['filing_date'])
    if not f_date:
        continue
    year = f_date.year
    
    # CPC
    try:
        cpc_list = json.loads(r['cpc'])
    except:
        continue
        
    codes = set()
    for item in cpc_list:
        code = item.get('code', '')
        if len(code) >= 3:
            codes.add(code[:3])
    
    for c in codes:
        filtered_data.append({'year': year, 'cpc': c})

df = pd.DataFrame(filtered_data)

if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Aggregation
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    min_year = counts['year'].min()
    max_year = counts['year'].max()
    all_years = range(min_year, max_year + 1)
    
    full_df_list = []
    unique_cpcs = counts['cpc'].unique()
    
    for cpc in unique_cpcs:
        cpc_df = counts[counts['cpc'] == cpc].set_index('year')
        cpc_df = cpc_df.reindex(all_years, fill_value=0).reset_index().rename(columns={'index': 'year'})
        cpc_df['cpc'] = cpc
        cpc_df['ema'] = cpc_df['count'].ewm(alpha=0.1, adjust=False).mean()
        full_df_list.append(cpc_df)
        
    full_df = pd.concat(full_df_list, ignore_index=True)
    
    # Identify winners per year
    top_per_year = full_df.loc[full_df.groupby('year')['ema'].idxmax()]
    
    # Distinct winners
    winner_cpcs = top_per_year['cpc'].unique()
    
    results = []
    for cpc in winner_cpcs:
        # Find best year for this CPC
        cpc_rows = full_df[full_df['cpc'] == cpc]
        best_row = cpc_rows.loc[cpc_rows['ema'].idxmax()]
        results.append({
            'cpc_group': cpc,
            'best_year': int(best_row['year']),
            'max_ema': float(best_row['ema'])
        })
        
    print('__RESULT__:')
    print(json.dumps(results))"""

env_args = {'var_function-call-9349135532436099927': 'file_storage/function-call-9349135532436099927.json', 'var_function-call-7996704792418014537': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-135606811111269997': [{'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B59/00', 'level': '7.0', 'titleFull': 'Devices specially adapted for connection between animals or tractors and agricultural machines or implements'}, {'symbol': 'A01B19/00', 'level': '7.0', 'titleFull': 'Harrows with non-rotating tools'}, {'symbol': 'A01B35/00', 'level': '7.0', 'titleFull': 'Other machines for working soil not specially adapted for working soil on which crops are growing'}, {'symbol': 'A01B13/00', 'level': '7.0', 'titleFull': 'Ploughs or like machines for special purposes ; Ditch diggers, trench ploughs, forestry ploughs, ploughs for land or marsh reclamation'}], 'var_function-call-14112593806741946107': [{'symbol': 'A01B1/00', 'level': '7.0'}, {'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-18427524461417541909': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.'}], 'var_function-call-8210490788658783622': 'file_storage/function-call-8210490788658783622.json', 'var_function-call-16513184790929394189': [{'cpc_group': 'B41', 'best_year': 2007, 'max_ema': 1.0}], 'var_function-call-14141029842649252917': {'status': 'debug complete'}, 'var_function-call-9123081436482311392': {'total_records': 50, 'parsed_grant_dates': 40, 'h2_2019': 17, 'filing_dates': 13, 'cpc_parsed': 13}, 'var_function-call-3476790115942514869': [{'count(*)': '11716'}], 'var_function-call-2231421690736791113': [{'count(*)': '53'}]}

exec(code, env_args)
