code = """import json
import re
from collections import defaultdict

# Read the file path for civic documents
civic_docs_file = locals()['var_functions.query_db:6']

# Load the full civic documents data
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

print('Loaded ' + str(len(civic_docs_data)) + ' civic documents')

# Function to extract projects from document text
def extract_projects_from_text(text, filename):
    projects = []
    text_lines = text.split('\n')
    
    current_section = None
    current_project = None
    
    # Patterns to identify sections
    section_patterns = [
        (r'Capital Improvement Projects \(Design\)', 'design', 'capital'),
        (r'Capital Improvement Projects \(Construction\)', 'construction', 'capital'),
        (r'Capital Improvement Projects \(Not Started\)', 'not started', 'capital'),
        (r'Disaster Recovery Projects', 'disaster_general', 'disaster'),
        (r'Disaster Recovery Projects \(Design\)', 'design', 'disaster'),
        (r'Disaster Recovery Projects \(Construction\)', 'construction', 'disaster'),
        (r'Disaster Recovery Projects \(Not Started\)', 'not started', 'disaster')
    ]
    
    # Patterns for disaster-related identifiers
    disaster_indicators = [
        'fema',
        'caloes',
        'caljpia',
        'woolsey fire',
        'disaster',
        'emergency',
        'recovery'
    ]
    
    # Topic keywords
    topic_keywords = [
        'park', 'road', 'fema', 'fire', 'emergency warning', 'drainage', 'storm drain',
        'highway', 'bridge', 'playground', 'water treatment', 'guardrail', 'culvert',
        'retaining wall', 'traffic', 'signal', 'solar', 'roof', 'skate park', 'walkway',
        'bench', 'arbor', 'biofilter', 'berm', 'curb', 'street', 'asphalt', 'concrete'
    ]
    
    i = 0
    while i < len(text_lines):
        line = text_lines[i].strip()
        i += 1
        
        # Check for section headers
        section_matched = False
        for pattern, status, proj_type in section_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                current_section = {'status': status, 'type': proj_type}
                section_matched = True
                break
        
        if section_matched:
            continue
            
        # Skip empty lines and common non-project lines
        if not line or line.startswith('(') or line.startswith('•') or line.startswith('●') or line.startswith('■'):
            continue
            
        # Skip update and schedule lines
        if any(keyword in line.lower() for keyword in ['updates', 'project schedule', 'estimated schedule', 'project description']):
            continue
            
        # Look for project names (typically bolded or capitalized)
        # Project names often appear before update/schedule sections
        if current_section and len(line) > 10 and not line.startswith('Page'):
            # Check if this looks like a project name
            # Usually title case or all caps, doesn't start with common non-project words
            non_project_starts = ['Staff', 'City', 'Project', 'On', 'Complete', 'Begin', 'Advertise', 'This project', 'The project']
            should_skip = False
            for start in non_project_starts:
                if line.startswith(start):
                    should_skip = True
                    break
            
            if not should_skip and not any(marker in line for marker in ['%', '$', ':', ';']):
                # This could be a project name
                project_name = line.strip()
                
                # Determine project type and topics
                proj_type = current_section['type']
                
                # Check if it's actually a disaster project based on name
                lower_name = project_name.lower()
                if any(indicator in lower_name for indicator in disaster_indicators):
                    proj_type = 'disaster'
                
                # Determine status
                if current_section['status'] == 'construction':
                    status = 'in_progress'  # Will refine later
                elif current_section['status'] == 'design':
                    status = 'design'
                elif current_section['status'] == 'not started':
                    status = 'not_started'
                else:
                    status = 'unknown'
                
                # Extract topics from project name
                topics = []
                for keyword in topic_keywords:
                    if keyword.lower() in lower_name:
                        topics.append(keyword)
                
                # Add disaster/emergency topics if applicable
                if 'fema' in lower_name or 'fema' in text.lower():
                    topics.append('fema')
                if 'emergency' in lower_name:
                    topics.append('emergency')
                
                topics = list(set(topics))  # Remove duplicates
                
                projects.append({
                    'Project_Name': project_name,
                    'topic': ','.join(topics) if topics else '',
                    'type': proj_type,
                    'status': status,
                    'st': '',  # Would need more parsing for dates
                    'et': '',
                    'source_file': filename
                })
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs_data:
    projects = extract_projects_from_text(doc.get('text', ''), doc.get('filename', ''))
    all_projects.extend(projects)

print('Extracted ' + str(len(all_projects)) + ' projects from documents')

# Show some sample projects
for i, proj in enumerate(all_projects[:10]):
    print(f"{i+1}. {proj['Project_Name'][:60]} - Type: {proj['type']}, Status: {proj['status']}, Topics: {proj['topic']}")

# Filter for projects related to emergency or FEMA
emergency_projects = []
for proj in all_projects:
    topics = proj['topic'].lower().split(',') if proj['topic'] else []
    name_lower = proj['Project_Name'].lower()
    
    if 'emergency' in topics or 'fema' in topics or 'emergency' in name_lower or 'fema' in name_lower:
        emergency_projects.append(proj)

print('\nFound ' + str(len(emergency_projects)) + ' emergency/FEMA related projects')

for i, proj in enumerate(emergency_projects[:10]):
    print(f"{i+1}. {proj['Project_Name'][:60]} - Type: {proj['type']}, Status: {proj['status']}")

print('__RESULT__:')
print(json.dumps({
    'total_projects': len(all_projects),
    'emergency_projects': len(emergency_projects),
    'sample_projects': all_projects[:20],
    'emergency_sample': emergency_projects[:20]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '23', 'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '27', 'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '30', 'Project_Name': 'Discussion', 'Funding_Source': 'International Aid', 'Amount': '80000'}, {'Funding_ID': '31', 'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project', 'Funding_Source': 'Philanthropic Donation', 'Amount': '90000'}, {'Funding_ID': '32', 'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs', 'Funding_Source': 'Municipal Fund', 'Amount': '56000'}, {'Funding_ID': '33', 'Project_Name': 'Encinal Canyon Road Drainage Improvements', 'Funding_Source': 'Non-profit Organization Grant', 'Amount': '34000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '36', 'Project_Name': 'Encinal Canyon Road Repairs', 'Funding_Source': 'State Development Grant', 'Amount': '47000'}, {'Funding_ID': '37', 'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '40', 'Project_Name': 'Harbor Vista Curb Return', 'Funding_Source': 'Social Impact Investment', 'Amount': '91000'}, {'Funding_ID': '41', 'Project_Name': 'Kanan Dume Biofilter', 'Funding_Source': 'Venture Capital Fund', 'Amount': '56000'}, {'Funding_ID': '42', 'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '45', 'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000'}, {'Funding_ID': '46', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 50, 'civic_docs': 19, 'fema_docs': 19, 'emergency_docs': 5}}

exec(code, env_args)
