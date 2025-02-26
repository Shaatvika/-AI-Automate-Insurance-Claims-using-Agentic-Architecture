#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ai_automated_claims.crew import AiAutomatedClaims

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    inputs = {
        'claimant_name': 'Dummy Patient',
        'policy_number': 'P123456789',
        'incident_date': '2023-01-19',
        'claim_amount': '3650.00',
        'current_year': str(datetime.now().year),
        'image_url' : "https://drive.google.com/file/d/1B0I-5OZOtHD132okAtrP7dtHxLFu2YUP/view?usp=sharing",
        'query' : "What is the reason for delay in my claims? I have been in pain for so long."
    }
    
    try:
        AiAutomatedClaims().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    inputs = {
        "claimant_name": "John Doe",
        "claim_amount": "5000 USD"
    }
    try:
        AiAutomatedClaims().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    try:
        AiAutomatedClaims().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    inputs = {
        "claimant_name": "John Doe",
        "claim_amount": "5000 USD"
    }
    try:
        AiAutomatedClaims().crew().test(n_iterations=int(sys.argv[1]), llm_model="gemini", inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
