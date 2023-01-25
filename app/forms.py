from typing import Dict, List, Any
import requests


async def async_search_book(title: str) -> List[Dict[str, Any]]:
    """Google Books API

    Args:
        title (str): query criteria

    Returns:
        List[Dict[str, Any]]: title, authos and pages
    """

    query = (
        f"https://www.googleapis.com/books/v1/volumes?q={title}&maxResults=20"
    )
    response = requests.get(query)
    response = response.json()

    if response:
        books = [book["volumeInfo"] for book in response["items"]]
        return books
    return None
