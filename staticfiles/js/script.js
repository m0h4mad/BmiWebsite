
const submitButton = document.getElementById("submitBtn");
const bmiModal = new bootstrap.Modal(document.getElementById("bmiModal"));

const UNDERWEIGHT = "underweight";
const NORMALWEIGHT = "normalweight";
const OVERWEIGHT = "overweight";
const OBESE = "obese";

submitButton.onclick = function (e) {
    e.preventDefault();
    let url = document.getElementById("bmiForm").action;
    let weight = document.getElementById("weightInput").value;
    let height = document.getElementById("heightInput").value;
    let gender = document.getElementById("genderInput").value;
    let year = document.getElementById("yearInput").value;
    let month = document.getElementById("monthInput").value;
    let day = document.getElementById("dayInput").value;

    var query = `?weight=${weight}&height=${height}&gender=${gender}&year=${year}&month=${month}&day=${day}`
    var endpoint = url + query;
    var xml = new XMLHttpRequest();

    xml.onload = function () {
        let response = JSON.parse(this.responseText);
        showModal(response);
    }
    
    xml.open("GET", endpoint);
    xml.send();
}

function showModal(data) {
    console.log(data);
    let modalTitle = document.getElementById("bmiModalTitle");
    let modalBody = document.getElementById("bmiModalBody");

    switch (data.weight) {
        case OBESE:
            modalTitle.classList.add("text-danger");
            modalTitle.innerHTML = "شما چاق هستید";
            break;
        
        case OVERWEIGHT:
            modalTitle.classList.add("text-warning");
            modalTitle.innerHTML = "شما اضافه وزن دارید";
            break;
        
        case NORMALWEIGHT:
            modalTitle.classList.add("text-success");
            modalTitle.innerHTML = "شما وزن نرمال دارید";
            break;
        
        case UNDERWEIGHT:
            modalTitle.classList.add("text-warning");
            modalTitle.innerHTML = "شما کمبود وزن دارید";
            break;
    }

    let gender = document.getElementById("genderInput").value;

    if (data.age > 19) {
        if (gender == "male") {
            var subject = "مرد";
        } else {
            var subject = "زن";
        }
    } else {
        if (gender == "male") {
            var subject = "پسر";
        } else {
            var subject = "دختر";
        }
    }

    modalBody.innerHTML = `این تست برای ${subject}ی ${data.age} ساله گرفته شده است<br>شاخص توده بدنی: ${data.bmi}`;

    bmiModal.show();
}
