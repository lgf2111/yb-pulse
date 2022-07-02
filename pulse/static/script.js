const income = parseFloat(document.getElementById('income').innerText)

setInterval(function () {
    var total_percentage = 0
    for (i=0;i<7;i++) {
        var cat = document.getElementsByClassName("form-group")[i];
        var amount = cat.querySelector('p > span');
        var percentage = cat.querySelector('div > div >input');
        if (!percentage.value) {
            var percentage_ = 0
        }
        else {
            var percentage_ = parseFloat(percentage.value);
        }
        var amount_ = income * percentage_ / 100;
        amount.innerText = amount_.toFixed(2);
        total_percentage += percentage_;
    }
    var total = document.getElementById('total');
    total.innerText = total_percentage;
    total.closest('p').classList.toggle('text-danger', total_percentage>100);
    var submit = document.getElementById("submit")
    submit.disabled = total_percentage==100 ? false : true;

}, 100);
