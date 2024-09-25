numero_placa = input("Digite o numero final da placa do veiculo: ")

match numero_placa:
    case "1" | "2": print("Rodizio na Segunda-feira")
    case "3" | "4": print("Rodizio na Terça-feira")
    case "5" | "6": print("Rodizio na Quarta-feira") 
    case "7" | "8": print("Rodizio na Quinta-feira")
    case "9" | "0": print("Rodizio na Sexta-feira")
    case _: print("Final da placa invalido")
    
    