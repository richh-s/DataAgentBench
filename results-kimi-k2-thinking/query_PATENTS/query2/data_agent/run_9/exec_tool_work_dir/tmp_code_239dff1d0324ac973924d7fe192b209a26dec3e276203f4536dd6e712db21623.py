code = """import json
import re

# Load German patents data
result_path = locals()['var_functions.query_db:42']
with open(result_path, 'r') as f:
    all_patents = json.load(f)

# Helper functions
def get_year(date_str):
    if not date_str:
        return None
    match = re.search(r'\b(20\d{2})\b', str(date_str))
    return int(match.group(1)) if match else None

def is_second_half(date_str):
    if not date_str or '2019' not in str(date_str):
        return False
    return bool(re.search(r'(Jul|Aug|Sep|Oct|Nov|Dec)', str(date_str), re.IGNORECASE))

# Process patents
sh_2019_patents = []
cpc_yearly_counts = {}

for patent in all_patents:
    grant_date = patent.get('grant_date', '')
    year = get_year(grant_date)
    
    if year:
        cpc_data = patent.get('cpc', '')
        if cpc_data:
            try:
                cpc_list = json.loads(cpc_data)
                year_codes = set()
                
                for item in cpc_list:
                    code = item.get('code', '')
                    if code and '/' in code:
                        level4 = code.split('/')[0]
                        year_codes.add(level4)
                
                if year not in cpc_yearly_counts:
                    cpc_yearly_counts[year] = {}
                
                for code in year_codes:
                    cpc_yearly_counts[year][code] = cpc_yearly_counts[year].get(code, 0) + 1
            except:
                pass
    
    if year == 2019 and is_second_half(grant_date):
        sh_2019_patents.append(patent)

# Get results
years = sorted(cpc_yearly_counts.keys())
sh_2019_cpc_codes = set()

for patent in sh_2019_patents:
    cpc_data = patent.get('cpc', '')
    if cpc_data:
        try:
            cpc_list = json.loads(cpc_data)
            for item in cpc_list:
                code = item.get('code', '')
                if code and '/' in code:
                    sh_2019_cpc_codes.add(code.split('/')[0])
        except:
            pass

# Generate summary
summary = {
    'sh_2019_patents': len(sh_2019_patents),
    'years': years,
    'cpc_codes_sh_2019': len(sh_2019_cpc_codes),
    'cpc_yearly_counts': cpc_yearly_counts
}

if 2019 in cpc_yearly_counts:
    cpc_2019 = cpc_yearly_counts[2019]
    summary['cpc_2019_total'] = len(cpc_2019)
    summary['top_15_2019'] = sorted(cpc_2019.items(), key=lambda x: x[1], reverse=True)[:15]

print('Results: SH 2019=' + str(len(sh_2019_patents)) + ', Years=' + str(years))

print('__RESULT__:')
print(json.dumps(summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.', 'grant_date': 'Mar 19th, 2019', 'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.', 'grant_date': 'Mar 12th, 2019', 'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.', 'grant_date': '2019 on Jul 12th', 'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.', 'grant_date': 'on March 14th, 2019', 'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.', 'grant_date': 'July 8th, 2019', 'cpc': '[\n  {\n    "code": "F25B2339/047",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2400/061",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/20",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/52",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D17/0005",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02B30/18",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F24D2200/123",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.', 'grant_date': '8th April 2019', 'cpc': '[\n  {\n    "code": "G01N33/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/56977",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/572",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/39",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N2333/70539",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/55527",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70503",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C07K14/70539",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01N33/505",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K39/0011",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K2039/5158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.', 'grant_date': '2019, May 30th', 'cpc': '[\n  {\n    "code": "B60P1/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.', 'grant_date': '22nd May 2019', 'cpc': '[\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/182",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B61D3/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02T30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.', 'grant_date': '2019 on Nov 14th', 'cpc': '[\n  {\n    "code": "F16K17/192",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16L43/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': [{'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019', 'cpc': '[\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01R31/389",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.execute_python:16': {'total_patents': 34, 'top_cpc': [['C04B2235', 32], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['F02D41', 9], ['H04W72', 9], ['B29C2049', 9], ['F02M59', 8], ['A61F5', 6]]}, 'var_functions.list_db:18': ['cpc_definition'], 'var_functions.execute_python:20': ['B41F21', 'B41F22', 'F02D41', 'F02M65', 'F02M59', 'F02M55', 'F04B53', 'G01D11', 'B23K1', 'B63B21', 'H04W72', 'H04L5', 'H04L1', 'H04W52', 'H04W76', 'Y02D30', 'B66C23', 'E02F9', 'B60S9', 'F02D15', 'F02D13', 'Y02T10', 'F16C33', 'A47J37', 'A21C9', 'A61F5', 'A43B17', 'A43B7', 'A43B13', 'F24B5', 'F23L15', 'F23L1', 'F23B60', 'F23B50', 'F23N1', 'Y02E20', 'H01J49', 'G01M1', 'F05D2270', 'F04D29', 'F05D2260', 'F16F15', 'F01D5', 'H01R35', 'B64D11', 'H01R2201', 'H01R24', 'H01R13', 'B60R16', 'H01L23'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'patents_2019_sh': 34, 'years': [], 'total_cpc_codes': 0, 'codes_2019_sh': 115, 'top_cpc_2019': []}, 'var_functions.execute_python:38': {'sh_2019_count': 0, 'years': [], 'cpc_codes_2019': 0, 'codes_in_sh_2019': 0, 'top_cpc_2019': []}, 'var_functions.query_db:40': [{'grant_date': '14th Aug 2019'}, {'grant_date': '14th Mar 2019'}, {'grant_date': '17th of October, 2019'}, {'grant_date': '19th of June, 2019'}, {'grant_date': '2019 on Aug 8th'}, {'grant_date': '2019 on Jan 17th'}, {'grant_date': '2019 on Jul 4th'}, {'grant_date': '2019 on Mar 14th'}, {'grant_date': '2019 on Mar 28th'}, {'grant_date': '2019 on Mar 7th'}, {'grant_date': '2019 on Nov 7th'}, {'grant_date': '2019 on Oct 10th'}, {'grant_date': '2019 on Oct 17th'}, {'grant_date': '2019 on Oct 24th'}, {'grant_date': '2019, April 4th'}, {'grant_date': '2019, December 24th'}, {'grant_date': '2019, July 18th'}, {'grant_date': '2019, June 19th'}, {'grant_date': '2019, May 23rd'}, {'grant_date': '2019, May 29th'}, {'grant_date': '2019, October 2nd'}, {'grant_date': '21st of February, 2019'}, {'grant_date': '22nd August 2019'}, {'grant_date': '22nd of August, 2019'}, {'grant_date': '23rd May 2019'}, {'grant_date': '24th December 2019'}, {'grant_date': '26th September 2019'}, {'grant_date': '28th Feb 2019'}, {'grant_date': '28th March 2019'}, {'grant_date': '28th Nov 2019'}, {'grant_date': '2nd Oct 2019'}, {'grant_date': '31st January 2019'}, {'grant_date': '4th of April, 2019'}, {'grant_date': '5th of December, 2019'}, {'grant_date': '6th Jun 2019'}, {'grant_date': '6th of June, 2019'}, {'grant_date': '7th March 2019'}, {'grant_date': '7th of March, 2019'}, {'grant_date': 'Apr 25th, 2019'}, {'grant_date': 'April the 25th, 2019'}, {'grant_date': 'Aug 14th, 2019'}, {'grant_date': 'Aug 29th, 2019'}, {'grant_date': 'August the 14th, 2019'}, {'grant_date': 'August the 29th, 2019'}, {'grant_date': 'December 19th, 2019'}, {'grant_date': 'December 24th, 2019'}, {'grant_date': 'February 28th, 2019'}, {'grant_date': 'Jan 3rd, 2019'}, {'grant_date': 'January the 24th, 2019'}, {'grant_date': 'July the 18th, 2019'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
