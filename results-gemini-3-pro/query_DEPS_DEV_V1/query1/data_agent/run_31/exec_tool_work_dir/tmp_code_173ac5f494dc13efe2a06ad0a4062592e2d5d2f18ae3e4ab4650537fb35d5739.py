code = """import json
import re

# Load files
with open('var_function-call-924986185008826223.json' if 'var_function-call-924986185008826223.json' in locals() else locals()['var_function-call-924986185008826223']) as f:
    packages = json.load(f)
with open('var_function-call-9589161961333179106.json' if 'var_function-call-9589161961333179106.json' in locals() else locals()['var_function-call-9589161961333179106']) as f:
    mappings = json.load(f)
with open('var_function-call-5288765901383785079.json' if 'var_function-call-5288765901383785079.json' in locals() else locals()['var_function-call-5288765901383785079']) as f:
    infos = json.load(f)

# Process Packages
pkg_dict = {}
for p in packages:
    if p['Name'] not in pkg_dict:
        pkg_dict[p['Name']] = p['Version']

# Process Mappings
map_dict = {}
for m in mappings:
    map_dict[(m['Name'], m['Version'])] = m['ProjectName']

# Process Infos
info_dict = {}
# Regex patterns
# Pattern: \b([a-zA-Z0-9\-_.]+/[a-zA-Z0-9\-_.]+)\b
re_repo_pat = r"\b([a-zA-Z0-9\-_.]+/[a-zA-Z0-9\-_.]+)\b"
# Pattern for stars
re_stars_pat = r"(?:with|has|of)\s+a?\s*total\s+of\s+([\d,]+)\s+stars|([\d,]+)\s+stars|stars\s+count\s+of\s+([\d,]+)"

for item in infos:
    text = item['Project_Information']
    
    # Extract Repo
    matches = re.findall(re_repo_pat, text)
    project_name = None
    for m in matches:
        if m.lower() == 'n/a': continue
        project_name = m
        break
    
    if not project_name:
        continue

    # Extract Stars
    # Remove newlines for easier matching
    clean_text = text.replace('\n', ' ')
    match = re.search(re_stars_pat, clean_text)
    found_stars = 0
    if match:
        s_str = match.group(1) or match.group(2) or match.group(3)
        if s_str:
            try:
                found_stars = int(s_str.replace(',', ''))
            except:
                pass
    
    info_dict[project_name] = found_stars

# Join
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

# Sort
final_list.sort(key=lambda x: x['Stars'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_list[:5]))"""

env_args = {'var_function-call-13107224867645322399': ['packageinfo'], 'var_function-call-13107224867645322232': ['project_info', 'project_packageversion'], 'var_function-call-13406757670486128015': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-16148261186527528638': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-924986185008826223': 'file_storage/function-call-924986185008826223.json', 'var_function-call-9589161961333179106': 'file_storage/function-call-9589161961333179106.json', 'var_function-call-5288765901383785079': 'file_storage/function-call-5288765901383785079.json'}

exec(code, env_args)
