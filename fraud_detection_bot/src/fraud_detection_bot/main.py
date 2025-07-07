#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from fraud_detection_bot.crew import FraudDetectionBot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {

    "data": [
        {"transaction_id": "1", "amount": 10000, "location": "USA", "time": "2024-07-26 10:00:00", "customer_id": "123"},
        {"transaction_id": "2", "amount": 50, "location": "USA", "time": "2024-07-26 10:05:00", "customer_id": "123"},
        {"transaction_id": "3", "amount": 2000, "location": "UK", "time": "2024-07-26 10:10:00", "customer_id": "123"}
    ]
    }
    
    try:
        FraudDetectionBot().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "data": [
        {"transaction_id": "1", "amount": 10000, "location": "USA", "time": "2024-07-26 10:00:00", "customer_id": "123"},
        {"transaction_id": "2", "amount": 50, "location": "USA", "time": "2024-07-26 10:05:00", "customer_id": "123"},
        {"transaction_id": "3", "amount": 2000, "location": "UK", "time": "2024-07-26 10:10:00", "customer_id": "123"}
    ]
    }
    try:
        FraudDetectionBot().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FraudDetectionBot().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
       "data": [
        {"transaction_id": "1", "amount": 10000, "location": "USA", "time": "2024-07-26 10:00:00", "customer_id": "123"},
        {"transaction_id": "2", "amount": 50, "location": "USA", "time": "2024-07-26 10:05:00", "customer_id": "123"},
        {"transaction_id": "3", "amount": 2000, "location": "UK", "time": "2024-07-26 10:10:00", "customer_id": "123"}
    ]
    }
    
    try:
        FraudDetectionBot().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
