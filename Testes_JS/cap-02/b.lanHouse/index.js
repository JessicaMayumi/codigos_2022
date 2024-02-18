const frm = document.querySelector("form")
const resp = document.querySelector("h4")

frm.addEventListener("submit", (e) => {
    const valor = Number(frm.inValor.value)
    const tempo = Number(frm.inTempo.value)

    const total = Math.ceil((tempo/15))

    resp.innerText = `Valor a Pagar: R$${(total*valor).toFixed(2)}`
    e.preventDefault()
})