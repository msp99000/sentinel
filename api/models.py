from pydantic import BaseModel

class Claim(BaseModel):
    claim_id: str
    description: str
    amount: float
    provider_id: str
