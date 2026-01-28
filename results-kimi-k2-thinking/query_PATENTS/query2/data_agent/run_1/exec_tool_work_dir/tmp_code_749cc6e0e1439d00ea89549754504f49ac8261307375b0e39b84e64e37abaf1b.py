code = """import json
from collections import defaultdict

file_path = locals()['var_functions.query_db:40']
with open(file_path, 'r') as f:
    data = json.load(f)

print('Records:', len(data))

# Filter for Germany patents
germany_patents = []
for record in data:
    if 'DE-' not in record.get('Patents_info', ''):
        continue
    
    grant_date = record.get('grant_date', '')
    year = None
    for y in range(2010, 2021):
        if str(y) in grant_date:
            year = y
            break
    
    if year:
        cpc_json = record.get('cpc', '[]')
        try:
            cpc_codes = json.loads(cpc_json)
        except:
            cpc_codes = []
        
        germany_patents.append({'year': year, 'cpc_codes': cpc_codes})

print('Valid patents:', len(germany_patents))

# Count CPC level 4 by year
yearly_counts = defaultdict(lambda: defaultdict(int))
cpc_code_map = {}

for patent in germany_patents:
    year = patent['year']
    for entry in patent['cpc_codes']:
        code = entry.get('code', '')
        if code:
            parts = code.split('/')
            if len(parts) >= 2:
                level4_code = parts[0] + '/' + parts[1][:2]
                yearly_counts[year][level4_code] += 1
                if level4_code not in cpc_code_map:
                    cpc_code_map[level4_code] = code

years = sorted(yearly_counts.keys())
print('Years:', years)

# Calculate EMA for each CPC code
alpha = 0.1
cpc_results = {}

for year in years:
    for code in yearly_counts[year]:
        if code not in cpc_results:
            cpc_results[code] = {'yearly_values': {}, 'ema_values': {}}
        count = yearly_counts[year][code]
        cpc_results[code]['yearly_values'][year] = count

for code, data in cpc_results.items():
    sorted_years = sorted(data['yearly_values'].keys())
    ema_prev = 0
    
    for year in sorted_years:
        value = data['yearly_values'][year]
        ema = alpha * value + (1 - alpha) * ema_prev
        data['ema_values'][year] = ema
        ema_prev = ema
    
    if data['ema_values']:
        best_year = max(data['ema_values'].keys(), key=lambda y: data['ema_values'][y])
        data['best_year'] = best_year
        data['best_ema'] = data['ema_values'][best_year]
        data['best_count'] = data['yearly_values'][best_year]

# Sort by best EMA
cpc_ranking = sorted(cpc_results.items(), key=lambda x: x[1]['best_ema'], reverse=True)

print('\nTop 20 by EMA:')
for i, (code, data) in enumerate(cpc_ranking[:20]):
    print(str(i+1) + '. ' + code + ': EMA=' + str(round(data['best_ema'], 2)) + 
          ' in ' + str(data['best_year']) + ' (count: ' + str(data['best_count']) + ')')

# Prepare final output
top_codes = []
for code, data in cpc_ranking[:20]:
    top_codes.append({
        'cpc_code': code,
        'full_code_example': cpc_code_map.get(code, ''),
        'best_year': data['best_year'],
        'best_count': data['best_count'],
        'best_ema': round(data['best_ema'], 2)
    })

result = {
    'top_cpc_codes': top_codes,
    'total_analyzed': len(cpc_results)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['cpc_definition'], 'var_functions.execute_python:18': {'cpc_counts': {'B41F21/10': 1, 'B41F22/00': 1, 'B41F21/00': 1, 'F02D41/30': 1, 'F02D41/20': 3, 'F02M65/00': 1, 'F02D41/00': 2, 'F02M59/10': 2, 'F02M55/04': 2, 'F02M59/44': 2, 'F02M59/06': 2, 'F04B53/00': 2, 'F02M59/36': 2, 'G01D11/24': 1, 'B23K1/00': 1, 'B63B21/50': 1, 'H04W72/21': 3, 'H04W72/56': 3, 'H04L5/00': 4, 'H04L1/16': 4, 'H04W52/02': 12, 'H04L1/18': 6, 'H04W72/04': 3, 'H04W76/28': 1, 'Y02D30/70': 2, 'B66C23/80': 1, 'E02F9/08': 1, 'B60S9/10': 1, 'F02D15/00': 1, 'F02D13/06': 1, 'Y02T10/12': 1, 'A61F5/14': 2, 'A61F5/01': 4, 'A43B17/00': 2, 'A43B7/20': 2, 'A43B13/22': 1, 'F24B5/02': 3, 'F23L15/04': 3, 'F23L1/00': 3, 'F23B60/00': 1, 'F23B50/12': 3, 'F23N1/02': 1, 'Y02E20/34': 1, 'H01R35/02': 1, 'B64D11/06': 1, 'H01R2201/26': 2, 'H01R24/60': 1, 'H01R13/63': 1, 'H01R35/04': 1, 'B60R16/02': 1, 'F02N2200/02': 2, 'F02N2300/20': 2, 'F02N11/08': 1, 'F02N11/04': 1, 'B60K6/48': 1, 'B60W30/19': 1, 'F02N11/00': 1, 'Y02T10/62': 1, 'Y02T10/40': 1, 'C04B2235/96': 2, 'C04B2235/77': 2, 'C04B2235/72': 2, 'C04B2235/66': 6, 'C04B2235/65': 6, 'C04B2235/54': 4, 'C04B2235/44': 2, 'C04B2235/32': 8, 'C04B35/64': 6, 'C04B35/62': 2, 'C04B35/54': 2, 'C04B35/51': 2, 'C09K11/77': 2, 'C04B40/00': 1, 'B29C49/42': 1, 'B29C2049/58': 7, 'B29C2049/42': 2, 'B29C49/06': 2, 'B29C49/58': 2, 'B29C2949/07': 1, 'G02B15/16': 1, 'A61B1/00': 3, 'G02B15/15': 2, 'G02B13/02': 1, 'G02B23/24': 5, 'G02B13/18': 1, 'G02B15/14': 2, 'Y10T70/70': 2, 'G07C9/00': 2, 'B29C2045/56': 2, 'B29D99/00': 1, 'H01H9/02': 2, 'B29C45/56': 2, 'H01H2009/18': 2, 'E05B19/00': 1, 'F16H37/04': 2, 'F16H2200/00': 2, 'F16H3/00': 1, 'E02F3/76': 2, 'E02F9/00': 2, 'E02F3/96': 1, 'F42B3/00': 2, 'F41H11/16': 2}, 'total_patents': 18, 'cpc_level4_codes': ['B41F21/10', 'B41F22/00', 'B41F21/00', 'F02D41/30', 'F02D41/20', 'F02M65/00', 'F02D41/00', 'F02M59/10', 'F02M55/04', 'F02M59/44', 'F02M59/06', 'F04B53/00', 'F02M59/36', 'G01D11/24', 'B23K1/00', 'B63B21/50', 'H04W72/21', 'H04W72/56', 'H04L5/00', 'H04L1/16', 'H04W52/02', 'H04L1/18', 'H04W72/04', 'H04W76/28', 'Y02D30/70', 'B66C23/80', 'E02F9/08', 'B60S9/10', 'F02D15/00', 'F02D13/06', 'Y02T10/12', 'A61F5/14', 'A61F5/01', 'A43B17/00', 'A43B7/20', 'A43B13/22', 'F24B5/02', 'F23L15/04', 'F23L1/00', 'F23B60/00', 'F23B50/12', 'F23N1/02', 'Y02E20/34', 'H01R35/02', 'B64D11/06', 'H01R2201/26', 'H01R24/60', 'H01R13/63', 'H01R35/04', 'B60R16/02', 'F02N2200/02', 'F02N2300/20', 'F02N11/08', 'F02N11/04', 'B60K6/48', 'B60W30/19', 'F02N11/00', 'Y02T10/62', 'Y02T10/40', 'C04B2235/96', 'C04B2235/77', 'C04B2235/72', 'C04B2235/66', 'C04B2235/65', 'C04B2235/54', 'C04B2235/44', 'C04B2235/32', 'C04B35/64', 'C04B35/62', 'C04B35/54', 'C04B35/51', 'C09K11/77', 'C04B40/00', 'B29C49/42', 'B29C2049/58', 'B29C2049/42', 'B29C49/06', 'B29C49/58', 'B29C2949/07', 'G02B15/16', 'A61B1/00', 'G02B15/15', 'G02B13/02', 'G02B23/24', 'G02B13/18', 'G02B15/14', 'Y10T70/70', 'G07C9/00', 'B29C2045/56', 'B29D99/00', 'H01H9/02', 'B29C45/56', 'H01H2009/18', 'E05B19/00', 'F16H37/04', 'F16H2200/00', 'F16H3/00', 'E02F3/76', 'E02F9/00', 'E02F3/96', 'F42B3/00', 'F41H11/16']}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:38': [{'symbol': 'H04L1/18', 'titleFull': 'Automatic repetition systems, e.g. Van Duuren systems'}, {'symbol': 'F02D41/00', 'titleFull': 'Electrical control of supply of combustible mixture or its constituents'}, {'symbol': 'F02M55/04', 'titleFull': 'Means for damping vibrations or pressure fluctuations in injection pump inlets or outlets'}, {'symbol': 'H04L5/00', 'titleFull': 'Arrangements affording multiple use of the transmission path'}, {'symbol': 'A61F5/01', 'titleFull': 'Orthopaedic devices, e.g. splints, casts or braces'}, {'symbol': 'F02D41/20', 'titleFull': 'Output circuits, e.g. for controlling currents in command coils'}, {'symbol': 'H04W52/02', 'titleFull': 'Power saving arrangements'}, {'symbol': 'H04W72/04', 'titleFull': 'Wireless resource allocation'}, {'symbol': 'H04L1/16', 'titleFull': 'Arrangements for detecting or preventing errors in the information received by using return channel in which the return channel carries supervisory signals, e.g. repetition request signals'}, {'symbol': 'F02M59/10', 'titleFull': 'Pumps specially adapted for fuel-injection and not provided for in groups F02M39/00 -F02M57/00, e.g. rotary cylinder-block type of pumps of reciprocating-piston or reciprocating-cylinder type characterised by the piston-drive'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
