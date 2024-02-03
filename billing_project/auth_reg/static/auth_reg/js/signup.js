import { showErrorToast, showSuccessToast } from "./notifications.js";
import btnStatus from "./btnStatus.js";

$(document).ready(function () { 
    $('#submitBtn').click(function () {
      btnStatus(false, $(this))
      let csrf = $('form input[name="csrfmiddlewaretoken"]').val();
      let data = {
        username: $('#usernameInput').val(),
        email: $('#emailInput').val(),
        password1: $('#passwordInput1').val(),
        password2: $('#passwordInput2').val()
      }
      console.log(data);
      $.ajax({
        url: '/auth/signup-ajax/',
        type: 'POST',
        data: data,
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrf);
            xhr.setRequestHeader('Content-Type', "application/x-www-form-urlencoded")
        },
      })
      .done((json) => {
        console.log(json);
        btnStatus(true, $(this), 'Зарегестрироваться')
        showSuccessToast('Вы успешно зарегестрировались! Войдите в аккаунт --> <a href="/auth/login/" class="btn btn-dark btn-sm">Войти</a>')
      })
      .fail((err) => {
        let data = JSON.parse(err.responseText);
        let cleanedData = JSON.parse(data.html)
        for(let field in cleanedData.form_errors) {
            let errorMessages = cleanedData.form_errors[field]
            console.log(errorMessages);
            for(let errorMessage of errorMessages) {
                showErrorToast(errorMessage, `Ошибка в ${field}`)
            }
        }
        btnStatus(true, $(this), 'Зарегестрироваться')
      })
    })
})


// 123fawefcw12432dzs