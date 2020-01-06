import dialogflow_v2 as dialogflow
from dotenv import load_dotenv
import os
import json


def create_intent(question):
    intent = {
        "display_name": question,
        "messages": [{
            "text":
            {"text": [questions_data[question].get('answer')]}
        }],
        "training_phrases": []
    }
    for phrase in questions_data[question].get('questions'):
        intent.get("training_phrases").append(
            {"parts": [{"text": phrase}]})
    return intent


def upload_intent(intent, project_id):
    client = dialogflow.IntentsClient()
    parent = client.project_agent_path(project_id)
    response = client.create_intent(parent, intent)


if __name__ == "__main__":
    load_dotenv()
    project_id = os.getenv("DIALOGFLOW_PROJECT_ID")
    with open('questions.json') as json_file:
        questions_data = json.load(json_file)

    for question in questions_data:
        intent = create_intent(question)
        upload_intent(intent, project_id)
