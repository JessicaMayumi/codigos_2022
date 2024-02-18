const primeiraNota = Number(prompt("Insira a primeira nota: "))
const segundaNota = Number(prompt("Insira a segunda nota: "))
const media = (primeiraNota+segundaNota)/2

alert (`Primeira Nota: ${primeiraNota.toFixed(1)}\nSegunda Nota: ${segundaNota.toFixed(1)}\nMédia: ${media.toFixed(1)}`)