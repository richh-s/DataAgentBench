code = """import json, pandas as pd

# Load metadata
metadata_path = var_call_lO8ZwQLmx9Y9IEIM65ZQE55T
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

# Load articles
articles_path = var_call_peNznCa8rzhVcOW1fPlxBLeC
with open(articles_path, 'r') as f:
    articles = json.load(f)

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

# Ensure types
md_df['article_id'] = md_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Filter year 2015
md_df['year'] = md_df['publication_date'].str.slice(0,4).astype(int)
md_2015 = md_df[md_df['year'] == 2015]

# Join
df = md_2015.merge(art_df, on='article_id', how='inner')

# Simple rule-based classifier for World vs other categories
# Keywords for categories (very rough)
world_kw = ['iraq','war','election','president','minister','government','united nations','un','attack','killed','palestinian','israel','eu','china','japan','russia','conflict','bomb','police','protest','violence','taliban','afghanistan']

business_kw = ['stock','stocks','shares','markets','economy','economic','bank','interest rate','oil','trade','ipo','fund','investment','investors','dollar','euro','currency','market']

sports_kw = ['football','nba','nfl','mlb','soccer','tennis','golf','olympics','cricket','baseball','basketball','hockey','cup','tournament','league','coach','team','player']

sci_kw = ['researchers','scientists','technology','software','hardware','computer','space','nasa','physics','biotech','genome','genetic','medical','vaccine','astronomy','science','scientific']


def classify(row):
    text = (str(row['title']) + ' ' + str(row['description'])).lower()
    def has_kw(kws):
        return any(k in text for k in kws)
    # Prioritize non-Business to avoid over-classifying markets as world
    if has_kw(sports_kw):
        return 'Sports'
    if has_kw(sci_kw):
        return 'Science/Technology'
    if has_kw(world_kw):
        return 'World'
    if has_kw(business_kw):
        return 'Business'
    # Default guess World for general news
    return 'World'

df['category'] = df.apply(classify, axis=1)

world_df = df[df['category'] == 'World']

counts = world_df.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = None
else:
    top_region = counts.idxmax()
    result = top_region

res_json = json.dumps(result)

print('__RESULT__:')
print(res_json)"""

env_args = {'var_call_lO8ZwQLmx9Y9IEIM65ZQE55T': 'file_storage/call_lO8ZwQLmx9Y9IEIM65ZQE55T.json', 'var_call_peNznCa8rzhVcOW1fPlxBLeC': 'file_storage/call_peNznCa8rzhVcOW1fPlxBLeC.json'}

exec(code, env_args)
