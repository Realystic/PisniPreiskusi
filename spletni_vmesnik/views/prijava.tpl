% rebase('base.tpl', title='Prijava')

<h2 class="mb-4">Prijava</h2>

% if napaka:
<div class="alert alert-danger">{{napaka}}</div>
% end

<form method="post" action="/prijava">
    <div class="mb-3">
        <label class="form-label">Uporabniško ime</label>
        <input type="text" name="uporabnik" class="form-control" required>
    </div>

    <div class="mb-3">
        <label class="form-label">Geslo</label>
        <input type="password" name="geslo" class="form-control" required>
    </div>

    <button type="submit" class="btn btn-primary">Prijava</button>
</form>