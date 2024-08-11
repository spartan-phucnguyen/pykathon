from __future__ import annotations

from typing import List

from service_platform.api.controller.{name_lower}.schema import (
    {name}Response,
)

from service_platform.db.{name_lower}.table import {name}Entity

class {name}ResponseConverter:
    def to_{name_lower}_response(
        self,
        {name_lower}: {name}Entity,
    ) -> {name}Response:
        return {name}Response(
            id={name_lower}.id,
            name={name_lower}.name,
        )

    def to_{name_lower}s_response(self, {name_lower}s: List[{name}Entity]) -> List[{name}Response]:
        return [self.to_{name_lower}_response(fol) for fol in {name_lower}s]
