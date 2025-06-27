import webbrowser
import os

def sudoku_to_html(sudoku, filename="sudoku_solution.html"):
    html = """
    <html>
    <head>
        <title>Solved Sudoku</title>
        <style>
            table { border-collapse: collapse; margin: 20px; }
            td {
                width: 40px; height: 40px;
                text-align: center; font-size: 24px;
                border: 1px solid #888;
            }
            /* Thicker borders for 3x3 blocks */
            td.block-right { border-right: 3px solid #000; }
            td.block-bottom { border-bottom: 3px solid #000; }
            td.block-left { border-left: 3px solid #000; }
            td.block-top { border-top: 3px solid #000; }
        </style>
    </head>
    <body>
        <h2>Solved Sudoku</h2>
        <table>\n"""
    for row in range(9):
        html += "<tr>"
        block_row = row // 3
        cell_row = row % 3
        for col in range(9):
            block_col = col // 3
            cell_col = col % 3
            value = sudoku[block_row][block_col][cell_row][cell_col]
            classes = []
            if col % 3 == 2 and col != 8:
                classes.append("block-right")
            if col % 3 == 0:
                classes.append("block-left")
            if row % 3 == 2 and row != 8:
                classes.append("block-bottom")
            if row % 3 == 0:
                classes.append("block-top")
            class_attr = f' class="{' '.join(classes)}"' if classes else ''
            html += f"<td{class_attr}>{value}</td>"
        html += "</tr>\n"
    html += """
        </table>
    </body>
    </html>
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    webbrowser.open('file://' + os.path.realpath(filename))
