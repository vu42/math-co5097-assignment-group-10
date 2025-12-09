import os
from pathlib import Path
from datetime import datetime


def generate_index(report_dir="report"):
    """Generate an index.html file that links to all HTML files in the report directory."""
    report_path = Path(report_dir)
    html_files = sorted(
        [f for f in report_path.glob("*.html") if f.name != "index.html"]
    )

    # Course info
    course_name = "Mathematics Foundations for Computer Science - CO5097"
    report_topic = "Probability and Statistics"

    # Team members information
    team_members = [
        {
            "name": "Nguyễn Viết Vũ",
            "id": "2570544",
            "role": "Leader",
            "responsibility": "22.8 Distributions",
        },
        {
            "name": "Phan Hoàng Tú",
            "id": "2570370",
            "role": "",
            "responsibility": "22.7 Maximum Likelihood + 22.9 Naive Bayes",
        },
        {
            "name": "Đinh Thị Thu Thuỷ",
            "id": "2570508",
            "role": "",
            "responsibility": "22.6 Random Variables",
        },
        {
            "name": "Đinh Trương Tuệ Linh",
            "id": "2570441",
            "role": "",
            "responsibility": "22.10 Statistics",
        },
        {
            "name": "Nguyễn Thị Cẩm Tú",
            "id": "2570369",
            "role": "",
            "responsibility": "2.6 Probability and Statistics",
        },
    ]
    group_name = "Group 10"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{course_name} – {report_topic} – Reports</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            line-height: 1.6;
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }}
        .subtitle {{
            margin-top: 5px;
            margin-bottom: 25px;
            color: #555;
            font-size: 0.95em;
        }}
        .report-list {{
            list-style: none;
            padding: 0;
        }}
        .report-list li {{
            margin: 15px 0;
            padding: 15px;
            background: #f5f5f5;
            border-radius: 5px;
            border-left: 4px solid #4CAF50;
        }}
        .report-list a {{
            text-decoration: none;
            color: #2196F3;
            font-size: 1.1em;
            font-weight: 500;
        }}
        .report-list a:hover {{
            color: #1976D2;
            text-decoration: underline;
        }}
        .meta {{
            color: #666;
            font-size: 0.85em;
            margin-top: 5px;
        }}
        .team-section {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 2px solid #4CAF50;
        }}
        .team-section h2 {{
            color: #333;
            font-size: 1.3em;
            margin-bottom: 15px;
        }}
        .team-members {{
            list-style: none;
            padding: 0;
        }}
        .team-members li {{
            margin: 10px 0;
            padding: 10px;
            background: #f9f9f9;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .member-info {{
            display: flex;
            flex-direction: column;
        }}
        .member-name {{
            font-weight: 500;
            color: #333;
        }}
        .member-id {{
            color: #666;
            font-size: 0.9em;
        }}
        .member-responsibility {{
            color: #555;
            font-size: 0.85em;
            margin-top: 2px;
            font-style: italic;
        }}
        .member-role {{
            color: #4CAF50;
            font-weight: 500;
            font-size: 0.9em;
        }}
        .footer {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            color: #999;
            font-size: 0.9em;
            text-align: center;
        }}
    </style>
</head>
<body>
    <h1>{course_name}</h1>
    <div class="subtitle">
        <strong>Topic:</strong> {report_topic}
    </div>

    <div class="team-section">
        <h2>{group_name} – Members and Responsibilities</h2>
        <ul class="team-members">
"""

    for member in team_members:
        role_html = (
            f'<span class="member-role">{member["role"]}</span>'
            if member["role"]
            else ""
        )
        responsibility_html = (
            f'<span class="member-responsibility">{member["responsibility"]}</span>'
            if member.get("responsibility")
            else ""
        )
        html_content += (
            f"""            <li>
                <div class="member-info">
                    <span class="member-name">{member["name"]}</span>
                    <span class="member-id">ID: {member["id"]}</span>
                    {responsibility_html}
                </div>
                {role_html}
            </li>
"""
        )

    html_content += """        </ul>
    </div>

    <h2>Table of Contents</h2>
    <ul class="report-list">
"""

    for html_file in html_files:
        file_name = html_file.stem
        display_name = file_name.replace("_", " ").title()
        mod_time = datetime.fromtimestamp(html_file.stat().st_mtime).strftime(
            "%Y-%m-%d %H:%M"
        )
        html_content += f"""        <li>
            <a href="{html_file.name}">{display_name}</a>
            <div class="meta">Last updated: {mod_time}</div>
        </li>
"""

    html_content += f"""    </ul>
    <div class="footer">
        Generated automatically • Total reports: {len(html_files)}
    </div>
</body>
</html>
"""

    index_path = report_path / "index.html"
    index_path.write_text(html_content, encoding="utf-8")
    print(f"Generated index.html with {len(html_files)} reports")


if __name__ == "__main__":
    generate_index()
