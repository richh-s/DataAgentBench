code = """import pandas as pd
import json

data = pd.read_json(locals()['var_function-call-6623226614519656190'])

# Filter for German patents and grant date in the second half of 2019
def is_german_patent(patents_info):
    return 'DE,' in patents_info

def is_second_half_2019(grant_date):
    try:
        if isinstance(grant_date, str):
            grant_date_str = grant_date.lower()
            if 'jul' in grant_date_str or 'aug' in grant_date_str or 'sep' in grant_date_str or \
               'oct' in grant_date_str or 'nov' in grant_date_str or 'dec' in grant_date_str:
                return True
        return False
    except:
        return False

filtered_patents = data[data['Patents_info'].apply(is_german_patent) &
                        data['grant_date'].apply(is_second_half_2019)].copy()

# Extract CPC codes and filing year
cpc_filing_data = []
for index, row in filtered_patents.iterrows():
    cpc_list = json.loads(row['cpc'])
    filing_date_str = row['filing_date']
    filing_year = None
    if isinstance(filing_date_str, str):
        for part in filing_date_str.split():
            if part.isdigit() and len(part) == 4:
                filing_year = int(part)
                break
    
    for cpc_item in cpc_list:
        cpc_code = cpc_item['code']
        if len(cpc_code) >= 4 and filing_year: # Ensure it's at least level 4
            cpc_group = cpc_code[:4] # Get level 4 CPC group
            cpc_filing_data.append({'cpc_group': cpc_group, 'filing_year': filing_year})

cpc_filing_df = pd.DataFrame(cpc_filing_data)

# Group by CPC group and filing year, then count filings
filings_by_cpc_year = cpc_filing_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='filings_count')

# Calculate EMA
alpha = 0.1
ema_results = []
for cpc_group in filings_by_cpc_year['cpc_group'].unique():
    cpc_group_df = filings_by_cpc_year[filings_by_cpc_year['cpc_group'] == cpc_group].sort_values(by='filing_year')
    
    # Initialize EMA for the first year
    if not cpc_group_df.empty:
        ema = 0
        if not cpc_group_df.empty:
            ema = cpc_group_df.iloc[0]['filings_count']
            ema_results.append({
                'cpc_group': cpc_group,
                'filing_year': cpc_group_df.iloc[0]['filing_year'],
                'ema': ema
            })
        
        # Calculate EMA for subsequent years
        for i in range(1, len(cpc_group_df)):
            ema = alpha * cpc_group_df.iloc[i]['filings_count'] + (1 - alpha) * ema
            ema_results.append({
                'cpc_group': cpc_group,
                'filing_year': cpc_group_df.iloc[i]['filing_year'],
                'ema': ema
            })

ema_df = pd.DataFrame(ema_results)

# Find the best year for each CPC group
best_years = ema_df.loc[ema_df.groupby('cpc_group')['ema'].idxmax()]

# Merge with original cpc_filing_data to get the full cpc_code for title lookup
merged_data = pd.merge(best_years, cpc_filing_df, on=['cpc_group', 'filing_year'], how='inner')

# Get unique full CPC codes (not just groups) for querying titles
unique_cpc_symbols = merged_data['cpc_group'].unique().tolist()

print("__RESULT__:")
print(json.dumps(unique_cpc_symbols))"""

env_args = {'var_function-call-6623226614519656190': 'file_storage/function-call-6623226614519656190.json', 'var_function-call-9406239657222584757': ['A43B', 'A61B', 'A61F', 'A61L', 'B23K', 'B41F', 'B60K', 'B60N', 'B60R', 'B60W', 'B64D', 'E02F', 'F01D', 'F02M', 'F02N', 'F04B', 'F04D', 'F05D', 'F16C', 'F16F', 'F16K', 'F17C', 'F41H', 'F42B', 'G01D', 'G01M', 'G01N', 'G02B', 'G05D', 'G08B', 'H01R', 'H02J', 'H03L', 'H04L', 'H04W', 'Y02D', 'Y02T'], 'var_function-call-6982923480119486199': [], 'var_function-call-17065823913741193205': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-3724504970294373724': [{'titleFull': 'CHARACTERISTIC FEATURES OF FOOTWEAR; PARTS OF FOOTWEAR', 'symbol': 'A43B', 'level': '5.0'}, {'titleFull': 'DIAGNOSIS; SURGERY; IDENTIFICATION', 'symbol': 'A61B', 'level': '5.0'}, {'titleFull': 'FILTERS IMPLANTABLE INTO BLOOD VESSELS; PROSTHESES; DEVICES PROVIDING PATENCY TO, OR PREVENTING COLLAPSING OF, TUBULAR STRUCTURES OF THE BODY, e.g. STENTS; ORTHOPAEDIC, NURSING OR CONTRACEPTIVE DEVICES; FOMENTATION; TREATMENT OR PROTECTION OF EYES OR EARS; BANDAGES, DRESSINGS OR ABSORBENT PADS; FIRST-AID KITS', 'symbol': 'A61F', 'level': '5.0'}, {'titleFull': 'SOLDERING OR UNSOLDERING; WELDING; CLADDING OR PLATING BY SOLDERING OR WELDING; CUTTING BY APPLYING HEAT LOCALLY, e.g. FLAME CUTTING; WORKING BY LASER BEAM', 'symbol': 'B23K', 'level': '5.0'}]}

exec(code, env_args)
