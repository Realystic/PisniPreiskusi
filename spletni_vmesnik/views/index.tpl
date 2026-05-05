% rebase('base.tpl', title=title)

<h2>Seznam pisnih preizkusov</h2>

% if not podatki:
    <p>Ni še vnesenih pisnih preizkusov.</p>
% else:
<table class="table table-striped">
    <thead>
        <tr>
            <th>Datum</th>
            <th>Ura</th>
            <th>Letnik</th>
            <th>Predmet</th>
            <th>Predavalnica</th>
            <th>Tip testa</th>
            <th>Teme</th>
            % if user and user.vloga == "admin":
            <th>Akcije</th>
% end

        </tr>
    </thead>
    <tbody>
    % for p in podatki:
        <tr>
            <td>{{p['datum']}}</td>
            <td>{{p['ura']}}</td>
            <td>{{p['letnik']}}</td>
            <td>{{p['predmet']}}</td>
            <td>{{p['predavalnica']}}</td>
            <td>{{p['tip']}}</td>
            <td>{{p['teme']}}</td>
        % if user and user.vloga == "admin":
            <td>
                <a href="/izbrisi/{{p['id']}}" class="btn btn-danger btn-sm"
                onclick="return confirm('Res želiš izbrisati ta preizkus?');">
                    Izbriši
                </a>
            </td>
        % end

        </tr>
    % end
    </tbody>
</table>
% end
