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

DEFAULT_EVENT_STORAGE_FILE = "data.json"


class EventStorage:
    def __init__(self):
        self.event_storage_dictionary = Data(**{
            "events": []
        })

    def read_existing_events(self, input_file_path=DEFAULT_EVENT_STORAGE_FILE):
        try:
            logger.info("Reading existing events")
            with open(input_file_path, "r") as file:
                loaded_data = json.load(file)
                self.event_storage_dictionary = Data(events=loaded_data["events"])
                logger.info("Reading existing events SUCCESS")
        except FileNotFoundError:
            logger.info("Existing events not found, continuing with empty list")
        except ValidationError as e:
            msg = "Failed to read existing events"
            print(msg)
            logger.error(msg)
            logger.error(e.errors())
            exit(1) # todo - in future we could handle this situation. Maybe offer user option to restore a backup


    def save_to_file(self, event_type, image_name, output_file_path=DEFAULT_EVENT_STORAGE_FILE):
        logger.info("Saving event to file")
        event = Event(timestamp=str(datetime.now()), event_type=event_type, image_name=image_name)
        self.event_storage_dictionary.events.append(event)
        # Serializing json
        json_object = json.dumps(self.event_storage_dictionary.model_dump(), indent=4)
    
        with open(output_file_path, "w") as outfile:
            outfile.write(json_object)

        logger.info("Saving event to file SUCCESS")