code = """import json
import re

# Load data
with open(locals()['var_function-call-15544277681777691989'], 'r') as f:
    project_info_list = json.load(f)

# Parse stars
project_stars = {}
star_pattern = re.compile(r'(\d{1,3}(?:,\d{3})*|\d+) stars')
name_pattern = re.compile(r'project (?:is hosted on [Gg]it[Hh]ub under the name |named |is a [Gg]it[Hh]ub repository named |[Gg]it[Hh]ub project |)([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+)')

for item in project_info_list:
    text = item.get('Project_Information', '')
    star_match = star_pattern.search(text)
    if star_match:
        stars = int(star_match.group(1).replace(',', ''))
    else:
        stars = 0
    
    name_match = name_pattern.search(text)
    project_name = None
    if name_match:
        project_name = name_match.group(1)
    else:
        potential_names = re.findall(r'([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+)', text)
        for name in potential_names:
            if 'github.com' not in name and ' ' not in name and name.count('/') == 1:
                project_name = name
                break
    
    if project_name:
        project_stars[project_name] = stars

# Sort by stars
sorted_projects = sorted(project_stars.items(), key=lambda x: x[1], reverse=True)
print("__RESULT__:")
print(json.dumps(sorted_projects[:10]))"""

env_args = {'var_function-call-12765485723334907841': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-17147732955394573907': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15577757168303682267': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-937565460572617818': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-286075157217291400': [{'count_star()': '770'}], 'var_function-call-10477545953268515295': [{'count_star()': '597602'}], 'var_function-call-12664628000143355413': [{'COUNT(*)': '661372'}], 'var_function-call-15544277681777691989': 'file_storage/function-call-15544277681777691989.json', 'var_function-call-6976636483719730651': 'file_storage/function-call-6976636483719730651.json', 'var_function-call-10135252399049147363': 'file_storage/function-call-10135252399049147363.json', 'var_function-call-4071359497304908248': [{'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'Project': 'sveltejs/svelte', 'Stars': 73499}, {'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'Project': 'sveltejs/svelte', 'Stars': 73499}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Project': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Project': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'Package': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'Project': 'strapi/strapi', 'Stars': 57236}], 'var_function-call-13368052741083968285': [{'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'Project': 'sveltejs/svelte', 'Stars': 73499}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Project': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'Package': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'Project': 'strapi/strapi', 'Stars': 57236}, {'Package': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Project': 'quilljs/quill', 'Stars': 42407}, {'Package': '@dothq/styled-components', 'Version': '6.0.2-prealpha-dot', 'Project': 'styled-components/styled-components', 'Stars': 39660}], 'var_function-call-15791329988958986514': {'lodash_pkg_count': 0, 'lodash_pv_count': 0}, 'var_function-call-13220690937153064747': {'pkg_len': 661372, 'pv_len': 597602}, 'var_function-call-13699943594931582652': {'lodash': False, 'react': False, 'svelte': False, 'tailwindcss': False, 'express': False, 'vue': False}}

exec(code, env_args)
