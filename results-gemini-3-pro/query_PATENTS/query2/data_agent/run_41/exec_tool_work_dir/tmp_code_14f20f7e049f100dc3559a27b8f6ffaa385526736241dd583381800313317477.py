code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-10833735353448938107']
with open(file_path, 'r') as f:
    data = json.load(f)

def parse_date(date_str):
    if not date_str: return None
    s = date_str.lower()
    y_match = re.search(r'(19|20)\d{2}', s)
    if not y_match: return None
    year = int(y_match.group(0))
    
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
        'sept': 9
    }
    mon = 1
    found = False
    for m, v in months.items():
        if m in s:
            mon = v
            found = True
            break
    if not found: return None
    return pd.Timestamp(year=year, month=mon, day=1)

filtered_rows = []
for p in data:
    p_info = p.get('Patents_info', '')
    if 'DE-' not in p_info and 'Germany' not in p_info:
        continue
        
    g_date = parse_date(p.get('grant_date', ''))
    if not g_date: continue
    if not (g_date.year == 2019 and g_date.month >= 7):
        continue
        
    f_date = parse_date(p.get('filing_date', ''))
    if not f_date: continue
    filing_year = f_date.year
    
    try:
        cpc_items = json.loads(p.get('cpc', '[]'))
    except:
        continue
        
    codes = set()
    for item in cpc_items:
        c = item.get('code', '')
        if '/' in c:
            mg = c.split('/')[0] + '/00'
            codes.add(mg)
            
    for c in codes:
        filtered_rows.append({'cpc': c, 'year': filing_year})

df = pd.DataFrame(filtered_rows)

if df.empty:
    print('__RESULT__:')
    print('[]')
else:
    counts = df.groupby(['cpc', 'year']).size().reset_index(name='count')
    
    results = []
    for g in counts['cpc'].unique():
        g_data = counts[counts['cpc'] == g].sort_values('year')
        if g_data.empty: continue
        
        min_y = int(g_data['year'].min())
        max_y = int(g_data['year'].max())
        
        all_years = pd.DataFrame({'year': range(min_y, max_y + 1)})
        merged = pd.merge(all_years, g_data, on='year', how='left').fillna(0)
        
        merged['ema'] = merged['count'].ewm(alpha=0.1, adjust=False).mean()
        
        best_idx = merged['ema'].idxmax()
        best_year = int(merged.loc[best_idx, 'year'])
        max_ema = float(merged.loc[best_idx, 'ema'])
        
        results.append({'cpc': g, 'best_year': best_year, 'max_ema': max_ema})
        
    results_df = pd.DataFrame(results).sort_values('max_ema', ascending=False)
    top_10 = results_df.head(10).to_dict(orient='records')
    
    print('__RESULT__:')
    print(json.dumps(top_10))"""

env_args = {'var_function-call-9074214398255594628': 'file_storage/function-call-9074214398255594628.json', 'var_function-call-11188452242720001348': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'cpc': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 7th October 2004', 'filing_date': 'dated 9th April 2003'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'cpc': '[\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'grant_date': '2006 on Apr 27th', 'filing_date': '18th of April, 2005'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'cpc': '[\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Nov 29th, 2007', 'filing_date': '2006, May 11th'}], 'var_function-call-12491615548516024427': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-7357196505551979428': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-18237947535018481639': [], 'var_function-call-2107829008354905422': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-10763119139085470634': [{'symbol': 'A01H', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}], 'var_function-call-12316160109210262569': [{'symbol': 'C13B50/00', 'titleFull': 'Sugar products, e.g. powdered, lump or liquid sugar; Working-up of sugar'}, {'symbol': 'C13B40/00', 'titleFull': 'Drying sugar'}, {'symbol': 'C13B99/00', 'titleFull': 'Subject matter not provided for in other groups of this subclass'}, {'symbol': 'C13B45/00', 'titleFull': 'Cutting machines specially adapted for sugar'}, {'symbol': 'C21B3/00', 'titleFull': 'General features in the manufacture of pig-iron'}], 'var_function-call-9041542466039756436': [{'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING'}], 'var_function-call-8684987341689648468': [{'symbol': 'C01B33/00', 'level': '7.0', 'titleFull': 'Silicon; Compounds thereof'}], 'var_function-call-796533376235459668': [{'symbol': 'H01M10/00', 'level': '7.0', 'titleFull': 'Secondary cells; Manufacture thereof'}], 'var_function-call-10833735353448938107': 'file_storage/function-call-10833735353448938107.json', 'var_function-call-15608670009252843561': [], 'var_function-call-12859489019716582260': [{'p_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'g_date': '14th Mar 2019'}, {'p_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'g_date': 'dated 21st November 2019'}, {'p_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'g_date': 'Mar 21st, 2019'}, {'p_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'g_date': '5th of December, 2019'}, {'p_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'g_date': '22nd of August, 2019'}], 'var_function-call-13532997939702611579': {'total': 73, 'de_filter': 68, 'grant_date_parsed': 0, 'h2_2019': 0, 'filing_date_parsed': 0, 'cpc_parsed': 0, 'rows_generated': 0}, 'var_function-call-1944981007828817298': [{'date': '14th Mar 2019', 'status': 'OK'}, {'date': 'dated 21st November 2019', 'status': 'OK'}, {'date': 'Mar 21st, 2019', 'status': 'OK'}, {'date': '5th of December, 2019', 'status': 'OK'}, {'date': '22nd of August, 2019', 'status': 'OK'}]}

exec(code, env_args)
