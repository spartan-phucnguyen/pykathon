from typing import List

class {name}Manager:
    async def create_{name_lower}(self, user_id: str, payload: Create{name}Request) -> {name}Response:
        # Implement the logic to create a {name_lower}
        pass

    async def update_{name_lower}(self, {name_lower}_id: uuid.UUID, payload: Update{name}Request) -> MessageResponse:
        # Implement the logic to update a {name_lower}
        pass

    async def delete_{name_lower}(self, {name_lower}_id: uuid.UUID) -> MessageResponse:
        # Implement the logic to delete a {name_lower}
        pass
