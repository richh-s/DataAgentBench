code = """import json

# Load funding data
with open(locals()['var_function-call-13069126616893175602'], 'r') as f:
    funding_data = json.load(f)

# The 9 base projects identified
base_projects = [
    "Marie Canyon Green Streets",
    "Bluffs Park Shade Structure",
    "Broad Beach Road Water Quality Infrastructure Repairs",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements",
    "Trancas Canyon Park Planting and Irrigation Repairs",
    "Trancas Canyon Park Slope Stabilization Project",
    "Latigo Canyon Road Culvert Repairs",
    "Civic Center Water Treatment Facility Phase 2",
    "Encinal Canyon Road Drainage Improvements"
]

total_funding = 0
matched_records = []

for record in funding_data:
    p_name = record['Project_Name']
    amount = int(record['Amount'])
    
    # Check if this record belongs to one of the base projects
    # strict startswith check
    for base in base_projects:
        if p_name == base or p_name.startswith(base + " ") or p_name.startswith(base + "("):
            total_funding += amount
            matched_records.append(p_name)
            break

print("__RESULT__:")
print(json.dumps({
    "count": len(base_projects),
    "total_funding": total_funding,
    "matched_records": matched_records
}))"""

env_args = {'var_function-call-11013100090032240627': ['Funding'], 'var_function-call-11013100090032239808': ['civic_docs'], 'var_function-call-13069126616893175602': 'file_storage/function-call-13069126616893175602.json', 'var_function-call-13069126616893177209': 'file_storage/function-call-13069126616893177209.json', 'var_function-call-2392722741691488193': 'file_storage/function-call-2392722741691488193.json', 'var_function-call-14951084394473417957': {'count': 9, 'total_funding': 459000, 'projects': ['Bluffs Park Shade Structure', 'Marie Canyon Green Streets', 'Trancas Canyon Park Slope Stabilization Project', 'Latigo Canyon Road Culvert Repairs', 'Civic Center Water Treatment Facility Phase 2', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Encinal Canyon Road Drainage Improvements', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Latigo Canyon Road Roadway/Retaining Wall Improvements']}, 'var_function-call-6752735360527361173': [{'project': 'Marie Canyon Green Streets', 'filename': 'malibucity_agenda__01262022-1835.txt', 'date_found': 'spring 2022\n\n', 'context': 'Marie Canyon Green Streets (cid:190) Updates:  (cid:131) A hydrology report was prepared and will be used to size the pre- manufactured biofilters. City staff is reviewing multiple biofilter manufactu'}, {'project': 'Bluffs Park Shade Structure', 'filename': 'malibucity_agenda__01262022-1835.txt', 'date_found': 'spring 2022\n\n', 'context': 'Bluffs Park Shade Structure  (cid:190) Project Description: This project consists of the installation of four single-post  shade structures at Malibu Bluffs Park.  (cid:190) Updates:  (cid:131) Staff '}, {'project': 'Broad Beach Road Water Quality Infrastructure Repairs', 'filename': 'malibucity_agenda__01262022-1835.txt', 'date_found': 'spring 2022\n\n', 'context': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)  (cid:190) Updates:  (cid:131) The project consultant prepared the specifications for the project. Staff  is finalizing the bid '}, {'project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'filename': 'malibucity_agenda__01262022-1835.txt', 'date_found': 'april 2022\n\n', 'context': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)  (cid:190) Updates:  (cid:131) Staff is finalizing the design of this project. (cid:131) Staff is also working with FEMA/CalOES to'}, {'project': 'Trancas Canyon Park Planting and Irrigation Repairs', 'filename': 'malibucity_agenda__01262022-1835.txt', 'date_found': 'spring 2022\n\n', 'context': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)  (cid:190) Updates:  (cid:131) The project consultant has started the design of this project.  (cid:190) Project Schedule:  ('}, {'project': 'Trancas Canyon Park Slope Stabilization Project', 'filename': 'malibucity_agenda__01262022-1835.txt', 'date_found': 'spring 2022\n\n', 'context': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)  (cid:190) Updates:  (cid:131) The project consultant has started the design of this project.  (cid:190) Project Schedule:  (cid:131) '}, {'project': 'Latigo Canyon Road Culvert Repairs', 'filename': 'malibucity_agenda__01262022-1835.txt', 'date_found': 'april 2022\n\n', 'context': 'Latigo Canyon Road Culvert Repairs (FEMA Project)  (cid:190) Project Description: This project consists of repairing the existing storm drain on Latigo Canyon Road located approximately 2,500 feet fro'}, {'project': 'Civic Center Water Treatment Facility Phase 2', 'filename': 'malibucity_agenda__01272021-1626.txt', 'date_found': 'march 2022\n\n', 'context': 'Civic Center Water Treatment Facility Phase 2  (cid:190) Updates:  (cid:131) Project is at the 65% design phase. (cid:131) Working with the Planning Department to send project to Planning  Commission '}, {'project': 'Latigo Canyon Road Culvert Repairs', 'filename': 'malibucity_agenda__01272021-1626.txt', 'date_found': 'spring 2022\n\n', 'context': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)  (cid:190) Project Description: This project consists of repairing the existing storm drain on Latigo Canyon Road located approximately 2,500 f'}, {'project': 'Encinal Canyon Road Drainage Improvements', 'filename': 'malibucity_agenda__01272021-1626.txt', 'date_found': 'spring 2022\n\n', 'context': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)  (cid:190) Project Description: This project consists of repairing damage storm drain facilities and roadway embankments that were damag'}, {'project': 'Civic Center Water Treatment Facility Phase 2', 'filename': 'malibucity_agenda__03022021-1648.txt', 'date_found': 'march 2022\n\npage 2 of 6\n\nagenda item ', 'context': 'Civic Center Water Treatment Facility Phase 2  (cid:190) Updates:  (cid:131) Project is at the 65% design phase. (cid:131) The City obtained a project CDP from Planning Commission on  February 1, 2021'}, {'project': 'Latigo Canyon Road Culvert Repairs', 'filename': 'malibucity_agenda__03022021-1648.txt', 'date_found': 'spring 2022\n\n', 'context': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)  (cid:190) Project Description: This project consists of repairing the existing storm drain on Latigo Canyon Road located approximately 2,500 f'}, {'project': 'Encinal Canyon Road Drainage Improvements', 'filename': 'malibucity_agenda__03022021-1648.txt', 'date_found': 'spring 2022\n\n', 'context': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)  (cid:190) Project Description: This project consists of repairing damage storm drain facilities and roadway embankments that were damag'}, {'project': 'Bluffs Park Shade Structure', 'filename': 'malibucity_agenda__03232022-1869.txt', 'date_found': 'spring 2022\n\n', 'context': 'Bluffs Park Shade Structure  (cid:190) Project Description: This project consists of the installation of four single-post  shade structures at Malibu Bluffs Park.  (cid:190) Updates:  (cid:131) Staff '}, {'project': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'filename': 'malibucity_agenda__03232022-1869.txt', 'date_found': 'spring 2022\n\npage 5 of 8\n\nagenda item ', 'context': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)  (cid:190) Updates:  (cid:131) Staff is finalizing the design of this project. (cid:131) Staff is also working with FEMA/CalOES to'}, {'project': 'Latigo Canyon Road Culvert Repairs', 'filename': 'malibucity_agenda__03232022-1869.txt', 'date_found': 'spring 2022\n\n', 'context': 'Latigo Canyon Road Culvert Repairs (FEMA Project)  (cid:190) Project Description: This project consists of repairing the existing storm drain on Latigo Canyon Road located approximately 2,500 feet fro'}]}

exec(code, env_args)
