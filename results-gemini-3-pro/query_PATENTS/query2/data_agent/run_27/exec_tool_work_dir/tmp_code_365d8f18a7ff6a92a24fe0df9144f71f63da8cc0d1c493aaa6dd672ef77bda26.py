code = """import json
import re

with open(locals()['var_function-call-15606792083185834976'], 'r') as f:
    data = json.load(f)

# Date parser
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
    'Sept': 9
}

def parse_date(date_str):
    if not date_str:
        return None
    year_match = re.search(r'\d{4}', date_str)
    if not year_match:
        return None
    year = int(year_match.group(0))
    month = None
    for m_name, m_val in month_map.items():
        if m_name in date_str:
            month = m_val
            break
    if month is None:
        return None
    return year, month

total_loaded = len(data)
valid_grant_h2_2019 = 0
valid_filing = 0
cpc_found = 0

for entry in data:
    g_d = entry.get('grant_date', '')
    parsed_g = parse_date(g_d)
    if parsed_g:
        y, m = parsed_g
        if y == 2019 and m >= 7:
            valid_grant_h2_2019 += 1
            f_d = entry.get('filing_date', '')
            parsed_f = parse_date(f_d)
            if parsed_f:
                valid_filing += 1
                try:
                    cpcs = json.loads(entry.get('cpc', '[]'))
                    if cpcs:
                        cpc_found += 1
                except:
                    pass

print('__RESULT__:')
print(json.dumps({
    "total_loaded": total_loaded,
    "valid_grant_h2_2019": valid_grant_h2_2019,
    "valid_filing": valid_filing,
    "cpc_found": cpc_found
}))"""

env_args = {'var_function-call-1199938574274535269': 'file_storage/function-call-1199938574274535269.json', 'var_function-call-2446296467746717570': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-2588780312602812612': [{'symbol': 'H04L2025/03496', 'level': '16.0'}, {'symbol': 'H04L2025/0349', 'level': '16.0'}, {'symbol': 'H04L2025/03503', 'level': '16.0'}, {'symbol': 'H04Q2213/161', 'level': '8.0'}, {'symbol': 'H04Q2213/281', 'level': '8.0'}, {'symbol': 'H04Q2213/292', 'level': '8.0'}, {'symbol': 'H04', 'level': '4.0'}, {'symbol': 'H04Q2213/296', 'level': '8.0'}, {'symbol': 'H04Q2213/299', 'level': '8.0'}, {'symbol': 'H04Q2213/34', 'level': '8.0'}], 'var_function-call-1690403253581886321': [{'symbol': 'H04W', 'level': '5.0'}], 'var_function-call-3298910611970813522': [{'len': '3', 'cnt': '137'}], 'var_function-call-7172290236493635481': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.', 'cpc': '[\n  {\n    "code": "E06B1/702",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.', 'cpc': '[\n  {\n    "code": "A61Q5/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K8/355",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61Q5/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61K8/355",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.', 'cpc': '[\n  {\n    "code": "F16F13/14",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/14",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16F13/20",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.', 'cpc': '[\n  {\n    "code": "F01D25/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02C6/12",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F05D2220/40",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02B37/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F01D25/12",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F05D2240/51",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F05D2260/232",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02T10/12",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.', 'cpc': '[\n  {\n    "code": "H01J37/32724",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32522",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32724",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32522",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32724",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01J37/32522",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01L23/427",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-15606792083185834976': 'file_storage/function-call-15606792083185834976.json', 'var_function-call-17533103393791133462': {'yearly_winners': [{'year': 2007, 'cpc': 'B29', 'ema': 1.0}, {'year': 2008, 'cpc': 'B29', 'ema': 0.9}, {'year': 2009, 'cpc': 'B29', 'ema': 0.81}, {'year': 2010, 'cpc': 'B29', 'ema': 0.7290000000000001}, {'year': 2011, 'cpc': 'B29', 'ema': 0.6561000000000001}, {'year': 2012, 'cpc': 'B29', 'ema': 0.6904900000000002}, {'year': 2013, 'cpc': 'B29', 'ema': 0.6214410000000001}, {'year': 2014, 'cpc': 'B29', 'ema': 0.5592969000000001}, {'year': 2015, 'cpc': 'B29', 'ema': 0.5033672100000001}, {'year': 2016, 'cpc': 'B29', 'ema': 0.4530304890000001}, {'year': 2017, 'cpc': 'B29', 'ema': 0.4077274401000001}, {'year': 2018, 'cpc': 'G01', 'ema': 0.47876784401000005}], 'cpc_best_years': {'B29': 2007, 'G01': 2018}, 'unique_cpcs': ['B29', 'G01']}, 'var_function-call-10730708656171422675': [['dated 21st November 2019', [2019, 11], '16th of July, 2007', [2007, 7]], ['5th of December, 2019', [2019, 12], 'dated 14th October 2010', [2010, 10]], ['22nd of August, 2019', [2019, 8], 'July 21st, 2014', [2014, 7]], ['September the 19th, 2019', [2019, 9], 'on October 29th, 2015', [2015, 10]], ['17th of October, 2019', [2019, 10], 'on August 8th, 2014', [2014, 8]]]}

exec(code, env_args)
