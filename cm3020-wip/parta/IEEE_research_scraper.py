import requests
import pandas as pd
from collections import defaultdict
import json
import re
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import numpy as np
from tqdm import tqdm
from ratelimit import limits, sleep_and_retry

class IEEEResearchScraper:
    def __init__(self, api_key: str):
        """
        Initialize the IEEE Xplore scraper with your API key.
        
        Args:
            api_key: Your IEEE Xplore API key
        """
        self.api_key = api_key
        self.base_url = "http://ieeexploreapi.ieee.org/api/v1/search/articles"
        self.papers = []
        
    @sleep_and_retry
    @limits(calls=10, period=1)  # Rate limit: 10 calls per second
    def _make_api_request(self, params: Dict) -> Dict:
        """
        Make a rate-limited API request to IEEE Xplore.
        """
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'apikey': self.api_key
        }
        
        response = requests.get(self.base_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def search_ieee(self,
                   query: str,
                   max_records: int = 50,
                   start_year: Optional[int] = None,
                   end_year: Optional[int] = None,
                   content_type: Optional[str] = None) -> List[Dict]:
        """
        Search IEEE Xplore for research papers.
        
        Args:
            query: Search query string
            max_records: Maximum number of results to return
            start_year: Start year for date filtering
            end_year: End year for date filtering
            content_type: Type of content (e.g., 'Conferences', 'Journals')
        """
        try:
            params = {
                'querytext': query,
                'max_records': min(max_records, 200),  # IEEE API limit
                'start_record': 1,
                'sort_order': 'desc',
                'sort_field': 'publication_year'
            }
            
            # Add date range if specified
            if start_year and end_year:
                params['start_year'] = start_year
                params['end_year'] = end_year
            
            # Add content type filter if specified
            if content_type:
                params['content_type'] = content_type

            results = []
            total_fetched = 0
            
            with tqdm(total=min(max_records, 200)) as pbar:
                while total_fetched < max_records:
                    params['start_record'] = total_fetched + 1
                    
                    response_data = self._make_api_request(params)
                    
                    if 'articles' not in response_data:
                        break
                        
                    articles = response_data['articles']
                    
                    for article in articles:
                        paper_dict = {
                            'title': article.get('title', ''),
                            'authors': article.get('authors', {}).get('authors', []),
                            'publication_year': article.get('publication_year', ''),
                            'abstract': article.get('abstract', ''),
                            'doi': article.get('doi', ''),
                            'publication_title': article.get('publication_title', ''),
                            'publisher': article.get('publisher', ''),
                            'document_type': article.get('content_type', ''),
                            'conference_location': article.get('conference_location', ''),
                            'citations': article.get('citing_paper_count', 0),
                            'keywords': article.get('index_terms', {}).get('ieee_terms', []),
                            'pdf_url': article.get('pdf_url', '')
                        }
                        results.append(paper_dict)
                        
                    total_fetched += len(articles)
                    pbar.update(len(articles))
                    
                    if len(articles) < params['max_records']:
                        break
            
            return results
            
        except Exception as e:
            print(f"Error in IEEE search: {e}")
            return []

    def analyze_papers(self,
                      papers: List[Dict],
                      keywords: List[str]) -> Dict:
        """
        Analyze papers for specific keywords and create a detailed summary.
        """
        analysis = {
            'total_papers': len(papers),
            'papers_by_year': defaultdict(int),
            'papers_by_type': defaultdict(int),
            'keyword_frequency': defaultdict(int),
            'citation_analysis': {
                'total_citations': 0,
                'average_citations': 0,
                'highly_cited_papers': []
            },
            'author_stats': defaultdict(int),
            'publication_venues': defaultdict(int),
            'geographical_distribution': defaultdict(int)
        }

        for paper in papers:
            # Count papers by year
            year = paper['publication_year']
            analysis['papers_by_year'][year] += 1
            
            # Count papers by type
            doc_type = paper['document_type']
            analysis['papers_by_type'][doc_type] += 1
            
            # Analyze keyword frequency
            text_to_search = f"{paper['title']} {paper['abstract']}".lower()
            for keyword in keywords:
                if keyword.lower() in text_to_search:
                    analysis['keyword_frequency'][keyword] += 1
            
            # Citation analysis
            citations = paper['citations']
            analysis['citation_analysis']['total_citations'] += citations
            if citations >= 10:  # Threshold for highly cited papers
                analysis['citation_analysis']['highly_cited_papers'].append({
                    'title': paper['title'],
                    'citations': citations,
                    'year': year
                })
            
            # Author statistics
            for author in paper['authors']:
                author_name = author.get('full_name', '')
                if author_name:
                    analysis['author_stats'][author_name] += 1
            
            # Publication venues
            venue = paper['publication_title']
            if venue:
                analysis['publication_venues'][venue] += 1
            
            # Geographical distribution
            location = paper['conference_location']
            if location:
                analysis['geographical_distribution'][location] += 1

        # Calculate average citations
        if analysis['total_papers'] > 0:
            analysis['citation_analysis']['average_citations'] = (
                analysis['citation_analysis']['total_citations'] / analysis['total_papers']
            )

        # Sort highly cited papers
        analysis['citation_analysis']['highly_cited_papers'].sort(
            key=lambda x: x['citations'],
            reverse=True
        )

        return analysis

    def extract_quotes(self,
                      text: str,
                      keywords: List[str],
                      context_words: int = 20) -> List[str]:
        """
        Extract relevant quotes from text based on keywords, with context.
        """
        quotes = []
        words = text.split()
        
        for i, word in enumerate(words):
            if any(keyword.lower() in word.lower() for keyword in keywords):
                start = max(0, i - context_words)
                end = min(len(words), i + context_words + 1)
                quote = ' '.join(words[start:end])
                quotes.append(f"...{quote}...")
                
        return list(set(quotes))

    def generate_report(self,
                       analysis: Dict,
                       quotes: List[str]) -> str:
        """
        Generate a comprehensive research report.
        """
        report = "IEEE Xplore Research Analysis Report\n"
        report += "=================================\n\n"
        
        # Summary statistics
        report += f"Total papers analyzed: {analysis['total_papers']}\n"
        report += f"Total citations: {analysis['citation_analysis']['total_citations']}\n"
        report += f"Average citations per paper: {analysis['citation_analysis']['average_citations']:.2f}\n\n"
        
        # Publication trends
        report += "Publication Trends by Year:\n"
        for year, count in sorted(analysis['papers_by_year'].items()):
            report += f"- {year}: {count} papers\n"
        report += "\n"
        
        # Document types
        report += "Document Type Distribution:\n"
        for doc_type, count in sorted(analysis['papers_by_type'].items(),
                                    key=lambda x: x[1], reverse=True):
            report += f"- {doc_type}: {count} papers\n"
        report += "\n"
        
        # Top publication venues
        report += "Top Publication Venues:\n"
        top_venues = sorted(analysis['publication_venues'].items(),
                          key=lambda x: x[1], reverse=True)[:10]
        for venue, count in top_venues:
            report += f"- {venue}: {count} papers\n"
        report += "\n"
        
        # Most cited papers
        report += "Highly Cited Papers:\n"
        for paper in analysis['citation_analysis']['highly_cited_papers'][:5]:
            report += f"- {paper['title']} ({paper['year']}) - {paper['citations']} citations\n"
        report += "\n"
        
        # Top authors
        report += "Most Productive Authors:\n"
        top_authors = sorted(analysis['author_stats'].items(),
                           key=lambda x: x[1], reverse=True)[:10]
        for author, count in top_authors:
            report += f"- {author}: {count} papers\n"
        report += "\n"
        
        # Geographical distribution
        if analysis['geographical_distribution']:
            report += "Geographical Distribution:\n"
            top_locations = sorted(analysis['geographical_distribution'].items(),
                                 key=lambda x: x[1], reverse=True)[:10]
            for location, count in top_locations:
                report += f"- {location}: {count} papers\n"
            report += "\n"
        
        # Key quotes
        report += "Relevant Quotes:\n"
        for quote in quotes[:10]:
            report += f"- \"{quote}\"\n"
            
        return report

def main():
    # Your IEEE API key
    api_key = "YOUR_IEEE_API_KEY"
    
    # Initialize scraper
    scraper = IEEEResearchScraper(api_key)
    
    # Search parameters
    search_query = "artificial intelligence game playing"
    keywords = ["game playing", "artificial intelligence", "reinforcement learning",
                "deep learning", "neural network", "game theory"]
    
    # Perform search
    print("Searching IEEE Xplore...")
    papers = scraper.search_ieee(
        query=search_query,
        max_records=100,
        start_year=2015,
        end_year=2024,
        content_type="Conferences,Journals"
    )
    
    # Analyze results
    print("Analyzing papers...")
    analysis = scraper.analyze_papers(papers, keywords)
    
    # Extract quotes from abstracts
    print("Extracting relevant quotes...")
    all_quotes = []
    for paper in papers:
        quotes = scraper.extract_quotes(
            text=paper['abstract'],
            keywords=keywords
        )
        all_quotes.extend(quotes)
    
    # Generate report
    print("Generating report...")
    report = scraper.generate_report(analysis, all_quotes)
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save report
    with open(f'ieee_report_{timestamp}.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Save raw data
    with open(f'ieee_raw_data_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent=2)
    
    # Save analysis results
    with open(f'ieee_analysis_{timestamp}.json', 'w', encoding='utf-8') as f:
        # Convert defaultdict to regular dict for JSON serialization
        analysis_copy = json.loads(json.dumps(analysis, default=str))
        json.dump(analysis_copy, f, indent=2)
    
    print(f"Results saved with timestamp {timestamp}")

if __name__ == "__main__":
    main()