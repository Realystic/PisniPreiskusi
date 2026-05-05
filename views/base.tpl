<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{title or 'Projekt'}}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
</head>
<body class="p-4">



<nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">Preizkusi</a>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/">Pregled</a>
                </li>

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