# # main.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import requests

# app = Flask(__name__)
# CORS(app)

# @app.route("/generate", methods=["POST"])
# def generate():
#     data = request.json
#     command = data.get("command")  # <-- match frontend
#     if not command:
#         return jsonify({"error": "No command provided"}), 400

#     try:
#         # Call Ollama API
#         res = requests.post(
#             "http://127.0.0.1:11434/api/generate",
#             json={"model": "llama3:latest", "prompt": command, "stream": False},
#         )
#         res.raise_for_status()
#         output = res.json()
#         return jsonify({"response": output.get("response", "No response from Ollama")})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)

# backend/main.py


# -----------------------------------------------------------


# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import unquote, urlparse, parse_qs
# from playwright.sync_api import sync_playwright
# import os

# app = Flask(__name__)
# CORS(app)

# SCREENSHOT_DIR = "screenshots"
# os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# # --- DuckDuckGo search with real URLs ---
# def search_duckduckgo(query, limit=5):
#     url = f"https://duckduckgo.com/html/?q={query}"
#     headers = {"User-Agent": "Mozilla/5.0"}
#     r = requests.get(url, headers=headers, timeout=10)
#     soup = BeautifulSoup(r.text, "html.parser")

#     results = []
#     for a in soup.select(".result__a")[:limit]:
#         title = a.get_text(strip=True)
#         href = a["href"]
        
#         # Extract the real URL from uddg parameter
#         parsed = urlparse(href)
#         qs = parse_qs(parsed.query)
#         real_url = unquote(qs.get("uddg", [href])[0])
#         results.append({"title": title, "link": real_url})
#     return results

# # --- Fetch page content and screenshot ---
# def fetch_page_content_and_screenshot(url, idx):
#     result = {"content": "Failed to load page.", "screenshot": None}
#     try:
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=True)
#             context = browser.new_context(
#                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
#             )
#             page = context.new_page()
#             page.goto(url, timeout=20000)  # 20s timeout
#             page.wait_for_load_state("networkidle", timeout=15000)

#             # Screenshot
#             screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{idx}.png")
#             page.screenshot(path=screenshot_path, full_page=True)

#             # Extract text content (first 500 chars)
#             text_content = page.inner_text("body")[:500]
#             result["content"] = text_content
#             result["screenshot"] = screenshot_path

#             browser.close()
#     except Exception as e:
#         # keep fallback message in result['content']
#         result["content"] = f"Failed to load page: {str(e)}"
#     return result

# # --- API endpoint ---
# @app.route("/execute", methods=["POST"])
# def execute():
#     data = request.json
#     command = data.get("command", "").strip()

#     if not command:
#         return jsonify({"results": [], "error": "No command provided"})

#     try:
#         results = search_duckduckgo(command, limit=5)
#         enhanced_results = []
#         for idx, res in enumerate(results):
#             extra = fetch_page_content_and_screenshot(res["link"], idx)
#             enhanced_results.append({
#                 "title": res["title"],
#                 "link": res["link"],
#                 "content": extra["content"],
#                 "screenshot": extra["screenshot"]
#             })
#         return jsonify({"results": enhanced_results})
#     except Exception as e:
#         return jsonify({"results": [], "error": str(e)})

# # --- Serve screenshots ---
# @app.route("/screenshot/<filename>")
# def get_screenshot(filename):
#     path = os.path.join(SCREENSHOT_DIR, filename)
#     if os.path.exists(path):
#         return send_file(path, mimetype="image/png")
#     return "Not found", 404

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from PIL import Image, ImageOps
import os
import requests
from urllib.parse import urlparse, parse_qs, unquote
import hashlib
import time

app = Flask(__name__)
CORS(app)

SCREENSHOT_DIR = "screenshots"
THUMBNAIL_DIR = "thumbnails"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(THUMBNAIL_DIR, exist_ok=True)

# --- Decode DuckDuckGo redirect links ---
def get_real_url(ddg_link):
    try:
        parsed = urlparse(ddg_link)
        if "uddg" in parse_qs(parsed.query):
            real_url = parse_qs(parsed.query)["uddg"][0]
            return unquote(real_url)
        return ddg_link
    except:
        return ddg_link

# --- DuckDuckGo search ---
def search_duckduckgo(query, limit=5):
    url = f"https://duckduckgo.com/html/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    results = []

    timestamp = int(time.time() * 1000)  # unique per search

    for idx, a in enumerate(soup.select(".result__a")[:limit]):
        title = a.get_text(strip=True)
        link = get_real_url(a["href"])  # decode redirect to actual URL

        # Fetch snippet
        try:
            r2 = requests.get(link, headers=headers, timeout=8)
            soup2 = BeautifulSoup(r2.text, "html.parser")
            paragraphs = soup2.find_all("p")
            content_snippet = " ".join([p.get_text() for p in paragraphs[:2]])[:200]
        except:
            content_snippet = "Preview not available."

        # Use hash of URL + timestamp for unique filenames
        hash_str = hashlib.md5(f"{link}_{timestamp}".encode()).hexdigest()
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{hash_str}.png")
        thumbnail_path = os.path.join(THUMBNAIL_DIR, f"thumbnail_{hash_str}.png")

        # Screenshot
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(link, timeout=15000)
                page.screenshot(path=screenshot_path, full_page=True)
                browser.close()

            # High-quality thumbnail (350x200)
            with Image.open(screenshot_path) as img:
                img_thumb = ImageOps.fit(img, (350, 200), Image.LANCZOS)
                img_thumb.save(thumbnail_path, quality=95)
        except:
            screenshot_path = None
            thumbnail_path = None

        results.append({
            "title": title,
            "link": link,
            "content": content_snippet,
            "screenshot": screenshot_path,
            "thumbnail": thumbnail_path
        })
    return results

# --- Routes ---
@app.route("/execute", methods=["POST"])
def execute():
    data = request.json
    command = data.get("command", "")
    if not command.strip():
        return jsonify({"error": "No command provided"})

    try:
        results = search_duckduckgo(command, limit=5)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/screenshot/<filename>")
def get_screenshot(filename):
    return send_from_directory(SCREENSHOT_DIR, filename)

@app.route("/thumbnail/<filename>")
def get_thumbnail(filename):
    return send_from_directory(THUMBNAIL_DIR, filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)



