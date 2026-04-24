import random
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, get_db, Base
from models import Calculation
from schemas import GameId, CalculateRequest, CalculationResponse
from calc import GAME_CONFIG, run_simulation, get_expected_pulls

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gacha Calculator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GAME_CONFIG = {
    "genshin": {"pull_cost": 160, "soft_pity": 74, "hard_pity": 90, "base_rate": 0.006, "soft_rate_inc": 0.06},
    "hsr":     {"pull_cost": 160, "soft_pity": 74, "hard_pity": 90, "base_rate": 0.006, "soft_rate_inc": 0.06},
    "zzz":     {"pull_cost": 160, "soft_pity": 74, "hard_pity": 90, "base_rate": 0.006, "soft_rate_inc": 0.06},
}
# ── Routes ────────────────────────────────────────────────────────────────────

# POST — run simulation and save to DB
@app.post("/api/calculations", response_model=CalculationResponse, status_code=201)
def create_calculation(req: CalculateRequest, db: Session = Depends(get_db)):
    cfg = GAME_CONFIG[req.game]
    row = Calculation(
        game               = req.game,
        pity               = req.pity,
        pulls              = req.pulls,
        guaranteed         = req.guaranteed,
        copies             = req.copies,
        probability        = round(run_simulation(cfg, req.pity, req.guaranteed, req.pulls, req.copies), 4),
        expected_pulls     = get_expected_pulls(cfg, req.pity, req.guaranteed),
        currency_cost      = req.pulls * cfg["pull_cost"],
        pulls_to_hard_pity = 90 - req.pity,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

# GET all — return full history
@app.get("/api/calculations", response_model=list[CalculationResponse])
def get_calculations(db: Session = Depends(get_db)):
    return db.query(Calculation).order_by(Calculation.created_at.desc()).all()

# GET one — return a single calculation by ID
@app.get("/api/calculations/{id}", response_model=CalculationResponse)
def get_calculation(id: int, db: Session = Depends(get_db)):
    row = db.query(Calculation).filter(Calculation.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Calculation not found")
    return row

# DELETE — remove a calculation by ID
@app.delete("/api/calculations/{id}", status_code=204)
def delete_calculation(id: int, db: Session = Depends(get_db)):
    row = db.query(Calculation).filter(Calculation.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Calculation not found")
    db.delete(row)
    db.commit()