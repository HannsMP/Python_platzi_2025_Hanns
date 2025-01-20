from typing import Optional, List

def find_employee(employe_ids: list[int], employe_id: int) -> Optional[int]:
    if employe_id in employe_ids:
        return employe_ids
    return None