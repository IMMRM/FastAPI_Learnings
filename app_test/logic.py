def is_eligible_for_load(income:float, credit_score:int, is_employed:bool) -> bool:
    if income >= 50000 and credit_score >= 700 and is_employed:
        return True
    return False