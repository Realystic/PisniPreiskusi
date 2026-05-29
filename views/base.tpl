<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{title or 'Projekt'}}</title>
    %# Bootstrap CSS za lepši izgled
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
    %# Font Awesome za ikone
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body class="p-4">



<nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">Preizkusi</a>



        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">

                % if user:
                <li class="nav-item">
                    <a class="nav-link" href="/dodaj-preizkus">Dodaj</a>
                </li>
                % end
            </ul>

            <ul class="navbar-nav ms-auto">

            % if user:
                <li class="nav-item">
                    <span class="nav-link text-light">
                        <i class="fa-solid fa-user me-1"></i>
                        Prijavljen: <strong>{{user.ime}}</strong>
                        
                    </span>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/odjava">Odjava</a>
                </li>

            % else:
                <li class="nav-item">
                    <a class="nav-link" href="/prijava">Prijava</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/registracija">Registracija</a>
                </li>
            % end

        </ul>


        </div>
    </div>
</nav>


    <div class="container">
        {{!base}}
    </div>

</body>
</html>