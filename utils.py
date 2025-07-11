def generate_alert(current_remaining, target_remaining, threshold=0.20):
    """
    Sends an alert if current_remaining is not at least 20% above target_remaining.
    """
    if target_remaining == 0:
        return "⚠️ Target remaining is zero. Cannot compute deviation."

    deviation = (current_remaining - target_remaining) / target_remaining
    percent = round(deviation * 100)

    if deviation > threshold:
        return None
    else:
        return f"⚠️ You are only {percent}% above (or below) target. Monitor your spending!"
