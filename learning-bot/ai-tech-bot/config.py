# Set your name
NAME = "Chinmay"

# Choose your OpenAI Model (Chat only) - GPT-3.5 Turbo is 13x cheaper than GPT-4
MODEL_NAME = "gpt-3.5-turbo"

# Word count for keyword summaries (the longer the more detailed the summaries will be)
WORD_COUNT = '200'

# Define category limits for the trending keywords - it will grab by top count first (check safron.io to look over your options)
CATEGORY_LIMITS = {
    "Platforms & Search Engines": 2,
    "Companies & Organizations": 2,
    "Concepts & Methods": 5,
    "Frameworks & Libraries": 5,
    "Tools & Services": 3,
    "AI Models & Assistants": 2,
}

# Set your keywords of interest - should always be there regardless if they are trending yesterday or not
KEYWORDS_OF_INTEREST = ["NLP", "Hacker News", "Django", "Climate Change", "Transformers", "AGI"]

# Set a category as something that is always there - categories grabs the highest count rather than if trending
CATEGORIES_OF_INTEREST = []

########## SES Email Configs - Make sure you change these ########

SOURCE_EMAIL = 'noreply@chinsays.xyz' 
TO_ADRESS = 'taniyapopat05@gmail.com'
AWS_REGION_NAME = 'us-east-2'


