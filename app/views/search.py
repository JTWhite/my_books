from typing import Dict, Any
from flask import Blueprint, render_template
from flask import request, jsonify
from ..forms import async_search_book

search = Blueprint(
    "/views/search",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@search.route("/search")
def index():
    return render_template("search.html")


@search.route("/search/json", methods=["GET", "POST"])
async def search_book() -> Dict[str, Any]:

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
