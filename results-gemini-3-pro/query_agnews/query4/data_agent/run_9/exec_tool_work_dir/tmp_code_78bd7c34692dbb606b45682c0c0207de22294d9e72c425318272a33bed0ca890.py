code = """import json
import collections

# Load 2015 metadata
path_2015 = locals()['var_function-call-5697295960649122566']
with open(path_2015, 'r') as f:
    data_2015 = json.load(f)
    # data_2015 is a dict {"count": ..., "ids": ...}. 
    # Wait, the previous output format for 2015 data was derived from var_function-call-1215328646878465519
    # which was the raw SQL result.
    # In my last execute_python, I printed {"count": 6696, "ids": [...]}.
    # BUT I need the REGION too.
    # The raw SQL result (var_function-call-1215328646878465519) contains region.
    # So I should load the SQL result file directly.

path_sql_result = locals()['var_function-call-1215328646878465519']
with open(path_sql_result, 'r') as f:
    articles_2015_list = json.load(f)

# Create a map id -> region
# Ensure IDs are strings to match Mongo results if necessary, or normalize both.
# Mongo preview showed "article_id": "0". SQL preview showed "article_id": "13".
# So normalize to string.
id_to_region = {str(item['article_id']): item['region'] for item in articles_2015_list}

# Load all articles
path_articles = locals()['var_function-call-13855097331714845970']
with open(path_articles, 'r') as f:
    all_articles = json.load(f)

# Define keywords
keywords = {
    "World": [
        "president", "minister", "prime minister", "official", "leader", "parliament", "congress", "senate", "election", "vote", "poll", "campaign",
        "war", "military", "army", "troop", "soldier", "rebel", "militia", "attack", "bomb", "blast", "explosion", "kill", "death", "dead", "injured", "casualty",
        "peace", "treaty", "agreement", "talks", "summit", "meeting", "negotiation", "diplomacy", "diplomat", "envoy", "ambassador",
        "united nations", "un", "nato", "eu", "european union", "au", "african union",
        "government", "state", "federal", "national", "agency", "court", "judge", "law", "legal", "ban", "rule",
        "iraq", "iran", "syria", "afghanistan", "israel", "palestine", "gaza", "egypt", "libya", "sudan", "russia", "ukraine", "china", "korea", "japan", "india", "pakistan", "usa", "uk", "france", "germany", "italy", "spain", "canada", "australia", "brazil", "mexico"
    ],
    "Sports": [
        "sport", "game", "match", "tournament", "championship", "league", "cup", "series", "season", "playoff", "final",
        "team", "club", "squad", "player", "athlete", "coach", "manager", "referee", "umpire",
        "win", "won", "lose", "lost", "beat", "defeat", "draw", "tie", "score", "goal", "point", "run", "touchdown", "basket",
        "football", "soccer", "baseball", "basketball", "tennis", "golf", "cricket", "rugby", "hockey", "racing", "driver", "olympic", "medal"
    ],
    "Business": [
        "business", "company", "firm", "corporation", "corp", "inc", "ltd", "enterprise", "startup",
        "market", "stock", "share", "equity", "bond", "trade", "exchange", "wall street", "dow jones", "nasdaq",
        "economy", "economic", "financial", "finance", "bank", "central bank", "fed", "reserve", "interest rate", "inflation", "deflation", "recession", "gdp",
        "profit", "loss", "revenue", "earnings", "quarter", "result", "dividend",
        "price", "cost", "value", "expensive", "cheap", "sale", "buy", "sell", "merge", "acquisition", "deal", "bid", "offer",
        "oil", "gas", "energy", "crude", "barrel",
        "ceo", "cfo", "executive", "chairman", "director", "manager"
    ],
    "Sci/Tech": [
        "science", "scientific", "scientist", "research", "study", "discovery", "experiment", "lab", "laboratory",
        "technology", "tech", "technological", "computer", "computing", "software", "hardware", "internet", "web", "online", "digital", "cyber", "network", "server", "data",
        "phone", "mobile", "cellphone", "smartphone", "tablet", "device", "gadget", "app", "application",
        "space", "nasa", "astronomy", "planet", "mars", "moon", "star", "galaxy", "orbit", "satellite", "launch", "rocket",
        "biology", "biological", "chemistry", "chemical", "physics", "physical", "medical", "medicine", "drug", "virus", "disease", "health", "cancer", "gene", "genetic", "dna",
        "microsoft", "google", "apple", "ibm", "intel", "facebook", "twitter", "amazon", "yahoo"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                scores[cat] += 1
    # Return category with max score
    # If tie, prioritize World > Sports > Business > Sci/Tech (arbitrary, or based on list order)
    # Actually, let's just use max.
    if max(scores.values()) == 0:
        return "Unknown"
    return max(scores, key=scores.get)

world_region_counts = collections.Counter()

for article in all_articles:
    aid = str(article.get('article_id'))
    if aid in id_to_region:
        title = article.get('title', '')
        desc = article.get('description', '')
        full_text = title + " " + desc
        category = classify(full_text)
        
        if category == "World":
            region = id_to_region[aid]
            world_region_counts[region] += 1

print("__RESULT__:")
print(json.dumps(world_region_counts))"""

env_args = {'var_function-call-1215328646878465519': 'file_storage/function-call-1215328646878465519.json', 'var_function-call-5697295960649122566': 'file_storage/function-call-5697295960649122566.json', 'var_function-call-17915382622122817248': [{'_id': '6944f27fa4e85337bc21f1cb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f27fa4e85337bc21f1cc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f27fa4e85337bc21f1cd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f27fa4e85337bc21f1ce', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f27fa4e85337bc21f1cf', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13990457352297790652': {'type': 'list', 'count': 5}, 'var_function-call-13855097331714845970': 'file_storage/function-call-13855097331714845970.json'}

exec(code, env_args)
