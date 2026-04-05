from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.financial_record import FinancialRecord
from app.middleware.role_guard import require_role
from sqlalchemy import extract

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role(["admin", "analyst", "viewer"])
    )
):
    total_income = db.query(
        func.sum(FinancialRecord.amount)
    ).filter(
        FinancialRecord.type == "income"
    ).scalar() or 0

    total_expense = db.query(
        func.sum(FinancialRecord.amount)
    ).filter(
        FinancialRecord.type == "expense"
    ).scalar() or 0

    net_balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance
    }

@router.get("/category-summary")
def get_category_summary(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role(["admin", "analyst", "viewer"])
    )
):
    records = db.query(
        FinancialRecord.category,
        FinancialRecord.type,
        func.sum(FinancialRecord.amount).label("total")
    ).group_by(
        FinancialRecord.category,
        FinancialRecord.type
    ).all()

    result = []

    for record in records:
        result.append({
            "category": record.category,
            "type": record.type,
            "total": record.total
        })

    return result    

@router.get("/monthly-trend")
def get_monthly_trend(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role(["admin", "analyst", "viewer"])
    )
):
    records = db.query(
        extract("month", FinancialRecord.date).label("month"),
        FinancialRecord.type,
        func.sum(FinancialRecord.amount).label("total")
    ).group_by(
        extract("month", FinancialRecord.date),
        FinancialRecord.type
    ).all()

    result = []

    for record in records:
        result.append({
            "month": int(record.month),
            "type": record.type,
            "total": record.total
        })

    return result