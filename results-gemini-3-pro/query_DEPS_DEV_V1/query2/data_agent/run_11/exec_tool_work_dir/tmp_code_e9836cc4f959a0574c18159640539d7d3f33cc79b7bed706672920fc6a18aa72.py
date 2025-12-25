code = """import json
import re

# Load valid packages
with open(locals()['var_function-call-17508330561994061544'], 'r') as f:
    valid_pkgs_list = json.load(f)
    valid_pkgs = set((p['Name'], p['Version']) for p in valid_pkgs_list)

# Load project info
with open(locals()['var_function-call-5512869477547604686'], 'r') as f:
    project_infos = json.load(f)

# Parse project info
project_stats = {} # {ProjectName: fork_count}

# Helper to parse fork count
def get_forks(text):
    # patterns
    # "... and 0 forks." -> "and (\d+) forks"
    # "... forks count of 988." -> "forks count of (\d+)"
    # "... forked 12 times." -> "forked (\d+) times"
    # "... 1 fork." -> "(\d+) fork"
    
    # Combined regex logic
    # Try specific patterns first
    m = re.search(r'forks count of ([\d,]+)', text)
    if m: return int(m.group(1).replace(',', ''))
    
    m = re.search(r'forked ([\d,]+) times', text)
    if m: return int(m.group(1).replace(',', ''))
    
    m = re.search(r'and ([\d,]+) forks?', text)
    if m: return int(m.group(1).replace(',', ''))
    
    m = re.search(r'([\d,]+) forks?', text) # generic fallback, might match other things
    # But usually "X open issues, Y stars, and Z forks" -> Z is last.
    # Be careful.
    
    # Let's stick to context aware regexes
    # "X forks" or "X fork"
    # Usually preceded by space.
    matches = re.findall(r'([\d,]+) forks?', text)
    if matches:
        # The text usually ends with forks count. Or has "stars, and X forks"
        # Let's look at the text structure.
        # "X open issues, Y stars, and Z forks"
        # If multiple matches, usually the last one?
        # Let's try to match "and X forks" or ", X forks"
        m2 = re.search(r'(?:and|,)\s+([\d,]+)\s+forks?', text)
        if m2: return int(m2.group(1).replace(',', ''))
        
        return int(matches[-1].replace(',', ''))
    
    return 0

# Helper to parse project name
def get_name(text):
    # "The project owner/repo ..."
    # "The project named owner/repo ..."
    # "The GitHub project owner/repo ..."
    # "The project is hosted on GitHub under the name owner/repo ..."
    
    # Greedy match for owner/repo
    # Pattern: \b[\w.-]+/[\w.-]+\b
    # But filtering out "open-source/library" or generic terms is hard if they look like names.
    # However, usually the project name appears early.
    
    # Specific extraction
    m = re.search(r'under the name ([\w.-]+/[\w.-]+)', text)
    if m: return m.group(1)
    
    # "The project <name>"
    m = re.search(r'The (?:GitHub )?project (?:named )?([\w.-]+/[\w.-]+)', text)
    if m: return m.group(1)
    
    # "The project on GitHub, named <name>"
    m = re.search(r'named ([\w.-]+/[\w.-]+)', text)
    if m: return m.group(1)

    return None

for pi in project_infos:
    txt = pi['Project_Information']
    name = get_name(txt)
    forks = get_forks(txt)
    if name:
        project_stats[name] = forks

# Load mappings
# The file contains a list of dicts: Name, Version, ProjectName
with open(locals()['var_function-call-11150717459793807436'], 'r') as f:
    mappings = json.load(f)

# Filter mappings
candidate_projects = set()
for m in mappings:
    if (m['Name'], m['Version']) in valid_pkgs:
        candidate_projects.add(m['ProjectName'])

# Intersect
final_projects = []
for proj in candidate_projects:
    if proj in project_stats:
        final_projects.append({'project': proj, 'forks': project_stats[proj]})
    # else: project info not found (maybe filtered out or missing in project_info table)

# Sort
final_projects.sort(key=lambda x: x['forks'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_projects[:5]))"""

env_args = {'var_function-call-2090987646599017399': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-6552111881093755275': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-17508330561994061544': 'file_storage/function-call-17508330561994061544.json', 'var_function-call-9709182247556147480': [{'count_star()': '591699'}], 'var_function-call-17495712327254216188': 176998, 'var_function-call-15411850235090304115': [{'count_star()': '770'}], 'var_function-call-5512869477547604686': 'file_storage/function-call-5512869477547604686.json', 'var_function-call-11150717459793807436': 'file_storage/function-call-11150717459793807436.json'}

exec(code, env_args)
