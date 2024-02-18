const frm = document.querySelector("form")
const resp1 = document.querySelector("h3")
const resp2 = document.querySelector("h4")

frm.addEventListener("submit", (e) => {
    const nome = frm.inNome.value
    const preco = Number(frm.inPreco.value)

    const promocao = Math.floor(preco*2)

    resp1.innerText = `Promoção de ${nome}`
    resp2.innerText = `Leve 2 por apenas R$${promocao.toFixed(2)}`

    e.preventDefault()
})