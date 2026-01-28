code = """import json
from collections import defaultdict

# Load data from query result
file_path = locals()['var_functions.query_db:46']
with open(file_path, 'r') as f:
    data = json.load(f)

# Analyze German patents granted in second half 2019
cpc_monthly = defaultdict(lambda: defaultdict(int))
total_patents = 0

for rec in data:
    # Check grant date for second half 2019
    grant_date = rec.get('grant_date', '').lower()
    month = 0
    
    # Determine month
    if 'jul' in grant_date:
        month = 7
    elif 'aug' in grant_date:
        month = 8
    elif 'sep' in grant_date:
        month = 9
    elif 'oct' in grant_date:
        month = 10
    elif 'nov' in grant_date:
        month = 11
    elif 'dec' in grant_date:
        month = 12
    else:
        continue
    
    # Parse CPC codes
    cpc_str = rec.get('cpc', '')
    if not cpc_str:
        continue
    
    try:
        cpc_codes = json.loads(cpc_str)
        for cpc in cpc_codes:
            code = cpc.get('code', '')
            # Extract level 4 (format: XXXXXX... -> first 6 chars: XXXXXX)
            if code and len(code) >= 6 and '/' in code:
                level4 = code[:6]
                cpc_monthly[level4][month] += 1
                total_patents += 1
    except:
        continue

# Calculate EMA (alpha=0.1)
alpha = 0.1
ema_results = []

for cpc_code, months in cpc_monthly.items():
    ema = None
    best_month = None
    best_ema = 0
    
    for m in range(7, 13):
        count = months.get(m, 0)
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        if ema > best_ema:
            best_ema = ema
            best_month = m
    
    # Only include if we had patents in at least 2 months
    if best_ema > 0 and len([c for c in months.values() if c > 0]) >= 2:
        ema_results.append({
            'cpc_code': cpc_code,
            'best_month': best_month,
            'ema_score': best_ema,
            'total_patents': sum(months.values())
        })

# Sort by EMA descending
ema_results.sort(key=lambda x: x['ema_score'], reverse=True)

# Take top results
top_results = ema_results[:20]

print('Processed', total_patents, 'patents')
print('Found', len(top_results), 'CPC groups with EMA data')
print('Top 5 CPC by EMA:')
for r in top_results[:5]:
    print(r['cpc_code'], 'EMA=%.2f' % r['ema_score'], 'Best Month=%d' % r['best_month'])

# Create query for CPC definitions
cpc_codes = [r['cpc_code'] for r in top_results]

# Build SQL query with LIKE patterns
sql_parts = []
for code in cpc_codes:
    # Add wildcard for CPC symbols
    sql_parts.append("symbol LIKE '{}%'".format(code))

query = "SELECT symbol, titleFull FROM cpc_definition WHERE level = 4 AND ({})".format(' OR '.join(sql_parts))

print('Generated SQL query for CPC definitions')
print('First 100 chars:', query[:100])

# Store results for next step
output = {
    'top_cpc_results': top_results,
    'sql_query': query
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'grant_date': '8th April 2019', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'grant_date': '2019, May 30th', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'grant_date': '22nd May 2019', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'grant_date': '2019 on Nov 14th', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:42': [], 'var_functions.list_db:44': ['cpc_definition'], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [{'cpc_code': 'G02B15', 'best_month': 7, 'ema_score': 5, 'total_patents': 5}, {'cpc_code': 'G02B23', 'best_month': 7, 'ema_score': 5, 'total_patents': 5}, {'cpc_code': 'C04B22', 'best_month': 12, 'ema_score': 3.2, 'total_patents': 32}, {'cpc_code': 'H01L23', 'best_month': 7, 'ema_score': 3, 'total_patents': 3}, {'cpc_code': 'A61B1/', 'best_month': 7, 'ema_score': 3, 'total_patents': 3}, {'cpc_code': 'B29C20', 'best_month': 8, 'ema_score': 2.7, 'total_patents': 11}, {'cpc_code': 'H01L29', 'best_month': 7, 'ema_score': 2, 'total_patents': 2}, {'cpc_code': 'G02B13', 'best_month': 7, 'ema_score': 2, 'total_patents': 2}, {'cpc_code': 'Y10T70', 'best_month': 7, 'ema_score': 2, 'total_patents': 2}, {'cpc_code': 'G07C9/', 'best_month': 7, 'ema_score': 2, 'total_patents': 2}, {'cpc_code': 'H01H9/', 'best_month': 7, 'ema_score': 2, 'total_patents': 2}, {'cpc_code': 'B29C45', 'best_month': 7, 'ema_score': 2, 'total_patents': 2}, {'cpc_code': 'H01H20', 'best_month': 7, 'ema_score': 2, 'total_patents': 2}, {'cpc_code': 'H04W52', 'best_month': 8, 'ema_score': 1.2000000000000002, 'total_patents': 12}, {'cpc_code': 'C04B35', 'best_month': 12, 'ema_score': 1.2000000000000002, 'total_patents': 12}], 'var_functions.query_db:52': [], 'var_functions.query_db:54': [{'symbol': 'G02B15/08', 'level': '10.0', 'titleFull': 'Optical objectives with means for varying the magnification by changing, adding, or subtracting a part of the objective, e.g. convertible objective by changing a part by changing the rear part'}, {'symbol': 'G02B15/06', 'level': '10.0', 'titleFull': 'Optical objectives with means for varying the magnification by changing, adding, or subtracting a part of the objective, e.g. convertible objective by changing a part by changing the front part'}, {'symbol': 'G02B15/12', 'level': '10.0', 'titleFull': 'Optical objectives with means for varying the magnification by changing, adding, or subtracting a part of the objective, e.g. convertible objective by adding a part, e.g. close-up attachment by adding telescopic attachments'}, {'symbol': 'G02B15/163', 'level': '10.0', 'titleFull': 'Optical objectives with means for varying the magnification by axial movement of one or more lenses or groups of lenses relative to the image plane for continuously varying the equivalent focal length of the objective with interdependent non-linearly related movements between one lens or lens group, and another lens or lens group having a first movable lens or lens group and a second movable lens or lens group, both in front of a fixed lens or lens group'}, {'symbol': 'G02B15/20', 'level': '10.0', 'titleFull': 'Optical objectives with means for varying the magnification by axial movement of one or more lenses or groups of lenses relative to the image plane for continuously varying the equivalent focal length of the objective with interdependent non-linearly related movements between one lens or lens group, and another lens or lens group having an additional movable lens or lens group for varying the objective focal length'}]}

exec(code, env_args)
