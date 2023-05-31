# Projeto da aula
# Objetivo: Gerar automáticamente PDFs com Python
# Cenário: Emitir orçamentos para uma empresa

# Instalando a biblioteca para gerar o orçamento em PDF: !pip install fpdf
from fpdf import FPDF # importando a biblioteca

#Criando um arquivo PDF
pdf = FPDF()
pdf.add_page() # inserindo página
pdf.set_font('Arial') # escolhendo a fonte


# Dados para serem inseridos no PDF
projeto = input('Digite a descrição do projeto: ')
horas_estimadas = input('Digite o total de horas estimadas: ')
valor_hora = input('Digite o valor da hora trabalhada: R$')
prazo_estimado = input('Prazo de entrega: ')
valor_total = int(horas_estimadas) * int(valor_hora) #note que não foi usado input neste campo, porque é preenchido automáticamente.
# print(type(valor_total))

# Inserindo os dados no PDF
pdf.image('template.png', x = 0, y = 0) # usando o template oferecido na aula, com estas coordenadas pega toda a extensão do PDF
pdf.text(115, 145, projeto) # estes números são as coordenadas no PDF (y, x, variável que alimenta o input)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total))

pdf.output('Orcamento.pdf') # nome do arquivo e sua extensão
print('Orçamento gerado com sucesso!') # mensagem que aparece após o relatório ser gerado
# Lembre-se: Fechar o PDF antes de fazer modificações no código dele.