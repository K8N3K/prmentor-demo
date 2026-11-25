def running_total(values):
    """Return the cumulative total after each value."""
    totals = []
    current = 0
    for value in values:
        current += value
        totals.append(current)
    return totals
