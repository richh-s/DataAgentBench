code = """import json
import pandas as pd
import re

file_path = locals()['var_function-call-13601185424003768990']
with open(file_path, 'r') as f:
    data = json.load(f)

stats = {"total_rows": len(data)}

def parse_date_str(date_str):
    if not date_str:
        return None
    clean_str = date_str.lower().replace('dated', '').replace('on', '').replace('the', '').replace(',', '').strip()
    try:
        return pd.to_datetime(clean_str)
    except:
        match = re.search(r'\d{4}', clean_str)
        if match:
            return pd.to_datetime(match.group(0), format='%Y')
        return None

start_date = pd.Timestamp('2019-07-01')
end_date = pd.Timestamp('2019-12-31')

cnt_grant = 0
cnt_filing = 0
cnt_cpc = 0
sample_codes = set()

for row in data:
    g_date = parse_date_str(row.get('grant_date'))
    if g_date and start_date <= g_date <= end_date:
        cnt_grant += 1
        f_date = parse_date_str(row.get('filing_date'))
        if f_date:
            cnt_filing += 1
            cpc_json = row.get('cpc')
            if cpc_json:
                try:
                    cpc_list = json.loads(cpc_json)
                    found = False
                    for item in cpc_list:
                        code = item.get('code', '')
                        if len(code) >= 3:
                            sample_codes.add(code[:3])
                            found = True
                    if found:
                        cnt_cpc += 1
                except:
                    pass

stats["rows_2H_2019"] = cnt_grant
stats["rows_with_filing"] = cnt_filing
stats["rows_with_cpc"] = cnt_cpc
stats["sample_codes"] = list(sample_codes)[:10]

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-16016236543642685128': 'file_storage/function-call-16016236543642685128.json', 'var_function-call-16016236543642684803': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-13561635954094791069': [{'cpc': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 7th October 2004', 'filing_date': 'dated 9th April 2003', 'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}], 'var_function-call-13561635954094789046': [{'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B13/00', 'level': '7.0', 'titleFull': 'Ploughs or like machines for special purposes ; Ditch diggers, trench ploughs, forestry ploughs, ploughs for land or marsh reclamation'}, {'symbol': 'A01B35/00', 'level': '7.0', 'titleFull': 'Other machines for working soil not specially adapted for working soil on which crops are growing'}, {'symbol': 'A01B59/00', 'level': '7.0', 'titleFull': 'Devices specially adapted for connection between animals or tractors and agricultural machines or implements'}, {'symbol': 'A01B67/00', 'level': '7.0', 'titleFull': 'Devices for controlling the tractor motor by resistance of tools'}], 'var_function-call-317795769849267931': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-16573650118009255803': [{'symbol': 'H', 'level': '2.0'}, {'symbol': 'H01', 'level': '4.0'}, {'symbol': 'H01R', 'level': '5.0'}, {'symbol': 'H01R13/631', 'level': '10.0'}], 'var_function-call-13601185424003768990': 'file_storage/function-call-13601185424003768990.json', 'var_function-call-14579850432442259947': [{'code': 'H04', 'max_ema': 2.0, 'best_year': 2015}, {'code': 'Y02', 'max_ema': 1.0, 'best_year': 2015}, {'code': 'A61', 'max_ema': 1.0, 'best_year': 2016}, {'code': 'A43', 'max_ema': 1.0, 'best_year': 2016}, {'code': 'F04', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'F05', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'F01', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'G01', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'F16', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'H02', 'max_ema': 1.0, 'best_year': 2009}, {'code': 'H03', 'max_ema': 1.0, 'best_year': 2015}, {'code': 'F41', 'max_ema': 1.0, 'best_year': 2012}, {'code': 'F42', 'max_ema': 1.0, 'best_year': 2012}, {'code': 'E02', 'max_ema': 1.0, 'best_year': 2012}], 'var_function-call-9662522869629261925': 'debug done'}

exec(code, env_args)
