code = """import json

# Access file paths
path_funding = locals()['var_function-call-12694910972065598501']

with open(path_funding) as f:
    funding_data = json.load(f)

high_funding_names = []
for row in funding_data:
    try:
        amt = float(row['Amount'])
        if amt > 50000:
            high_funding_names.append(row['Project_Name'].strip())
    except:
        pass

high_funding_names.sort()

print('__RESULT__:')
print(json.dumps({'high_funding_names': high_funding_names}))"""

env_args = {'var_function-call-12694910972065598501': 'file_storage/function-call-12694910972065598501.json', 'var_function-call-12694910972065599408': 'file_storage/function-call-12694910972065599408.json', 'var_function-call-14720826093064389612': 'file_storage/function-call-14720826093064389612.json', 'var_function-call-13186996373007626590': {'count': 10, 'matches': ['Civic Center Stormwater Diversion Structure', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Permanent Skate Park', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Storm Drain Master Plan', 'Outdoor Warning Signs'], 'debug_found': ['Clover Heights Storm Drainage Improvements', 'PCH Signal Synchronization System Improvements Project', 'sending this project out to bid during the Spring of 2022.', 'with the property owners regarding their proposed assessments.', 'review by the Council.', 'bidding.', 'Westward Beach Road Improvements Project', 'feasible traffic safety improvements can be constructed at this location.', 'Civic Center Stormwater Diversion Structure', 'PCH at Trancas Canyon Road Right Turn Lane', 'Malibu Bluffs Park South Walkway Repairs', 'evaluating the project costs.', 'to review', 'the County.', 'Trancas Canyon Park Playground', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Bluffs Park Shade Structure', 'Resources review for the SRF funding application', 'project', 'Marie Canyon Green Streets', 'Malibu Park Drainage Improvements', 'Fund program.', 'the Spring 2023.', 'property owners.', 'advertised for construction bids shortly after this date.', 'PCH Median Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Permanent Skate Park', 'Malibu Canyon Road Traffic Study', 'or phasing out the project', 'the County and will be finalizing the design.', 'assessments.', 'shade structures at Malibu Bluffs Park.', 'of the assessment district to June 30, 2022.', 'Westward Beach Road Repair Project', 'the agreement.', 'Commission in February.', 'Westward Beach Road Drainage Improvements Project', 'Metro.', 'management services was approved by Council on March 14, 2022.', 'amenities such as trash cans, benches, tables, and restrooms.', 'Storm Drain Master Plan', 'overall project costs.', 'Outdoor Warning Signs', 'February 1, 2021.', 'scheduled for the April 11, 2022 Council meeting.', 'cleared the project.', 'will begin in conjunction with the PCH Median Improvement', 'been finalized and incorporated into GIS.', 'agreement will be sent to City Council in March.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'modification of the schedule has been requested.', 'to finalize plans and specifications', 'and rejected all bids due to a budget shortfall', 'project will begin in conjunction with the PCH Median Improvement', 'Civic Center Water Treatment Facility Phase 2', 'program.', 'construction bids.', 'project and will submit to the County for review.', "Council's direction.", 'assessment district will be created.', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'March 2022', 'management.']}}

exec(code, env_args)
