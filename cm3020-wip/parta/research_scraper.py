import requests
from bs4 import BeautifulSoup
import pandas as pd
from scholarly import scholarly
from collections import defaultdict
import json
import re
from typing import List, Dict, Tuple

class ResearchScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.papers = []

    def search_google_scholar(self, query: str, num_results: int = 10) -> List[Dict]:
            """
            Search Google Scholar for research papers.
            """
            try:
                search_query = scholarly.search_pubs(query)
                results = []
                for i, paper in enumerate(search_query):
                    if i >= num_results:
                        break
                    
                    paper_dict = {
                        'title': paper['bib'].get('title', ''),
                        'authors': paper['bib'].get('author', ''),
                        'year': paper['bib'].get('year', ''),
                        'citations': paper.get('num_citations', 0),
                        'abstract': paper['bib'].get('abstract', ''),
                        'url': paper['pub_url']
                    }
                    results.append(paper_dict)
                    
                return results
            except Exception as e:
                print(f"Error in Google Scholar search: {e}")
                return []

    def analyze_papers(self, papers: List[Dict], keywords: List[str]) -> Dict:
        """
        Analyze papers for specific keywords and create a summary.
        """
        analysis = {
            'total_papers': len(papers),
            'papers_by_year': defaultdict(int),
            'keyword_frequency': defaultdict(int),
            'top_cited_papers': [],
            'key_findings': []
        }

        for paper in papers:
            # Count papers by year
            if paper['year']:
                analysis['papers_by_year'][paper['year']] += 1

            # Analyze keyword frequency in abstracts
            if paper['abstract']:
                for keyword in keywords:
                    if keyword.lower() in paper['abstract'].lower():
                        analysis['keyword_frequency'][keyword] += 1

            # Track citation counts
            if paper['citations']:
                analysis['top_cited_papers'].append({
                    'title': paper['title'],
                    'citations': paper['citations']
                })

        # Sort top cited papers
        analysis['top_cited_papers'] = sorted(
            analysis['top_cited_papers'],
            key=lambda x: x['citations'],
            reverse=True
        )[:5]

        return analysis

    def extract_quotes(self, text: str, keywords: List[str]) -> List[str]:
        """
        Extract relevant quotes from text based on keywords.
        """
        quotes = []
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        for sentence in sentences:
            if any(keyword.lower() in sentence.lower() for keyword in keywords):
                quotes.append(sentence.strip())
                
        return quotes

    def generate_report(self, analysis: Dict, quotes: List[str]) -> str:
        """
        Generate a formatted research report.
        """
        report = "Research Analysis Report\n"
        report += "=====================\n\n"
        
        # Summary statistics
        report += f"Total papers analyzed: {analysis['total_papers']}\n\n"
        
        # Publication trends
        report += "Publication Trends:\n"
        for year, count in sorted(analysis['papers_by_year'].items()):
            report += f"- {year}: {count} papers\n"
        report += "\n"
        
        # Keyword frequency
        report += "Keyword Frequency:\n"
        for keyword, freq in analysis['keyword_frequency'].items():
            report += f"- '{keyword}': found in {freq} papers\n"
        report += "\n"
        
        # Top cited papers
        report += "Most Cited Papers:\n"
        for paper in analysis['top_cited_papers']:
            report += f"- {paper['title']} (Citations: {paper['citations']})\n"
        report += "\n"
        
        # Relevant quotes
        report += "Key Quotes:\n"
        for quote in quotes:
            report += f"- \"{quote}\"\n"
            
        return report

def main():
    # Initialize scraper
    scraper = ResearchScraper()
    
    # Search parameters
    search_query = "AI game playing systems research justification"
    keywords = ["game playing", "artificial intelligence", "justification", 
                "research motivation", "benefits", "applications"]
    
    # Perform search
    papers = scraper.search_google_scholar(search_query)
    
    # Analyze results
    analysis = scraper.analyze_papers(papers, keywords)
    
    # Extract quotes from abstracts
    all_quotes = []
    for paper in papers:
        quotes = scraper.extract_quotes(paper['abstract'], keywords)
        all_quotes.extend(quotes)
    
    # Generate report
    report = scraper.generate_report(analysis, all_quotes)
    
    # Save results
    with open('research_report.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    
    with open('raw_data.json', 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent=2)

if __name__ == "__main__":
    main()