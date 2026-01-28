code = """import json
import re
from collections import defaultdict, Counter

# Load all German patents
result_file = locals()['var_functions.query_db:22']
with open(result_file, 'r') as f:
    german_patents = json.load(f)

# Extract yearly data for CPC level 4 codes
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
year_pattern = re.compile(r'(\d{4})')

for patent in german_patents:
    try:
        grant_date = patent['grant_date']
        year_match = year_pattern.search(grant_date)
        if not year_match:
            continue
        year = int(year_match.group(1))
        
        cpc_list = json.loads(patent['cpc'])
        for cpc in cpc_list:
            code = cpc['code']
            if '/' not in code:
                continue
            
            main_part, subgroup = code.split('/')
            if len(main_part) <= 4:
                continue
                
            section = main_part[0]
            class_num = main_part[1:3]
            subclass = main_part[3] if len(main_part) > 3 else ''
            group_digits = main_part[4:]
            
            level4_code = f"{section}{class_num}{subclass}{group_digits}"
            cpc_yearly_counts[level4_code][year] += 1
    except:
        continue

# Identify codes from H2 2019
h2_2019_codes = set()
for patent in german_patents:
    try:
        grant_date = patent['grant_date']
        year_match = year_pattern.search(grant_date)
        if not year_match or int(year_match.group(1)) != 2019:
            continue
            
        grant_date_lower = grant_date.lower()
        if any(month in grant_date_lower for month in ['july', 'august', 'september', 'october', 'november', 'december']):
            cpc_list = json.loads(patent['cpc'])
            for cpc in cpc_list:
                code = cpc['code']
                if '/' not in code:
                    continue
                
                main_part, subgroup = code.split('/')
                if len(main_part) <= 4:
                    continue
                
                section = main_part[0]
                class_num = main_part[1:3]
                subclass = main_part[3] if len(main_part) > 3 else ''
                group_digits = main_part[4:]
                
                level4_code = f"{section}{class_num}{subclass}{group_digits}"
                h2_2019_codes.add(level4_code)
    except:
        continue

# Calculate EMA for all H2 2019 codes
smoothing_factor = 0.1
ema_results = []

for cpc_code in h2_2019_codes:
    yearly_counts = cpc_yearly_counts[cpc_code]
    if not yearly_counts:
        continue
    
    years = sorted(yearly_counts.keys())
    if len(years) < 2:
        continue
    
    # Calculate EMA
    emas = {}
    prev_ema = None
    
    for year in years:
        count = yearly_counts[year]
        if prev_ema is None:
            ema = count
        else:
            ema = (count * smoothing_factor) + (prev_ema * (1 - smoothing_factor))
        
        emas[year] = ema
        prev_ema = ema
    
    # Find best year
    best_year = max(emas.keys(), key=lambda y: emas[y])
    
    # Create CPC group code for title lookup
    section = cpc_code[0]
    class_num = cpc_code[1:3]
    subclass = cpc_code[3]
    group = cpc_code[4:]
    cpc_group_code = f"{section}{class_num}{subclass}/{group}"
    
    # Get actual CPC symbol for title lookup (e.g., "B29C45/00")
    lookup_symbol = f"{section}{class_num}{subclass}/00"
    
    ema_results.append({
        'cpc_level4': cpc_code,
        'cpc_group_code': cpc_group_code,
        'lookup_symbol': lookup_symbol,
        'best_year': best_year,
        'best_year_ema': round(emas[best_year], 3),
        'patents_h2_2019': yearly_counts.get(2019, 0),
        'year_range': f"{min(years)}-{max(years)}"
    })

# Sort by EMA descending
ema_results.sort(key=lambda x: x['best_year_ema'], reverse=True)

print(f"__RESULT__:")
print(json.dumps({
    "candidates_for_analysis": len(h2_2019_codes),
    "qualified_for_ema": len(ema_results),
    "ranked_results": ema_results,
    "sample_codes": list(h2_2019_codes)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_patents': 18, 'first_patent': {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 21st November 2019'}, 'sample_cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, 'var_functions.execute_python:14': {'total_level4_codes': 219, 'unique_level4_codes': 69, 'top_level4_codes': {'C04B2235': 32, 'H04W52': 12, 'C04B35': 12, 'H04L1': 10, 'H04W72': 9, 'B29C2049': 9, 'F02M59': 8, 'F02D41': 6, 'A61F5': 6, 'B29C49': 5}, 'all_level4_codes': ['B41F21', 'B41F22', 'F02D41', 'F02M65', 'F02M59', 'F02M55', 'F04B53', 'G01D11', 'B23K1', 'B63B21', 'H04W72', 'H04L5', 'H04L1', 'H04W52', 'H04W76', 'Y02D30', 'B66C23', 'E02F9', 'B60S9', 'F02D15', 'F02D13', 'Y02T10', 'A61F5', 'A43B17', 'A43B7', 'A43B13', 'F24B5', 'F23L15', 'F23L1', 'F23B60', 'F23B50', 'F23N1', 'Y02E20', 'H01R35', 'B64D11', 'H01R2201', 'H01R24', 'H01R13', 'B60R16', 'F02N2200', 'F02N2300', 'F02N11', 'B60K6', 'B60W30', 'C04B2235', 'C04B35', 'C09K11', 'C04B40', 'B29C49', 'B29C2049', 'B29C2949', 'G02B15', 'A61B1', 'G02B13', 'G02B23', 'Y10T70', 'G07C9', 'B29C2045', 'B29D99', 'H01H9', 'B29C45', 'H01H2009', 'E05B19', 'F16H37', 'F16H2200', 'F16H3', 'E02F3', 'F42B3', 'F41H11']}, 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:18': {'total_patents_processed': 510, 'cpc_level4_groups': 1038, 'year_range': '2010 - 2019', 'sample_cpc_groups': ['B26B5', 'B64G1', 'F16C33', 'F16C2326', 'F16C19', 'F16C32', 'G01D5', 'B60N3', 'B60N2', 'F41H7'], 'sample_yearly_counts': {'B26B5': {'2010': 4}, 'B64G1': {'2016': 6}, 'F16C33': {'2016': 2, '2014': 2, '2010': 2, '2019': 3, '2013': 9}}}, 'var_functions.execute_python:20': {'h2_2019_patents': 21, 'unique_cpc_level4_groups_in_h2_2019': 75, 'sample_cpc_groups': ['G07C9', 'H04W72', 'F23B50', 'G02B23', 'G08B19', 'H01R35', 'H04L1', 'F02D15', 'F04B53', 'F23N1', 'B41F21', 'B41F22', 'A43B13', 'F02D41', 'F02M65', 'B60S9', 'F24B5', 'F41H11', 'F16H37', 'Y02T10']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'h2_2019_patents_count': 5, 'unique_cpc_level4_codes': 21, 'sample_cpc_codes': ['G08B17', 'H01H2009', 'B41F21', 'B41F22', 'F02N2200', 'B29D99', 'B60K6', 'F02N11', 'B60W30', 'F02N2300', 'H01H9', 'F02M55', 'G07C9', 'F04B53', 'F02M59', 'E05B19', 'B29C45', 'B29C2045', 'Y02T10', 'Y10T70']}, 'var_functions.execute_python:26': {'cpc_codes_in_h2_2019': 21, 'results_with_ema': 7, 'top_10_ema_results': [{'cpc_level4': 'F02N2200', 'cpc_group_code': 'F02N/2200', 'best_year': 2019, 'best_year_ema': 2, 'total_years': 2, 'recent_year_count': 2}, {'cpc_level4': 'F04B53', 'cpc_group_code': 'F04B/53', 'best_year': 2017, 'best_year_ema': 2, 'total_years': 2, 'recent_year_count': 2}, {'cpc_level4': 'B29C45', 'cpc_group_code': 'B29C/45', 'best_year': 2019, 'best_year_ema': 1.8155, 'total_years': 5, 'recent_year_count': 2}, {'cpc_level4': 'Y02T10', 'cpc_group_code': 'Y02T/10', 'best_year': 2019, 'best_year_ema': 1.3710000000000002, 'total_years': 5, 'recent_year_count': 3}, {'cpc_level4': 'B29C2045', 'cpc_group_code': 'B29C/2045', 'best_year': 2019, 'best_year_ema': 1.1, 'total_years': 2, 'recent_year_count': 2}, {'cpc_level4': 'B29D99', 'cpc_group_code': 'B29D/99', 'best_year': 1995, 'best_year_ema': 1, 'total_years': 2, 'recent_year_count': 1}, {'cpc_level4': 'E05B19', 'cpc_group_code': 'E05B/19', 'best_year': 2006, 'best_year_ema': 1, 'total_years': 2, 'recent_year_count': 1}], 'all_level4_codes': ['G08B19', 'F02M55', 'B60W30', 'B29C2045', 'B29C45', 'F02N11', 'F02M59', 'F02N2200', 'G07C9', 'G08B17', 'F02N2300', 'B41F22', 'Y10T70', 'F04B53', 'B41F21', 'B29D99', 'B60K6', 'E05B19', 'H01H2009', 'H01H9', 'Y02T10']}, 'var_functions.query_db:30': [{'symbol': 'B29C45/00', 'title_full': 'Injection moulding, i.e. forcing the required volume of moulding material through a nozzle into a closed mould; Apparatus therefor', 'level': '7.0'}, {'symbol': 'B41F22/00', 'title_full': 'Means preventing smudging of machine parts or printed articles', 'level': '7.0'}, {'symbol': 'B41F21/00', 'title_full': 'Devices for conveying sheets through printing apparatus or machines', 'level': '7.0'}, {'symbol': 'B60K6/00', 'title_full': 'Arrangement or mounting of plural diverse prime-movers for mutual or common propulsion, e.g. hybrid propulsion systems comprising electric motors and internal combustion engines ; Control systems therefor, i.e. systems controlling two or more prime movers, or controlling one of these prime movers and any of the transmission, drive or drive units Informative references: mechanical gearings with secondary electric drive F16H3/72; arrangements for handling mechanical energy structurally associated with the dynamo-electric machine H02K7/00; machines comprising structurally interrelated motor and generator parts H02K51/00; dynamo-electric machines not otherwise provided for in H02K see H02K99/00', 'level': '7.0'}, {'symbol': 'B29D99/00', 'title_full': 'Subject matter not provided for in other groups of this subclass', 'level': '7.0'}, {'symbol': 'B60W30/00', 'title_full': 'Purposes of road vehicle drive control systems not related to the control of a particular sub-unit, e.g. of systems using conjoint control of vehicle sub-units', 'level': '7.0'}, {'symbol': 'Y10T70/00', 'title_full': 'Locks', 'level': '7.0'}, {'symbol': 'E05B19/00', 'title_full': 'Keys; Accessories therefor', 'level': '7.0'}, {'symbol': 'F02M55/00', 'title_full': 'Fuel-injection apparatus characterised by their fuel conduits or their venting means; Arrangements of conduits between fuel tank and pump F02M37/00', 'level': '7.0'}, {'symbol': 'F02M59/00', 'title_full': 'Pumps specially adapted for fuel-injection and not provided for in groups F02M39/00 -F02M57/00, e.g. rotary cylinder-block type of pumps', 'level': '7.0'}, {'symbol': 'F02N2200/00', 'title_full': 'Parameters used for control of starting apparatus', 'level': '7.0'}, {'symbol': 'F02N2300/00', 'title_full': 'Control related aspects of engine starting', 'level': '7.0'}, {'symbol': 'F02N11/00', 'title_full': 'Starting of engines by means of electric motors', 'level': '7.0'}, {'symbol': 'F04B53/00', 'title_full': 'Component parts, details or accessories not provided for in, or of interest apart from, groups F04B1/00\xa0-\xa0F04B23/00 or F04B39/00\xa0-\xa0F04B47/00', 'level': '7.0'}, {'symbol': 'G07C9/00', 'title_full': 'Individual registration on entry or exit', 'level': '7.0'}, {'symbol': 'G08B17/00', 'title_full': 'Fire alarms; Alarms responsive to explosion', 'level': '7.0'}, {'symbol': 'G08B19/00', 'title_full': 'Alarms responsive to two or more different undesired or abnormal conditions, e.g. burglary and fire, abnormal temperature and abnormal rate of flow', 'level': '7.0'}, {'symbol': 'H01H9/00', 'title_full': 'Details of switching devices, not covered by groups H01H1/00\xa0-\xa0H01H7/00', 'level': '7.0'}, {'symbol': 'Y02T10/00', 'title_full': 'Road transport of goods or passengers', 'level': '7.0'}], 'var_functions.execute_python:34': {'cpc_definitions_loaded': 19, 'sample_titles': {'B29C45/00': 'Injection moulding, i.e. forcing the required volume of moulding material through a nozzle into a cl', 'B41F22/00': 'Means preventing smudging of machine parts or printed articles', 'B41F21/00': 'Devices for conveying sheets through printing apparatus or machines'}}}

exec(code, env_args)
