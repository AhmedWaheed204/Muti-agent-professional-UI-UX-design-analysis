from duckduckgo_search import DDGS
from typing import List, Dict

class DuckDuckGoTools:
    """Wrapper class for DuckDuckGo search functionality."""
    
    def __init__(self):
        self.client = DDGS()

    def search(self, query: str, max_results: int = 5) -> str:
        """
        Perform a web search and return formatted results.
        
        Args:
            query: Search query
            max_results: Maximum number of results to return
            
        Returns:
            Formatted search results as string
        """
        try:
            results = self.client.text(query, max_results=max_results)
            return self._format_results(results)
        except Exception as e:
            return f"Search error: {str(e)}"

    def _format_results(self, results: List[Dict]) -> str:
        """Format search results into readable string."""
        return "\n".join([f"• {r['title']}: {r['body']}" for r in results])