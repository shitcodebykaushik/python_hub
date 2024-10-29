const startBtn = document.getElementById('start-btn');
const submitBtn = document.getElementById('submit-btn');
const nextLevelBtn = document.getElementById('next-level-btn');
const bcaPathBtn = document.getElementById('bca-path-btn');
const btechPathBtn = document.getElementById('btech-path-btn');

const startSection = document.getElementById('start-section');
const quizSection = document.getElementById('quiz-section');
const resultSection = document.getElementById('result-section');

const questionContainer = document.getElementById('question-container');
const resultMessage = document.getElementById('result-message');
const quizLevel = document.getElementById('quiz-level');

let userId = "user123";
let currentLevel = "start";
let selectedPath = null;

// Start the quiz
startBtn.addEventListener('click', () => {
    fetch(`http://127.0.0.1:5000/start?user_id=${userId}`)
        .then(response => response.json())
        .then(data => {
            loadQuestions(data.questions, 1);
            currentLevel = "level1";
            toggleSections(quizSection);
        });
});

// Submit answers for each level
submitBtn.addEventListener('click', () => {
    const answers = Array.from(document.querySelectorAll('.answer')).map(input => input.value);

    fetchLevelEndpoint(currentLevel, answers).then(data => {
        resultMessage.textContent = data.message;
        toggleSections(resultSection);

        if (data.options) {
            document.getElementById('path-selection').classList.remove('hidden');
        } else if (data.questions) {
            nextLevelBtn.classList.remove('hidden');
            nextLevelBtn.onclick = () => loadQuestions(data.questions, currentLevel === "level1" ? 2 : 3);
        }
    });
});

// Choose between BCA or B.Tech path
bcaPathBtn.addEventListener('click', () => selectPath("bca"));
btechPathBtn.addEventListener('click', () => selectPath("btech"));

// Load questions for each level
function loadQuestions(questions, level) {
    questionContainer.innerHTML = "";
    quizLevel.textContent = `Level ${level}`;
    
    questions.forEach((question, index) => {
        const questionEl = document.createElement('div');
        questionEl.className = 'question';
        questionEl.innerHTML = `
            <p>${index + 1}. ${question[0]}</p>
            <input type="text" class="answer" placeholder="Your answer">
        `;
        questionContainer.appendChild(questionEl);
    });

    toggleSections(quizSection);
}

// Toggle sections visibility
function toggleSections(showSection) {
    [startSection, quizSection, resultSection].forEach(section => {
        section.classList.add('hidden');
    });
    showSection.classList.remove('hidden');
}

// Submit answers to the correct endpoint based on the level
async function fetchLevelEndpoint(level, answers) {
    let endpoint = `http://127.0.0.1:5000/${level}`;
    let payload = { user_id: userId, answers };

    if (level === "level3") payload.path = selectedPath;

    const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
    return response.json();
}

// Select BCA or B.Tech path
function selectPath(path) {
    selectedPath = path;
    currentLevel = "level3";
    fetchLevelEndpoint("level3", []).then(data => {
        resultMessage.textContent = data.message;
        toggleSections(resultSection);
    });
}
