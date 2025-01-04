import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
import json
import re
from datetime import datetime
from typing import List, Dict
import time
from tqdm import tqdm

class AcademicResearchScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
    def search_arxiv(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search arXiv using their RSS feed and HTML interface
        """
        base_url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
        
        try:
            response = requests.get(base_url)
            soup = BeautifulSoup(response.content, 'xml')
            entries = soup.find_all('entry')
            
            results = []
            for entry in entries:
                paper = {
                    'title': entry.title.text,
                    'authors': [author.text for author in entry.find_all('author')],
                    'published': entry.published.text,
                    'summary': entry.summary.text,
                    'link': entry.find('link', type='text/html')['href'],
                    'pdf': entry.find('link', title='pdf')['href'],
                    'source': 'arXiv'
                }
                results.append(paper)
            
            return results
        except Exception as e:
            print(f"Error in arXiv search: {e}")
            return []

    def search_semantic_scholar(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search Semantic Scholar's public API (no key required)
        """
        base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            'query': query,
            'limit': max_results,
            'fields': 'title,abstract,year,authors,citationCount,url'
        }
        
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            
            results = []
            for paper in data.get('data', []):
                paper_dict = {
                    'title': paper.get('title', ''),
                    'authors': [author.get('name', '') for author in paper.get('authors', [])],
                    'year': paper.get('year'),
                    'abstract': paper.get('abstract', ''),
                    'citations': paper.get('citationCount', 0),
                    'url': paper.get('url', ''),
                    'source': 'Semantic Scholar'
                }
                results.append(paper_dict)
            
            return results
        except Exception as e:
            print(f"Error in Semantic Scholar search: {e}")
            return []

    def search_dblp(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search DBLP Computer Science Bibliography
        """
        base_url = f"https://dblp.org/search/publ/api"
        params = {
            'q': query,
            'format': 'json',
            'h': max_results
        }
        
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            hits = data.get('result', {}).get('hits', {}).get('hit', [])
            
            results = []
            for hit in hits:
                info = hit.get('info', {})
                paper_dict = {
                    'title': info.get('title', ''),
                    'authors': info.get('authors', {}).get('author', []),
                    'year': info.get('year'),
                    'venue': info.get('venue', ''),
                    'type': info.get('type', ''),
                    'url': info.get('url', ''),
                    'source': 'DBLP'
                }
                results.append(paper_dict)
            
            return results
        except Exception as e:
            print(f"Error in DBLP search: {e}")
            return []

    def search_citeseerx(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search CiteSeerX digital library
        """
        base_url = "https://citeseerx.ist.psu.edu/api/search"
        params = {
            'q': query,
            'sort': 'cite',
            'rows': max_results
        }
        
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            docs = data.get('response', {}).get('docs', [])
            
            results = []
            for doc in docs:
                paper_dict = {
                    'title': doc.get('title', [''])[0],
                    'authors': doc.get('author', []),
                    'year': doc.get('year', [None])[0],
                    'abstract': doc.get('abstract', [''])[0],
                    'citations': doc.get('citedby', 0),
                    'url': f"https://citeseerx.ist.psu.edu/viewdoc/summary?doi={doc.get('doi', [''])[0]}",
                    'source': 'CiteSeerX'
                }
                results.append(paper_dict)
            
            return results
        except Exception as e:
            print(f"Error in CiteSeerX search: {e}")
            return []

    def search_unpaywall(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search Unpaywall for open access papers
        """
        base_url = "https://api.unpaywall.org/v2/search"
        params = {
            'query': query,
            'is_oa': 'true',
            'page_size': max_results
        }
        
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            results = []
            
            for item in data.get('results', []):
                paper_dict = {
                    'title': item.get('title', ''),
                    'authors': [author.get('name', '') for author in item.get('authors', [])],
                    'year': item.get('published_date', '')[:4],
                    'doi': item.get('doi', ''),
                    'url': item.get('best_oa_location', {}).get('url', ''),
                    'journal': item.get('journal_name', ''),
                    'source': 'Unpaywall'
                }
                results.append(paper_dict)
            
            return results
        except Exception as e:
            print(f"Error in Unpaywall search: {e}")
            return []

    def search_opencitations(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search OpenCitations for paper metadata and citations
        """
        base_url = "https://opencitations.net/index/api/v1/search"
        params = {
            'query': query,
            'limit': max_results
        }
        
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            
            results = []
            for item in data:
                paper_dict = {
                    'title': item.get('title', ''),
                    'authors': item.get('author', '').split(';'),
                    'year': item.get('year', ''),
                    'doi': item.get('doi', ''),
                    'citations': item.get('citation_count', 0),
                    'references': item.get('reference_count', 0),
                    'source': 'OpenCitations'
                }
                results.append(paper_dict)
            
            return results
        except Exception as e:
            print(f"Error in OpenCitations search: {e}")
            return []

    def search_core(self, query: str, max_results: int = 50) -> List[Dict]:
        """
        Search CORE's public API (minimal rate limits)
        """
        base_url = "https://core.ac.uk:443/api/v3/search/works"
        params = {
            'q': query,
            'limit': max_results,
            'scroll': True
        }
        
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            
            results = []
            for work in data.get('results', []):
                paper_dict = {
                    'title': work.get('title', ''),
                    'authors': work.get('authors', []),
                    'year': work.get('yearPublished'),
                    'abstract': work.get('abstract', ''),
                    'doi': work.get('doi'),
                    'url': work.get('downloadUrl', ''),
                    'source': 'CORE'
                }
                results.append(paper_dict)
            
            return results
        except Exception as e:
            print(f"Error in CORE search: {e}")
            return []

    def analyze_papers(self, papers: List[Dict], keywords: List[str]) -> Dict:
        """
        Analyze papers from multiple sources
        """
        analysis = {
            'total_papers': len(papers),
            'papers_by_source': defaultdict(int),
            'papers_by_year': defaultdict(int),
            'keyword_frequency': defaultdict(int),
            'author_frequency': defaultdict(int),
            'key_findings': []
        }
        
        for paper in papers:
            # Count by source
            analysis['papers_by_source'][paper['source']] += 1
            
            # Count by year
            if 'year' in paper and paper['year']:
                analysis['papers_by_year'][str(paper['year'])] += 1
            
            # Analyze keywords
            text_to_search = f"{paper['title']} {paper.get('abstract', '')}".lower()
            for keyword in keywords:
                if keyword.lower() in text_to_search:
                    analysis['keyword_frequency'][keyword] += 1
            
            # Count author frequencies
            for author in paper.get('authors', []):
                if isinstance(author, str):
                    analysis['author_frequency'][author] += 1
                elif isinstance(author, dict) and 'name' in author:
                    analysis['author_frequency'][author['name']] += 1

        return analysis

    def extract_quotes(self, papers: List[Dict], keywords: List[str]) -> List[Dict]:
        """
        Extract relevant quotes from papers
        """
        quotes = []
        
        for paper in papers:
            abstract = paper.get('abstract', '')
            if not abstract:
                continue
                
            sentences = re.split(r'(?<=[.!?])\s+', abstract)
            for sentence in sentences:
                if any(keyword.lower() in sentence.lower() for keyword in keywords):
                    quote = {
                        'text': sentence.strip(),
                        'paper_title': paper['title'],
                        'source': paper['source']
                    }
                    quotes.append(quote)
        
        return quotes

    def generate_report(self, analysis: Dict, quotes: List[Dict]) -> str:
        """
        Generate a comprehensive research report
        """
        report = "Research Analysis Report\n"
        report += "=====================\n\n"
        
        # Summary statistics
        report += f"Total papers analyzed: {analysis['total_papers']}\n\n"
        
        # Source distribution
        report += "Papers by Source:\n"
        for source, count in analysis['papers_by_source'].items():
            report += f"- {source}: {count} papers\n"
        report += "\n"
        
        # Publication trends
        report += "Publication Trends by Year:\n"
        for year, count in sorted(analysis['papers_by_year'].items()):
            report += f"- {year}: {count} papers\n"
        report += "\n"
        
        # Keyword frequency
        report += "Keyword Frequency:\n"
        sorted_keywords = sorted(analysis['keyword_frequency'].items(), 
                               key=lambda x: x[1], reverse=True)
        for keyword, count in sorted_keywords:
            report += f"- '{keyword}': found in {count} papers\n"
        report += "\n"
        
        # Top authors
        report += "Most Frequent Authors:\n"
        top_authors = sorted(analysis['author_frequency'].items(), 
                           key=lambda x: x[1], reverse=True)[:10]
        for author, count in top_authors:
            report += f"- {author}: {count} papers\n"
        report += "\n"
        
        # Relevant quotes
        report += "Key Quotes:\n"
        for quote in quotes[:10]:
            report += f"- \"{quote['text']}\"\n"
            report += f"  Source: {quote['source']} - {quote['paper_title']}\n\n"
        
        return report

def main():
    # Initialize scraper
    scraper = AcademicResearchScraper()
    
    # Search parameters
    search_query = "artificial intelligence game playing"
    keywords = ["game playing", "artificial intelligence", "reinforcement learning",
                "deep learning", "neural network", "game theory"]
    
    # Collect papers from multiple sources
    print("Searching academic sources...")
    papers = []
    
    print("Searching arXiv...")
    arxiv_papers = scraper.search_arxiv(search_query)
    papers.extend(arxiv_papers)
    
    print("Searching Semantic Scholar...")
    semantic_papers = scraper.search_semantic_scholar(search_query)
    papers.extend(semantic_papers)
    
    print("Searching DBLP...")
    dblp_papers = scraper.search_dblp(search_query)
    papers.extend(dblp_papers)
    
    print("Searching CiteSeerX...")
    citeseer_papers = scraper.search_citeseerx(search_query)
    papers.extend(citeseer_papers)
    
    print("Searching Unpaywall...")
    unpaywall_papers = scraper.search_unpaywall(search_query)
    papers.extend(unpaywall_papers)
    
    print("Searching OpenCitations...")
    opencitations_papers = scraper.search_opencitations(search_query)
    papers.extend(opencitations_papers)
    
    print("Searching CORE...")
    core_papers = scraper.search_core(search_query)
    papers.extend(core_papers)
    
    # Analyze results
    print("Analyzing papers...")
    analysis = scraper.analyze_papers(papers, keywords)
    
    # Extract quotes
    print("Extracting relevant quotes...")
    quotes = scraper.extract_quotes(papers, keywords)
    
    # Generate report
    print("Generating report...")
    report = scraper.generate_report(analysis, quotes)
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save report
    with open(f'research_report_{timestamp}.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Save raw data
    with open(f'raw_data_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent=2, default=str)
    
    # Save analysis
    with open(f'analysis_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, default=str)
    
    print(f"Results saved with timestamp {timestamp}")

if __name__ == "__main__":
    main()