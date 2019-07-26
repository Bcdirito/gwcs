// Using the variables below, how can we add a hover event where we change our loremText to the revLorem text?

// How can we change it back through leaving on our mouse?

let loremText = document.getElementById("lorem").innerText

const revLorem = "sequi Culpa corporis natus commodi doloribus exercitationem praesentium quidem itaque nam tenetur rem est alias doloremque earum maxime perferendis quaerat fugiat Dolorem elit adipisicing consectetur amet sit dolor ipsum Lorem"




// The following algorithm was written to reverse the lorem text and remove punctuation

// const reverseText = () => {
//     let revString = ""
    
//     loremText.split(" ").forEach(word => {
//         let filtWord = word.split("").filter(char => {
//             return char !== "," && char !== "."
//         }).join("")
        
//         revString = `${filtWord} ` + revString
//     })

//     return revString
// }

// let reverse = reverseText()
