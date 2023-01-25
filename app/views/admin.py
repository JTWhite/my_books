from flask import Blueprint

admin = Blueprint(
    "/views/admin",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@admin.route("/admin")
def about():
    return "Admin page"
