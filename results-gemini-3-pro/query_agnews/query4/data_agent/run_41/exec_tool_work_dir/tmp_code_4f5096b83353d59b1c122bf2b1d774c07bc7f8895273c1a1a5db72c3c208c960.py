code = """# Re-run the classification logic (I need to redefine it since locals are lost)
# and print samples.

import json
import pandas as pd

# Load data
meta_file = locals()['var_function-call-1582016694630583511']
with open(meta_file, 'r') as f:
    meta_data = json.load(f)

articles_file = locals()['var_function-call-7872325636991379809']
with open(articles_file, 'r') as f:
    articles_data = json.load(f)

df_meta = pd.DataFrame(meta_data)
df_meta['article_id'] = df_meta['article_id'].astype(int)

df_articles = pd.DataFrame(articles_data)
df_articles['article_id'] = df_articles['article_id'].astype(int)

df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

keywords = {
    "World": [
        "iraq", "iran", "syria", "gaza", "israel", "palestinian", "afghanistan", "pakistan", "russia", "ukraine", 
        "china", "korea", "japan", "europe", "africa", "asia", "middle east", "un", "united nations", 
        "war", "military", "troops", "rebels", "insurgents", "attack", "bomb", "blast", "killed", "dead", "death", 
        "president", "prime minister", "minister", "official", "government", "parliament", "election", "vote", 
        "diplomat", "treaty", "peace", "agreement", "talks", "summit", "protest", "police", "crisis", "disaster", 
        "hostage", "terror", "qaeda", "nato", "nuclear", "army", "soldier", "security", "leader", "court", "trial",
        "putin", "bush", "kerry", "blair", "sharon", "arafat", "law", "rights", "aid", "refugee", "storm", "hurricane",
        "tsunami", "earthquake", "typhoon", "crash", "plane", "accident", "fire", "flood", "virus", "flu", "h5n1"
    ],
    "Sports": [
        "sport", "game", "match", "team", "club", "player", "coach", "manager", "league", "cup", "tournament", 
        "championship", "champion", "olympic", "athens", "gold", "medal", "win", "won", "victory", "lose", "lost", 
        "score", "goal", "points", "football", "soccer", "basketball", "nba", "baseball", "mlb", "hockey", "nhl", 
        "tennis", "golf", "racing", "f1", "formula one", "driver", "athlete", "stadium", "season", "final", 
        "yankees", "red sox", "lakers", "arsenal", "real madrid", "manchester", "united", "chelsea", "liverpool"
    ],
    "Business": [
        "business", "market", "stock", "share", "wall street", "dow", "nasdaq", "economy", "economic", "financial", 
        "finance", "bank", "invest", "investment", "money", "dollar", "euro", "yen", "currency", "trade", "deal", 
        "merger", "acquisition", "buyout", "profit", "loss", "earnings", "revenue", "sales", "price", "oil", "crude", 
        "barrel", "fed", "federal reserve", "rates", "interest", "inflation", "growth", "company", "corp", "inc", 
        "ceo", "cfo", "executive", "job", "employment", "hiring", "layoff", "gm", "ford", "boeing", "airline", 
        "retail", "consumer", "spending"
    ],
    "Sci_Tech": [
        "technology", "tech", "science", "computer", "software", "hardware", "internet", "web", "online", "net", 
        "cyber", "virus", "hacker", "security", "microsoft", "google", "yahoo", "apple", "intel", "ibm", "linux", 
        "windows", "browser", "search engine", "phone", "mobile", "wireless", "telecom", "space", "nasa", 
        "astronaut", "orbit", "mars", "moon", "planet", "galaxy", "astronomy", "research", "study", "scientist", 
        "laboratory", "drug", "fda", "cancer", "disease", "medical", "health", "gene", "dna", "robot", "broadband"
    ]
}

def categorize(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    scores = {k: 0 for k in keywords}
    
    if "world cup" in text:
        scores["Sports"] += 10
    if "google ipo" in text:
        scores["Business"] += 5
    
    for cat, words in keywords.items():
        for w in words:
            if w in text:
                scores[cat] += 1
                
    return max(scores, key=scores.get)

df['category'] = df.apply(categorize, axis=1)

# Sample of World articles
sample_world = df[df['category'] == 'World'][['title', 'category']].head(5).to_dict(orient='records')

# Sample of ambiguous ones?
# Let's check region counts again
counts = df[df['category'] == 'World']['region'].value_counts()

print("__RESULT__:")
print(json.dumps({"sample_world": sample_world, "counts": counts.to_dict()}))"""

env_args = {'var_function-call-1582016694630583511': 'file_storage/function-call-1582016694630583511.json', 'var_function-call-8744902824758175518': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_function-call-607457671861550025': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13447300378826587909': {'sample': [], 'total_merged': 0}, 'var_function-call-139548067748344674': {'count': 5, 'first_ids': ['0', '1', '2', '3', '4']}, 'var_function-call-334473003933806917': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-11380162437698432518': [{'_id': '69451e3040c0657ea168210a', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-7872325636991379809': 'file_storage/function-call-7872325636991379809.json', 'var_function-call-1485038341254323483': [{'region': 'South America', 'count': 682}, {'region': 'North America', 'count': 654}, {'region': 'Asia', 'count': 652}, {'region': 'Europe', 'count': 645}, {'region': 'Africa', 'count': 633}]}

exec(code, env_args)
