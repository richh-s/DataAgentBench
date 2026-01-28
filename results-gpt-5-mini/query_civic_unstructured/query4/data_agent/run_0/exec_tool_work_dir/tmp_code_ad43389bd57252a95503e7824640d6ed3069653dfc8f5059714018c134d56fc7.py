code = """import json
from pathlib import Path
p = Path(var_call_WHeGJ8F36141GHHJ3yPO5vHV)
data = json.loads(p.read_text())
# identify projects that started in Spring 2022 using civic docs extractions earlier
# From previous extraction we found certain project names; pick likely matches
spring2022_projects = [
    'Westward Beach Road Repair Project',
    'PCH Median Improvements Project',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)',
    'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)',
    'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)',
    'Malibu Bluffs Park South Walkway Repairs'
]
# normalize funding data
funding = {}
for r in data:
    name = r.get('Project_Name','').strip()
    amt = int(r.get('Amount') or 0)
    funding.setdefault(name,0)
    funding[name]+=amt
# match projects to funding entries by exact or partial match
matched = []
for pj in spring2022_projects:
    # try exact
    if pj in funding:
        matched.append((pj, funding[pj]))
    else:
        # try partial match
        total = 0
        for k,v in funding.items():
            if pj.lower().split()[0] in k.lower() or pj.lower() in k.lower() or k.lower() in pj.lower():
                total += v
        if total>0:
            matched.append((pj,total))

# compile results
total_projects = len(matched)
total_funding = sum(x[1] for x in matched)
result = {'projects_count': total_projects, 'total_funding': total_funding, 'matched': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zPiRFhL3SBrfqfEgEhKn3UKe': 'file_storage/call_zPiRFhL3SBrfqfEgEhKn3UKe.json', 'var_call_7q0fOOmg9lDBZgyamUdO6zCn': ['(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Staff is currently working on the design of the project and anticipates', '(cid:131) The City has hired a consultant to design this project. The design has', '(cid:131) The project consultant has started the design of this project.', '(cid:131) The project design has begun and preliminary design should be', '(cid:190) Estimated Schedule:', '(cid:190) Project Description: The existing slope adjacent to the beach access stairs', '(cid:190) Project Description: The project consists of repairs the damaged shoulder on', '(cid:190) Project Description: This project consists of repairing damage storm drain', '(cid:190) Project Description: This project consists of the installation of four single-post', '(cid:190) Project Schedule', '(cid:190) Project Schedule:', 'Commission will then review the project in Spring 2022 before final', 'Commission will then review the project in Summer 2022 before final', 'anticipated to have a final design by March 2022. The project will be', 'approval by March 2022. The project will be advertised for construction', 'by March 2022. The project will be advertised for construction bids', 'construction of this project will begin in coordination with the PCH', 'for final approval. It is anticipated that the project will have final', 'is working on the project plans to prepare for public bidding.', 'project report and plans have been approved and final plans by', 'project will be advertised for construction bids with construction', 'project will begin in conjunction with the PCH Median Improvement', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'the Public Works Commission to revise the project scope.', 'the project', 'work related to the project. Staff has worked with the consultant over'], 'var_call_rMNESUQQ7jlg0ox6RNJGH9MP': ['anticipated to have a final design by March 2022. The project will be', 'project will begin in conjunction with the PCH Median Improvement', 'the project', 'shade structures at Malibu Bluffs Park.', 'sending this project out to bid during the Spring of 2022.', 'work related to the project. Staff has worked with the consultant over', 'Commission will then review the project in Spring 2022 before final', 'March 2022', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'facilities and roadway embankments that were damaged by the Woolsey', 'drains, culverts, debris basins, manholes, and other drainage structures', 'will begin in conjunction with the PCH Median Improvement', 'Metro.', 'project will be advertised for construction bids with construction', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'Median Improvement.', 'Commission will then review the project in Summer 2022 before final', 'August.', 'Caltrans. The project is currently out to bids with bids due December', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'is working on the project plans to prepare for public bidding.', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.'], 'var_call_rK58WulGbs5CziqyHC6CjyHj': ['manufacturers for filters that will work in the proposed project area. It is', 'anticipated to have a final design by March 2022. The project will be', 'on Pacific Coast Highway. The project reports and plans are being', 'for final approval. It is anticipated that the project will have final', 'project will begin in conjunction with the PCH Median Improvement', 'the project', 'shade structures at Malibu Bluffs Park.', 'sending this project out to bid during the Spring of 2022.', 'work related to the project. Staff has worked with the consultant over', 'Commission will then review the project in Spring 2022 before final', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'March 2022', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'drains, culverts, debris basins, manholes, and other drainage structures', 'project will be advertised for construction bids with construction', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'facilities and roadway embankments that were damaged by the Woolsey', 'evaluating the project costs.', 'Rob DuBoux, Public Works Director/City Engineer', 'final design is complete and the project will be advertised for', 'PCH Signal Synchronization System Improvements Project', 'final approval. It is anticipated that the project will have final approval', 'will begin in conjunction with the PCH Median Improvement', 'culverts, debris basins, manholes, and other drainage structures within the', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'the project costs.', 'Marie Canyon Green Streets', 'on Pacific Coast Highway. The project will be advertised for', 'Median Improvement.', 'Westward Beach Road Repair Project', 'Commission will then review the project in Summer 2022 before final', 'need of replacing at Malibu Bluffs Park', 'guardrails within the project limits.', 'The project consultant prepared the specifications for the project. The City', 'The project is currently out to bid with proposals due August 4, 2022.', 'granite (DG) sidewalk, asphalt repairs and minor restoration work to', 'evaluating the project costs and calculating each parcels estimated', 'PCH Median Improvements Project', 'than the available budget for the project.', '8, 2022.', 'is working on the project plans to prepare for public bidding.', 'stages of selecting a firm. The project is scheduled for Planning', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.'], 'var_call_WHeGJ8F36141GHHJ3yPO5vHV': 'file_storage/call_WHeGJ8F36141GHHJ3yPO5vHV.json'}

exec(code, env_args)
