code = """import json
import re

# Load data
with open(locals()['var_function-call-15464599018766236292'], 'r') as f:
    packages = json.load(f)
with open(locals()['var_function-call-15464599018766236039'], 'r') as f:
    mappings = json.load(f)
with open(locals()['var_function-call-15464599018766235786'], 'r') as f:
    project_infos = json.load(f)

# valid_packages
valid_packages = set()
for p in packages:
    valid_packages.add((p['Name'], p['Version']))

# target_projects
target_projects = set()
for m in mappings:
    if (m['Name'], m['Version']) in valid_packages:
        target_projects.add(m['ProjectName'])

# Parse Project Info
fork_pattern = re.compile(r'(\d+(?:,\d+)*) forks')
valid_project_metrics = []

for entry in project_infos:
    text = entry.get('Project_Information', '')
    if not text:
        continue
        
    # Find fork count
    fork_match = fork_pattern.search(text)
    if fork_match:
        forks_str = fork_match.group(1).replace(',', '')
        forks = int(forks_str)
    else:
        forks = 0
        
    # Find project name by splitting
    words = text.split()
    found_name = None
    for w in words:
        # Strip common punctuation
        clean_w = w.strip(".,;:()[]{}'\"")
        if clean_w in target_projects:
            found_name = clean_w
            break
            
    if found_name:
        valid_project_metrics.append({
            'ProjectName': found_name,
            'Forks': forks
        })

# Deduplicate
final_metrics = {}
for item in valid_project_metrics:
    p = item['ProjectName']
    f = item['Forks']
    if p not in final_metrics or f > final_metrics[p]:
        final_metrics[p] = f

# Sort and take top 5
sorted_projects = sorted(final_metrics.items(), key=lambda x: x[1], reverse=True)
top_5 = [p[0] for p in sorted_projects[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-18382953924067546539': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-18382953924067545130': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-1141334543695048906': [{'count_star()': '770'}], 'var_function-call-15464599018766236292': 'file_storage/function-call-15464599018766236292.json', 'var_function-call-15464599018766236039': 'file_storage/function-call-15464599018766236039.json', 'var_function-call-15464599018766235786': 'file_storage/function-call-15464599018766235786.json', 'var_function-call-16826417345324770412': [], 'var_function-call-9328321450557075305': {'valid_packages_count': 0, 'sample_valid_package': None, 'target_projects_count': 0, 'sample_target_projects': None, 'matched_projects_in_info': 0, 'sample_matches': [], 'first_info_text': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, 'var_function-call-2931262593813026115': [], 'var_function-call-10200247261718120357': {'valid_packages_count': 84744, 'sample_valid_package': ['@ecodev/natural', '10.1.0'], 'target_projects_count': 5430, 'sample_target_projects': ['ecoba-vn/tas-feature', 'taixw2/dx', 'mirrorjs/mirror', 'dyegoaurelio/react-scale-text', 'ecreeth/tw.macro'], 'matched_projects_in_info': 0, 'sample_matches': [], 'extracted_samples': [['The project lberrocal/npm-packages-template is hos', []], ['The project leaflet/leaflet on GitHub is a popular', []], ['The project leaflet/leaflet.fullscreen on GitHub c', []], ['The project leaflet/leaflet.markercluster is hoste', []], ['The project leandrowd/react-responsive-carousel on', []]]}}

exec(code, env_args)
