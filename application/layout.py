html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%css%}
        </head>
        <body class="dash-template">
            <header>
            
                <div class="w3-top">
                   
                <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                    <div class="w3-bar w3-white w3-wide w3-padding w3-card">
                        
                        <a class="logo" href = "/index" >
                            <img src="https://raw.githubusercontent.com/tuanio/vis-for-teacher/main/dashboard/assets/imgs/logo_iuh.png" 
                            alt="" width="10%">
                        </a>

                        <div class="w3-right w3-hide-small" style = "padding-top:10px">
                            <a href="/index" class="w3-bar-item w3-button">Projects</a>
                            <a href="/dash" class="w3-bar-item w3-button">Dashboard</a>
                            <a href="/about" class="w3-bar-item w3-button">About</a>
                        </div>
                    </div>
                </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""