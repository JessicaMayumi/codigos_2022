const frm = document.querySelector("form")
const resp = document.querySelector("h2")

frm.addEventListener("submit", (e)=> {
    const vPermitida = Number(frm.inPermitida.value)
    const vCondutor = Number(frm.inCondutor.value)

    let situacao
    if (vCondutor<=vPermitida){
    situacao = "Sem Multa"
    } else if ((vPermitida*1.2)<vCondutor){
    situacao = "Multa Grave"
    } else {
    situacao = "Multa Leve"
    }

    resp.innerText = `Situação: ${situacao}`
    e.preventDefault()
})