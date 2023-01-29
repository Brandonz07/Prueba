let playerAttack
let enemyAttack

function startgame() { 
    let buttonPetsPlayer = document.getElementById('button-pets')
    buttonPetsPlayer.addEventListener('click', selectionpetplayer)

    let buttonFire = document.getElementById('button-fire')
    buttonFire.addEventListener('click', fireAttack)
    let buttonWater = document.getElementById('button-water')
    buttonWater.addEventListener('click', waterAttack)
    let buttonLand = document.getElementById('button-land')
    buttonLand.addEventListener('click', landAttack)
}

function selectionpetplayer() {
    let inputhipodoge = document.getElementById('hipodoge')
    let inputcapipepo = document.getElementById('capipepo')
    let inputratigueya = document.getElementById('ratigueya')
    let spanPetPlayer = document.getElementById('pet-player')

    if (inputhipodoge.checked) {
        spanPetPlayer.innerHTML = 'Hipodoge'
    }else if (inputcapipepo.checked) {
        spanPetPlayer.innerHTML = 'Capipepo'
    }else if (inputratigueya.checked) {
        spanPetPlayer.innerHTML = 'Ratigueya'
    }else {
        alert('you did not select anything')
    }

    selectionpetenemy()
}

function selectionpetenemy() {
    let aleatoryPet = aleatory(1,3)
    let spanpetenemy = document.getElementById ('pet-enemy')

    if (aleatoryPet == 1) {
        spanpetenemy.innerHTML = 'Hipedoge'
    } else if (aleatoryPet == 2) {
        spanpetenemy.innerHTML = 'Capipepo'
    } else if (aleatoryPet == 3) {
        spanpetenemy.innerHTML = 'Ratigueya'
    }
}

function fireAttack() {
    playerAttack = 'FIRE'
    enemyAleatoryAttack()
}
function waterAttack() {
    playerAttack = 'WATER'
    enemyAleatoryAttack()
}
function landAttack() {
    playerAttack = 'LAND'
    enemyAleatoryAttack()
}

function enemyAleatoryAttack() {
    let aleatoryAttack = aleatory(1,3)

    if (aleatoryAttack == 1) {
        enemyAttack = 'FIRE'
    } else if (aleatoryAttack == 2) {
        enemyAttack = 'WATER'
    } else if (aleatoryAttack == 3) {
        enemyAttack = 'LAND'
    }

    createMessage()
}

function createMessage() {
    let sectionMessanges = document.getElementById('messanges')
    
    let paragraph = document.createElement('p')
    paragraph.innerHTML = 'your pet attack with ' + playerAttack + ', the enemys pet attack whit ' + enemyAttack +',earring '

    sectionMessanges.appendChild(paragraph)
}

function aleatory (min, max) {
    return Math.floor(Math.random() * (max - min + 1) + 1)
}

window.addEventListener('load', startgame)