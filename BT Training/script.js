// Age verification check
function checkAge() {
    const isOldEnough = confirm("Are you 21 years old or older?");
    if (isOldEnough) {
        document.getElementById('content').style.display = 'block';
        updatePresentation(); // Initialize the first presentation
    } else {
        alert("You must be 21 years or older to view this content.");
        window.location.href = "https://www.google.com"; // Redirect or handle as needed
    }
}

// Array of Google Sheets presentation URLs
const presentations = [
    "https://docs.google.com/spreadsheets/d/your-first-sheet-id/preview",
    "https://docs.google.com/spreadsheets/d/your-second-sheet-id/preview",
    "https://docs.google.com/spreadsheets/d/your-third-sheet-id/preview"
];

// Current presentation index
let currentIndex = 0;

// Function to update the iframe src
function updatePresentation() {
    const frame = document.getElementById('presentation-frame');
    frame.src = presentations[currentIndex];
}

// Event listeners for buttons
document.getElementById('prev-button').addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        updatePresentation();
    }
});

document.getElementById('next-button').addEventListener('click', () => {
    if (currentIndex < presentations.length - 1) {
        currentIndex++;
        updatePresentation();
    }
});

// Run the age check when the page loads
window.onload = checkAge;
