import openpyxl

# carregado arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')

# seleciona uma pagina
pagina_frutas = book['Frutas']

# Imprimindo os dados de cada linha
for rows in pagina_frutas.iter_rows(min_row=2,max_row=5):
    for cell in rows:
        # mudar o nome da celula
        if cell.value == 'Banana':
            cell.value = "laranja Crava"
    #    print(cell.value)
    #print(rows[0].value,rows[1].value,rows[2].value)

 # salvar a planilha
book.save('Planilha de Compras_v2.xlsx')   

