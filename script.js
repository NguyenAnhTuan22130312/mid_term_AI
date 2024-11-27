function checkSpam() {
    var emailMessage = document.getElementById("emailInput").value;

    fetch("http://127.0.0.1:5000/check_spam", {  // Chắc chắn rằng URL trỏ đến Flask server
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: emailMessage })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Kết quả: " + data.result;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
