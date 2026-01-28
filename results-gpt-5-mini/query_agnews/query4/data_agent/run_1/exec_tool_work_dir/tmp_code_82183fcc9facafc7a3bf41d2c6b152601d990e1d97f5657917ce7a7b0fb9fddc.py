code = """import json
import pandas as pd

# Load data from storage file paths
with open(var_call_LlJ1rGMyyeNyiIXPHSNp3fIl, 'r', encoding='utf-8') as f:
    articles = json.load(f)
with open(var_call_bS09D4b93rH8QdbcafMn2ZW3, 'r', encoding='utf-8') as f:
    metadata_2015 = json.load(f)

# Create DataFrames
df_articles = pd.DataFrame(articles)
df_meta = pd.DataFrame(metadata_2015)

# Ensure article_id types align
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_meta['article_id'] = df_meta['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Fill NaNs
df['title'] = df['title'].fillna('')
df['description'] = df['description'].fillna('')

# Build classifier
import re

def count_keywords(text, keywords):
    text = text.lower()
    cnt = 0
    for kw in keywords:
        # escape kw for regex
        pattern = r"\\b" + re.escape(kw.lower()) + r"\\b"
        cnt += len(re.findall(pattern, text))
    return cnt

world_kw = ['president','government','election','reuters','iraq','syria','china','russia','minister','army','military','bomb','attack','killed','refugee','embassy','border','sanctions','conflict','protest','peace','ceasefire','court','trial','diplomat','foreign','country','countries','international','global','afp','ap','united states','u.s.','u.s','world']

sports_kw = ['football','soccer','match','score','goal','tournament','olympic','olympics','nba','mlb','nfl','cricket','tennis','player','coach','season','win','defeat','race','stadium','cup','league','goalkeeper','striker','batting','innings','victory']

business_kw = ['market','stocks','shares','ipo','company','firm','economy','bank','finance','profit','invest','investment','merger','acquisition','dollar','billion','money','dow','nasdaq','oil prices','oil','stock']

sci_kw = ['scientist','research','study','technology','computer','google','ibm','nasa','science','researchers','drug','clinical','lab','scientific','software','internet','email','e-mail','robot','space','tech','phone','mobile','engineer']

categories = []
for _, row in df.iterrows():
    text = (row.get('title','') + ' ' + row.get('description','')).lower()
    scores = {
        'World': count_keywords(text, world_kw),
        'Sports': count_keywords(text, sports_kw),
        'Business': count_keywords(text, business_kw),
        'Science/Technology': count_keywords(text, sci_kw)
    }
    # If all zero, fallback: simple heuristics based on words occurrence
    if sum(scores.values()) == 0:
        # fallback: if any country name appear, world
        if re.search(r"\\b(us|u\.s\.|united states|china|russia|india|europe|africa|asia|south america|north america|europe)\\b", text):
            cat = 'World'
        elif re.search(r"\\b(google|ibm|nasa|scientists|research)\\b", text):
            cat = 'Science/Technology'
        elif re.search(r"\\b(football|match|league|score|player)\\b", text):
            cat = 'Sports'
        else:
            # default to World (broad news)
            cat = 'World'
    else:
        # choose max score; tie-breaker priority World > Business > Sports > Science
        max_score = max(scores.values())
        # find categories with max
        winners = [k for k,v in scores.items() if v==max_score]
        if len(winners) == 1:
            cat = winners[0]
        else:
            priority = ['World','Business','Sports','Science/Technology']
            for p in priority:
                if p in winners:
                    cat = p
                    break
    categories.append(cat)

df['category'] = categories

# Count World by region
world_df = df[df['category']=='World']
counts = world_df.groupby('region').size().to_dict()

# Determine top region
if counts:
    top_region = max(counts.items(), key=lambda x: x[1])[0]
    top_count = counts[top_region]
else:
    top_region = None
    top_count = 0

result = {'top_region': top_region, 'count': top_count, 'counts': counts}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LlJ1rGMyyeNyiIXPHSNp3fIl': 'file_storage/call_LlJ1rGMyyeNyiIXPHSNp3fIl.json', 'var_call_bS09D4b93rH8QdbcafMn2ZW3': 'file_storage/call_bS09D4b93rH8QdbcafMn2ZW3.json'}

exec(code, env_args)
