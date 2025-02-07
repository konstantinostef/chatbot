import json
from datetime import datetime
from dateutil import parser

def normalize_datetime(dt_str):
    """
    Converts a datetime string to a standard format.
    Handles different datetime formats including timezone information.
    """
    try:
        return parser.parse(dt_str).isoformat()
    except (ValueError, TypeError):
        return dt_str


def normalize_recurrence(recurrence):
    """
    Parses recurrence strings or dictionaries and converts them to a comparable form.
    """
    if isinstance(recurrence, list):
        return [normalize_datetime(str(rule).strip().lower()) for rule in recurrence]
    return recurrence


def compare_json_objects(json1, json2):
    """
    Compares two JSON-like Python dictionaries and prints differences.
    """
    # Normalize JSON data
    json1 = {k.lower(): v for k, v in json1.items()}
    json2 = {k.lower(): v for k, v in json2.items()}

    differences = []

    for key in set(json1.keys()).union(json2.keys()):
        val1 = json1.get(key)
        val2 = json2.get(key)

        # Handle nested dictionaries (e.g., start and end)
        if isinstance(val1, dict) and isinstance(val2, dict):
            for sub_key in set(val1.keys()).union(val2.keys()):
                sub_val1 = normalize_datetime(val1.get(sub_key))
                sub_val2 = normalize_datetime(val2.get(sub_key))
                if sub_val1 != sub_val2:
                    differences.append(f"Difference in '{key}.{sub_key}': '{sub_val1}' vs '{sub_val2}'")

        # Handle list comparison for recurrence rules
        elif isinstance(val1, list) or isinstance(val2, list):
            val1_normalized = normalize_recurrence(val1) if val1 else []
            val2_normalized = normalize_recurrence(val2) if val2 else []
            if val1_normalized != val2_normalized:
                differences.append(f"Difference in '{key}': '{val1_normalized}' vs '{val2_normalized}'")

        # Compare other types directly
        else:
            val1_str = str(val1).strip().lower() if val1 is not None else None
            val2_str = str(val2).strip().lower() if val2 is not None else None
            if val1_str != val2_str:
                differences.append(f"Difference in '{key}': '{val1_str}' vs '{val2_str}'")

    return differences


def test(json1, json2):
    return compare_json_objects(json1, json2)