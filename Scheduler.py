def is_market_open_today():
    today = datetime.datetime.now(IST).date()
    # Implement a check for NSE/BSE calendar holiday (custom API or static list)
    return True  # Placeholder: For demo purposes

def start_playbook():
    if is_market_open_today():
        logging.info("Launching Daily_NIFTY_Ascendant_Playbook")
        execute_playbook()
    else:
        logging.info("Market closed. Playbook skipped.")

# Scheduler
schedule.every().monday.at("08:30").do(start_playbook)
schedule.every().tuesday.at("08:30").do(start_playbook)
schedule.every().wednesday.at("08:30").do(start_playbook)
schedule.every().thursday.at("08:30").do(start_playbook)
schedule.every().friday.at("08:30").do(start_playbook)
