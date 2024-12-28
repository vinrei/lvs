from datetime import datetime
import json
from pydantic import BaseModel, ValidationError
from typing import List

# Define the model for JSON file
class Event(BaseModel):
    timestamp: str
    event_type: str
    image_name: str
class Data(BaseModel):
    events: List[Event]

event_storage_dictionary = Data(**{
    "events": [
    ]
})

# Read existing events
try:
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
        event_storage_dictionary = Data(events=loaded_data["events"])
        pass
except FileNotFoundError:
    print("existing events not found, continuing with empty list")
except ValidationError as e:
    print(e.errors())
    exit(1)


def save_to_file(event_type, image_name):
    event = Event(timestamp=str(datetime.now()), event_type=event_type, image_name=image_name)
    event_storage_dictionary.events.append(event)
    # Serializing json
    json_object = json.dumps(event_storage_dictionary.model_dump(), indent=4)
 
    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)