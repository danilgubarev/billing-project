function showErrorToast(error, ...errorTitle) {
    let currDate = new Date();
    let toastErrMsg = `
    <div class="toast text-bg-danger" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
          <strong class="me-auto">${errorTitle ? errorTitle : 'Уведомление'}</strong>
          <small class="text-body-secondary">${currDate.toLocaleString()}</small>
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
          ${error}
        </div>
    </div>`
    $('.toast-container').append(toastErrMsg)
    new bootstrap.Toast($('.toast')).show()
}

function showSuccessToast(msg) {
  let currDate = new Date();
  let toastSuccessMsg = `
  <div class="toast text-bg-success" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-header">
        <strong class="me-auto">Уведомление</strong>
        <small class="text-body-secondary">${currDate.toLocaleString()}</small>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
      <div class="toast-body">
        ${msg}
      </div>
  </div>`
  $('.toast-container').append(toastSuccessMsg)
  new bootstrap.Toast($('.toast')).show()
}

export {showErrorToast, showSuccessToast}


// 1234dsfsgfsdgd