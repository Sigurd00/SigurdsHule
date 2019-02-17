/* ------------- VARIABLER -------------- */
//forms
let button = document.getElementById("calc_button");
let save_button = document.getElementById('save_button');
let textArea = document.getElementsByName("Text1")[0];
let lixScoreField = document.getElementById("lixScore_field");
let numWordsField = document.getElementById("numWords_field");
let numPeriodsField = document.getElementById("numPeriods_field");
let numSentencesField = document.getElementById("numSentences_field");
let avgSentenceLengthField = document.getElementById("avgSentenceLength_field");
let classField = document.getElementById("class_field");
let mostUsedWord = document.getElementById("mostUsedWord_field");
//labels
let lixScoreLabel = document.getElementById("lixScore_label");
let numWordsLabel = document.getElementById("numWords_label");
let numPeriodsLabel = document.getElementById("numPeriods_label");
let numSentencesLabel = document.getElementById("numSentences_label");
let avgSentenceLengthLabel = document.getElementById("avgSentenceLength_label");
let classLabel = document.getElementById("class_label");
let mostUsedWordLabel = document.getElementById("mostUsedWord_label");

// Lister
let words;// = ["Mercury","Gemini","Apollo","Skylab","Skylab B","ISS"]
let dots;
let sætninger;
let classColors = ["#00FF00","#32CD32","#00FFFF","#008080","#FFFF00","#FFA500","#FF4500","#FF0000","#800000"];


/* ------------- ARBEJDE -------------- */
button.onclick = function () {

    /* Kald jeres funktioner her! */
    /* Hvad skal der ske når vi trykker på knappen? */

    /* I kan få teksten indtastet af brugeren således: */
    let userInput = textArea.value;

    // Andet arbejde
    dots = numDots(userInput);
    words = ordListe(userInput);
    sentences = numSentences(userInput);

    /* I kan udfylde de grå kasser således: */
    if (dots !== 0) {
        if (!document.getElementById("errorMessage").classList.contains('d-none')) {
            document.getElementById("errorMessage").classList.add('d-none')
        }
        lixScoreField.innerHTML = lixtal(words, dots);
        numWordsField.innerHTML = words.length;
        numPeriodsField.innerHTML = dots;
        numSentencesField.innerHTML = sentences;
        avgSentenceLengthField.innerHTML = words.length / dots;
        classField.innerHTML = getKlasseTrin(lixtal(words, dots)) + ". Klasse";
        mostUsedWord.innerHTML = getMostUsedWord(words);
        classLabel.style.color = classColors[getKlasseTrin(lixtal(words, dots)) - 1];
        //Labels
        lixScoreLabel.innerHTML = lixtal(words, dots);
        numWordsLabel.innerHTML = words.length;
        numPeriodsLabel.innerHTML = dots;
        numSentencesLabel.innerHTML = sentences;
        avgSentenceLengthLabel.innerHTML = words.length / dots;
        classLabel.innerHTML = getKlasseTrin(lixtal(words, dots)) + ". Klasse";
        mostUsedWordLabel.innerHTML = getMostUsedWord(words);
    }
    else {
        document.getElementById("errorMessage").classList.remove('d-none')
    }
};




/* ------------- FUNKTIONER -------------- */



/* Retunere antal punktummer i teksten. */
function numDots(myString) {
    let sum = 0
    for (let i =0; i < myString.length; i++){
        if (myString[i] === "."){
            sum++
        }
    }
    return sum
}

function numSentences(myString) {
    let sum = 0
    for (let i =0; i < myString.length; i++){
        if (myString[i] === "." && (i-1 >= 0 && myString[i-1] !== ".")){
            sum++
        }
    }
    return sum
}

/* Retunere antallet af lange ord */
function longWordsCount(words) {
    let sum = 0;
    for (let i = 0; i < words.length; i++) {
        if (words[i].length >=7){
            sum++
        }
    }
    return sum
}


/* Retunere lixtallet */
function lixtal(words, dots) {
    let A = words.length;
    let B = dots;
    let C = longWordsCount(words);
    return A/B + (C*100/A)
}

/*Retunere hvilket klassetrin teksten passer til */
function getKlasseTrin(lixtal) {
    if(lixtal < 10) {
        return 1
    }
    else if (lixtal < 20) {
        return 2
    }
    else if (lixtal < 25) {
        return 3
    }
    else if (lixtal < 30) {
        return 4
    }
    else if (lixtal < 35) {
        return 5
    }
    else if (lixtal < 40) {
        return 6
    }
    else if (lixtal < 45) {
        return 7
    }
    else if (lixtal < 50) {
        return 8
    }
    else {
        return 9
    }
}

/* Returnerer 'true' hvis symbolet er et bogstav, ellers returneres 'false' */
function isLetter(str) {
    return str.length === 1 && str.match(/[a-z]/i);
}

/*
Tager teksten i en string som input og returnerer
en liste af ord uden kommaer eller punktummer.
*/
function ordListe(text) {

    let WordList = text.split(" ");

    for (var i = 0; i < WordList.length; i++) {
        WordList[i] = WordList[i].split(',').join("");
        WordList[i] = WordList[i].split('.').join("");
    }

    return WordList;
}

/* Finder det mest brugte ord */

function getMostUsedWord(words){
    let seenWords = [];
    let numSeen = [];
    for(let i = 0; i < words.length; i++){
        let index = wordSeen(words[i],seenWords)
        if(index !== -1){
            numSeen[index] = numSeen[index] + 1
        }
        else {
            numSeen.push(1);
            seenWords.push(words[i])
        }
    }
    index = 0
    for (let i = 1; i < numSeen.length; i++){
        if (numSeen[index] < numSeen[i]){
            index = i
        }
    }
    return seenWords[index]
}

function wordSeen(word,seenWords){
    for(let i = 0; i < seenWords.length; i++){
        if (seenWords[i] === word){
            return i
        }
    }
    return -1
}
