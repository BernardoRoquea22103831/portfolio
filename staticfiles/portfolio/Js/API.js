document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            const tmim = data.data[0].tMin;
            const tMax = data.data[0].tMax;
            document.getElementById('tMin').innerHTML = 'Temp Min:' + tmim + 'ºC';
            document.getElementById('tMax').innerHTML = 'Temp Max:' + tMax + 'ºC';
        });

});
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1131200.json')
        .then(response => response.json())
        .then(data => {
            const tmim = data.data[0].tMin;
            const tMax = data.data[0].tMax;
            document.getElementById('teMin').innerHTML = 'Temp Min:' + tmim + 'ºC';
            document.getElementById('teMax').innerHTML = 'Temp Max:' + tMax + 'ºC';
        });

});
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1080500.json')
        .then(response => response.json())
        .then(data => {
            const tmim = data.data[0].tMin;
            const tMax = data.data[0].tMax;
            document.getElementById('temMin').innerHTML = 'Temp Min:' + tmim + 'ºC';
            document.getElementById('temMax').innerHTML = 'Temp Max:' + tMax + 'ºC';
        });

});
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1050200.json')
        .then(response => response.json())
        .then(data => {
            const tmim = data.data[0].tMin;
            const tMax = data.data[0].tMax;
            document.getElementById('tempMin').innerHTML = 'Temp Min:' + tmim + 'ºC';
            document.getElementById('tempMax').innerHTML = 'Temp Max:' + tMax + 'ºC';
        });

});
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            const tmim = data.data[1].tMin;
            const tMax = data.data[1].tMax;
            document.getElementById('tempMin1').innerHTML = 'Temp Min:' + tmim + 'ºC';
            document.getElementById('tempMax1').innerHTML = 'Temp Max:' + tMax + 'ºC';
        });

});
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1131200.json')
        .then(response => response.json())
        .then(data => {
            const tmim = data.data[1].tMin;
            const tMax = data.data[1].tMax;
            document.getElementById('tempMin2').innerHTML = 'Temp Min:' + tmim + 'ºC';
            document.getElementById('tempMax2').innerHTML = 'Temp Max:' + tMax + 'ºC';
        });

});
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1080500.json')
        .then(response => response.json())
        .then(data => {
            const tmim = data.data[1].tMin;
            const tMax = data.data[1].tMax;
            document.getElementById('tempMin3').innerHTML = 'Temp Min:' + tmim + 'ºC';
            document.getElementById('tempMax3').innerHTML = 'Temp Max:' + tMax + 'ºC';
        });

});
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1050200.json')
        .then(response => response.json())
        .then(data => {
            const tmim = data.data[1].tMin;
            const tMax = data.data[1].tMax;
            document.getElementById('tempMin4').innerHTML = 'Temp Min:' + tmim + 'ºC';
            document.getElementById('tempMax4').innerHTML = 'Temp Max:' + tMax + 'ºC';
        });

});