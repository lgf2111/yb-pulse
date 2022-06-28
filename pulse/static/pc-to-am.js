const income = parseFloat(document.getElementById('income').innerText)

setInterval(function () {
    var total_percentage = 0
    for (i=0;i<7;i++) {
        var cat = document.getElementsByClassName("form-group")[i];
        var amount = cat.querySelector('p > span')
        var percentage = cat.querySelector('div > div >input')
        var percentage_ = parseFloat(percentage.value)
        var amount_ = income * percentage_ / 100
        amount.innerText = amount_
        total_percentage += percentage_
    }
    var total = document.getElementById('total')
    total.innerText = total_percentage

}, 100);