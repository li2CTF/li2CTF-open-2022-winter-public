# Secure vault v3.0 writeup
На сайте есть форма логина с полями юзернейма и пароля. SQL-инъекции не работают, так что давайте изучать сайт в поиске интересного.

Кук нету, в html никаких секретиков. Единственное, что можно изучить - как отправляется форма. Взглянем на html формы:

```html
<form action="" method="post" class="justify-content-center" id="login-form" onsubmit="return validateForm();">
	<p>
	 	<label class="form-check-label" for="username" style="align:center">Username</label>
		<br>
		<input id="form-username" name="username" required type="text" value=""> </p>
	<p>
		<label class="form-check-label" for="password" style="align:center">Password</label>
		<br>
		<input id="form-password" name="password" required type="password" value="">
	</p>
	<p>
		<input class="btn btn-danger" id="form-button" name="submit" type="submit" value="Login">
	</p>
</form>
```

Как видно в тэге `<form>`,  обработкой формы занимается функция `validateForm()`. Взглянем на нее:

```js
function validateForm() {
    if ($("#form-username")[0].value == "user" && $("#form-password")[0].value == "user") {
        return true;
    }
    
    if ($("#form-username")[0].value == "dima" && $("#form-password")[0].value == "qwerty123") {
        return true;
    }

    if ($("#form-username")[0].value == "vasya" && $("#form-password")[0].value == "Zxp0-aD1bMDl") {
        return true;
    }

    if ($("#form-username")[0].value == "admin" && $("#form-password")[0].value == "Hx1m&az3!xJa5c_cRs") {
        return true;
    }

    if ($("#form-username")[0].value == "alex" && $("#form-password")[0].value == "1_4M_N07_4_FL4G_L0L") {
        return true;
    }

    $("#error-msg")[0].innerHTML = "Incorrect username or password."
    return false;
};
```

Функция сравнивает поля **username** и **password** с определенными значениями, и, если они подходят под какие-то данные, то возвращается true и форма отправляется. В противном случае выводится ошибка о неправильном логине/пароле (это и есть та самая "оптимизация трафика").

Попробуем войти под учетными данными `admin`, получим:

```html
<div class="p-3 mb-2 bg-secondary text-white row justify-content-center">
	li2CTF{bruh__7h15_15_n07_s3cur3_700_:c}
</div>
```

Флаг: `li2CTF{bruh__7h15_15_n07_s3cur3_700_:c}`
