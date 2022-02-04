from datetime import date


def molt_validator(molt, update_molt=False):
    error = None
    spider = molt.spider
    all_molts = spider.molt_set.all()
    if update_molt == False and molt.number in [m.number for m in all_molts]:
        error = "This molt is alreday added. Check the molt number."
    elif molt.number != update_molt and molt.number in [m.number for m in all_molts]:
        error = "This molt is alreday added. Check the molt number."
    if molt.date > date.today():
        error = "You can't add molt with date in future."
    prev_molts = [m for m in all_molts if m.number < molt.number]
    if len(prev_molts) > 0:
        previous_molt = prev_molts[0]
        if previous_molt.date > molt.date:
            error = f"On your list is molt L{previous_molt.number} in date {previous_molt.date}. You can't add L{molt.number} before it."
    next_molts = [m for m in all_molts if m.number > molt.number]
    if len(next_molts) > 0:
        next_molt = next_molts[-1]
        if next_molt.date < molt.date:
            error = f"On your list is molt L{next_molt.number} in date {next_molt.date}. You can't add L{molt.number} after it."

    return error