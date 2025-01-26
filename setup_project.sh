#!/bin/bash

# Project Setup Script for Flashcard AI

# Create project root directory
PROJECT_ROOT="flashcard-ai"
mkdir -p $PROJECT_ROOT/src/api
mkdir -p $PROJECT_ROOT/src/core
mkdir -p $PROJECT_ROOT/src/content_generation
mkdir -p $PROJECT_ROOT/src/learning
mkdir -p $PROJECT_ROOT/src/storage
mkdir -p $PROJECT_ROOT/tests

# Create source files with basic content
create_init_file() {
    touch "$1/__init__.py"
}

create_py_file() {
    touch "$1"
    echo "# ${2}" > "$1"
}

# Create __init__.py files
create_init_file $PROJECT_ROOT/src
create_init_file $PROJECT_ROOT/src/api
create_init_file $PROJECT_ROOT/src/core
create_init_file $PROJECT_ROOT/src/content_generation
create_init_file $PROJECT_ROOT/src/learning
create_init_file $PROJECT_ROOT/src/storage

# Create source files
create_py_file "$PROJECT_ROOT/src/api/main.py" "api Entry Point"
create_py_file "$PROJECT_ROOT/src/api/commands.py" "Argument Parsing and Command Handlers"
create_py_file "$PROJECT_ROOT/src/core/flashcard_engine.py" "CRUD Operations for Flashcards"
create_py_file "$PROJECT_ROOT/src/core/state_graph.py" "LangGraph Workflow Management"
create_py_file "$PROJECT_ROOT/src/content_generation/phi4_interface.py" "LM Studio API Integration"
create_py_file "$PROJECT_ROOT/src/content_generation/content_generator.py" "Content Creation Logic"
create_py_file "$PROJECT_ROOT/src/learning/spaced_repetition.py" "Learning Algorithm"
create_py_file "$PROJECT_ROOT/src/learning/quiz_mode.py" "Quiz Generation and Tracking"
create_py_file "$PROJECT_ROOT/src/storage/database.py" "SQLAlchemy or JSON Storage"
create_py_file "$PROJECT_ROOT/src/storage/models.py" "Data Models"

# Create test files
create_py_file "$PROJECT_ROOT/tests/test_api.py" "api Tests"
create_py_file "$PROJECT_ROOT/tests/test_content_generation.py" "Content Generation Tests"
create_py_file "$PROJECT_ROOT/tests/test_learning.py" "Learning Tests"

# Create project metadata files
touch "$PROJECT_ROOT/requirements.txt"
touch "$PROJECT_ROOT/README.md"
touch "$PROJECT_ROOT/setup.py"

# Add basic content to requirements.txt
cat << EOF > "$PROJECT_ROOT/requirements.txt"
apick
langgraph
sqlalchemy
pytest
openai
EOF

# Add basic README content
cat << EOF > "$PROJECT_ROOT/README.md"
# Flashcard AI

An AI-powered flashcard generation and learning system.

## Setup

1. Create a virtual environment
2. Install dependencies: \`pip install -r requirements.txt\`
3. Run the application
EOF

# Create a basic setup.py
cat << EOF > "$PROJECT_ROOT/setup.py"
from setuptools import setup, find_packages

setup(
    name='flashcard-ai',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fastapi',
        'langgraph',
        'sqlalchemy',
        'pytest',
        'uvicorn',
        'pydantic'
    ],
    entry_points={
        'console_scripts': [
            'flashcard-ai=api.main:main',
        ],
    }
)
EOF

echo "Project structure created successfully in $PROJECT_ROOT"