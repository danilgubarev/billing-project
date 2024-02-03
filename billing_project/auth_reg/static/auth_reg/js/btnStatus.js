const btnStatus = (isActive, btn, ...btnName) => {
    if (isActive) {
      btn.attr('disabled', false);
      btn.text(btnName)
    } else {
        btn.attr('disabled', true);
        btn.text('Загрузка...') 
    }
}

export default btnStatus