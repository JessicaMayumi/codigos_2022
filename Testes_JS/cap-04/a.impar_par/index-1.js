const frm = document.querySelector("form")
const resp = document.querySelector("h3")

frm.addEventListener("submit", (e) => {
    const num = Number(frm.inNumber.value)

    const verificador = num%2==0 ? "par" : "ímpar"

    resp.innerText = `${num} é ${verificador}.`
    e.preventDefault()
})