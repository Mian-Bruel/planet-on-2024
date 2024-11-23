from datetime import datetime

def filter_and_sort_events(events):
    """
    Filters events to include only those with a date today or in the future,
    and sorts them by date in ascending order.

    Args:
        events (list): A list of dictionaries, each containing an 'title' and 'date' key.

    Returns:
        list: A sorted list of upcoming events.
    """
    today = datetime.now().date()
    return sorted(
        [event for event in events if datetime.strptime(event["date"], "%Y-%m-%d").date() >= today],
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d")
    )
