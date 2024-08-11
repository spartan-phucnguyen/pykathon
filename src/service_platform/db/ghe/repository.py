from sqlalchemy.orm import Session

from service_platform.db.ghe.table import GheEntity


class GheRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_ghe(self, ghe_id: str) -> GheEntity:
        return self.db.query(GheEntity).filter(GheEntity.id == ghe_id).first()

    def create_ghe(self, ghe: GheEntity) -> GheEntity:
        self.db.add(ghe)
        self.db.commit()
        self.db.refresh(ghe)
        return ghe

    def update_ghe(self, ghe: GheEntity) -> GheEntity:
        self.db.merge(ghe)
        self.db.commit()
        return ghe

    def delete_ghe(self, ghe_id: str) -> None:
        ghe = self.db.query(GheEntity).filter(GheEntity.id == ghe_id).first()
        if ghe:
            self.db.delete(ghe)
            self.db.commit()
