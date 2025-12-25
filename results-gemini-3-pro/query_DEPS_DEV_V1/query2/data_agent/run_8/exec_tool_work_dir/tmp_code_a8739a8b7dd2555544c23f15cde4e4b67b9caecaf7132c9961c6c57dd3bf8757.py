code = """import json
import re

# Load data
with open(locals()['var_function-call-15464599018766236292'], 'r') as f:
    packages = json.load(f)
with open(locals()['var_function-call-15464599018766236039'], 'r') as f:
    mappings = json.load(f)
with open(locals()['var_function-call-15464599018766235786'], 'r') as f:
    project_infos = json.load(f)

debug_info = {}

# Filter packages strictly
valid_packages = set()
for p in packages:
    try:
        licenses = json.loads(p['Licenses'])
        version_info = json.loads(p['VersionInfo'])
        
        # Check License (MIT)
        has_mit = False
        if isinstance(licenses, list):
            for l in licenses:
                if 'MIT' in l:
                    has_mit = True
                    break
        
        # Check Release
        is_release = version_info.get('IsRelease', False)
        
        if has_mit and is_release:
            valid_packages.add((p['Name'], p['Version']))
    except Exception as e:
        pass

debug_info['valid_packages_count'] = len(valid_packages)
debug_info['sample_valid_package'] = list(valid_packages)[0] if valid_packages else None

# Find relevant ProjectNames
target_projects = set()
for m in mappings:
    if (m['Name'], m['Version']) in valid_packages:
        target_projects.add(m['ProjectName'])

debug_info['target_projects_count'] = len(target_projects)
debug_info['sample_target_projects'] = list(target_projects)[:5] if target_projects else None

# Check matching in project_infos
matched_count = 0
sample_text = project_infos[0].get('Project_Information', '') if project_infos else ""

matches = []
for entry in project_infos:
    text = entry.get('Project_Information', '')
    potential_names = re.findall(r'\b[a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+\b', text)
    for name in potential_names:
        if name in target_projects:
            matches.append(name)
            matched_count += 1
            break

debug_info['matched_projects_in_info'] = matched_count
debug_info['sample_matches'] = matches[:5]
debug_info['first_info_text'] = sample_text

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-18382953924067546539': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-18382953924067545130': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-1141334543695048906': [{'count_star()': '770'}], 'var_function-call-15464599018766236292': 'file_storage/function-call-15464599018766236292.json', 'var_function-call-15464599018766236039': 'file_storage/function-call-15464599018766236039.json', 'var_function-call-15464599018766235786': 'file_storage/function-call-15464599018766235786.json', 'var_function-call-16826417345324770412': []}

exec(code, env_args)
