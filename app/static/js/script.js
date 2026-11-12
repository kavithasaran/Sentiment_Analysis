
const form = document.getElementById("sentimentForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const heading = document.getElementById("heading").value;
    const review = document.getElementById("review").value;
    const modelName = document.getElementById("model").value;

    resultDiv.innerHTML = "Predicting sentiment...";

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                heading: heading,
                review: review,
                model_name: modelName
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Prediction failed.");
        }

        resultDiv.innerHTML =
            `Predicted Sentiment: ${data.sentiment}`;

    } catch (error) {

        resultDiv.innerHTML = `Error: ${error.message}`;

    }

});
