from typing import Dict, List

TABLE_DATE_COLUMNS: Dict[str, List[str]] = dict(
    user=["event_ts"], marketing=["event_ts"]
)

__all__ = ["TABLE_DATE_COLUMNS"]
