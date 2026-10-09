---
name: python-stats
description: Count Python files and source lines in a project using a Python script. Use when the user asks to analyze Python file counts or line counts.
---

# Python Statistics Skill

When the user asks to count Python files or calculate Python source line counts:

1. Use the shell tool to execute the Python script.
2. Run the script from the current project root:

   `python .opencode/skills/python-stats/scripts/count_lines.py .`

3. Read the JSON output.
4. Report the Python file count and total line count to the user.
5. Do not estimate the numbers yourself. Use the actual script output.
6. If the script fails, explain the error instead of inventing results.