# Secure vault v3.0 writeup
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

Function compares fields **username** and **password** with the specific values, and, if something matches, the function return true and the form is sent. Otherwise, the wrong username/password error is printed.

Having logged in as `admin`, we get:

```html
<div class="p-3 mb-2 bg-secondary text-white row justify-content-center">
	li2CTF{bruh__7h15_15_n07_s3cur3_700_:c}
</div>
```

Flag: `li2CTF{bruh__7h15_15_n07_s3cur3_700_:c}`
