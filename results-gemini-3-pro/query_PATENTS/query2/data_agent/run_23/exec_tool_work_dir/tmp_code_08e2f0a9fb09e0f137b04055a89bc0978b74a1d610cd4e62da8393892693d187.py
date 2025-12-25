code = """import json
import pandas as pd

# Previous results (top_results from call 14579850432442259947)
# I'll hardcode the valid codes and their stats from the previous output to ensure I have them available
# The previous output was:
prev_results = [
    {"code": "H04", "max_ema": 2.0, "best_year": 2015},
    {"code": "Y02", "max_ema": 1.0, "best_year": 2015},
    {"code": "A61", "max_ema": 1.0, "best_year": 2016},
    {"code": "A43", "max_ema": 1.0, "best_year": 2016},
    {"code": "F04", "max_ema": 1.0, "best_year": 2018},
    {"code": "F05", "max_ema": 1.0, "best_year": 2018},
    {"code": "F01", "max_ema": 1.0, "best_year": 2018},
    {"code": "G01", "max_ema": 1.0, "best_year": 2018},
    {"code": "F16", "max_ema": 1.0, "best_year": 2018},
    {"code": "H02", "max_ema": 1.0, "best_year": 2009},
    {"code": "H03", "max_ema": 1.0, "best_year": 2015},
    {"code": "F41", "max_ema": 1.0, "best_year": 2012},
    {"code": "F42", "max_ema": 1.0, "best_year": 2012},
    {"code": "E02", "max_ema": 1.0, "best_year": 2012}
]

# Titles from the query result
titles_list = locals()['var_function-call-2511582570902758343']
# Convert to dict
titles_map = {item['symbol']: item['titleFull'] for item in titles_list}

final_output = []
for item in prev_results:
    code = item['code']
    title = titles_map.get(code, "Unknown Title")
    final_output.append({
        "CPC Group Code": code,
        "Full Title": title,
        "Best Year": item['best_year'],
        "Max EMA": item['max_ema']
    })

# Sort by Max EMA descending, then Best Year descending (or Code)
final_output.sort(key=lambda x: (x['Max EMA'], x['Best Year']), reverse=True)

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-16016236543642685128': 'file_storage/function-call-16016236543642685128.json', 'var_function-call-16016236543642684803': [{'symbol': 'A01K2227/108', 'level': '9.0', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'level': '9.0', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'level': '9.0', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'level': '9.0', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'level': '9.0', 'titleFull': 'Ovine'}], 'var_function-call-13561635954094791069': [{'cpc': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/5224",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R13/631",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'dated 7th October 2004', 'filing_date': 'dated 9th April 2003', 'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.'}], 'var_function-call-13561635954094789046': [{'symbol': 'A01B', 'level': '5.0', 'titleFull': 'SOIL WORKING IN AGRICULTURE OR FORESTRY; PARTS, DETAILS, OR ACCESSORIES OF AGRICULTURAL MACHINES OR IMPLEMENTS, IN GENERAL'}, {'symbol': 'A01B13/00', 'level': '7.0', 'titleFull': 'Ploughs or like machines for special purposes ; Ditch diggers, trench ploughs, forestry ploughs, ploughs for land or marsh reclamation'}, {'symbol': 'A01B35/00', 'level': '7.0', 'titleFull': 'Other machines for working soil not specially adapted for working soil on which crops are growing'}, {'symbol': 'A01B59/00', 'level': '7.0', 'titleFull': 'Devices specially adapted for connection between animals or tractors and agricultural machines or implements'}, {'symbol': 'A01B67/00', 'level': '7.0', 'titleFull': 'Devices for controlling the tractor motor by resistance of tools'}], 'var_function-call-317795769849267931': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-16573650118009255803': [{'symbol': 'H', 'level': '2.0'}, {'symbol': 'H01', 'level': '4.0'}, {'symbol': 'H01R', 'level': '5.0'}, {'symbol': 'H01R13/631', 'level': '10.0'}], 'var_function-call-13601185424003768990': 'file_storage/function-call-13601185424003768990.json', 'var_function-call-14579850432442259947': [{'code': 'H04', 'max_ema': 2.0, 'best_year': 2015}, {'code': 'Y02', 'max_ema': 1.0, 'best_year': 2015}, {'code': 'A61', 'max_ema': 1.0, 'best_year': 2016}, {'code': 'A43', 'max_ema': 1.0, 'best_year': 2016}, {'code': 'F04', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'F05', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'F01', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'G01', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'F16', 'max_ema': 1.0, 'best_year': 2018}, {'code': 'H02', 'max_ema': 1.0, 'best_year': 2009}, {'code': 'H03', 'max_ema': 1.0, 'best_year': 2015}, {'code': 'F41', 'max_ema': 1.0, 'best_year': 2012}, {'code': 'F42', 'max_ema': 1.0, 'best_year': 2012}, {'code': 'E02', 'max_ema': 1.0, 'best_year': 2012}], 'var_function-call-9662522869629261925': 'debug done', 'var_function-call-18416690200511783833': {'total_rows': 14, 'rows_2H_2019': 6, 'rows_with_filing': 6, 'rows_with_cpc': 6, 'sample_codes': ['F16', 'A43', 'F41', 'F42', 'F04', 'G01', 'H03', 'F01', 'E02', 'Y02']}, 'var_function-call-2511582570902758343': [{'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE', 'level': '4.0'}, {'symbol': 'A43', 'titleFull': 'FOOTWEAR', 'level': '4.0'}, {'symbol': 'E02', 'titleFull': 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING', 'level': '4.0'}, {'symbol': 'F41', 'titleFull': 'WEAPONS', 'level': '4.0'}, {'symbol': 'F01', 'titleFull': 'MACHINES OR ENGINES IN GENERAL; ENGINE PLANTS IN GENERAL; STEAM ENGINES', 'level': '4.0'}, {'symbol': 'F04', 'titleFull': 'POSITIVE - DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS FOR LIQUIDS OR ELASTIC FLUIDS', 'level': '4.0'}, {'symbol': 'F16', 'titleFull': 'ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL', 'level': '4.0'}, {'symbol': 'F05', 'titleFull': 'INDEXING SCHEMES RELATING TO ENGINES OR PUMPS IN VARIOUS SUBCLASSES OF CLASSES F01-F04', 'level': '4.0'}, {'symbol': 'F42', 'titleFull': 'AMMUNITION; BLASTING', 'level': '4.0'}, {'symbol': 'G01', 'titleFull': 'MEASURING; TESTING', 'level': '4.0'}, {'symbol': 'H03', 'titleFull': 'ELECTRONIC CIRCUITRY', 'level': '4.0'}, {'symbol': 'H04', 'titleFull': 'ELECTRIC COMMUNICATION TECHNIQUE', 'level': '4.0'}, {'symbol': 'H02', 'titleFull': 'GENERATION; CONVERSION OR DISTRIBUTION OF ELECTRIC POWER', 'level': '4.0'}, {'symbol': 'Y02', 'titleFull': 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE', 'level': '4.0'}]}

exec(code, env_args)
