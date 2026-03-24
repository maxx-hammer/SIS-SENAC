<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login — SIS</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <style>
        body { display:flex; justify-content:center; align-items:center; min-height:100vh; background:#f0f4f8; }
        .login-box { background:#fff; padding:40px; border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,.12); width:100%; max-width:380px; }
        .login-box h2 { margin-bottom:24px; color:#1a3c5e; text-align:center; }
        .field { display:flex; flex-direction:column; margin-bottom:16px; }
        .field label { font-size:.85rem; font-weight:600; margin-bottom:6px; color:#444; }
        .field input { padding:10px 12px; border:1px solid #ccc; border-radius:8px; font-size:1rem; }
        .field input:focus { outline:none; border-color:#1a3c5e; }
        .btn-login { width:100%; padding:12px; background:#1a3c5e; color:#fff; border:none; border-radius:8px; font-size:1rem; font-weight:600; cursor:pointer; margin-top:8px; }
        .btn-login:hover { background:#15304e; }
        .flash-erro { background:#fee2e2; color:#b91c1c; padding:10px; border-radius:8px; margin-bottom:16px; font-size:.9rem; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>🏥 SIS — Login</h2>

        {% with msgs = get_flashed_messages(with_categories=True) %}
            {% for cat, msg in msgs %}
                <div class="flash-{{ cat }}">{{ msg }}</div>
            {% endfor %}
        {% endwith %}

        <form method="POST" action="{{ url_for('auth.login') }}">
            <div class="field">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="seu@email.com" required>
            </div>
            <div class="field">
                <label for="senha">Senha</label>
                <input type="password" id="senha" name="senha" placeholder="••••••••" required>
            </div>
            <button type="submit" class="btn-login">Entrar</button>
        </form>
    </div>
</body>
</html>
