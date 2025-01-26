# Content Creation Logic
from pydoc_data.topics import topics

from phi4_interface import query_lmstudio

"""
topics decider, 
- input: wage topics or check list

- output: json list of topics which well save to a db
"""

def check_list_creator(topic: str):
    json_format = {{
        "main_topic":topic,
        "learning_hierarchy": [
            {{
                "category": "Foundational Knowledge",
                "subtopics": [
                    #// Core fundamentals required to understand the topic
                ]
            }},
            {{
                "category": "Advanced Concepts",
                "subtopics": [
                    #// Complex and specialized aspects of the topic
                ]
            }},
            {{
                "category": "Practical Skills",
                "subtopics": [
                    #// Hands-on applications and real-world implementations
                ]
            }},
            {{
                "category": "Specialized Areas",
                "subtopics": [
                    #// Niche or emerging subdomains within the topic
                ]
            }}
        ],
        "recommended_learning_path": [
            #// Suggested order of learning progression
        ],
        "resources_types": [
            #// Suggested learning resource categories
        ]
    }}
    prompt = f"""You are an expert curriculum designer tasked with creating a comprehensive learning roadmap for mastering 'topic'.

    Create a JSON output with the following structure:
    {json_format}
    Requirements for generation:
    1. Provide at least 3-5 subtopics in each category
    2. Ensure logical progression from basic to advanced concepts
    3. Include cutting-edge or emerging areas of the topic
    4. Make the roadmap comprehensive yet focused
    5. Use clear, concise language
    6. Aim for a learning path that can take 6-12 months to master

    Prioritize depth of knowledge and practical applicability."""

    result = query_lmstudio(context=prompt, user_query=f"topic: {topic}")
    return result