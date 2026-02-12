const form = document.getElementById("sentimentForm")
const textInput = document.getElementById("textInput")
const resultContainer = document.getElementById("resultContainer")
const errorContainer = document.getElementById("errorContainer")
const sentimentResult = document.getElementById("sentimentResult")
const confidenceResult = document.getElementById("confidenceResult")
const errorMessage = document.getElementById("errorMessage")

form.addEventListener("submit", async (e) => {
  e.preventDefault()

  const text = textInput.value.trim()

  if (!text) {
    showError("Please enter some text")
    return
  }

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    })

    const data = await response.json()

    if (!response.ok) {
      showError(data.error || "An error occurred")
      return
    }

    displayResult(data)
  } catch (error) {
    showError("Failed to analyze sentiment. Please try again.")
    console.error("Error:", error)
  }
})

function displayResult(data) {
  errorContainer.classList.add("hidden")

  const sentiment = data.sentiment.toLowerCase()
  const confidence = data.confidence

  sentimentResult.innerHTML = `
        <div class="sentiment-label">Detected Sentiment</div>
        <div class="sentiment-value ${sentiment}">
            ${data.sentiment}
        </div>
    `

  confidenceResult.innerHTML = `
        <div class="confidence-label">Confidence Score</div>
        <div class="confidence-bar">
            <div class="confidence-fill" style="width: ${confidence}%"></div>
        </div>
        <div class="confidence-value">${confidence}%</div>
    `

  resultContainer.classList.remove("hidden")
}

function showError(message) {
  resultContainer.classList.add("hidden")
  errorMessage.textContent = message
  errorContainer.classList.remove("hidden")
}
