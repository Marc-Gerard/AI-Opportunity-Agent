from scraper import scrape_website
from agent import analyze_website

def main():
    url = input("Enter a website URL to analyze: ")
    
    print("\nScraping website...")
    content = scrape_website(url)
    
    print("Analyzing with AI...\n")
    report = analyze_website(content, url)
    
    print("=" * 50)
    print("BUSINESS OPPORTUNITY REPORT")
    print("=" * 50)
    print(report)
    print("=" * 50)

if __name__ == "__main__":
    main()