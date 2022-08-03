from flask import Blueprint, jsonify


api = Blueprint("api",__name__)


@api.get("/blogs/")
def blog_list():
    return jsonify([
        {
            "name":"anies",
            "position":20
        }
    ])


@api.get("/blogs/<int:id>")
def blog_retrieve(id):
    return "blog with id "+str(id)