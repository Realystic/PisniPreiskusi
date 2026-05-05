% rebase('base.tpl', title=title)

<h2>Dodaj pisni preizkus</h2>

% if napaka:
<div class="alert alert-danger">{{napaka}}</div>
% end

<form method="post" action="/dodaj-preizkus">
    <div class="mb-3">
        <label class="form-label">Datum</label>
        <input type="date" name="datum" class="form-control" required>
    </div>

    <div class="mb-3">
        <label class="form-label">Ura</label>
        <input type="time" name="ura" class="form-control" required>
    </div>

    <div class="mb-3">
        <label class="form-label">Letnik</label>
        <select name="letnik" class="form-select" required>
            % for l in letniki:
                <option value="{{l.id}}">{{l.letnik}}</option>
            % end
        </select>
    </div>

    <div class="mb-3">
        <label class="form-label">Predmet</label>
        <select name="predmet" class="form-select" required>
            % for pr in predmeti:
                <option value="{{pr.id}}">{{pr.ime}}</option>
            % end
        </select>
    </div>

    <div class="mb-3">
        <label class="form-label">Predavalnica</label>
        <select name="predavalnica" class="form-select" required>
            % for d in predavalnice:
                <option value="{{d.id}}">{{d.ime}}</option>
            % end
        </select>
    </div>

    <div class="mb-3">
        <label class="form-label">Tip testa</label>
        <select name="tip" class="form-select" required>
            % for t in tipi:
                <option value="{{t.id}}">{{t.tip}}</option>
            % end
        </select>
    </div>

    <button type="submit" class="btn btn-primary">Dodaj</button>
</form>
