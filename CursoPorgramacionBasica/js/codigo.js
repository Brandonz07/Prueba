function aleatory (min, max) {
    return Math.floor(Math.random() * (max - min + 1) + 1)
}

function choice(move) {
    let result = ''
    if(move == 1) {
        result = 'rock🥌'
    } else if(move == 2) {
        result = 'paper🧻'
    } else if(move == 3){
        result = 'scissor✂'
    } else {
        result = 'you did not choose any number'
    }
    return result
}

function combat () {
    if(pc == player) {
        alert('tie')
    } else if((player == 1 && pc == 3) || (player == 2 && pc == 1) || (player == 3 && pc == 2)) {
        alert('you win')
        succes += 1 
    }else {
        alert('you lose')
        losses += 1
    }
}

// 1 is rock, 2 is paper, 3 is scisssor
let player = 0
let pc = 0 
let succes = 0
let losses = 0

while (succes < 3 && losses < 3) {
    pc = aleatory (1, 3)
    player = prompt('choose: 1 for rock, 2 for paper, 3 for scissor')
    //alert('you chose ' + player)

    alert('you chose ' + choice(player))
    alert('pc chose ' + choice(pc))

    //combat
    combat()
}

alert('you won ' + succes + ' times. you lost ' + losses + ' times.')

