from flask import Blueprint

# from flask import request
import asyncio
import requests

search = Blueprint(
    "/views/search",
    __name__,
    template_folder="templates",
    static_folder="static",
)


async def async_search_book(title):

    query = f"https://www.googleapis.com/books/v1/volumes?q={title}"
    response = requests.get(query)
    response = response.json()

    if response:
        books = [book["volumeInfo"] for book in response["items"]]
        books = [book["title"] for book in books if "title" in book]
        return books

    return None


# @search.route("/search", methods=["GET", "POST"])
@search.route("/search/<title>")
async def search_book(title: str = None):

    if title:
        response = await async_search_book(title)
        if response:
            return "<br>".join(response)

    return "No matching books found"
