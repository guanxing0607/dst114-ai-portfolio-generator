
from flask import Flask,jsonify,send_file,send_from_directory
from pathlib import Path

app=Flask(__name__)

BASE_DIR=Path(__file__).resolve().parent

PROFILE={
    "name":"Alex Chen",
    "education":"BSc Computer Science",
    "skills":["Python","Flask","Git"],
    "projects":["Portfolio Generator"],
    "experience":"Student developer",
    "github":"https://github.com/example",
    "career_goal":"Software engineer"
}


@app.route("/",methods=["GET"])
def home():
    """
    Return the generated portfolio website.
    """
    portfolio_file=BASE_DIR/"portfolio.html"

    if not portfolio_file.exists():
        return jsonify({
            "error":"portfolio.html was not found"
        }),404

    return send_file(portfolio_file)


@app.route("/images/<path:filename>",methods=["GET"])
def serve_image(filename):
    """
    Serve AI-generated images used by the portfolio website.
    """
    image_dir=BASE_DIR/"images"

    return send_from_directory(
        image_dir,
        filename
    )


@app.route("/uml/<path:filename>",methods=["GET"])
def serve_uml(filename):
    """
    Serve generated UML source files.
    """
    uml_dir=BASE_DIR/"uml"

    return send_from_directory(
        uml_dir,
        filename
    )


@app.route("/requirements_and_user_stories.md",methods=["GET"])
def serve_documentation():
    """
    Serve generated requirements and user stories.
    """
    documentation_file=BASE_DIR/"requirements_and_user_stories.md"

    if not documentation_file.exists():
        return jsonify({
            "error":"requirements_and_user_stories.md was not found"
        }),404

    return send_file(documentation_file)


@app.route("/api/profile",methods=["GET"])
def get_profile():
    """
    Return profile data as JSON.
    """
    return jsonify(PROFILE)


@app.route("/api/artefacts",methods=["GET"])
def get_artefacts():
    """
    Return the generated artefact list.
    """
    artefacts={
        "portfolio_html":"portfolio.html",
        "ai_visual":"images/portfolio_hero.png",
        "requirements_and_user_stories":
            "requirements_and_user_stories.md",
        "use_case_diagram":
            "uml/use_case_diagram.puml",
        "sequence_diagram":
            "uml/sequence_diagram.puml"
    }

    return jsonify(artefacts)


@app.route("/health",methods=["GET"])
def health_check():
    """
    Simple endpoint for testing and deployment checks.
    """
    return jsonify({
        "status":"ok"
    })


if __name__=="__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
