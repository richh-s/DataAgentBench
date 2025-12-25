code = """import json
import re

# Load data
file_path = locals()['var_function-call-9958536016874276289']
with open(file_path, 'r') as f:
    data = json.load(f)

projects = []

for entry in data:
    info = entry.get('Project_Information', '')
    
    # Extract Stars
    # Pattern: "X stars" where X can be "1,234" or "1234"
    stars_match = re.search(r'([\d,]+) stars', info)
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        stars = int(stars_str)
    else:
        stars = 0
        
    # Extract Project Name
    # Heuristics based on examples
    # 1. "The project owner/repo "
    # 2. "The project named owner/repo "
    # 3. "The GitHub project owner/repo "
    # 4. "The GitHub project named owner/repo "
    # 5. "under the name owner/repo"
    # 6. "project owner/repo on GitHub"
    
    # We can try to look for the "owner/repo" pattern directly if it helps, 
    # but we must be careful not to match URLs.
    # Pattern for name: alphanumeric, hyphen, underscore, dot / same
    
    name = None
    # Try specific prefixes first
    prefixes = [
        r"The project named ([^\s,]+)",
        r"The GitHub project named ([^\s,]+)",
        r"under the name ([^\s,]+)",
        r"The project ([^\s,]+) is",
        r"The project ([^\s,]+) on",
        r"The GitHub project ([^\s,]+) currently",
    ]
    
    for p in prefixes:
        m = re.search(p, info)
        if m:
            name = m.group(1)
            # Clean up trailing punctuation if any (though \s, excludes comma, maybe period?)
            name = name.rstrip('.')
            break
            
    if not name:
        # Fallback: find any "owner/repo" that isn't part of a URL
        # Excluding http/https
        candidates = re.findall(r'(?<!https://)(?<!http://)(?:github\.com/)?([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', info)
        # Filter out common false positives if any? 
        # Usually the first valid looking one is it.
        for c in candidates:
            if c not in ['github.com', 'open-source']:
                name = c
                break
                
    if name and stars > 0:
        projects.append({'ProjectName': name, 'Stars': stars})

# Sort by Stars DESC
projects.sort(key=lambda x: x['Stars'], reverse=True)

# Top 20
top_projects = projects[:20]

print("__RESULT__:")
print(json.dumps(top_projects))"""

env_args = {'var_function-call-1166278330031295683': ['project_info', 'project_packageversion'], 'var_function-call-1166278330031292934': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-7576608018762177383': [{'COUNT(*)': '661372'}], 'var_function-call-7576608018762178154': [{'count_star()': '597602'}], 'var_function-call-7576608018762174829': [{'count_star()': '770'}], 'var_function-call-9958536016874276289': 'file_storage/function-call-9958536016874276289.json'}

exec(code, env_args)
