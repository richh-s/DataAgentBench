code = """import json
import pandas as pd
import re

# Load the German H2 2019 data from the first query
file_path = locals()['var_functions.query_db:2']
print('Loading H2 2019 German patent data from:', file_path)

with open(file_path, 'r') as f:
    data = json.load(f)

print(f'Total records in first dataset: {len(data)}')

# Filter for German patents in second half of 2019
h2_2019_patents = []
for record in data:
    if 'DE-' in record['Patents_info']:
        grant_date_str = record['grant_date']
        if '2019' in grant_date_str and ('Jul' in grant_date_str or 'Aug' in grant_date_str or 
           'Sep' in grant_date_str or 'Oct' in grant_date_str or 'Nov' in grant_date_str or 
           'Dec' in grant_date_str):
            h2_2019_patents.append(record)

print(f'German patents granted in H2 2019: {len(h2_2019_patents)}')

# Extract CPC groups (level 4) from these patents
cpc_groups_h2_2019 = set()
cpc_codes_full = []

for record in h2_2019_patents:
    cpc_json = record['cpc']
    if cpc_json and cpc_json != '[]':
        try:
            cpc_list = json.loads(cpc_json)
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code and len(code) >= 4:
                    group_code = code.split('/')[0][:4]
                    cpc_groups_h2_2019.add(group_code)
                    cpc_codes_full.append({
                        'patent_info': record['Patents_info'],
                        'group_code': group_code,
                        'full_code': code,
                        'grant_date': record['grant_date']
                    })
        except:
            if '[{"code":' in cpc_json:
                codes = re.findall(r'"code":\s*"([^"]+)"', cpc_json)
                for code in codes:
                    if len(code) >= 4:
                        group_code = code.split('/')[0][:4]
                        cpc_groups_h2_2019.add(group_code)
                        cpc_codes_full.append({
                            'patent_info': record['Patents_info'],
                            'group_code': group_code,
                            'full_code': code,
                            'grant_date': record['grant_date']
                        })

print(f'Unique CPC groups found in H2 2019: {len(cpc_groups_h2_2019)}')
print('Sample CPC groups:', list(cpc_groups_h2_2019)[:10])

result = {
    'h2_2019_patent_count': len(h2_2019_patents),
    'unique_cpc_groups': list(cpc_groups_h2_2019),
    'total_cpc_codes': len(cpc_codes_full)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'german_patents_h2_2019': 34, 'total_cpc_entries': 313, 'cpc_groups_count': 62, 'top_50_cpc_groups': ['C04B', 'H04W', 'G02B', 'B29C', 'F02D', 'H04L', 'F02M', 'H01J', 'F02N', 'E02F', 'A61F', 'F23L', 'H01R', 'H01L', 'H02J', 'H03L', 'A43B', 'A61B', 'F16H', 'Y02T', 'F23B', 'G01M', 'H01F', 'F02P', 'H01H', 'G01L', 'B41F', 'F16C', 'F24B', 'B60K', 'F16D', 'B60N', 'F04B', 'Y02D', 'F05D', 'F01D', 'B62D', 'C09K', 'G01N', 'A61L', 'Y10T', 'G07C', 'G01F', 'F42B', 'F41H', 'G08B', 'G01D', 'B23K', 'B63B', 'B66C']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'total_german_patents': 3757, 'total_cpc_entries': 26277, 'unique_cpc_groups': 564, 'year_range': {'min': 1882, 'max': 2024}, 'top_groups_by_ema': [{'cpc_group': 'H01L', 'total_patents': 1519, 'best_year': 2024, 'best_year_count': 95, 'best_year_ema': 70.24120163002297, 'years_active': 37}, {'cpc_group': 'Y10T', 'total_patents': 1038, 'best_year': 2009, 'best_year_count': 104, 'best_year_ema': 45.489558466385965, 'years_active': 44}, {'cpc_group': 'C10M', 'total_patents': 395, 'best_year': 1997, 'best_year_count': 64, 'best_year_ema': 29.782342000000007, 'years_active': 11}, {'cpc_group': 'A61K', 'total_patents': 533, 'best_year': 2008, 'best_year_count': 60, 'best_year_ema': 29.707493637350268, 'years_active': 31}, {'cpc_group': 'A61F', 'total_patents': 501, 'best_year': 2009, 'best_year_count': 98, 'best_year_ema': 26.881183164527222, 'years_active': 27}, {'cpc_group': 'A61B', 'total_patents': 439, 'best_year': 2009, 'best_year_count': 26, 'best_year_ema': 24.72901581974437, 'years_active': 29}, {'cpc_group': 'A61P', 'total_patents': 337, 'best_year': 2008, 'best_year_count': 49, 'best_year_ema': 21.898398971854412, 'years_active': 26}, {'cpc_group': 'C04B', 'total_patents': 329, 'best_year': 2019, 'best_year_count': 45, 'best_year_ema': 19.87692639604831, 'years_active': 20}, {'cpc_group': 'H04L', 'total_patents': 320, 'best_year': 2008, 'best_year_count': 46, 'best_year_ema': 18.855209247853953, 'years_active': 27}, {'cpc_group': 'B29C', 'total_patents': 477, 'best_year': 2007, 'best_year_count': 36, 'best_year_ema': 18.802022845887514, 'years_active': 38}, {'cpc_group': 'G11B', 'total_patents': 316, 'best_year': 2002, 'best_year_count': 20, 'best_year_ema': 18.725416093910003, 'years_active': 26}, {'cpc_group': 'C07D', 'total_patents': 317, 'best_year': 2005, 'best_year_count': 67, 'best_year_ema': 17.815352260794686, 'years_active': 26}, {'cpc_group': 'H04N', 'total_patents': 340, 'best_year': 2010, 'best_year_count': 26, 'best_year_ema': 17.759321350780155, 'years_active': 28}, {'cpc_group': 'C07C', 'total_patents': 323, 'best_year': 2005, 'best_year_count': 60, 'best_year_ema': 17.341983618400313, 'years_active': 32}, {'cpc_group': 'B60G', 'total_patents': 309, 'best_year': 2022, 'best_year_count': 41, 'best_year_ema': 16.35458218544046, 'years_active': 22}, {'cpc_group': 'G01N', 'total_patents': 387, 'best_year': 2006, 'best_year_count': 26, 'best_year_ema': 15.618590255115366, 'years_active': 34}, {'cpc_group': 'F16H', 'total_patents': 408, 'best_year': 2021, 'best_year_count': 33, 'best_year_ema': 15.558496848871837, 'years_active': 38}, {'cpc_group': 'Y10S', 'total_patents': 372, 'best_year': 2006, 'best_year_count': 25, 'best_year_ema': 13.432065549635661, 'years_active': 42}, {'cpc_group': 'G06F', 'total_patents': 295, 'best_year': 2008, 'best_year_count': 18, 'best_year_ema': 12.54966069046279, 'years_active': 32}, {'cpc_group': 'B01D', 'total_patents': 281, 'best_year': 2018, 'best_year_count': 12, 'best_year_ema': 11.848124157768797, 'years_active': 37}], 'cpc_groups_needing_definitions': ['H01L', 'Y10T', 'C10M', 'A61K', 'A61F', 'A61B', 'A61P', 'C04B', 'H04L', 'B29C', 'G11B', 'C07D', 'H04N', 'C07C', 'B60G', 'G01N', 'F16H', 'Y10S', 'G06F', 'B01D']}, 'var_functions.query_db:20': [{'symbol': 'A61K', 'titleFull': 'PREPARATIONS FOR MEDICAL, DENTAL OR TOILETRY PURPOSES'}, {'symbol': 'A61B', 'titleFull': 'DIAGNOSIS; SURGERY; IDENTIFICATION'}, {'symbol': 'A61F', 'titleFull': 'FILTERS IMPLANTABLE INTO BLOOD VESSELS; PROSTHESES; DEVICES PROVIDING PATENCY TO, OR PREVENTING COLLAPSING OF, TUBULAR STRUCTURES OF THE BODY, e.g. STENTS; ORTHOPAEDIC, NURSING OR CONTRACEPTIVE DEVICES; FOMENTATION; TREATMENT OR PROTECTION OF EYES OR EARS; BANDAGES, DRESSINGS OR ABSORBENT PADS; FIRST-AID KITS'}, {'symbol': 'A61P', 'titleFull': 'SPECIFIC THERAPEUTIC ACTIVITY OF CHEMICAL COMPOUNDS OR MEDICINAL PREPARATIONS'}, {'symbol': 'B01D', 'titleFull': 'SEPARATION'}, {'symbol': 'B29C', 'titleFull': 'SHAPING OR JOINING OF PLASTICS; SHAPING OF MATERIAL IN A PLASTIC STATE, NOT OTHERWISE PROVIDED FOR; AFTER-TREATMENT OF THE SHAPED PRODUCTS, e.g. REPAIRING'}, {'symbol': 'B60G', 'titleFull': 'VEHICLE SUSPENSION ARRANGEMENTS'}, {'symbol': 'C04B', 'titleFull': 'LIME, MAGNESIA; SLAG; CEMENTS; COMPOSITIONS THEREOF, e.g. MORTARS, CONCRETE OR LIKE BUILDING MATERIALS; ARTIFICIAL STONE; CERAMICS; REFRACTORIES; TREATMENT OF NATURAL STONE'}, {'symbol': 'C07D', 'titleFull': 'HETEROCYCLIC COMPOUNDS'}, {'symbol': 'C07C', 'titleFull': 'ACYCLIC OR CARBOCYCLIC COMPOUNDS'}, {'symbol': 'C10M', 'titleFull': 'LUBRICATING COMPOSITIONS; USE OF CHEMICAL SUBSTANCES EITHER ALONE OR AS LUBRICATING INGREDIENTS IN A LUBRICATING COMPOSITION'}, {'symbol': 'G11B', 'titleFull': 'INFORMATION STORAGE BASED ON RELATIVE MOVEMENT BETWEEN RECORD CARRIER AND TRANSDUCER'}, {'symbol': 'H04N', 'titleFull': 'PICTORIAL COMMUNICATION, e.g. TELEVISION'}, {'symbol': 'Y10T', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER US CLASSIFICATION'}, {'symbol': 'Y10S', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS'}, {'symbol': 'F16H', 'titleFull': 'GEARING'}, {'symbol': 'G01N', 'titleFull': 'INVESTIGATING OR ANALYSING MATERIALS BY DETERMINING THEIR CHEMICAL OR PHYSICAL PROPERTIES'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION'}, {'symbol': 'G06F', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}]}

exec(code, env_args)
