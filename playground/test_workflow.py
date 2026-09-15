import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent) + "/app")
import logging

import nest_asyncio
from utils.event_loader import EventLoader
from workflows.email_workflow import EmailWorkflow

nest_asyncio.apply()

logging.basicConfig(level=logging.INFO)


# --------------------------------------------------------------
# Load event (update with your event uuid)
# --------------------------------------------------------------

message_event = EventLoader.load_event(
    "182c31c2-b499-11f0-afbf-391e827e2ece"
)  # update with your event uuid
spam_event = EventLoader.load_event(
    "f647c0c6-3158-11f0-9a4f-a121bae11c9f"
)  # update with your event uuid
invoice_event = EventLoader.load_event(
    "2222bd2c-3159-11f0-9a4f-a121bae11c9f"
)  # update with your event uuid


# --------------------------------------------------------------
# Run workflow
# --------------------------------------------------------------

workflow = EmailWorkflow()
result = workflow.run(message_event)


print(result.nodes["ClassificationNode"]["result"].output.category)
print(result.model_dump_json(indent=4))
