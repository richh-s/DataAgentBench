code = """import json
import pandas as pd

# Load the articles
file_path = locals()['var_function-call-5424179638557031609']
with open(file_path, 'r') as f:
    articles = json.load(f)

print(f"Total articles loaded: {len(articles)}")

# Define keywords
# Expanded lists based on common news categorization
keywords = {
    "Sports": [
        "sport", "sports", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", 
        "cricket", "rugby", "athlete", "coach", "stadium", "tournament", "championship", "cup", 
        "league", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "wta", "atp", "pga", "nascar", "f1", 
        "formula one", "racing", "swimming", "track and field", "marathon", "sprint", "team", "score", 
        "win", "loss", "victory", "defeat", "champion", "title", "playoff", "super bowl", "world series", 
        "stanley cup", "doping", "drug test", "referee", "umpire", "olympics", "olympic", "medal", "gold", 
        "silver", "bronze", "athens", "games", "match", "red sox", "yankees", "lakers", "bulls", "knicks", 
        "rangers", "giants", "cowboys", "patriots", "eagles", "steelers", "49ers", "raiders", "real madrid", 
        "barcelona", "manchester united", "arsenal", "liverpool", "chelsea", "bayern munich", "juventus", "milan",
        "inter", "f1", "nascar", "driver", "lap", "pole position", "grand prix", "wimbledon", "us open", "french open",
        "australian open", "davis cup", "fed cup", "ryder cup", "masters", "pga championship", "british open", "touchdown",
        "homerun", "goal", "penalty", "corner kick", "free kick", "yellow card", "red card", "offside", "foul", "inning",
        "quarterback", "pitcher", "striker", "defender", "midfielder", "goalkeeper", "manager", "contract", "trade", "draft"
    ],
    "Business": [
        "business", "economy", "market", "stock", "trade", "investment", "investor", "profit", "loss", "revenue", 
        "earnings", "share", "company", "corp", "corporation", "inc", "bank", "finance", "financial", "dollar", 
        "euro", "yen", "currency", "exchange", "rate", "inflation", "tax", "budget", "deficit", "debt", "loan", 
        "mortgage", "real estate", "retail", "sales", "consumer", "spending", "growth", "recession", "depression", 
        "job", "employment", "unemployment", "wage", "salary", "bonus", "ceo", "cfo", "executive", "manager", 
        "director", "board", "shareholder", "dividend", "merger", "acquisition", "deal", "contract", "offer", "bid", 
        "ipo", "public offering", "bond", "treasury", "fed", "federal reserve", "central bank", "interest rate", 
        "oil", "gas", "energy", "price", "cost", "production", "supply", "demand", "export", "import", "tariff", 
        "subsidy", "wto", "imf", "world bank", "nafta", "eu", "european union", "opec", "nyse", "nasdaq", "dow jones", 
        "s&p", "ftse", "nikkei", "hang seng", "wall street", "audit", "fraud", "scandal", "lawsuit", "settlement",
        "bankruptcy", "chapter 11", "restructuring", "layoff", "outsourcing", "offshoring", "union", "strike"
    ],
    "Sci/Tech": [
        "science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "digital", 
        "cyber", "network", "server", "data", "database", "cloud", "security", "virus", "worm", "trojan", "hacker", 
        "hacking", "encryption", "privacy", "password", "login", "user", "interface", "app", "application", "program", 
        "code", "coding", "programming", "developer", "engineer", "algorithm", "ai", "artificial intelligence", 
        "robot", "robotics", "automation", "machine learning", "mobile", "phone", "smartphone", "cellphone", "wireless", 
        "wifi", "bluetooth", "gps", "satellite", "space", "nasa", "esa", "rocket", "launch", "orbit", "planet", "star", 
        "galaxy", "universe", "astronomy", "physics", "chemistry", "biology", "genetics", "dna", "gene", "genome", 
        "cell", "bacteria", "virus", "disease", "medicine", "medical", "health", "doctor", "hospital", "drug", 
        "pharmaceutical", "biotech", "energy", "solar", "wind", "nuclear", "power", "battery", "electric", "car", 
        "vehicle", "engine", "motor", "microsoft", "google", "apple", "amazon", "facebook", "twitter", "intel", 
        "ibm", "oracle", "cisco", "dell", "hp", "linux", "windows", "macos", "android", "ios", "browser", "search engine"
    ],
    "World": [
        "world", "international", "politics", "government", "policy", "law", "legal", "court", "judge", "trial", 
        "jury", "verdict", "sentence", "prison", "jail", "crime", "police", "arrest", "suspect", "victim", "witness", 
        "investigation", "fbi", "cia", "intelligence", "security", "terrorism", "terrorist", "attack", "bomb", 
        "explosion", "blast", "war", "conflict", "battle", "fight", "military", "army", "navy", "air force", 
        "troops", "soldiers", "guerrilla", "rebel", "insurgent", "militia", "peace", "treaty", "agreement", "ceasefire", 
        "negotiation", "diplomacy", "diplomat", "ambassador", "embassy", "president", "prime minister", "chancellor", 
        "minister", "senator", "representative", "congress", "parliament", "election", "vote", "poll", "campaign", 
        "candidate", "party", "democrat", "republican", "labour", "conservative", "liberal", "socialist", "communist", 
        "dictator", "regime", "human rights", "refugee", "asylum", "immigration", "migration", "border", "customs", 
        "visa", "passport", "citizenship", "country", "nation", "state", "city", "town", "village", "iraq", "afghanistan", 
        "iran", "syria", "israel", "palestine", "gaza", "west bank", "jerusalem", "baghdad", "kabul", "tehran", "damascus", 
        "beirut", "cairo", "egypt", "libya", "sudan", "darfur", "africa", "asia", "europe", "america", "latin america", 
        "middle east", "russia", "china", "japan", "india", "pakistan", "korea", "north korea", "south korea", "united nations", 
        "un", "nato", "eu", "au"
    ]
}

# Classification function
def classify_article(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text: # simple substring match might be too aggressive (e.g. "us" in "virus")
                           # better: check word boundaries or rely on enough unique keywords
                # simple fix: pad text with spaces and check " kw "
                if f" {kw} " in f" {text} " or text.startswith(f"{kw} ") or text.endswith(f" {kw}"):
                    scores[cat] += 1
    
    # Heuristics for specific common words that might be ambiguous
    # "oil" -> Business (mostly)
    # "iraq" -> World
    # "game" -> Sports or Tech (video game) -> Context matters. 
    
    # Find max score
    max_score = -1
    best_cat = None
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
            # Tie breaking
            # If Sports is involved in tie, maybe check specific sports terms?
            # For now, let's just stick to the first one or use hierarchy
            # Order in dict: Sports, Business, Sci/Tech, World
            # If Sports is first, it wins tie.
            pass
            
    return best_cat, max_score, scores

sports_articles = []
for art in articles:
    cat, score, scores = classify_article(art.get('title', ''), art.get('description', ''))
    # Only consider it sports if score > 0
    if cat == "Sports" and score > 0:
        sports_articles.append(art)

print(f"Number of Sports articles found: {len(sports_articles)}")

# Find longest description
longest_desc_len = -1
best_article = None

for art in sports_articles:
    desc = art.get('description', '')
    if len(desc) > longest_desc_len:
        longest_desc_len = len(desc)
        best_article = art

result = {}
if best_article:
    result = {
        "title": best_article['title'],
        "description_length": longest_desc_len,
        "description": best_article['description']
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4105202590194221422': ['articles'], 'var_function-call-4105202590194223563': ['authors', 'article_metadata'], 'var_function-call-17850915415032394466': [{'_id': '69447340826b7850ce02734f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-17850915415032395251': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-4116783351500848285': [{'_id': '69447340826b7850ce02734f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447340826b7850ce027350', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447340826b7850ce027351', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447340826b7850ce027352', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447340826b7850ce027353', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12552155713391860353': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}], 'var_function-call-11673459665629763925': [{'_id': '69447340826b7850ce02734f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447340826b7850ce027350', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447340826b7850ce027351', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447340826b7850ce027352', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447340826b7850ce027353', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17308268192770250264': 'file_storage/function-call-17308268192770250264.json', 'var_function-call-5424179638557031609': 'file_storage/function-call-5424179638557031609.json'}

exec(code, env_args)
