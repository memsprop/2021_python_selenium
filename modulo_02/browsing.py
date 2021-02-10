""""Browsing example using selenium"""
from pathlib import Path
from selenium import webdriver

def get_project_root() -> Path:
    return Path(__file__).parent.parent

def get_chrome_path() -> Path:
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver')
