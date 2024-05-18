"""Request note schema"""
from marshmallow import Schema, fields, post_load, validate

from src.models.enums import ServiceRequestStatus
from src.models.service_request import ServiceRequestModel


class CreateRequestNoteSchema(Schema):
    """
    {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "text": {
            "type": "string",
            "description": "Descripción de la solicitud."
            }
        },
        "required": [
            "text"
        ]
    }
    """

    text = fields.Str(required=True)
    type = fields.Str()
    descrition = fields.Str()

    @post_load
    def make_request(self, data, **kwargs):
        """Create a new request object"""
        # TODO: Set creation date to now and ending date to zero, also check if this logic works
        return ServiceRequestModel(
            title=data["title"],
            description=data["description"],
            status=ServiceRequestStatus.PENDING,
            # TODO: Set user_id to the authenticated user and service_id to the service received
            user_id=1,
            service_id=1,
        )


create_request_schema = CreateRequestNoteSchema()
