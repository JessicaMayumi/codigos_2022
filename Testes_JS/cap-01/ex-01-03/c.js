const preco = Number(prompt("Insira o valor do produto: "))

alert (`Preço: ${preco.toFixed(2)}\nÀ vista: R$${(preco*0.90).toFixed(2)}\nOu 3x de: R$${(preco/3).toFixed(2)}`)