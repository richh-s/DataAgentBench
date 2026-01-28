code = """import json
import pandas as pd

with open(locals()['var_function-call-2604806260123295524'], 'r') as f:
    civic_docs = json.load(f)

NEWLINE = chr(10)
target = "Legacy Park Paver Repair Project"
snippets = []

for doc in civic_docs:
    if target in doc['text']:
        lines = doc['text'].splitlines()
        for i, line in enumerate(lines):
            if target in line:
                snippets.append(NEWLINE.join(lines[i:i+15]))

print('__RESULT__:')
print(json.dumps(snippets))"""

env_args = {'var_function-call-2604806260123295524': 'file_storage/function-call-2604806260123295524.json', 'var_function-call-2604806260123292981': 'file_storage/function-call-2604806260123292981.json', 'var_function-call-11287208145778595060': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}, 'var_function-call-595158838709480876': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs', 'amenities such as trash cans, benches, tables, and restrooms.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'amenities such as trash cans, benches, tables, and restrooms.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.'], 'var_function-call-15851896367516110086': {'texts': {'Bluffs Park Shade Structure': 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff received bids on February 24, 2022. Award of contract is\n\nscheduled for the April 11, 2022 Council meeting.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: Spring 2022\n\nPermanent Skate Park\n\n(cid:190) Project Description: This project includes designing and constructing a', 'Broad Beach Road Water Quality Repair': 'Broad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoint Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nCapital Improvement Projects (Not Started)\n\nPCH Median Improvements at Paradise Cove and Zuma Beach\n\n(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study\nand includes installing new raised medians and improvements. New raised\nmedians are proposed east and west of PCH and Paradise Cove Road. The', 'Point Dume Walkway Repairs': 'Point Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nCapital Improvement Projects (Not Started)\n\nPCH Median Improvements at Paradise Cove and Zuma Beach\n\n(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study\nand includes installing new raised medians and improvements. New raised\nmedians are proposed east and west of PCH and Paradise Cove Road. The\nproposed improvements also include the relocation of the existing bus stop\nand new signage. The project will also include the installation of new raised\nmedians on PCH in the areas where the double yellow lines exist in the vicinity\nof Zuma Beach, specifically where the yellow paddles are installed.\n\n(cid:190) Project Updates: City has submitted an application through Measure R and is\n'}, 'funding': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': 21000}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': 93000}, {'Project_Name': 'Point Dume Walkway Repairs', 'Amount': 59000}]}}

exec(code, env_args)
