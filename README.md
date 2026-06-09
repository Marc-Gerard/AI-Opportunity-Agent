# AI Opportunity Agent

An AI agent that analyzes any website and generates a business opportunity report.

## What it does
Give it any URL and it will return:
- What the site sells and who it targets
- Potential friction points
- Missed opportunities
- 3 concrete recommendations

## Tech stack
- Python
- Groq (llama-3.3-70b-versatile)
- BeautifulSoup4

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your keys:
4. `GROQ_API_KEY=your_key_here`

5. Run: `python main.py`

## Example output
Analyzed [ShipFast](https://shipfa.st) and identified 4 friction points
and 3 actionable recommendations in under 10 seconds.
