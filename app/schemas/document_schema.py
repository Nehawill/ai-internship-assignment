from pydantic import BaseModel
from typing import List, Dict


class ComparisonResponse(BaseModel):
    added: List[Dict]
    removed: List[Dict]
    modified: List[Dict]