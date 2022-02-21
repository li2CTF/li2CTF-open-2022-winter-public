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
    Promise.all(checkPassword());
    if (isCorrect) {
        isCorrect = false;
        return true;
    }
    return false;  
}

