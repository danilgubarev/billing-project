import { showErrorToast, showSuccessToast } from "./notifications.js";

$(document).ready(function () {
    $('#submitBtn').click(function () {
        let csrf = $('form input[name="csrfmiddlewaretoken"]').val()
        console.log('click');
        let data = {
            csrfmiddlewaretoken: csrf,
            login: $('#usernameInput').val(),
            password: $('#passwordInput').val()
        }
        $.ajax({
            url: '/auth/login-ajax/',
            type: 'POST',
            data: data,
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrf);
                xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded")
            },
        })
        .done((resp) => {
            showSuccessToast('Вы успешно вошли в аккаунт!')
        })
        .fail((err) => {
            console.log(err);
            let data = JSON.parse(err.responseText);
            let cleanedData = JSON.parse(data.html);
            showErrorToast(cleanedData.form_errors.__all__[0])
            console.log(cleanedData.form_errors.__all__);
        })
    })
})