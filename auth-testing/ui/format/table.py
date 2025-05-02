

def format_row(items):
    headers = ['Title', 'Description', 'Created On', 'Due Date', 'Completed']
    column_widths = [20, 30, 15, 15, 10]
    return "| " + " | ".join(f"{str(item)[:width]:<{width}}" for item, width in zip(items, column_widths)) + " |"
