code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-8170898954798864343'], 'r') as f:
    packages_data = json.load(f)
df_packages = pd.DataFrame(packages_data)

with open(locals()['var_function-call-9880616322736191733'], 'r') as f:
    mapping_data = json.load(f)
df_mapping = pd.DataFrame(mapping_data)

with open(locals()['var_function-call-8466107741308955836'], 'r') as f:
    info_data = json.load(f)
df_info = pd.DataFrame(info_data)

# Process Packages
df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
df_latest = df_packages.sort_values(['Name', 'UpstreamPublishedAt'], ascending=[True, False]).drop_duplicates('Name', keep='first')

# Process Mapping
df_mapping = df_mapping.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])

# Process Project Info
def extract_info(text):
    name_match = re.search(r'(?:project|name)\s+(?:is\s+)?(?:named\s+)?(?:hosted\s+on\s+GitHub\s+under\s+the\s+name\s+)?([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)', text, re.IGNORECASE)
    stars_match1 = re.search(r'([\d,]+)\s+stars', text, re.IGNORECASE)
    stars_match2 = re.search(r'stars\s+count\s+of\s+([\d,]+)', text, re.IGNORECASE)
    
    name = name_match.group(1) if name_match else None
    
    stars = 0
    if stars_match2:
        stars = int(stars_match2.group(1).replace(',', ''))
    elif stars_match1:
        stars = int(stars_match1.group(1).replace(',', ''))
        
    return name, stars

extracted = df_info['Project_Information'].apply(extract_info)
df_info_extracted = pd.DataFrame(extracted.tolist(), columns=['ProjectName', 'Stars'])
df_info_extracted = df_info_extracted.dropna(subset=['ProjectName'])
df_info_extracted = df_info_extracted.groupby('ProjectName')['Stars'].max().reset_index()

# Merge
merged = pd.merge(df_latest, df_mapping, on=['Name', 'Version'], how='inner')
final = pd.merge(merged, df_info_extracted, on='ProjectName', how='inner')

# Sort
final = final.sort_values(['Stars', 'Name'], ascending=[False, True])
top_10 = final[['Name', 'Version', 'Stars', 'ProjectName']].head(10).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-2557747426360575779': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-8170898954798864343': 'file_storage/function-call-8170898954798864343.json', 'var_function-call-9880616322736191733': 'file_storage/function-call-9880616322736191733.json', 'var_function-call-8466107741308955836': 'file_storage/function-call-8466107741308955836.json', 'var_function-call-16012428326548668287': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}], 'var_function-call-12085323872354770526': [{'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dollarshaveclub/cli>1.5.6>lodash', 'Version': '4.17.4', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.7.1>lodash', 'Version': '4.17.5', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.5.7>lodash', 'Version': '4.17.4', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.8.0>lodash', 'Version': '4.17.5', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>2.0.0>lodash', 'Version': '4.17.11', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.6.0>lodash', 'Version': '4.17.4', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}], 'var_function-call-14147342399592802608': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'Stars': 57236, 'ProjectName': 'strapi/strapi'}, {'Name': '@dolsem/actioncable', 'Version': '7.0.0-alpha-simple-5s-step-backoff', 'Stars': 55319, 'ProjectName': 'rails/rails'}, {'Name': '@dreampie/semantic-ui', 'Version': '2.2.11', 'Stars': 51069, 'ProjectName': 'semantic-org/semantic-ui'}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Stars': 42407, 'ProjectName': 'quilljs/quill'}, {'Name': '@dothq/styled-components', 'Version': '6.0.2-prealpha-dot', 'Stars': 39660, 'ProjectName': 'styled-components/styled-components'}, {'Name': '@dynasty/styled-components', 'Version': '3.2.1', 'Stars': 39660, 'ProjectName': 'styled-components/styled-components'}, {'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'Stars': 38715, 'ProjectName': 'leaflet/leaflet'}, {'Name': '@docid/monaco-editor', 'Version': '0.31.1-x1', 'Stars': 36025, 'ProjectName': 'microsoft/monaco-editor'}]}

exec(code, env_args)
