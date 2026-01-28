code = """import json

# Load funding data (> $50,000)
funding_json = locals()['var_functions.query_db:98']
with open(funding_json, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_json = locals()['var_functions.query_db:5']
with open(civic_json, 'r') as f:
    civic_docs = json.load(f)

# Create funded project name set
design_status_count = 0
funded_names = set(rec['Project_Name'].lower() for rec in funding_records)

# Find design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section using simple search
    design_section_start = text.find('Capital Improvement Projects (Design)')
    if design_section_start == -1:
        continue
    
    # Get remainder of text after design section header
    after_design = text[design_section_start:]
    
    # Find where construction section starts
    construction_start = after_design.find('Capital Improvement Projects (Construction)')
    if construction_start == -1:
        design_section_text = after_design
    else:
        design_section_text = after_design[:construction_start]
    
    # Extract lines that could be project names
    lines = design_section_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or 'CID:' in line:
            continue
        
        # Check if line contains project-related words
        line_lower = line.lower()
        has_keywords = any(word in line_lower for word in ['road','drive','avenue','project','repair','drain','park','walkway'])
        skip_words = any(word in line_lower for word in ['schedule','updates','advertise','construction'])
        
        if has_keywords and not skip_words:
            # Clean project name
            clean_name = line.split('- ')[0] if '- ' in line else line
            clean_name = clean_name.split(':')[0] if ':' in clean_name else clean_name
            clean_name = ' '.join(clean_name.split())
            
            if len(clean_name) > 10:
                design_projects.append(clean_name)

# Remove duplicates and check matches
unique_design = list(set(design_projects))

# Count projects that have funding
for project_name in unique_design:
    if project_name.lower() in funded_names:
        design_status_count += 1

print('__RESULT__:')
print(design_status_count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_projects_over_50k': 276, 'project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Discussion', 'Dume Drive and Fernhill Drive Speed Humps Project', 'Encinal Canyon 60-inch Storm Drain Repairs', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Harbor Vista Curb Return', 'Kanan Dume Biofilter', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Retaining Wall Repair Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Legacy Park Paver Repair Project', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Malibu Seafood Undercrossing', 'Michael Landon Center HVAC Replacement Project', 'Michael Landon Center Roof Replacement Project', 'Outdoor Warning Signs', 'Outdoor Warning Sirens (FEMA)', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'PCH Median Improvements Project', 'PCH Overhead Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'Point Dume Decomposed Granite Walkway Repair Project', 'Point Dume Walkway Repairs', 'Recommended Action', 'Storm Drain Master Plan', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Playground Resurfacing', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Playground Resurfacing', 'Vehicle Protection Devices', 'Westward Beach Road Drainage Improvements Project', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'project_471', 'project_307', 'project_166', 'project_426', 'project_158', 'project_123', 'project_124', 'project_491', 'project_41', 'project_249', 'project_36', 'project_390', 'project_273', 'project_66', 'project_338', 'project_244', 'project_282', 'project_85', 'project_136', 'project_447', 'project_109', 'project_277', 'project_387', 'project_205', 'project_192', 'project_225', 'project_232', 'project_62', 'project_127', 'project_33', 'project_174', 'project_302', 'project_284', 'project_118', 'project_441', 'project_113', 'project_4', 'project_37', 'project_31', 'project_35', 'project_17', 'project_170', 'project_264', 'project_143', 'project_343', 'project_479', 'project_461', 'project_371', 'project_296', 'project_125', 'project_402', 'project_415', 'project_49', 'project_50', 'project_500', 'project_221', 'project_28', 'project_345', 'project_335', 'project_51', 'project_32', 'project_99', 'project_410', 'project_230', 'project_72', 'project_424', 'project_493', 'project_227', 'project_469', 'project_26', 'project_420', 'project_8', 'project_48', 'project_425', 'project_86', 'project_247', 'project_206', 'project_432', 'project_468', 'project_195', 'project_2', 'project_233', 'project_147', 'project_384', 'project_285', 'project_250', 'project_80', 'project_388', 'project_486', 'project_347', 'project_480', 'project_245', 'project_258', 'project_342', 'project_42', 'project_96', 'project_477', 'project_305', 'project_430', 'project_121', 'project_394', 'project_330', 'project_21', 'project_452', 'project_215', 'project_299', 'project_423', 'project_154', 'project_38', 'project_5', 'project_289', 'project_303', 'project_276', 'project_365', 'project_309', 'project_397', 'project_126', 'project_190', 'project_146', 'project_336', 'project_484', 'project_279', 'project_466', 'project_438', 'project_294', 'project_145', 'project_108', 'project_399', 'project_259', 'project_496', 'project_129', 'project_478', 'project_355', 'project_114', 'project_416', 'project_144', 'project_29', 'project_20', 'project_242', 'project_378', 'project_177', 'project_274', 'project_495', 'project_95', 'project_111', 'project_444', 'project_79', 'project_383', 'project_204', 'project_406', 'project_412', 'project_92', 'project_64', 'project_315', 'project_449', 'project_91', 'project_359', 'project_270', 'project_159', 'project_451', 'project_61', 'project_319', 'project_208', 'project_46', 'project_106', 'project_201', 'project_172', 'project_458', 'project_482', 'project_57', 'project_317', 'project_431', 'project_231', 'project_59', 'project_494', 'project_408', 'project_457', 'project_18', 'project_325', 'project_165', 'project_131', 'project_252', 'project_138', 'project_196', 'project_372', 'project_364', 'project_149', 'project_193', 'project_361', 'project_153', 'project_348', 'project_89', 'project_464', 'project_392', 'project_183', 'project_389', 'project_409', 'project_488', 'project_499', 'project_308', 'project_376', 'project_386', 'project_178', 'project_222', 'project_216', 'project_77', 'project_84', 'project_337', 'project_87', 'project_332', 'project_401', 'project_187', 'project_255', 'project_71', 'project_107', 'project_304', 'project_320', 'project_228', 'project_391', 'project_101', 'project_75', 'project_356', 'project_474', 'project_202', 'project_151', 'project_213']}, 'var_functions.execute_python:14': {'count': 276, 'first_20': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Discussion', 'Dume Drive and Fernhill Drive Speed Humps Project', 'Encinal Canyon 60-inch Storm Drain Repairs', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Harbor Vista Curb Return', 'Kanan Dume Biofilter', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Retaining Wall Repair Project']}, 'var_functions.execute_python:16': {'total_documents': 5, 'sample_document_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:48': {'funding_type': "<class 'dict'>", 'funding_keys': ['total_projects_over_50k', 'project_names'], 'civic_path_type': "<class 'str'>", 'civic_path_value': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:64': {'type': "<class 'str'>", 'is_string': True, 'length': 38, 'starts_with': 'file_storage/functions.query_db:0.json'}, 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.execute_python:94': {'record_count': 276, 'sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}, 'var_functions.query_db:98': 'file_storage/functions.query_db:98.json'}

exec(code, env_args)
