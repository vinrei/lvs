from datetime import datetime
import json
import logging
from pydantic import BaseModel, ValidationError
from typing import List

logger = logging.getLogger(__name__)

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
    logger.info("Reading existing events")
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
        event_storage_dictionary = Data(events=loaded_data["events"])
        logger.info("Reading existing events SUCCESS")
except FileNotFoundError:
    logger.info("Existing events not found, continuing with empty list")
except ValidationError as e:
    msg = "Failed to read existing events"
    print(msg)
    logger.error(msg)
    logger.error(e.errors())
    exit(1)


def save_to_file(event_type, image_name):
    logger.info("Saving event to file")
    event = Event(timestamp=str(datetime.now()), event_type=event_type, image_name=image_name)
    event_storage_dictionary.events.append(event)
    # Serializing json
    json_object = json.dumps(event_storage_dictionary.model_dump(), indent=4)
 
    with open("data.json", "w") as outfile:
        outfile.write(json_object)

    logger.info("Saving event to file SUCCESS")