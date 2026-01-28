code = """import json

# Load the CPC codes from previous result
cpc_data = locals()['var_functions.execute_python:18']
cpc_codes = cpc_data['cpc_level4_codes']

print('Number of CPC level 4 codes to analyze: ' + str(len(cpc_codes)))
print('Sample codes: ' + str(cpc_codes[:10]))

# Build a query to get historical data for these CPC codes
# We need to query for all years to calculate EMA
# Let's query for patents with these CPC codes from Germany

# Build WHERE clause for CPC codes
cpc_where_clauses = []
for code in cpc_codes:
    main_class = code.split('/')[0]
    # Match codes starting with the level 4 pattern
    pattern = main_class + '/' + code.split('/')[1][:2] + '%'
    cpc_where_clauses.append("cpc LIKE '%\"code\": \"" + pattern + "%'")

# Combine with OR
cpc_where = ' OR '.join(cpc_where_clauses)
query = """
SELECT 
    Patents_info,
    grant_date,
    cpc,
    CASE 
        WHEN grant_date LIKE '%2010%' THEN 2010
        WHEN grant_date LIKE '%2011%' THEN 2011
        WHEN grant_date LIKE '%2012%' THEN 2012
        WHEN grant_date LIKE '%2013%' THEN 2013
        WHEN grant_date LIKE '%2014%' THEN 2014
        WHEN grant_date LIKE '%2015%' THEN 2015
        WHEN grant_date LIKE '%2016%' THEN 2016
        WHEN grant_date LIKE '%2017%' THEN 2017
        WHEN grant_date LIKE '%2018%' THEN 2018
        WHEN grant_date LIKE '%2019%' THEN 2019
        WHEN grant_date LIKE '%2020%' THEN 2020
        ELSE NULL
    END as grant_year
