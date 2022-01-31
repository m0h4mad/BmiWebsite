
const submitButton = document.getElementById("submitBtn");
const bmiModal = new bootstrap.Modal(document.getElementById("bmiModal"));

const UNDERWEIGHT = "underweight";
const NORMALWEIGHT = "normalweight";
const OVERWEIGHT = "overweight";
const OBESE = "obese";

submitButton.onclick = function (e) {
    e.preventDefault();
    let url = document.getElementById("bmiForm").action;
    let data = {
        weight: document.getElementById("weightInput").value,
        height: document.getElementById("heightInput").value,
        gender: document.getElementById("genderInput").value,
        year: document.getElementById("yearInput").value,
        month: document.getElementById("monthInput").value,
        day: document.getElementById("dayInput").value,
    };
    
    var query = `?weight=${data.weight}&height=${data.height}&gender=${data.gender}&year=${data.year}&month=${data.month}&day=${data.day}`
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
            coloringModalTitle(modalTitle, "text-danger");
            modalTitle.innerHTML = "شما چاق هستید";
            break;
        
        case OVERWEIGHT:
            coloringModalTitle(modalTitle, "text-warning");
            modalTitle.innerHTML = "شما اضافه وزن دارید";
            break;
        
        case NORMALWEIGHT:
            coloringModalTitle(modalTitle, "text-success");
            modalTitle.innerHTML = "شما وزن نرمال دارید";
            break;
        
        case UNDERWEIGHT:
            coloringModalTitle(modalTitle, "text-warning");
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

function coloringModalTitle(element, colorClass) {
    if (element.classList.length > 1) {
        element.classList.remove(element.classList[1]);
    }

    element.classList.add(colorClass);
}
