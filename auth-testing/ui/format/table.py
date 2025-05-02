import textwrap

def print_table(title, headers, rows, column_widths):
    def wrap_cell(text, width):
        return textwrap.wrap(str(text), width) or ['']  # Ensure at least one line

    def format_row_lines(wrapped_cells):
        max_lines = max(len(cell) for cell in wrapped_cells)
        lines = []
        for i in range(max_lines):
            line = "| " + " | ".join(
                f"{(cell[i] if i < len(cell) else ''):<{width}}"
                for cell, width in zip(wrapped_cells, column_widths)
            ) + " |"
            lines.append(line)
        return lines

    def wrap_and_format_row(row):
        wrapped_cells = [wrap_cell(item, width) for item, width in zip(row, column_widths)]
        return format_row_lines(wrapped_cells)

    border = "-" * (sum(column_widths) + len(column_widths) * 3 + 1)

    print(f"\n\n{title}")
    print("=" * len(title))
    print(border)
    print(format_row_lines([wrap_cell(h, w) for h, w in zip(headers, column_widths)])[0])
    print(border)

    for row in rows:
        for line in wrap_and_format_row(row):
            print(line)
        print(border)