from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.financial_record import FinancialRecord
from app.schemas.record_schema import RecordCreate
from app.middleware.role_guard import require_role

router = APIRouter(
    prefix="/records",
    tags=["Financial Records"]
)


@router.post("/")
def create_record(
    record_data: RecordCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
    new_record = FinancialRecord(
        amount=record_data.amount,
        type=record_data.type,
        category=record_data.category,
        date=record_data.date,
        description=record_data.description
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return {
        "message": "Record created successfully",
        "record_id": new_record.id
    }
    
@router.get("/")
def get_records(
    category: str = None,
    record_type: str = None,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role(["admin", "analyst", "viewer"])
    )
):
    query = db.query(FinancialRecord)

    if category:
        query = query.filter(
            FinancialRecord.category == category
        )

    if record_type:
        query = query.filter(
            FinancialRecord.type == record_type
        )

    records = query.all()

    return records

@router.put("/{record_id}")
def update_record(
    record_id: int,
    record_data: RecordCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
    record = db.query(FinancialRecord).filter(
        FinancialRecord.id == record_id
    ).first()

    if not record:
        return {"message": "Record not found"}

    record.amount = record_data.amount
    record.type = record_data.type
    record.category = record_data.category
    record.date = record_data.date
    record.description = record_data.description

    db.commit()

    return {"message": "Record updated successfully"}

@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(["admin"]))
):
    record = db.query(FinancialRecord).filter(
        FinancialRecord.id == record_id
    ).first()

    if not record:
        return {"message": "Record not found"}

    db.delete(record)
    db.commit()

    return {"message": "Record deleted successfully"}