FROM publicationinfo 
WHERE Patents_info LIKE '%DE-%' 
    AND (""" + cpc_where + ")
    AND grant_year IS NOT NULL
ORDER BY grant_year
"""

print('Query built for historical data')
print('__RESULT__:')
print(json.dumps({'query': query, 'cpc_count': len(cpc_codes)}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['cpc_definition'], 'var_functions.execute_python:18': {'cpc_counts': {'B41F21/10': 1, 'B41F22/00': 1, 'B41F21/00': 1, 'F02D41/30': 1, 'F02D41/20': 3, 'F02M65/00': 1, 'F02D41/00': 2, 'F02M59/10': 2, 'F02M55/04': 2, 'F02M59/44': 2, 'F02M59/06': 2, 'F04B53/00': 2, 'F02M59/36': 2, 'G01D11/24': 1, 'B23K1/00': 1, 'B63B21/50': 1, 'H04W72/21': 3, 'H04W72/56': 3, 'H04L5/00': 4, 'H04L1/16': 4, 'H04W52/02': 12, 'H04L1/18': 6, 'H04W72/04': 3, 'H04W76/28': 1, 'Y02D30/70': 2, 'B66C23/80': 1, 'E02F9/08': 1, 'B60S9/10': 1, 'F02D15/00': 1, 'F02D13/06': 1, 'Y02T10/12': 1, 'A61F5/14': 2, 'A61F5/01': 4, 'A43B17/00': 2, 'A43B7/20': 2, 'A43B13/22': 1, 'F24B5/02': 3, 'F23L15/04': 3, 'F23L1/00': 3, 'F23B60/00': 1, 'F23B50/12': 3, 'F23N1/02': 1, 'Y02E20/34': 1, 'H01R35/02': 1, 'B64D11/06': 1, 'H01R2201/26': 2, 'H01R24/60': 1, 'H01R13/63': 1, 'H01R35/04': 1, 'B60R16/02': 1, 'F02N2200/02': 2, 'F02N2300/20': 2, 'F02N11/08': 1, 'F02N11/04': 1, 'B60K6/48': 1, 'B60W30/19': 1, 'F02N11/00': 1, 'Y02T10/62': 1, 'Y02T10/40': 1, 'C04B2235/96': 2, 'C04B2235/77': 2, 'C04B2235/72': 2, 'C04B2235/66': 6, 'C04B2235/65': 6, 'C04B2235/54': 4, 'C04B2235/44': 2, 'C04B2235/32': 8, 'C04B35/64': 6, 'C04B35/62': 2, 'C04B35/54': 2, 'C04B35/51': 2, 'C09K11/77': 2, 'C04B40/00': 1, 'B29C49/42': 1, 'B29C2049/58': 7, 'B29C2049/42': 2, 'B29C49/06': 2, 'B29C49/58': 2, 'B29C2949/07': 1, 'G02B15/16': 1, 'A61B1/00': 3, 'G02B15/15': 2, 'G02B13/02': 1, 'G02B23/24': 5, 'G02B13/18': 1, 'G02B15/14': 2, 'Y10T70/70': 2, 'G07C9/00': 2, 'B29C2045/56': 2, 'B29D99/00': 1, 'H01H9/02': 2, 'B29C45/56': 2, 'H01H2009/18': 2, 'E05B19/00': 1, 'F16H37/04': 2, 'F16H2200/00': 2, 'F16H3/00': 1, 'E02F3/76': 2, 'E02F9/00': 2, 'E02F3/96': 1, 'F42B3/00': 2, 'F41H11/16': 2}, 'total_patents': 18, 'cpc_level4_codes': ['B41F21/10', 'B41F22/00', 'B41F21/00', 'F02D41/30', 'F02D41/20', 'F02M65/00', 'F02D41/00', 'F02M59/10', 'F02M55/04', 'F02M59/44', 'F02M59/06', 'F04B53/00', 'F02M59/36', 'G01D11/24', 'B23K1/00', 'B63B21/50', 'H04W72/21', 'H04W72/56', 'H04L5/00', 'H04L1/16', 'H04W52/02', 'H04L1/18', 'H04W72/04', 'H04W76/28', 'Y02D30/70', 'B66C23/80', 'E02F9/08', 'B60S9/10', 'F02D15/00', 'F02D13/06', 'Y02T10/12', 'A61F5/14', 'A61F5/01', 'A43B17/00', 'A43B7/20', 'A43B13/22', 'F24B5/02', 'F23L15/04', 'F23L1/00', 'F23B60/00', 'F23B50/12', 'F23N1/02', 'Y02E20/34', 'H01R35/02', 'B64D11/06', 'H01R2201/26', 'H01R24/60', 'H01R13/63', 'H01R35/04', 'B60R16/02', 'F02N2200/02', 'F02N2300/20', 'F02N11/08', 'F02N11/04', 'B60K6/48', 'B60W30/19', 'F02N11/00', 'Y02T10/62', 'Y02T10/40', 'C04B2235/96', 'C04B2235/77', 'C04B2235/72', 'C04B2235/66', 'C04B2235/65', 'C04B2235/54', 'C04B2235/44', 'C04B2235/32', 'C04B35/64', 'C04B35/62', 'C04B35/54', 'C04B35/51', 'C09K11/77', 'C04B40/00', 'B29C49/42', 'B29C2049/58', 'B29C2049/42', 'B29C49/06', 'B29C49/58', 'B29C2949/07', 'G02B15/16', 'A61B1/00', 'G02B15/15', 'G02B13/02', 'G02B23/24', 'G02B13/18', 'G02B15/14', 'Y10T70/70', 'G07C9/00', 'B29C2045/56', 'B29D99/00', 'H01H9/02', 'B29C45/56', 'H01H2009/18', 'E05B19/00', 'F16H37/04', 'F16H2200/00', 'F16H3/00', 'E02F3/76', 'E02F9/00', 'E02F3/96', 'F42B3/00', 'F41H11/16']}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
