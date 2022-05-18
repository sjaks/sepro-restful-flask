from common.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Secret(db.Model):
    __tablename__ = "secret"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug = db.Column(db.String(255), nullable=False)
    user = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f'<Secret {self.slug}>'
