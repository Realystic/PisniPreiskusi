% rebase('base.tpl', title='Registracija')

<h2>Registracija</h2>

% if napaka:
    <p style="color:red">{{napaka}}</p>
% end

<form method="post" action="/registracija">
    <div class="mb-3">
        <label class="form-label">Uporabniško ime</label>
        <input type="text" name="ime" class="form-control" required>
    </div>

    <div class="mb-3">
        <label class="form-label">Email</label>
        <input type="text" name="email" class="form-control" required>
    </div>
    
    <div class="mb-3">
        <label class="form-label">Geslo</label>
        <input type="password" name="geslo" class="form-control" required>
    </div>

    <button type="submit" class="btn btn-primary">Registriraj se</button>
</form>