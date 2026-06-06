import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

def test_health():
    """Test health check endpoint"""
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_homepage():
    """Test portfolio homepage"""
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    assert "<html" in r.text

def test_profile_endpoint():
    """Test profile JSON endpoint"""
    r = requests.get(f"{BASE_URL}/api/profile")
    assert r.status_code == 200
    data = r.json()
    assert "name" in data
    assert "skills" in data
    assert "projects" in data

def test_artefacts_endpoint():
    """Test artefacts JSON endpoint"""
    r = requests.get(f"{BASE_URL}/api/artefacts")
    assert r.status_code == 200
    data = r.json()
    assert "portfolio_html" in data
    assert "ai_visual" in data
    assert "use_case_diagram" in data
    assert "sequence_diagram" in data
    assert "requirements_and_user_stories" in data

def test_ai_visual_file():
    """Test that AI image file is accessible"""
    r = requests.get(f"{BASE_URL}/images/portfolio_hero.png")
    assert r.status_code == 200
    assert r.headers["Content-Type"] == "image/png"