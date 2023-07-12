empresa = "DAVDA COMPANY"
pesos_total = "Capital neto en Pesos: 550.000 ARS "
venta_de_iphone ="La venta del iPhone nos genero " + str(550000) 
binance_P2p = "La compra de ARS A USDT ES DE 1200$"
usdt_a_Guaranies = 1200 *(7230)
usdt_a_Guaranies2 = "La conversion de USDT a Guaranies es de " +str(usdt_a_Guaranies)
compra_del_iphone = "La compra del iPhone es de " + str(usdt_a_Guaranies -(6000000))
ganancia = "La ganancia total es de " + str(usdt_a_Guaranies -(6000000))

total =empresa + "\n" + "\n" + pesos_total + "\n" + venta_de_iphone + "\n" + binance_P2p +"\n" + usdt_a_Guaranies2 + "\n" + compra_del_iphone + "\n" + ganancia

print(total)
input("Presiona Enter para continuar...")