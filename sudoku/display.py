import copy
import os
import subprocess

def sudoku_to_html(sudoku, original=None, filename="sudoku_solution.html", solved=True, show_both=False):
    if original is None:
        original = copy.deepcopy(sudoku)
    def make_table(board, highlight=None, solved=False):
        table_html = "<table>\n"
        for row in range(9):
            table_html += "<tr>"
            block_row = row // 3
            cell_row = row % 3
            for col in range(9):
                block_col = col // 3
                cell_col = col % 3
                value = board[block_row][block_col][cell_row][cell_col]
                classes = []
                if col % 3 == 2:
                    classes.append("block-right")
                if col % 3 == 0:
                    classes.append("block-left")
                if row % 3 == 2:
                    classes.append("block-bottom")
                if row % 3 == 0:
                    classes.append("block-top")
                if solved and highlight and highlight[block_row][block_col][cell_row][cell_col] == ".":
                    classes.append("solved")
                class_attr = f' class="{' '.join(classes)}"' if classes else ''
                cell_val = value if value != "." else "" if not solved else value
                table_html += f"<td{class_attr}>{cell_val}</td>"
            table_html += "</tr>\n"
        table_html += "</table>"
        return table_html
    html = """
    <html>
    <head>
        <title>Sudoku Comparison</title>
        <style>
            table { border-collapse: collapse; margin: 20px; display: inline-block; }
            td {
                width: 40px; height: 40px;
                text-align: center; font-size: 24px;
                border: 1px solid #888;
            }
            td.solved { color: red; }
            td.block-right { border-right: 3px solid #000; }
            td.block-bottom { border-bottom: 3px solid #000; }
            td.block-left { border-left: 3px solid #000; }
            td.block-top { border-top: 3px solid #000; }
            .sudoku-container { display: flex; gap: 40px; }
            h2 { text-align: center; }
        </style>
    </head>
    <body>
        <h2>Unsolved and Solved Sudoku</h2>
        <div class="sudoku-container">
    """
    if show_both:
        html += f"<div><h3>Unsolved Sudoku</h3>{make_table(original, solved=False)}</div>"
        html += f"<div><h3>Solved Sudoku</h3>{make_table(sudoku, highlight=original, solved=True)}</div>"
    else:
        html += make_table(sudoku, highlight=original, solved=solved)
    html += """
        </div>
    </body>
    </html>
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    filepath = os.path.realpath(filename)
    subprocess.Popen(['start', '', filepath], shell=True)