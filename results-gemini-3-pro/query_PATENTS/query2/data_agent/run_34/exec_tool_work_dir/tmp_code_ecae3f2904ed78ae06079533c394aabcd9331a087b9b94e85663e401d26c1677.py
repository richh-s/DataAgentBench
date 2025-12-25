code = """import json
import pandas as pd

# Data from previous steps
results_list = [
    {"code": "A61", "best_year": 2016, "max_ema": 2.0},
    {"code": "A21", "best_year": 2015, "max_ema": 1.0},
    {"code": "A43", "best_year": 2016, "max_ema": 1.0},
    {"code": "A47", "best_year": 2015, "max_ema": 1.0},
    {"code": "B23", "best_year": 2015, "max_ema": 1.0},
    {"code": "B29", "best_year": 2012, "max_ema": 1.0},
    {"code": "B41", "best_year": 2007, "max_ema": 1.0},
    {"code": "B60", "best_year": 2009, "max_ema": 1.0},
    {"code": "B62", "best_year": 2010, "max_ema": 1.0},
    {"code": "B64", "best_year": 2018, "max_ema": 1.0},
    {"code": "B66", "best_year": 2016, "max_ema": 1.0},
    {"code": "E02", "best_year": 2012, "max_ema": 1.0},
    {"code": "E05", "best_year": 2012, "max_ema": 1.0},
    {"code": "F01", "best_year": 2018, "max_ema": 1.0},
    {"code": "F02", "best_year": 2010, "max_ema": 1.0},
    {"code": "F04", "best_year": 2018, "max_ema": 1.0},
    {"code": "F05", "best_year": 2018, "max_ema": 1.0},
    {"code": "F16", "best_year": 2009, "max_ema": 1.0},
    {"code": "F41", "best_year": 2012, "max_ema": 1.0},
    {"code": "F42", "best_year": 2012, "max_ema": 1.0},
    {"code": "G01", "best_year": 2008, "max_ema": 1.0},
    {"code": "G02", "best_year": 2018, "max_ema": 1.0},
    {"code": "G07", "best_year": 2012, "max_ema": 1.0},
    {"code": "G08", "best_year": 2017, "max_ema": 1.0},
    {"code": "H01", "best_year": 2008, "max_ema": 1.0},
    {"code": "H02", "best_year": 2009, "max_ema": 1.0},
    {"code": "H03", "best_year": 2015, "max_ema": 1.0},
    {"code": "H04", "best_year": 2015, "max_ema": 1.0},
    {"code": "Y02", "best_year": 2013, "max_ema": 1.0},
    {"code": "Y10", "best_year": 2012, "max_ema": 1.0}
]

titles_list = [
    {"symbol": "A61", "titleFull": "MEDICAL OR VETERINARY SCIENCE; HYGIENE"},
    {"symbol": "A43", "titleFull": "FOOTWEAR"},
    {"symbol": "A47", "titleFull": "FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL"},
    {"symbol": "A21", "titleFull": "BAKING; EDIBLE DOUGHS"},
    {"symbol": "B66", "titleFull": "HOISTING; LIFTING; HAULING"},
    {"symbol": "B62", "titleFull": "LAND VEHICLES FOR TRAVELLING OTHERWISE THAN ON RAILS"},
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
    {"symbol": "B29", "titleFull": "WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL"},
    {"symbol": "B23", "titleFull": "MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR"}
]

# Merge
df_res = pd.DataFrame(results_list)
df_titles = pd.DataFrame(titles_list)
merged = pd.merge(df_res, df_titles, left_on='code', right_on='symbol', how='left')

# Sort by Max EMA descending, then Code
merged = merged.sort_values(by=['max_ema', 'code'], ascending=[False, True])

# Format
output_lines = []
for idx, row in merged.iterrows():
    title = row['titleFull']
    # Truncate title if too long?
    line = f"{row['code']}: {title} (Best Year: {int(row['best_year'])})"
    output_lines.append(line)

print("__RESULT__:")
print(json.dumps(output_lines))"""

