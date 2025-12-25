code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-3949446733573800903'], 'r') as f:
    patents = json.load(f)

count_all = len(patents)
count_de = 0
count_h2_2019 = 0
count_valid = 0

from dateutil import parser
import datetime

start_date = datetime.datetime(2019, 7, 1)
end_date = datetime.datetime(2019, 12, 31)

for p in patents:
    # Check DE
    is_de = 'DE-' in p['Patents_info'] or 'Germany' in p['Patents_info'] or ' DE ' in p['Patents_info']
    if is_de:
        count_de += 1
    
    # Check Date
    try:
        g_date = parser.parse(p['grant_date'])
        is_h2_2019 = (start_date <= g_date <= end_date)
        if is_h2_2019:
            count_h2_2019 += 1
            if is_de:
                count_valid += 1
    except:
        pass

print(f"Total fetched: {count_all}")
print(f"DE patents (any date): {count_de}")
print(f"H2 2019 patents (any country): {count_h2_2019}")
print(f"Valid patents (DE + H2 2019): {count_valid}")"""

env_args = {'var_function-call-249731938256102390': 'file_storage/function-call-249731938256102390.json', 'var_function-call-17156139253207712376': 'file_storage/function-call-17156139253207712376.json', 'var_function-call-17156139253207714637': [{'Patents_info': 'VITTORI GIANFRANCO DE holds the FR patent filing (app. number FR-7811408-A), with publication number FR-2388575-B3.', 'grant_date': '1980 on Nov 14th', 'filing_date': '18th of April, 1978', 'cpc': '[\n  {\n    "code": "E01F9/627",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E04H12/32",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/685",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E04H12/32",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/627",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E01F9/685",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/40",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63C19/062",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/357",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63C19/062",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A63B57/40",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th', 'filing_date': '18th of April, 2005', 'cpc': '[\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K1/024",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G01K2207/02",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007', 'filing_date': '2006, May 11th', 'cpc': '[\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B5/103",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B65/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65B35/38",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B65B43/56",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B65G25/02",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th', 'filing_date': '30th June 2007', 'cpc': '[\n  {\n    "code": "H01F41/0233",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01F27/263",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017', 'filing_date': 'on August 3rd, 2000', 'cpc': '[\n  {\n    "code": "G01D5/34715",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01D5/36",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_function-call-3949446733573800408': 'file_storage/function-call-3949446733573800408.json', 'var_function-call-3949446733573800903': 'file_storage/function-call-3949446733573800903.json', 'var_function-call-9111100024939923774': [{'CPC Group Code': 'B29', 'Full Title': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'Best Year': 2007, 'Max EMA': 1.0}, {'CPC Group Code': 'F02', 'Full Title': 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS', 'Best Year': 2017, 'Max EMA': 0.2916541}, {'CPC Group Code': 'G01', 'Full Title': 'MEASURING; TESTING', 'Best Year': 2018, 'Max EMA': 0.29000000000000004}, {'CPC Group Code': 'H01', 'Full Title': 'ELECTRIC ELEMENTS', 'Best Year': 2018, 'Max EMA': 0.24174653401000004}, {'CPC Group Code': 'B60', 'Full Title': 'VEHICLES IN GENERAL', 'Best Year': 2018, 'Max EMA': 0.22465900000000003}, {'CPC Group Code': 'F04', 'Full Title': 'POSITIVE - DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS FOR LIQUIDS OR ELASTIC FLUIDS', 'Best Year': 2018, 'Max EMA': 0.22465900000000003}, {'CPC Group Code': 'F16', 'Full Title': 'ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL', 'Best Year': 2018, 'Max EMA': 0.21343969000000007}, {'CPC Group Code': 'A61', 'Full Title': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE', 'Best Year': 2016, 'Max EMA': 0.2}, {'CPC Group Code': 'G02', 'Full Title': 'OPTICS', 'Best Year': 2018, 'Max EMA': 0.18100000000000002}, {'CPC Group Code': 'Y02', 'Full Title': 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE', 'Best Year': 2017, 'Max EMA': 0.16561000000000003}]}

exec(code, env_args)
