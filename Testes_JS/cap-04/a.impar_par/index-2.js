const frm = document.querySelector("form")
const resp = document.querySelector("h3")

frm.addEventListener("submit", (e) => {
    const num = Number(frm.inNumber.value)
    const valor = num%2

    let verificador
    if (valor==0) {
        verificador = "par"
    } else {
        verificador = "ímpar"
    }

    resp.innerText = `${num} é ${verificador}.`
    e.preventDefault()
})