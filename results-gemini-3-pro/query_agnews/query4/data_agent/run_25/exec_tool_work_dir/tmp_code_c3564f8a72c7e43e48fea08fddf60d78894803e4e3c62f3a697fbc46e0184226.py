code = """import json
import re
import random
import collections

# Load Data
with open(locals()['var_function-call-8192239243877575471'], 'r') as f:
    metadata_list = json.load(f)
with open(locals()['var_function-call-13229976580628931333'], 'r') as f:
    articles_list = json.load(f)

articles_map = {str(art['article_id']): art['title'] + " " + art['description'] for art in articles_list}

keywords = {
    "World": set([
        "president", "minister", "election", "parliament", "government", "official", "leader", 
        "war", "military", "troops", "army", "soldier", "rebel", "militia", "attack", "kill", "bomb", "blast", "explosion", 
        "terror", "hostage", "kidnap", "peace", "treaty", "nuclear", "weapon", "protest", "riot", "strike", 
        "storm", "hurricane", "flood", "earthquake", "tsunami", "crash", "disaster", "aid", "refugee", 
        "un", "nato", "eu", "iraq", "iran", "syria", "israel", "palestine", "gaza", "afghanistan", "pakistan", 
        "russia", "ukraine", "china", "korea", "sudan", "libya", "egypt", "venezuela", "turkey", "lebanon",
        "baghdad", "kabul", "tehran", "jerusalem", "beijing", "moscow", "pyongyang",
        "prime", "premier", "chancellor", "senate", "congress", "law", "legislation", "court", "judge", "police", 
        "arrest", "jail", "prison", "execution", "human", "rights", "insurgent", "guerrilla", "clash", "violence"
    ]),
    "Business": set([
        "market", "stock", "dow", "nasdaq", "invest", "trade", "economy", "dollar", "euro", "bank", "fed", "rate", 
        "inflation", "profit", "loss", "sales", "deal", "merger", "acquisition", "ipo", "share", "oil", "price", 
        "company", "corp", "inc", "business", "ceo", "manager", "google", "microsoft", "yahoo", "apple", "ibm", 
        "boeing", "airbus", "walmart", "retail", "financial", "finance", "sector", "industry", "revenue", "dividend"
    ]),
    "Sports": set([
        "sport", "game", "match", "team", "league", "cup", "olympic", "medal", "score", "win", "lose", "victory", 
        "defeat", "champion", "coach", "player", "football", "soccer", "basketball", "baseball", "hockey", "tennis", 
        "golf", "cricket", "athlete", "f1", "racing", "stadium", "season", "final", "semi"
    ]),
    "Sci_Tech": set([
        "science", "technology", "computer", "software", "internet", "web", "online", "mobile", "phone", "wireless", 
        "chip", "data", "server", "virus", "hacker", "space", "nasa", "orbit", "planet", "galaxy", "drug", "medicine", 
        "cancer", "disease", "study", "research", "scientist", "laboratory", "microsoft", "google", "apple", "intel", 
        "linux", "windows", "browser", "spam", "mail"
    ])
}

def classify(text):
    text = text.lower()
    tokens = re.findall(r'\w+', text)
    scores = {k: 0 for k in keywords}
    for t in tokens:
        for cat, kws in keywords.items():
            if t in kws:
                scores[cat] += 1
    
    if max(scores.values()) == 0:
        return "Unknown"
    return max(scores, key=scores.get)

counts = collections.defaultdict(int)
samples = []

for item in metadata_list:
    aid = str(item.get('article_id', ''))
    if aid in articles_map:
        content = articles_map[aid]
        cat = classify(content)
        counts[cat] += 1
        if len(samples) < 20:
            samples.append((content[:50], cat))

print("__RESULT__:")
print(json.dumps({"counts": counts, "samples": samples}))"""

env_args = {'var_function-call-8192239243877575471': 'file_storage/function-call-8192239243877575471.json', 'var_function-call-4285467361081759445': 6696, 'var_function-call-13346176432867388839': [{'_id': '69450821ec4d8e6298d328d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450821ec4d8e6298d328d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450821ec4d8e6298d328d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450821ec4d8e6298d328da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450821ec4d8e6298d328db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-152803809967091269': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13229976580628931333': 'file_storage/function-call-13229976580628931333.json', 'var_function-call-14357045956631284067': {'region': 'Africa', 'count': 27, 'all_counts': {'South America': 23, 'Europe': 21, 'Asia': 22, 'North America': 20, 'Africa': 27}}, 'var_function-call-2003783828452005932': 6696}

exec(code, env_args)
