code = """import json

# Previous results
ema_results = [
    {"cpc_group": "A61", "best_year": 2016, "max_ema": 3.0}, 
    {"cpc_group": "H04", "best_year": 2015, "max_ema": 2.0}, 
    {"cpc_group": "G01", "best_year": 2018, "max_ema": 1.01}, 
    {"cpc_group": "A43", "best_year": 2016, "max_ema": 1.0}, 
    {"cpc_group": "B23", "best_year": 2015, "max_ema": 1.0}, 
    {"cpc_group": "B29", "best_year": 2007, "max_ema": 1.0}, 
    {"cpc_group": "B41", "best_year": 2007, "max_ema": 1.0}, 
    {"cpc_group": "B60", "best_year": 2009, "max_ema": 1.0}, 
    {"cpc_group": "B64", "best_year": 2018, "max_ema": 1.0}, 
    {"cpc_group": "E02", "best_year": 2012, "max_ema": 1.0}, 
    {"cpc_group": "E05", "best_year": 2012, "max_ema": 1.0}, 
    {"cpc_group": "F01", "best_year": 2018, "max_ema": 1.0}, 
    {"cpc_group": "F02", "best_year": 2010, "max_ema": 1.0}, 
    {"cpc_group": "F04", "best_year": 2014, "max_ema": 1.0}, 
    {"cpc_group": "F05", "best_year": 2018, "max_ema": 1.0}, 
    {"cpc_group": "F16", "best_year": 2009, "max_ema": 1.0}, 
    {"cpc_group": "F23", "best_year": 2018, "max_ema": 1.0}, 
    {"cpc_group": "F24", "best_year": 2018, "max_ema": 1.0}, 
    {"cpc_group": "F41", "best_year": 2012, "max_ema": 1.0}, 
    {"cpc_group": "F42", "best_year": 2012, "max_ema": 1.0}, 
    {"cpc_group": "G02", "best_year": 2016, "max_ema": 1.0}, 
    {"cpc_group": "G07", "best_year": 2012, "max_ema": 1.0}, 
    {"cpc_group": "G08", "best_year": 2017, "max_ema": 1.0}, 
    {"cpc_group": "H01", "best_year": 2012, "max_ema": 1.0}, 
    {"cpc_group": "H02", "best_year": 2009, "max_ema": 1.0}, 
    {"cpc_group": "H03", "best_year": 2015, "max_ema": 1.0}, 
    {"cpc_group": "Y02", "best_year": 2013, "max_ema": 1.0}, 
    {"cpc_group": "Y10", "best_year": 2012, "max_ema": 1.0}
]

titles_data = [
    {"symbol": "B29", "titleFull": "WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL"}, 
    {"symbol": "A61", "titleFull": "MEDICAL OR VETERINARY SCIENCE; HYGIENE"}, 
    {"symbol": "A43", "titleFull": "FOOTWEAR"}, 
    {"symbol": "B64", "titleFull": "AIRCRAFT; AVIATION; COSMONAUTICS"}, 
    {"symbol": "B60", "titleFull": "VEHICLES IN GENERAL"}, 
    {"symbol": "B41", "titleFull": "PRINTING; LINING MACHINES; TYPEWRITERS; STAMPS"}, 
    {"symbol": "E05", "titleFull": "LOCKS; KEYS; WINDOW OR DOOR FITTINGS; SAFES"}, 
    {"symbol": "E02", "titleFull": "HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING"}, 
    {"symbol": "F41", "titleFull": "WEAPONS"}, 
    {"symbol": "F01", "titleFull": "MACHINES OR ENGINES IN GENERAL; ENGINE PLANTS IN GENERAL; STEAM ENGINES"}, 
    {"symbol": "F04", "titleFull": "POSITIVE - DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS FOR LIQUIDS OR ELASTIC FLUIDS"}, 
    {"symbol": "F16", "titleFull": "ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL"}, 
    {"symbol": "F05", "titleFull": "INDEXING SCHEMES RELATING TO ENGINES OR PUMPS IN VARIOUS SUBCLASSES OF CLASSES F01-F04"}, 
    {"symbol": "F42", "titleFull": "AMMUNITION; BLASTING"}, 
    {"symbol": "F02", "titleFull": "COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS"}, 
    {"symbol": "F23", "titleFull": "COMBUSTION APPARATUS; COMBUSTION PROCESSES"}, 
    {"symbol": "F24", "titleFull": "HEATING; RANGES; VENTILATING"}, 
    {"symbol": "G08", "titleFull": "SIGNALLING"}, 
    {"symbol": "G02", "titleFull": "OPTICS"}, 
    {"symbol": "G01", "titleFull": "MEASURING; TESTING"}, 
    {"symbol": "G07", "titleFull": "CHECKING-DEVICES"}, 
    {"symbol": "H03", "titleFull": "ELECTRONIC CIRCUITRY"}, 
    {"symbol": "H04", "titleFull": "ELECTRIC COMMUNICATION TECHNIQUE"}, 
    {"symbol": "H01", "titleFull": "ELECTRIC ELEMENTS"}, 
    {"symbol": "H02", "titleFull": "GENERATION; CONVERSION OR DISTRIBUTION OF ELECTRIC POWER"}, 
    {"symbol": "Y02", "titleFull": "TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE"}, 
    {"symbol": "Y10", "titleFull": "TECHNICAL SUBJECTS COVERED BY FORMER USPC"}, 
    {"symbol": "B23", "titleFull": "MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR"}
]

# Create map
title_map = {item['symbol']: item['titleFull'] for item in titles_data}

final_output = []
for item in ema_results:
    symbol = item['cpc_group']
    final_output.append({
        "Full Title": title_map.get(symbol, "Unknown"),
        "CPC Group Code": symbol,
        "Best Year": item['best_year']
    })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-4700514525902219296': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-4700514525902218863': [{'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '14th Mar 2019', 'filing_date': '2013, June 17th', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.'}, {'cpc': '[\n  {\n    "code": "A61D1/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/645",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/6425",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/64",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/60",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "A61B17/58",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 19th, 2019', 'filing_date': 'on December 4th, 2017', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.'}, {'cpc': '[\n  {\n    "code": "E21B33/136",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "E21B33/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'Mar 12th, 2019', 'filing_date': '2018 on Feb 15th', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.'}, {'cpc': '[\n  {\n    "code": "G01S13/42",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S5/18",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41G3/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F41H13/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': '2019 on Jul 12th', 'filing_date': '23rd May 2018', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.'}, {'cpc': '[\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/37",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G01S19/30",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'grant_date': 'on March 14th, 2019', 'filing_date': 'Jan 26th, 2015', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.'}], 'var_function-call-2784290657964579743': [{'symbol': 'G', 'level': '2.0', 'titleFull': 'PHYSICS'}, {'symbol': 'G06', 'level': '4.0', 'titleFull': 'COMPUTING; CALCULATING OR COUNTING'}, {'symbol': 'G06F', 'level': '5.0', 'titleFull': 'ELECTRIC DIGITAL DATA PROCESSING'}, {'symbol': 'G06F9/00', 'level': '7.0', 'titleFull': 'Arrangements for program control, e.g. control units'}], 'var_function-call-14097541545032493746': 'file_storage/function-call-14097541545032493746.json', 'var_function-call-14371907895498571290': [{'cpc_group': 'A61', 'best_year': 2016, 'max_ema': 3.0}, {'cpc_group': 'H04', 'best_year': 2015, 'max_ema': 2.0}, {'cpc_group': 'G01', 'best_year': 2018, 'max_ema': 1.01}, {'cpc_group': 'A43', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group': 'B23', 'best_year': 2015, 'max_ema': 1.0}, {'cpc_group': 'B29', 'best_year': 2007, 'max_ema': 1.0}, {'cpc_group': 'B41', 'best_year': 2007, 'max_ema': 1.0}, {'cpc_group': 'B60', 'best_year': 2009, 'max_ema': 1.0}, {'cpc_group': 'B64', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group': 'E02', 'best_year': 2012, 'max_ema': 1.0}, {'cpc_group': 'E05', 'best_year': 2012, 'max_ema': 1.0}, {'cpc_group': 'F01', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group': 'F02', 'best_year': 2010, 'max_ema': 1.0}, {'cpc_group': 'F04', 'best_year': 2014, 'max_ema': 1.0}, {'cpc_group': 'F05', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group': 'F16', 'best_year': 2009, 'max_ema': 1.0}, {'cpc_group': 'F23', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group': 'F24', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group': 'F41', 'best_year': 2012, 'max_ema': 1.0}, {'cpc_group': 'F42', 'best_year': 2012, 'max_ema': 1.0}, {'cpc_group': 'G02', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group': 'G07', 'best_year': 2012, 'max_ema': 1.0}, {'cpc_group': 'G08', 'best_year': 2017, 'max_ema': 1.0}, {'cpc_group': 'H01', 'best_year': 2012, 'max_ema': 1.0}, {'cpc_group': 'H02', 'best_year': 2009, 'max_ema': 1.0}, {'cpc_group': 'H03', 'best_year': 2015, 'max_ema': 1.0}, {'cpc_group': 'Y02', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group': 'Y10', 'best_year': 2012, 'max_ema': 1.0}], 'var_function-call-5051645618536125071': [{'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'symbol': 'B64', 'titleFull': 'AIRCRAFT; AVIATION; COSMONAUTICS'}, {'symbol': 'B60', 'titleFull': 'VEHICLES IN GENERAL'}, {'symbol': 'B41', 'titleFull': 'PRINTING; LINING MACHINES; TYPEWRITERS; STAMPS'}, {'symbol': 'E05', 'titleFull': 'LOCKS; KEYS; WINDOW OR DOOR FITTINGS; SAFES'}, {'symbol': 'E02', 'titleFull': 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING'}, {'symbol': 'F41', 'titleFull': 'WEAPONS'}, {'symbol': 'F01', 'titleFull': 'MACHINES OR ENGINES IN GENERAL; ENGINE PLANTS IN GENERAL; STEAM ENGINES'}, {'symbol': 'F04', 'titleFull': 'POSITIVE - DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS FOR LIQUIDS OR ELASTIC FLUIDS'}, {'symbol': 'F16', 'titleFull': 'ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL'}, {'symbol': 'F05', 'titleFull': 'INDEXING SCHEMES RELATING TO ENGINES OR PUMPS IN VARIOUS SUBCLASSES OF CLASSES F01-F04'}, {'symbol': 'F42', 'titleFull': 'AMMUNITION; BLASTING'}, {'symbol': 'F02', 'titleFull': 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'}, {'symbol': 'F23', 'titleFull': 'COMBUSTION APPARATUS; COMBUSTION PROCESSES'}, {'symbol': 'F24', 'titleFull': 'HEATING; RANGES; VENTILATING'}, {'symbol': 'G08', 'titleFull': 'SIGNALLING'}, {'symbol': 'G02', 'titleFull': 'OPTICS'}, {'symbol': 'G01', 'titleFull': 'MEASURING; TESTING'}, {'symbol': 'G07', 'titleFull': 'CHECKING-DEVICES'}, {'symbol': 'H03', 'titleFull': 'ELECTRONIC CIRCUITRY'}, {'symbol': 'H04', 'titleFull': 'ELECTRIC COMMUNICATION TECHNIQUE'}, {'symbol': 'H01', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'H02', 'titleFull': 'GENERATION; CONVERSION OR DISTRIBUTION OF ELECTRIC POWER'}, {'symbol': 'Y02', 'titleFull': 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'}, {'symbol': 'Y10', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER USPC'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}]}

exec(code, env_args)
