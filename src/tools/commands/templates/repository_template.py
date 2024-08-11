from sqlalchemy.orm import Session
from service_platform.db.{name_lower}.table import {name}Entity

class {name}Repository:
    def __init__(self, db: Session):
        self.db = db

    def get_{name_lower}(self, {name_lower}_id: str) -> {name}Entity:
        return self.db.query({name}Entity).filter({name}Entity.id == {name_lower}_id).first()

    def create_{name_lower}(self, {name_lower}: {name}Entity) -> {name}Entity:
        self.db.add({name_lower})
        self.db.commit()
        self.db.refresh({name_lower})
        return {name_lower}

    def update_{name_lower}(self, {name_lower}: {name}Entity) -> {name}Entity:
        self.db.merge({name_lower})
        self.db.commit()
        return {name_lower}

    def delete_{name_lower}(self, {name_lower}_id: str) -> None:
        {name_lower} = self.db.query({name}Entity).filter({name}Entity.id == {name_lower}_id).first()
        if {name_lower}:
            self.db.delete({name_lower})
            self.db.commit()
