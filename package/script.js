const output  = document.getElementById("output");
const startBtn = document.getElementById("startBtn");
let finalTranscript = "";

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.lang = "en-us"
recognition.interimResults = true;

startBtn.addEventListener('click', () => {
    finalTranscript = "";
    output.textContent = " ";
    recognition.start();
    startBtn.textContent = "Listening...";

});

recognition.addEventListener('result', (e) => {
    const transcript = Array.from(e.results).map(result => result[0].transcript).join('');

    if (e.results[0].isFinal){
        finalTranscript = transcript;
        output.textContent = finalTranscript;
    }
});

recognition.addEventListener('end', () => {
    startBtn.textContent = "START";
    recognition.start();
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape'){
        recognition.stop();
        startBtn.textContent = 'START';
    }
});