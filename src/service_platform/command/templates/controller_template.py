import uuid
from typing import Annotated, List

from fastapi import APIRouter, Depends, Body

router = APIRouter()

@class_router(router)
class {name}Router:
    def __init__(self, {name}_manager: {name}Manager = Depends()):
        self.manager = {name}_manager

    @router.post("/{name_lower}/create")
    async def create_{name_lower}(
        self,
        token_data: Annotated[TokenData, Depends(get_token_data)],
        payload: Create{name}Request = Body(Create{name}Request),
    ) -> {name}Response:
        return await self.manager.create_{name_lower}(
            user_id=token_data.user_id,
            payload=payload,
        )

    @router.post("/{name_lower}/update")
    async def update_{name_lower}(
        self,
        {name_lower}_id: uuid.UUID,
        payload: Update{name}Request = Body(Update{name}Request),
    ) -> MessageResponse:
        return await self.manager.update_{name_lower}(
            {name_lower}_id={name_lower}_id, payload=payload
        )

    @router.post("/{name_lower}/delete")
    async def delete_{name_lower}(
        self,
        {name_lower}_id: uuid.UUID,
    ) -> MessageResponse:
        return await self.manager.delete_{name_lower}({name_lower}_id)
