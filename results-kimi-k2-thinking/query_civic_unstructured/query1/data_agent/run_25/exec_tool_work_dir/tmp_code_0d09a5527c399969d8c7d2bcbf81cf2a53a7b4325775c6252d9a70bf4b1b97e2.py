code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:82']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_documents = json.load(f)

# Create a set of funded project names (lowercase)
funded_names = set()
for record in funding_records:
    funded_names.add(record['Project_Name'].lower())

# Extract design projects from civic documents
design_project_names = []

for doc in civic_documents:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Find the design section
    design_section_start = text_lower.find('capital improvement projects (design)')
    if design_section_start == -1:
        continue
    
    # Find where design section ends
    construction_section_start = text_lower.find('capital improvement projects (construction)', design_section_start)
    if construction_section_start == -1:
        construction_section_start = len(text_lower)
    
    # Get the design section text
    design_section = text[design_section_start:construction_section_start]
    design_section_lower = design_section.lower()
    
    # Look for project names (lines that look like project names)
    lines = design_section.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith('(') or line.startswith('CID:'):
            continue
        
        line_lower = line.lower()
        
        # Skip header lines
        if 'project schedule' in line_lower or 'updates:' in line_lower or 'complete design' in line_lower:
            continue
        
        # Look for lines with project-related words
        project_words = ['road', 'drive', 'avenue', 'street', 'project', 'improvement', 'repair', 'drain', 'park']
        has_project_word = any(word in line_lower for word in project_words)
        
        if has_project_word:
            # Clean up the project name
            clean_name = line
            if clean_name.endswith(':'):
                clean_name = clean_name[:-1]
            clean_name = clean_name.strip()
            
            if len(clean_name) > 10 and not clean_name.isupper():
                design_project_names.append(clean_name)

# Remove duplicates
design_project_names = list(set(design_project_names))

# Count funded design projects
funded_count = 0
for proj in design_project_names:
    proj_lower = proj.lower()
    if proj_lower in funded_names:
        funded_count += 1

print('__RESULT__:')
print(funded_count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_projects_over_50k': 276, 'project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Discussion', 'Dume Drive and Fernhill Drive Speed Humps Project', 'Encinal Canyon 60-inch Storm Drain Repairs', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Harbor Vista Curb Return', 'Kanan Dume Biofilter', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Retaining Wall Repair Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Legacy Park Paver Repair Project', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Malibu Seafood Undercrossing', 'Michael Landon Center HVAC Replacement Project', 'Michael Landon Center Roof Replacement Project', 'Outdoor Warning Signs', 'Outdoor Warning Sirens (FEMA)', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'PCH Median Improvements Project', 'PCH Overhead Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'Point Dume Decomposed Granite Walkway Repair Project', 'Point Dume Walkway Repairs', 'Recommended Action', 'Storm Drain Master Plan', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Playground Resurfacing', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Playground Resurfacing', 'Vehicle Protection Devices', 'Westward Beach Road Drainage Improvements Project', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'project_471', 'project_307', 'project_166', 'project_426', 'project_158', 'project_123', 'project_124', 'project_491', 'project_41', 'project_249', 'project_36', 'project_390', 'project_273', 'project_66', 'project_338', 'project_244', 'project_282', 'project_85', 'project_136', 'project_447', 'project_109', 'project_277', 'project_387', 'project_205', 'project_192', 'project_225', 'project_232', 'project_62', 'project_127', 'project_33', 'project_174', 'project_302', 'project_284', 'project_118', 'project_441', 'project_113', 'project_4', 'project_37', 'project_31', 'project_35', 'project_17', 'project_170', 'project_264', 'project_143', 'project_343', 'project_479', 'project_461', 'project_371', 'project_296', 'project_125', 'project_402', 'project_415', 'project_49', 'project_50', 'project_500', 'project_221', 'project_28', 'project_345', 'project_335', 'project_51', 'project_32', 'project_99', 'project_410', 'project_230', 'project_72', 'project_424', 'project_493', 'project_227', 'project_469', 'project_26', 'project_420', 'project_8', 'project_48', 'project_425', 'project_86', 'project_247', 'project_206', 'project_432', 'project_468', 'project_195', 'project_2', 'project_233', 'project_147', 'project_384', 'project_285', 'project_250', 'project_80', 'project_388', 'project_486', 'project_347', 'project_480', 'project_245', 'project_258', 'project_342', 'project_42', 'project_96', 'project_477', 'project_305', 'project_430', 'project_121', 'project_394', 'project_330', 'project_21', 'project_452', 'project_215', 'project_299', 'project_423', 'project_154', 'project_38', 'project_5', 'project_289', 'project_303', 'project_276', 'project_365', 'project_309', 'project_397', 'project_126', 'project_190', 'project_146', 'project_336', 'project_484', 'project_279', 'project_466', 'project_438', 'project_294', 'project_145', 'project_108', 'project_399', 'project_259', 'project_496', 'project_129', 'project_478', 'project_355', 'project_114', 'project_416', 'project_144', 'project_29', 'project_20', 'project_242', 'project_378', 'project_177', 'project_274', 'project_495', 'project_95', 'project_111', 'project_444', 'project_79', 'project_383', 'project_204', 'project_406', 'project_412', 'project_92', 'project_64', 'project_315', 'project_449', 'project_91', 'project_359', 'project_270', 'project_159', 'project_451', 'project_61', 'project_319', 'project_208', 'project_46', 'project_106', 'project_201', 'project_172', 'project_458', 'project_482', 'project_57', 'project_317', 'project_431', 'project_231', 'project_59', 'project_494', 'project_408', 'project_457', 'project_18', 'project_325', 'project_165', 'project_131', 'project_252', 'project_138', 'project_196', 'project_372', 'project_364', 'project_149', 'project_193', 'project_361', 'project_153', 'project_348', 'project_89', 'project_464', 'project_392', 'project_183', 'project_389', 'project_409', 'project_488', 'project_499', 'project_308', 'project_376', 'project_386', 'project_178', 'project_222', 'project_216', 'project_77', 'project_84', 'project_337', 'project_87', 'project_332', 'project_401', 'project_187', 'project_255', 'project_71', 'project_107', 'project_304', 'project_320', 'project_228', 'project_391', 'project_101', 'project_75', 'project_356', 'project_474', 'project_202', 'project_151', 'project_213']}, 'var_functions.execute_python:14': {'count': 276, 'first_20': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Discussion', 'Dume Drive and Fernhill Drive Speed Humps Project', 'Encinal Canyon 60-inch Storm Drain Repairs', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Harbor Vista Curb Return', 'Kanan Dume Biofilter', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Retaining Wall Repair Project']}, 'var_functions.execute_python:16': {'total_documents': 5, 'sample_document_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:48': {'funding_type': "<class 'dict'>", 'funding_keys': ['total_projects_over_50k', 'project_names'], 'civic_path_type': "<class 'str'>", 'civic_path_value': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:64': {'type': "<class 'str'>", 'is_string': True, 'length': 38, 'starts_with': 'file_storage/functions.query_db:0.json'}, 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json'}

exec(code, env_args)
