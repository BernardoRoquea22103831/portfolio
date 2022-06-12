function displayTime() {
    var dateTime = new Date();
    var hrs = dateTime.getHours();
    var mim = dateTime.getMinutes();
    var sec = dateTime.getSeconds();
    var seccao = document.getElementById('seccao');

    if (hrs >= 12) {
        seccao.innerHTML = 'PM';
    } else {
        seccao.innerHTML = 'AM';
    }

    document.getElementById('horas').innerHTML = hrs;
    document.getElementById('minutos').innerHTML = mim;
    document.getElementById('segundos').innerHTML = sec;

}

setInterval(displayTime, 10);