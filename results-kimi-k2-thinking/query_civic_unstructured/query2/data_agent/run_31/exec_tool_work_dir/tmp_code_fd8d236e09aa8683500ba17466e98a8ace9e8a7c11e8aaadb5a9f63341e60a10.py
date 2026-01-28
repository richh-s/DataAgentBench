code = """import json
import pandas as pd

# Load the civic documents
civic_path = var_functions.query_db:20
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print("Civic documents loaded:", len(civic_docs))

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for park projects with completion in 2022
    text_lower = text.lower()
    
    # Check if document contains both park references and 2022 completion
    if 'park' in text_lower and 'completed' in text_lower and '2022' in text_lower:
        # Extract lines containing park project information
        lines = text.split('\n')
        project_name = None
        
        for line in lines:
            line_lower = line.lower()
            
            # Look for project name (title case, contains park/project)
            if ('park' in line_lower and 
                (line.istitle() or '"' in line) and
                len(line.strip()) > 10):
                project_name = line.strip('"').strip()
            
            # Look for completion information
            if project_name and 'completed' in line_lower and '2022' in line_lower:
                park_projects_2022.append({
                    'project_name': project_name,
                    'filename': filename
                })
                project_name = None

# Also search for specific known park projects
known_park_projects = [
    'Bluffs Park Shade Structure',
    'Legacy Park',
    'Malibu Bluffs Park',
    'Trancas Canyon Park',
    'Point Dume'
]

for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    filename = doc.get('filename', '')
    
    if 'completed' in text_lower and '2022' in text_lower:
        for known_proj in known_park_projects:
            if known_proj.lower() in text_lower:
                # Check if already added
                exists = any(p['project_name'].lower() == known_proj.lower() 
                           for p in park_projects_2022)
                if not exists:
                    park_projects_2022.append({
                        'project_name': known_proj,
                        'filename': filename
                    })

print("Park projects completed in 2022 found:", len(park_projects_2022))

# Create a list of project names
project_names_list = []
for proj in park_projects_2022:
    name = proj['project_name']
    print(f"- {name}")
    project_names_list.append(name)

# Also include similar variations that might exist in funding table
additional_names = []
for name in project_names_list:
    if 'Bluffs Park Shade Structure' in name:
        additional_names.append('Bluffs Park Shade Structure')
    elif 'Legacy Park' in name:
        additional_names.extend(['Legacy Park Benches and Arbors Renovation', 
                                'Legacy Park Paver Repair Project'])
    elif 'Malibu Bluffs Park' in name:
        additional_names.extend(['Malibu Bluffs Park South Walkway', 
                                'Malibu Bluffs Park South Walkway Repairs'])

all_park_names = list(set(project_names_list + additional_names))

result_data = {
    'project_count': len(park_projects_2022),
    'project_names': all_park_names
}

print("__RESULT__:")
print(json.dumps(result_data))"""

env_args = {'var_functions.execute_python:0': {'collection': 'civic_docs', 'filter': {'text': {'$regex': 'park', '$options': 'i'}}, 'projection': {'filename': 1, 'text': 1}}, 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
