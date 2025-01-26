from setuptools import setup, find_packages

setup(
    name="flashcard_ai",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)

from typing import Dict
from lmStudio import query_lmstudio
from schema import Hello, Lms
from content_generation.content_generator import check_list_creator

def get_hello_message() -> Hello:
    """Logic for the root endpoint."""
    response = {"message": "hELLO"}
    return response

# Add logic functions for other endpoints as needed.
def post_lms_studio(context: str, query: str):
    lms_result = query_lmstudio(context=context, user_query=query)
    response = {"response": str(lms_result)}
    return response

