from __future__ import annotations

import uuid
from datetime import datetime
from typing import List

from service_platform.core.base_schema import CoreModel

class Create{name}Request(CoreModel):
    name: str

class Update{name}Request(CoreModel):
    name: str | None = None

class {name}Response(CoreModel):
    id: uuid.UUID
    name: str
