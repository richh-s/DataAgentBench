code = """import json
import pandas as pd
import re
import os

# Access the publication data file
pub_file = None
for key in list(globals().keys()):
    if 'query_db_48' in key:
        pub_file = globals()[key]
        break

if pub_file and os.path.exists(pub_file):
    print("Loading publication data from:", pub_file)
    with open(pub_file, 'r') as f:
        pub_data = json.load(f)
    print("Loaded", len(pub_data), "records")
    
    # Extract CPC codes and years
    records = []
    for item in pub_data:
        try:
            cpc_json = item.get('cpc', '[]')
            pub_date = item.get('publication_date', '')
            
            year_match = re.search(r'(\d{4})', pub_date)
            if year_match:
                year = int(year_match.group(1))
                
                cpc_list = json.loads(cpc_json)
                for entry in cpc_list:
                    code = entry.get('code', '')
                    if len(code) >= 5:
                        group_5 = code[:5]  # Level 5 group
                        records.append({
                            'year': year,
                            'cpc_group_5': group_5
                        })
        except:
            continue
    
    df = pd.DataFrame(records)
    print("Extracted", len(df), "CPC records")
    print("Year range:", df['year'].min(), "to", df['year'].max())
    print("Unique level-5 groups:", df['cpc_group_5'].nunique())
    
    # Count filings per year per group
    yearly_counts = df.groupby(['year', 'cpc_group_5']).size().reset_index(name='count')
    print("Yearly counts:", len(yearly_counts))
    
    # Calculate EMA for each group
    groups = yearly_counts['cpc_group_5'].unique()
    results = []
    alpha = 0.2
    
    for group in groups:
        group_data = yearly_counts[yearly_counts['cpc_group_5'] == group].copy()
        group_data = group_data.sort_values('year')
        
        ema = None
        best_year = None
        best_ema = -1
        
        for _, row in group_data.iterrows():
            count = row['count']
            year = row['year']
            
            if ema is None:
                ema = count
            else:
                ema = alpha * count + (1 - alpha) * ema
            
            if ema > best_ema:
                best_ema = ema
                best_year = year
        
        if best_year is not None:
            results.append({
                'cpc_group_5': group,
                'best_year': int(best_year),
                'best_ema': float(best_ema)
            })
    
    results_df = pd.DataFrame(results)
    
    # Filter for groups where best year is 2022
    best_2022 = results_df[results_df['best_year'] == 2022]
    final_codes = sorted(best_2022['cpc_group_5'].tolist())
    
    print("Groups with best year 2022:", len(final_codes))
    print("First 20 codes:", final_codes[:20])
    
    result = {
        'total_technology_areas': len(groups),
        'areas_best_year_2022': len(final_codes),
        'cpc_group_codes': final_codes
    }
else:
    result = {'error': 'Publication file not found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}, 'var_functions.execute_python:38': {'pub_records': 0, 'cpc_symbols': 0, 'sample_pub': None, 'sample_cpc': None}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:51': [], 'var_functions.execute_python:58': {'error': 'File not found', 'available_keys': ['var_functions.query_db:10', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:24', 'var_functions.query_db:48', 'var_functions.query_db:5', 'var_functions.query_db:51', 'var_functions.query_db:6']}, 'var_functions.execute_python:60': {'total_technology_areas': 3048, 'areas_best_year_2022': 268, 'cpc_group_codes': ['A01B6', 'A01G3', 'A01H5', 'A01H6', 'A01K1', 'A01K2', 'A21D1', 'A22B2', 'A23F5', 'A23K4', 'A23L3', 'A23V2', 'A23Y2', 'A41B1', 'A41B2', 'A41C3', 'A43B2', 'A45C7', 'A47C7', 'A47H1', 'A47H2', 'A47H5', 'A47J1', 'A47J3', 'A47J4', 'A47L1', 'A47L2', 'A61B3', 'A61B4', 'A61B5', 'A61B9', 'A61F5', 'A61H1', 'A61H3', 'A61K3', 'A61L2', 'A61M3', 'A61P3', 'A62C5', 'B01D4', 'B01F2', 'B01L2', 'B01L3', 'B01L9', 'B02B1', 'B02B5', 'B02C1', 'B02C7', 'B05D1', 'B06B2', 'B07C1', 'B07C2', 'B07C5', 'B08B1', 'B09B1', 'B09B2', 'B21J1', 'B22C2', 'B23K2', 'B25B7', 'B27C5', 'B27D1', 'B27M3', 'B28B1', 'B28B7', 'B28C5', 'B28D7', 'B29C7', 'B30B9', 'B32B2', 'B32B5', 'B33Y8', 'B43L1', 'B60B1', 'B60D1', 'B60H1', 'B60H2', 'B60K1', 'B60K2', 'B60P3', 'B60Q3', 'B60R1', 'B60R3', 'B60T2', 'B60T5', 'B60T7', 'B60W1', 'B60W2', 'B60W3', 'B60W5', 'B60W6', 'B60Y2', 'B61F5', 'B62D1', 'B62J1', 'B62K3', 'B62K7', 'B62M1', 'B63B8', 'B64C1', 'B64C5', 'B64D4', 'B64U8', 'B65D8', 'B65F1', 'B65G1', 'B65G4', 'B65G5', 'B66C5', 'B66D1', 'C01B3', 'C01D1', 'C01G3', 'C01G5', 'C04B1', 'C04B2', 'C05C9', 'C05G5', 'C07B2', 'C07C7', 'C07D4', 'C07D5', 'C08C1', 'C08G1', 'C08G6', 'C08L1', 'C09B1', 'C09C1', 'C09C2', 'C09C3', 'C09J9', 'C09K1', 'C09K5', 'C09K8', 'C11B5', 'C11D7', 'C12C7', 'C12L3', 'C12M1', 'C12N1', 'C12N9', 'C12P1', 'C12Y1', 'C12Y4', 'C21D6', 'C21D8', 'C22C3', 'C25B1', 'C25B3', 'D01F1', 'D06M1', 'D06N3', 'E01C1', 'E02F7', 'E04G9', 'E05B3', 'E05Y2', 'E21B2', 'E21D9', 'F01D5', 'F01D9', 'F02F3', 'F02K5', 'F03B1', 'F04C2', 'F16H1', 'F16H3', 'F16H6', 'F16J1', 'F16L5', 'F17C1', 'F17D5', 'F21S1', 'F21S4', 'F24C1', 'F24D2', 'F24D3', 'F24F1', 'F24F5', 'F24S3', 'F24S5', 'F25B2', 'F25B4', 'F25D2', 'F28G1', 'F28G2', 'F28G9', 'F41B9', 'G01F2', 'G01K1', 'G01K3', 'G01L1', 'G01L5', 'G01M3', 'G01N1', 'G01N2', 'G01N3', 'G02B2', 'G03F1', 'G04B1', 'G05B9', 'G05D1', 'G05G1', 'G06F1', 'G06F2', 'G06F7', 'G06F9', 'G06N7', 'G06V4', 'G07G1', 'G08B2', 'G08B5', 'G08B6', 'G09C1', 'G09F3', 'G09F9', 'G10K1', 'G10K9', 'G10L1', 'G10L2', 'G11C1', 'G11C8', 'G16B1', 'G16B4', 'G16B5', 'G16C1', 'G16C6', 'G16Y4', 'G21C9', 'H01B1', 'H01B3', 'H01B7', 'H01C7', 'H01J6', 'H01L2', 'H01L3', 'H01M1', 'H01M5', 'H01Q1', 'H01R4', 'H02J2', 'H02J3', 'H02K1', 'H02M1', 'H02M7', 'H02N2', 'H02P7', 'H03M9', 'H04L4', 'H04L5', 'H04L6', 'H04L9', 'H04N2', 'H04R1', 'H04W1', 'H04W4', 'H04W6', 'H04W7', 'H04W8', 'H05B6', 'H05K9', 'H10K7', 'H10N3', 'H10N5', 'H10N7', 'Y02E4', 'Y02P6', 'Y04S4']}}

exec(code, env_args)
