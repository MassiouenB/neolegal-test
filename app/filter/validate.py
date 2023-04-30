import json
from typing import Optional
from jsonschema import validate


def validate_schema(filter: Optional[str]):
    filters = json.loads(filter)
    # Define the JSON schema
    schema = {
        "type": "object",
        "properties": {
            "username": {"type": "string"},
            "firstname": {"type": "string"},
            "lastname": {"type": "string"},
        },
        "additionalProperties": False
    }

    validate(instance=filters, schema=schema)
    return filters