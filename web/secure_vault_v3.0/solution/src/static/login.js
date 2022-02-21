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