env_args = {'var_function-call-7712572374435619726': 'file_storage/function-call-7712572374435619726.json', 'var_function-call-9207544012969803277': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004', 'filing_date': 'dated 9th April 2003'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th', 'filing_date': '18th of April, 2005'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007', 'filing_date': '2006, May 11th'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th', 'filing_date': '30th June 2007'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010', 'filing_date': '2009, July 8th'}], 'var_function-call-9207544012969800986': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}], 'var_function-call-12829125581804936989': [{'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}], 'var_function-call-606694554395787070': [{'symbol': 'C01', 'level': '4.0', 'titleFull': 'INORGANIC CHEMISTRY'}, {'symbol': 'C01B', 'level': '5.0', 'titleFull': 'NON-METALLIC ELEMENTS; COMPOUNDS THEREOF; METALLOIDS OR COMPOUNDS THEREOF NOT COVERED BY SUBCLASS C01C'}], 'var_function-call-13685583688298079669': [{'count(*)': '11644'}], 'var_function-call-824216202442530492': 'file_storage/function-call-824216202442530492.json', 'var_function-call-10104036999913047761': [{'code': 'A61', 'best_year': 2016, 'max_ema': 2.0}, {'code': 'A21', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'A43', 'best_year': 2016, 'max_ema': 1.0}, {'code': 'A47', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'B23', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'B29', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'B41', 'best_year': 2007, 'max_ema': 1.0}, {'code': 'B60', 'best_year': 2009, 'max_ema': 1.0}, {'code': 'B62', 'best_year': 2010, 'max_ema': 1.0}, {'code': 'B64', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'B66', 'best_year': 2016, 'max_ema': 1.0}, {'code': 'E02', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'E05', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'F01', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F02', 'best_year': 2010, 'max_ema': 1.0}, {'code': 'F04', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F05', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F16', 'best_year': 2009, 'max_ema': 1.0}, {'code': 'F41', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'F42', 'best_year': 2012, 'max_ema': 1.0}], 'var_function-call-7319816257142469515': {'count': 30, 'years': [2019]}, 'var_function-call-1137987773701671683': [{'code': 'A61', 'best_year': 2016, 'max_ema': 2.0}, {'code': 'A21', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'A43', 'best_year': 2016, 'max_ema': 1.0}, {'code': 'A47', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'B23', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'B29', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'B41', 'best_year': 2007, 'max_ema': 1.0}, {'code': 'B60', 'best_year': 2009, 'max_ema': 1.0}, {'code': 'B62', 'best_year': 2010, 'max_ema': 1.0}, {'code': 'B64', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'B66', 'best_year': 2016, 'max_ema': 1.0}, {'code': 'E02', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'E05', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'F01', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F02', 'best_year': 2010, 'max_ema': 1.0}, {'code': 'F04', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F05', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'F16', 'best_year': 2009, 'max_ema': 1.0}, {'code': 'F41', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'F42', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'G01', 'best_year': 2008, 'max_ema': 1.0}, {'code': 'G02', 'best_year': 2018, 'max_ema': 1.0}, {'code': 'G07', 'best_year': 2012, 'max_ema': 1.0}, {'code': 'G08', 'best_year': 2017, 'max_ema': 1.0}, {'code': 'H01', 'best_year': 2008, 'max_ema': 1.0}, {'code': 'H02', 'best_year': 2009, 'max_ema': 1.0}, {'code': 'H03', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'H04', 'best_year': 2015, 'max_ema': 1.0}, {'code': 'Y02', 'best_year': 2013, 'max_ema': 1.0}, {'code': 'Y10', 'best_year': 2012, 'max_ema': 1.0}], 'var_function-call-11168513189211732119': [{'symbol': 'A61', 'titleFull': 'MEDICAL OR VETERINARY SCIENCE; HYGIENE'}, {'symbol': 'A43', 'titleFull': 'FOOTWEAR'}, {'symbol': 'A47', 'titleFull': 'FURNITURE; DOMESTIC ARTICLES OR APPLIANCES; COFFEE MILLS; SPICE MILLS; SUCTION CLEANERS IN GENERAL'}, {'symbol': 'A21', 'titleFull': 'BAKING; EDIBLE DOUGHS'}, {'symbol': 'B66', 'titleFull': 'HOISTING; LIFTING; HAULING'}, {'symbol': 'B62', 'titleFull': 'LAND VEHICLES FOR TRAVELLING OTHERWISE THAN ON RAILS'}, {'symbol': 'B64', 'titleFull': 'AIRCRAFT; AVIATION; COSMONAUTICS'}, {'symbol': 'B60', 'titleFull': 'VEHICLES IN GENERAL'}, {'symbol': 'B41', 'titleFull': 'PRINTING; LINING MACHINES; TYPEWRITERS; STAMPS'}, {'symbol': 'E05', 'titleFull': 'LOCKS; KEYS; WINDOW OR DOOR FITTINGS; SAFES'}, {'symbol': 'E02', 'titleFull': 'HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING'}, {'symbol': 'F41', 'titleFull': 'WEAPONS'}, {'symbol': 'F01', 'titleFull': 'MACHINES OR ENGINES IN GENERAL; ENGINE PLANTS IN GENERAL; STEAM ENGINES'}, {'symbol': 'F04', 'titleFull': 'POSITIVE - DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS FOR LIQUIDS OR ELASTIC FLUIDS'}, {'symbol': 'F16', 'titleFull': 'ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL'}, {'symbol': 'F05', 'titleFull': 'INDEXING SCHEMES RELATING TO ENGINES OR PUMPS IN VARIOUS SUBCLASSES OF CLASSES F01-F04'}, {'symbol': 'F42', 'titleFull': 'AMMUNITION; BLASTING'}, {'symbol': 'F02', 'titleFull': 'COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS'}, {'symbol': 'G08', 'titleFull': 'SIGNALLING'}, {'symbol': 'G02', 'titleFull': 'OPTICS'}, {'symbol': 'G01', 'titleFull': 'MEASURING; TESTING'}, {'symbol': 'G07', 'titleFull': 'CHECKING-DEVICES'}, {'symbol': 'H03', 'titleFull': 'ELECTRONIC CIRCUITRY'}, {'symbol': 'H04', 'titleFull': 'ELECTRIC COMMUNICATION TECHNIQUE'}, {'symbol': 'H01', 'titleFull': 'ELECTRIC ELEMENTS'}, {'symbol': 'H02', 'titleFull': 'GENERATION; CONVERSION OR DISTRIBUTION OF ELECTRIC POWER'}, {'symbol': 'Y02', 'titleFull': 'TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE'}, {'symbol': 'Y10', 'titleFull': 'TECHNICAL SUBJECTS COVERED BY FORMER USPC'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}]}

exec(code, env_args)
