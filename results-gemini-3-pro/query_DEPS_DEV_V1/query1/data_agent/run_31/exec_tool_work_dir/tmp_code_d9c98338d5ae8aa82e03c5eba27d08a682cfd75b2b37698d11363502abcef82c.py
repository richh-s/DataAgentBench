code = """import json
import re

# Load data from storage
with open(var_function_call_924986185008826223) as f:
    packages = json.load(f) # List of {Name, Version} (ranked by date)

with open(var_function_call_9589161961333179106) as f:
    mappings = json.load(f) # List of {Name, Version, ProjectName}

with open(var_function_call_5288765901383785079) as f:
    infos = json.load(f) # List of {Project_Information}

# 1. Process Packages: Get latest version for each Name
# The SQL query sorted by UpstreamPublishedAt DESC and ranked.
# We just need to take the first occurrence of each Name (since rank=1 is what we fetched)
# However, if there are multiple rank=1 rows (e.g. duplicates), we handle it.
pkg_dict = {}
for p in packages:
    if p['Name'] not in pkg_dict:
        pkg_dict[p['Name']] = p['Version']

# 2. Process Mappings: (Name, Version) -> ProjectName
map_dict = {}
for m in mappings:
    # Keying by Name and Version
    map_dict[(m['Name'], m['Version'])] = m['ProjectName']

# 3. Process Infos: ProjectName -> Stars
info_dict = {}
# Regex to capture `owner/repo`
# We avoid matching URLs like `github.com/...` if possible, but usually descriptions say "project owner/repo".
# A safe heuristic: look for token with exactly one slash, not starting with http/https.
# Pattern: word characters, dots, dashes, slash, word characters...
re_repo = re.compile(r'\b([a-zA-Z0-9\-_.]+/[a-zA-Z0-9\-_.]+)\b')

# Regex for stars
re_stars = re.compile(r'(?:with|has|of)\s+a?\s*total\s+of\s+([\d,]+)\s+stars|([\d,]+)\s+stars|stars\s+count\s+of\s+([\d,]+)')

for item in infos:
    text = item['Project_Information']
    
    # Extract Project Name
    # We iterate tokens or search.
    # The project name usually comes early or after "project".
    # Let's find all matches and pick the most likely one (usually the first one that isn't a common false positive).
    # In the preview, they are all clearly `owner/repo`.
    
    # Specific adjustment for "GitHub" which has no slash, but let's be careful not to match "NPM/..." if that appears.
    # The preview shows "lberrocal/npm-packages-template", "leaflet/leaflet".
    
    matches = re_repo.findall(text)
    project_name = None
    for m in matches:
        # Filter out common non-project tokens if any (unlikely with this pattern unless valid repo)
        # e.g. "and/or" - but words are \w.
        if m.lower() in ['n/a']: continue
        project_name = m
        break # Take the first valid-looking repo name
    
    if not project_name:
        continue

    # Extract Stars
    # Normalize text?
    # Matches:
    # 1. "total of X stars" -> group 1
    # 2. "X stars" -> group 2
    # 3. "stars count of X" -> group 3
    
    # We search the whole string
    # Because there might be multiple numbers (issues, forks), we need the one associated with stars.
    # The regex `([\d,]+)\s+stars` is quite specific.
    # But `stars count of ([\d,]+)` is also used.
    
    # Let's clean the text slightly to handle newlines etc if any.
    clean_text = text.replace('\n', ' ')
    
    found_stars = 0
    
    # Try the regex
    # We use search to find the first occurrence that matches any pattern
    # Note: Regex order in OR matters.
    # `([\d,]+)\s+stars` matches `0 stars`.
    # `stars count of ([\d,]+)` matches `stars count of 3761`.
    
    # Complex regex:
    # `(?:stars\s*(?:count)?\s*(?:of|:)?\s*|total\s+of\s+)([\d,]+)(?:\s+stars)?` ?? Too complex.
    
    # Let's stick to the groups defined in re_stars
    match = re_stars.search(clean_text)
    if match:
        # Find which group matched
        s_str = match.group(1) or match.group(2) or match.group(3)
        if s_str:
            try:
                found_stars = int(s_str.replace(',', ''))
            except:
                found_stars = 0
                
    info_dict[project_name] = found_stars

# 4. Join and Rank
final_list = []
for name, version in pkg_dict.items():
    proj_name = map_dict.get((name, version))
    if proj_name and proj_name in info_dict:
        stars = info_dict[proj_name]
        final_list.append({
            "Package": name,
            "Version": version,
            "Stars": stars
        })

# Sort by Stars desc
final_list.sort(key=lambda x: x['Stars'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_list[:5]))"""

env_args = {'var_function-call-13107224867645322399': ['packageinfo'], 'var_function-call-13107224867645322232': ['project_info', 'project_packageversion'], 'var_function-call-13406757670486128015': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-16148261186527528638': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-924986185008826223': 'file_storage/function-call-924986185008826223.json', 'var_function-call-9589161961333179106': 'file_storage/function-call-9589161961333179106.json', 'var_function-call-5288765901383785079': 'file_storage/function-call-5288765901383785079.json'}

exec(code, env_args)
