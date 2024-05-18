"""Service model"""
import sqlalchemy as sa

from src.core.database import HelperModel, db
from src.models.enums import ServiceTypes
from src.models.tsvector import TSVector


class ServiceModel(db.Model, HelperModel):
    """Main service model"""

    __tablename__ = "service"
    __table_args__ = (
        db.UniqueConstraint(
            "institution_id", "name", name="unique_institution_service"
        ),
    )

    id = db.Column(db.Integer(), primary_key=True)
    institution_id = db.Column(
        db.Integer(), db.ForeignKey("institution.id", ondelete="CASCADE")
    )
    name = db.Column(db.String())
    description = db.Column(db.String())
    keywords = db.Column(db.ARRAY(db.String()))
    service_type = db.Column(db.Enum(ServiceTypes))
    enabled = db.Column(db.Boolean(), default=False)

    ts_vector = sa.Column(
        TSVector(
            "name",
            "description",
            # "keywords",
            regconfig="argentino",
        ),
        sa.Computed(
            # "to_tsvector('spanglish', \"name\" || ' ' || \"description\" || ' ' || array_to_string(\"keywords\", ' '))",
            "to_tsvector('argentino', \"name\" || ' ' || \"description\")",
            persisted=True,
        ),
    )

    __table_args__ = (
        # Indexing the TSVector column
        sa.Index(
            "idx_service_ts_vector",
            ts_vector,
            postgresql_using="gin",
        ),
    )

    def __init__(
        self,
        name,
        inst_id,
        description,
        keywords,
        service_type,
        enabled=False,
    ):
        self.name = name
        self.institution_id = inst_id
        self.description = description
        self.keywords = keywords
        self.service_type = service_type
        self.enabled = enabled

    def __repr__(self):
        return f"<Service {self.name}>"
