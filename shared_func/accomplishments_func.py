import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df = df[['course', 'hours', 'link', 'plataform', 'date']]
    df['year'] = pd.to_datetime(df['date'], errors='coerce').dt.year
    return df

def generate_year_options(df):
    years = pd.to_numeric(df['year'], errors='coerce').dropna().astype(int).unique()
    return "\n".join(f"<option value='{year}'>{year}</option>" for year in sorted(years, reverse=True))

def generate_platform_options(df):
    platforms = df['plataform'].dropna().astype(str).unique()
    return "\n".join(f"<option value='{platform}'>{platform}</option>" for platform in sorted(platforms))

def generate_table_rows(df):
    rows = "\n".join(f"""
        <tr data-year="{row['year']}" data-hours="{row['hours']}" data-platform="{row['plataform']}">
            <td>{row['course']}</td>
            <td>{row['hours']}</td>
            <td>{row['plataform']}</td>
            <td>{row['date']}</td>
            <td><a href="{row['link']}" target="_blank">View</a></td>
        </tr>
    """ for _, row in df.iterrows())
    return rows

def generate_html(df):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accomplishments Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f4f4f4; cursor: pointer; }}
        input, select {{ margin-bottom: 10px; padding: 8px; width: 100%; }}
    </style>
</head>
<body>
    <h2 style="text-align: center;">Accomplishments Dashboard</h2>
    <input type="text" id="search" onkeyup="filterTable()" placeholder="Search for courses..">
    <label for="yearFilter">Filter by Year:</label>
    <select id="yearFilter" onchange="filterData()">
        <option value="">All Years</option>
        {generate_year_options(df)}
    </select>
    <label for="platformFilter">Filter by Platform:</label>
    <select id="platformFilter" onchange="filterData()">
        <option value="">All Platforms</option>
        {generate_platform_options(df)}
    </select>
    <div>
        <p><strong>Total Courses:</strong> <span id="totalCourses">0</span></p>
        <p><strong>Total Hours:</strong> <span id="totalHours">0</span></p>
    </div>
    <table id="data-table">
        <thead>
            <tr>
                <th onclick="sortTable(0, 'str')">Course</th>
                <th onclick="sortTable(1, 'num')">Hours</th>
                <th onclick="sortTable(2, 'str')">Platform</th>
                <th onclick="sortTable(3, 'str')">Date</th>
                <th>Link</th>
            </tr>
        </thead>
        <tbody>
            {generate_table_rows(df)}
        </tbody>
    </table>
    <script>
        function updateStatistics() {{
            var table = document.getElementById("data-table");
            var tr = table.getElementsByTagName("tr");
            var totalCourses = 0;
            var totalHours = 0;
            
            for (var i = 1; i < tr.length; i++) {{
                if (tr[i].style.display !== "none") {{
                    totalCourses++;
                    var hours = parseFloat(tr[i].getAttribute("data-hours")) || 0;
                    totalHours += hours;
                }}
            }}
            document.getElementById("totalCourses").innerText = totalCourses;
            document.getElementById("totalHours").innerText = totalHours.toFixed(1);
        }}

        function filterData() {{
            var yearFilter = document.getElementById("yearFilter").value;
            var platformFilter = document.getElementById("platformFilter").value.toLowerCase();
            var table = document.getElementById("data-table");
            var tr = table.getElementsByTagName("tr");
            for (var i = 1; i < tr.length; i++) {{
                var rowYear = tr[i].getAttribute("data-year");
                var rowPlatform = tr[i].getAttribute("data-platform").toLowerCase();
                if ((yearFilter === "" || rowYear === yearFilter) && (platformFilter === "" || rowPlatform === platformFilter)) {{
                    tr[i].style.display = "";
                }} else {{
                    tr[i].style.display = "none";
                }}
            }}
            updateStatistics();
        }}

        window.onload = updateStatistics;
    </script>
</body>
</html>
"""

def save_html(output_file, content):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Dashboard generated: {output_file}")

# Main execution
def accomplishments_html(data, output_file):
    df = load_data(data)
    html_content = generate_html(df)
    save_html(output_file=output_file, content=html_content)

