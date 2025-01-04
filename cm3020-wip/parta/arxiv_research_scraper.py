import arxiv
import pandas as pd
from collections import defaultdict
import json
import re
from datetime import datetime
from typing import List, Dict, Tuple
import numpy as np
from tqdm import tqdm

class ArxivResearchScraper:
    def __init__(self):
        self.client = arxiv.Client()
        self.papers = []
        
    def search_arxiv(self, 
                     query: str, 
                     max_results: int = 50,
                     categories: List[str] = None) -> List[Dict]:
        """
        Search arXiv for research papers.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            categories: List of arXiv categories to search in (e.g., ['cs.AI', 'cs.LG'])
        """
        try:
            # Construct category filter if provided
            if categories:
                category_filter = ' OR '.join(f'cat:{cat}' for cat in categories)
                search_query = f"({query}) AND ({category_filter})"
            else:
                search_query = query

            # Create search parameters
            search = arxiv.Search(
                query=search_query,
                max_results=max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending
            )

            results = []
            for paper in tqdm(self.client.results(search), total=max_results):
                paper_dict = {
                    'title': paper.title,
                    'authors': [str(author) for author in paper.authors],
                    'published': paper.published.strftime('%Y-%m-%d'),
                    'year': paper.published.year,
                    'abstract': paper.summary,
                    'doi': paper.doi,
                    'primary_category': paper.primary_category,
                    'categories': paper.categories,
                    'pdf_url': paper.pdf_url,
                    'entry_id': paper.entry_id
                }
                results.append(paper_dict)
            
            return results
            
        except Exception as e:
            print(f"Error in arXiv search: {e}")
            return []

    def analyze_papers(self, 
                      papers: List[Dict], 
                      keywords: List[str],
                      min_year: int = None) -> Dict:
        """
        Analyze papers for specific keywords and create a detailed summary.
        """
        analysis = {
            'total_papers': len(papers),
            'papers_by_year': defaultdict(int),
            'papers_by_category': defaultdict(int),
            'keyword_frequency': defaultdict(int),
            'keyword_by_year': defaultdict(lambda: defaultdict(int)),
            'author_frequency': defaultdict(int),
            'key_findings': [],
            'temporal_trends': {}
        }

        # Filter by year if specified
        if min_year:
            papers = [p for p in papers if int(p['year']) >= min_year]

        for paper in papers:
            # Count papers by year
            year = paper['year']
            analysis['papers_by_year'][year] += 1
            
            # Count papers by category
            for category in paper['categories']:
                analysis['papers_by_category'][category] += 1
            
            # Analyze keyword frequency in title and abstract
            combined_text = f"{paper['title']} {paper['abstract']}".lower()
            for keyword in keywords:
                if keyword.lower() in combined_text:
                    analysis['keyword_frequency'][keyword] += 1
                    analysis['keyword_by_year'][year][keyword] += 1
            
            # Count author frequencies
            for author in paper['authors']:
                analysis['author_frequency'][author] += 1

        # Calculate temporal trends
        years = sorted(analysis['papers_by_year'].keys())
        if years:
            analysis['temporal_trends'] = {
                'year_range': f"{min(years)}-{max(years)}",
                'yearly_growth': self._calculate_growth_rate(analysis['papers_by_year']),
                'keyword_trends': self._analyze_keyword_trends(analysis['keyword_by_year'])
            }

        return analysis

    def _calculate_growth_rate(self, yearly_counts: Dict[int, int]) -> float:
        """
        Calculate the average yearly growth rate of publications.
        """
        years = sorted(yearly_counts.keys())
        if len(years) < 2:
            return 0.0
            
        values = [yearly_counts[year] for year in years]
        growth_rates = [(values[i] - values[i-1]) / values[i-1] if values[i-1] != 0 else 0 
                       for i in range(1, len(values))]
        return np.mean(growth_rates) if growth_rates else 0.0

    def _analyze_keyword_trends(self, keyword_by_year: Dict) -> Dict:
        """
        Analyze trends in keyword usage over time.
        """
        trends = {}
        years = sorted(keyword_by_year.keys())
        
        for keyword in set().union(*[keyword_by_year[year].keys() for year in years]):
            counts = [keyword_by_year[year].get(keyword, 0) for year in years]
            if len(counts) > 1:
                trend = np.polyfit(range(len(counts)), counts, 1)[0]
                trends[keyword] = {
                    'trend': 'increasing' if trend > 0 else 'decreasing',
                    'slope': float(trend)
                }
        
        return trends

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
                
        return list(set(quotes))  # Remove duplicates

    def generate_report(self, 
                       analysis: Dict, 
                       quotes: List[str], 
                       include_plots: bool = True) -> str:
        """
        Generate a detailed research report with optional visualizations.
        """
        report = "arXiv Research Analysis Report\n"
        report += "===========================\n\n"
        
        # Summary statistics
        report += f"Total papers analyzed: {analysis['total_papers']}\n"
        report += f"Date range: {analysis['temporal_trends']['year_range']}\n"
        if 'yearly_growth' in analysis['temporal_trends']:
            report += f"Average yearly growth rate: {analysis['temporal_trends']['yearly_growth']:.2%}\n\n"
        
        # Publication trends
        report += "Publication Trends by Year:\n"
        for year, count in sorted(analysis['papers_by_year'].items()):
            report += f"- {year}: {count} papers\n"
        report += "\n"
        
        # Category distribution
        report += "Top Categories:\n"
        top_categories = sorted(analysis['papers_by_category'].items(), 
                              key=lambda x: x[1], reverse=True)[:10]
        for category, count in top_categories:
            report += f"- {category}: {count} papers\n"
        report += "\n"
        
        # Keyword trends
        report += "Keyword Trends:\n"
        for keyword, trend_data in analysis['temporal_trends']['keyword_trends'].items():
            report += f"- '{keyword}': {trend_data['trend']} "
            report += f"(slope: {trend_data['slope']:.3f})\n"
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
        for quote in quotes[:10]:  # Limit to top 10 quotes
            report += f"- \"{quote}\"\n"
            
        return report

def main():
    # Initialize scraper
    scraper = ArxivResearchScraper()
    
    # Search parameters
    search_query = "artificial intelligence game playing"
    categories = ['cs.AI', 'cs.LG', 'cs.GT']  # AI, Machine Learning, Game Theory
    keywords = ["game playing", "artificial intelligence", "reinforcement learning", 
               "deep learning", "neural network", "game theory"]
    
    # Perform search
    print("Searching arXiv...")
    papers = scraper.search_arxiv(
        query=search_query,
        max_results=100,
        categories=categories
    )
    
    # Analyze results
    print("Analyzing papers...")
    analysis = scraper.analyze_papers(
        papers=papers,
        keywords=keywords,
        min_year=2015
    )
    
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
    with open(f'arxiv_report_{timestamp}.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Save raw data
    with open(f'arxiv_raw_data_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent=2)
    
    # Save analysis results
    with open(f'arxiv_analysis_{timestamp}.json', 'w', encoding='utf-8') as f:
        # Convert defaultdict to regular dict for JSON serialization
        analysis_copy = json.loads(json.dumps(analysis, default=str))
        json.dump(analysis_copy, f, indent=2)
    
    print(f"Results saved with timestamp {timestamp}")

if __name__ == "__main__":
    main()
