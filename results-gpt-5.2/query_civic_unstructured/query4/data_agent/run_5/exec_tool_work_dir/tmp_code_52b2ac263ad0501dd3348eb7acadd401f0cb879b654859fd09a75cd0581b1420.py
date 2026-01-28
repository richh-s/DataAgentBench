code = """import json

projects = var_call_iaHjBRQFMV1YvBz9QqJLXdV8['projects']

path = var_call_ULn2IgOL2zo1Wsy3jhfY8IZg
with open(path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}

matched=[]
missing=[]
total=0
for p in projects:
    amt = fund_map.get(p)
    if amt is None:
        missing.append(p)
    else:
        matched.append({'Project_Name': p, 'total_funding': amt})
        total += amt

result = {
    'count_projects_started_spring_2022': len(projects),
    'projects': projects,
    'matched_funding_projects': matched,
    'missing_funding_projects': missing,
    'total_funding_matched': total
}
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_LDig9FmJRw9vPmKNbUKgBomP': ['Funding'], 'var_call_P1s7LCEzcpwRpCzrFpVtCvNc': ['civic_docs'], 'var_call_bFT0LzLw79r9xBgBKESnVmpw': 'file_storage/call_bFT0LzLw79r9xBgBKESnVmpw.json', 'var_call_rn7TZs6Br9Hucjj0u18Fvagq': 'file_storage/call_rn7TZs6Br9Hucjj0u18Fvagq.json', 'var_call_WAybRsjHEQ4ukQh8zVFV5kJS': {'projects': ['Fire.', 'March 2022', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'meeting was held on May 16, 2022 and the design is underway.', 'project will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 17}, 'var_call_Mr3EU3oH8Dl8xM8jHPwNcLUy': {'projects': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'meeting was held on May 16, 2022 and the design is underway.', 'project will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 15}, 'var_call_wBYaNRrcjlUUtxiblmGfWACO': {'projects': [], 'count': 0}, 'var_call_wTuzNZLOs8MrYIQslKV0tHOh': {'projects': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'facilities and roadway embankments that were damaged by the Woolsey', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'project will be advertised for construction bids with construction'], 'count': 12}, 'var_call_1Ui6dAs44AtdS4iXwdGjhi39': {'projects': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'facilities and roadway embankments that were damaged by the Woolsey', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'project will be advertised for construction bids with construction'], 'count': 12}, 'var_call_iaHjBRQFMV1YvBz9QqJLXdV8': {'projects': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'count': 7}, 'var_call_ULn2IgOL2zo1Wsy3jhfY8IZg': 'file_storage/call_ULn2IgOL2zo1Wsy3jhfY8IZg.json'}

exec(code, env_args)
