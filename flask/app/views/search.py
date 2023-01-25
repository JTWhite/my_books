from typing import Dict, List, Any
from flask import Blueprint, render_template
from flask import request, jsonify
import requests

search = Blueprint(
    "/views/search",
    __name__,
    template_folder="templates",
    static_folder="static",
)


async def async_search_book(title: str) -> List[Dict[str, Any]]:

    query = (
        f"https://www.googleapis.com/books/v1/volumes?q={title}&maxResults=20"
    )
    response = requests.get(query)
    response = response.json()

    if response:
        books = [book["volumeInfo"] for book in response["items"]]
        return books
    return None


@search.route("/search")
def index():
    return render_template("search.html")


@search.route("/search/json", methods=["GET", "POST"])
async def search_book() -> Dict[str:Any]:

    if request.method == "POST":
        book = request.form["query"]

        if book:
            response = await async_search_book(book)
            numrows = len(response)

    return jsonify(
        {
            "htmlresponse": render_template(
                "search_response.html", employee=response, numrows=numrows
            )
        }
    )
