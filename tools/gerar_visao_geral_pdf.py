from reportlab.lib.pagesizes import A4
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import sys

D = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('Sans', D + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('Sans-B', D + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Sans-I', D + 'DejaVuSans-Oblique.ttf'))
pdfmetrics.registerFont(TTFont('Serif-B', D + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Serif', D + 'DejaVuSerif.ttf'))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('Sans', normal='Sans', bold='Sans-B', italic='Sans-I', boldItalic='Sans-B')

OCRE = colors.HexColor('#8a5a24'); ESCURO = colors.HexColor('#2a1c10'); CLARO = colors.HexColor('#f6efe3'); LINHA = colors.HexColor('#d8c6a8'); VERDE = colors.HexColor('#3d5a3a'); CINZA = colors.HexColor('#6b5b4a')
st = {
 'h1': ParagraphStyle('h1', fontName='Serif-B', fontSize=20, leading=25, textColor=ESCURO, spaceBefore=4, spaceAfter=10),
 'h2': ParagraphStyle('h2', fontName='Sans-B', fontSize=12.5, leading=16, textColor=OCRE, spaceBefore=12, spaceAfter=6),
 'p': ParagraphStyle('p', fontName='Sans', fontSize=9.6, leading=14, textColor=ESCURO, spaceAfter=6),
 'li': ParagraphStyle('li', fontName='Sans', fontSize=9.6, leading=14, textColor=ESCURO, leftIndent=12, bulletIndent=2, spaceAfter=2),
 'small': ParagraphStyle('small', fontName='Sans', fontSize=8.2, leading=11, textColor=CINZA),
 'cell': ParagraphStyle('cell', fontName='Sans', fontSize=8.4, leading=11.2, textColor=ESCURO),
 'cellb': ParagraphStyle('cellb', fontName='Sans-B', fontSize=8.4, leading=11.2, textColor=ESCURO),
 'th': ParagraphStyle('th', fontName='Sans-B', fontSize=8.4, leading=11, textColor=colors.white),
 'box': ParagraphStyle('box', fontName='Sans', fontSize=9.6, leading=14, textColor=ESCURO),
}
P = lambda t, s='p': Paragraph(t, st[s])
def bullets(items): return [Paragraph(i, st['li'], bulletText='•') for i in items]
def tabela(rows, widths, head=True):
    data = [[Paragraph(c, st['th'] if (head and r == 0) else (st['cellb'] if j == 0 else st['cell'])) for j, c in enumerate(row)] for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if head else 0)
    s = [('VALIGN', (0, 0), (-1, -1), 'TOP'), ('GRID', (0, 0), (-1, -1), .4, LINHA), ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5)]
    if head: s += [('BACKGROUND', (0, 0), (-1, 0), OCRE)]
    for i in range(1 if head else 0, len(rows)):
        if i % 2 == 0: s.append(('BACKGROUND', (0, i), (-1, i), CLARO))
    t.setStyle(TableStyle(s)); return t
def caixa(texto, cor=CLARO, borda=OCRE):
    t = Table([[Paragraph(texto, st['box'])]], colWidths=[17 * cm]); t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), cor), ('BOX', (0, 0), (-1, -1), .8, borda), ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10), ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)])); return t

def capa(c, d):
    c.saveState(); W, H = A4
    c.setFillColor(ESCURO); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(OCRE); c.rect(0, H * .36, W, 3, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#f0d6a8')); c.setFont('Serif-B', 44); c.drawCentredString(W / 2, H * .62, 'GILGAMESH')
    c.setFont('Serif', 17); c.setFillColor(colors.HexColor('#d9b98a')); c.drawCentredString(W / 2, H * .62 - 30, 'Aquele que viu o abismo')
    c.setFont('Sans', 12.5); c.setFillColor(colors.HexColor('#efe4d2')); c.drawCentredString(W / 2, H * .5, 'Visão geral do projeto: direção, o que já temos,')
    c.drawCentredString(W / 2, H * .5 - 18, 'o que falta e o que instalar')
    c.setFont('Sans', 10); c.setFillColor(colors.HexColor('#b59a77')); c.drawCentredString(W / 2, H * .3, '5 de novembro de 2026  ·  versão 1')
    c.drawCentredString(W / 2, H * .3 - 16, 'Repositório: github.com/cristianojoseblanco/gilgamesh')
    c.restoreState()
def pagina(c, d):
    c.saveState(); W, H = A4
    c.setStrokeColor(LINHA); c.setLineWidth(.5); c.line(2 * cm, H - 1.4 * cm, W - 2 * cm, H - 1.4 * cm)
    c.setFont('Sans', 7.8); c.setFillColor(CINZA); c.drawString(2 * cm, H - 1.2 * cm, 'GILGAMESH · visão geral do projeto'); c.drawRightString(W - 2 * cm, H - 1.2 * cm, '5 nov. 2026')
    c.drawCentredString(W / 2, 1.1 * cm, str(d.page - 1)); c.restoreState()

doc = BaseDocTemplate(sys.argv[1], pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=1.8 * cm, title='Gilgamesh — visão geral do projeto', author='Cristiano Blanco')
fr = Frame(2 * cm, 1.8 * cm, A4[0] - 4 * cm, A4[1] - 3.8 * cm, id='f')
doc.addPageTemplates([PageTemplate(id='capa', frames=[fr], onPage=capa), PageTemplate(id='normal', frames=[fr], onPage=pagina)])
from reportlab.platypus import NextPageTemplate
S = [NextPageTemplate('normal'), PageBreak()]

# 1. Em uma página
S += [P('1. O projeto em uma página', 'h1')]
S += [P('<b>O que é.</b> Um jogo 3D de ação e aventura narrativa baseado na <i>Epopeia de Gilgamesh</i>, o poema mais antigo da humanidade. O jogador vive as 12 tabuletas da versão padrão babilônica como Gilgamesh, rei de Uruk, e em alguns trechos como Enkidu. A moldura é um escriba de Nínive copiando as tabuletas antes da queda da cidade.')]
S += [P('<b>O que o torna diferente.</b> Fidelidade ao texto e à arqueologia, com transparência: tudo o que aparece no jogo é marcado no <b>Codex</b> como <i>evidência</i>, <i>interpretação</i> ou <i>invenção do jogo</i>, com fonte. Trechos que faltam nas tabuletas antigas começam "quebrados" no jogo e são completados por <b>fragmentos</b> que o jogador encontra.')]
S += [P('<b>Quem faz.</b> Cristiano Blanco e um amigo, em dupla, com o PC do amigo em uso constante, mais o Claude para roteiro, pesquisa, dados, guias passo a passo e prévias.')]
S += [P('<b>Onde estamos.</b> A fundação está pronta: decisões tomadas, roteiro do Ato 1 em rascunho, dados estruturados, pesquisa visual de época, três prévias jogáveis no navegador e o material para começar no Unreal. O próximo passo é instalar tudo no PC e criar o projeto no Unreal Engine.')]
S += [Spacer(1, 6), caixa('<b>A direção em cinco linhas</b><br/>1. <b>Unreal Engine 5, estilo realista</b>, com luz de cinema e materiais fotográficos.<br/>2. <b>Uruk em escala real</b>: cerca de 9 km de muralha, braço do Eufrates, canais e barcos de junco.<br/>3. <b>Fiel ao poema e à arqueologia</b>, sem esconder o que é invenção (Codex com três camadas).<br/>4. <b>O medo e a amizade como sensações jogáveis</b>: a viagem à Floresta de Cedros é tensa como um jogo de terror, e Enkidu é o único remédio.<br/>5. <b>Primeiro um protótipo do Ato 1</b> (Tabuletas I e II); só depois o jogo inteiro.')]

# 2. Direção
S += [P('2. A direção do projeto', 'h1')]
S += [P('Pilares', 'h2')]
S += bullets(['<b>A obra no centro.</b> O roteiro segue a versão padrão babilônica (George 2003 para conferir; Brandão 2017 para o português). Todo texto do jogo é escrito pelo projeto, sem copiar traduções modernas.',
 '<b>Transparência histórica.</b> Cada personagem, roupa, objeto e prédio tem uma ficha com fonte. O que vem de outra época aparece como interpretação no Codex.',
 '<b>Lacunas como mecânica.</b> Cenas danificadas no original começam quebradas; fragmentos coletados completam a cena ou abrem a versão babilônica antiga.',
 '<b>Sensação antes de espetáculo.</b> A repetição ritual da viagem, o silêncio da floresta, o peso de dobrar o joelho na luta: o jogo tenta fazer sentir o que o poema faz sentir.',
 '<b>Escopo honesto.</b> Protótipo pequeno, decisão formal depois dele, atos cortáveis se preciso.'])
S += [P('Decisões já tomadas', 'h2')]
S += [tabela([['Nº', 'Decisão', 'Resumo'],
 ['001', 'Escala de Uruk', 'Escala real (muralha de ~9 km, cerca de 17 mil casas na prévia). A escala comprimida (30 a 40%) fica guardada como alternativa.'],
 ['002', 'Fundação', 'Moldura: o escriba copia as tabuletas e o jogo termina na escavação. Edição de referência: George 2003 + Brandão 2017. Gilgamesh à frente dos outros projetos, com mais de 10 horas por semana. Nome final e GPU em aberto.'],
 ['003', 'Engine e estilo', 'Unreal Engine 5 e estilo realista, no lugar de Godot e estilo pintado. Custos aceitos: hardware, curva de aprendizado e repositório pesado.'],
 ['—', 'Equipe', 'Projeto em dupla, com PC constante. Regras de colaboração para não perder trabalho em arquivos do Unreal.']], [1.2 * cm, 3.2 * cm, 12.6 * cm])]
S += [P('Estrutura do jogo', 'h2')]
S += [tabela([['Ato', 'Tabuletas', 'Conteúdo'],
 ['Moldura', '—', 'Nínive, por volta de 640 a.C.: o escriba copia; no fim, a cidade cai e as tabuletas são escavadas no século XIX.'],
 ['1', 'I e II', 'O rei que não dá descanso, Enkidu na estepe, Shamhat, os sonhos, os pastores, a luta à porta e a amizade. <b>É o protótipo.</b>'],
 ['2', 'III a V', 'Os conselhos, a viagem do medo, a Floresta de Cedros e Humbaba.'],
 ['3', 'VI a VIII', 'Ishtar e o Touro do Céu, a morte de Enkidu, o luto.'],
 ['4', 'IX e X', 'O caminho do sol, Siduri, as águas da morte.'],
 ['5', 'XI', 'O dilúvio, a prova do sono, a planta e a serpente, a volta à muralha.'],
 ['Epílogo', 'XII', 'Outra tradição: Enkidu no mundo dos mortos.']], [1.8 * cm, 2.2 * cm, 13 * cm])]

# 3. O que já temos
S += [PageBreak(), P('3. O que já temos', 'h1')]
S += [P('Prévias jogáveis (abrem no navegador do celular)', 'h2')]
S += [tabela([['Prévia', 'O que mostra', 'Link'],
 ['Uruk em escala real', 'A cidade inteira: muralha de ~9 km, Eufrates e canais, barcos de junco, zigurate de Eanna, terraço de Anu, minimapa, 4 fragmentos.', '<link href="https://claude.ai/artifact/5DrjnZcyZzWZCXUoHjgFxF" color="#8a5a24"><u>claude.ai/artifact/5DrjnZcyZzWZCXUoHjgFxF</u></link>'],
 ['Ato 1 jogável', 'O roteiro das Tabuletas I e II em 8 capítulos: mesa do escriba, estepe com Enkidu, sonhos, pastores e combate, a luta à porta, a amizade.', '<link href="https://claude.ai/artifact/MVba6GTmdFEfDWSWtnVmM9" color="#8a5a24"><u>claude.ai/artifact/MVba6GTmdFEfDWSWtnVmM9</u></link>'],
 ['Prévia do medo (Ato 2)', 'As cinco noites do ritual, a borda da floresta, a cacofonia e o silêncio, Humbaba com auras e os ventos de Shamash. Sistema de Pavor com visão turva e som.', '<link href="https://claude.ai/artifact/2dg8FGtYZ2u1hRnUhcsGTg" color="#8a5a24"><u>claude.ai/artifact/2dg8FGtYZ2u1hRnUhcsGTg</u></link>']], [3.4 * cm, 8.2 * cm, 5.4 * cm])]
S += [P('As prévias são privadas da conta do Cristiano até ele compartilhar o link com o amigo. Todas foram feitas só com geometria gerada por código: servem para validar escala, roteiro e ritmo, não são a arte final.', 'small')]
S += [P('No repositório (<link href="https://github.com/cristianojoseblanco/gilgamesh">github.com/cristianojoseblanco/gilgamesh</link>)', 'h2')]
S += [tabela([['Onde', 'O que tem'],
 ['docs/GDD-v1.0.pdf + GDD-1.1-adendo.md', 'Documento de design completo e as seções atualizadas para Unreal e realismo (prazos, arquitetura, riscos).'],
 ['docs/decisoes/', 'Decisões 001 (escala), 002 (fundação) e 003 (Unreal e realismo), com o porquê de cada uma.'],
 ['docs/roteiro/ato1.md', 'Roteiro do Ato 1 cena a cena, com falas do jogo separadas do texto antigo.'],
 ['docs/design/medo-a-caminho-da-floresta.md', 'Design do medo: repetição como mecânica, sistema de Pavor, as cinco noites, Encorajar, silêncio da floresta, combate com Humbaba, acessibilidade e como fazer no Unreal.'],
 ['docs/pesquisa/visual-dinastico-arcaico.md', 'Pesquisa visual de época com fontes: cabelo, roupa, joias, armas, animais, arquitetura, barcos e uma lista do que evitar.'],
 ['docs/personagens/fichas-ato1.md', 'Fichas para criar os MetaHumans: Gilgamesh, Enkidu (duas fases), Shamhat, Ninsun, caçador, pastores, multidão.'],
 ['docs/unreal/ 01 e 02', 'Guias passo a passo dos primeiros Blueprints: fragmento coletável e mesa do escriba.'],
 ['docs/fim-de-semana-pc.md', 'Roteiro da primeira ida ao PC: instalação e 4 sessões.'],
 ['docs/colaboracao.md + diario.md', 'Regras de trabalho em dupla e diário de sessões.'],
 ['data/', 'Roteiro e Codex em dados: 12 tabuletas, 12 episódios, 6 fragmentos, 10 entradas do Codex, 15 fontes e a planta de Uruk (layout_uruk.json).'],
 ['unreal/importar/', 'Pronto para importar: blockout de Uruk em escala real (glTF, 73 malhas, ~820 mil triângulos), DataTables em JSON e imagens provisórias da mesa do escriba.'],
 ['tools/', 'Validador dos dados, exportadores para o Unreal e montador da prévia do Ato 1.'],
 ['previa-web/', 'Código das três prévias.']], [5.6 * cm, 11.4 * cm])]

# 4. O que falta
S += [PageBreak(), P('4. O que falta fazer', 'h1')]
S += [P('Estimativas para duas pessoas com mais de 10 horas por semana cada e PC em uso constante. Dupla não dobra a velocidade: parte do tempo vai em coordenação e em aprender juntos.')]
S += [tabela([['Fase', 'Entregas', 'Status', 'Prazo'],
 ['0. Fundação', 'Repositório, decisões, fontes, dados', '<font color="#3d5a3a"><b>Feita</b></font> (falta conferir fontes nos livros)', '—'],
 ['1. Aprender Unreal', 'Projeto criado, Uruk importada, personagem andando, primeiros Blueprints', 'Próxima', '3 a 4 semanas'],
 ['2. Roteiro do protótipo', 'Tabuletas I e II, diálogos, Codex, fragmentos', '<font color="#3d5a3a"><b>Rascunho 1 feito</b></font>; revisar com George e Brandão', 'em paralelo'],
 ['3. Protótipo cinza', 'Todo o Ato 1 jogável sem arte, seguindo a prévia', 'A fazer', '6 a 8 semanas'],
 ['4. Arte e som do protótipo', 'Materiais de época, MetaHumans com roupa de época, animação, áudio', 'A fazer', '10 a 16 semanas'],
 ['5. Teste e polimento', '5 a 10 pessoas jogando, desempenho, acessibilidade', 'A fazer', '3 a 4 semanas'],
 ['6. Decisão', 'Seguir, reduzir escopo ou parar', 'A fazer', '1 semana'],
 ['7. Atos 2 a 5', 'O jogo completo', 'Design do medo do Ato 2 adiantado', '14 a 24 meses'],
 ['8. Lançamento', 'Inglês, loja, trailer', 'A fazer', '2 a 3 meses']], [3.6 * cm, 6.2 * cm, 4.6 * cm, 2.6 * cm])]
S += [Spacer(1, 6), caixa('<b>Leitura honesta dos prazos.</b> Protótipo realista: <b>5 a 8 meses</b>. Jogo completo: <b>2 a 3 anos</b>. O item mais caro é fazer personagens realistas de época (roupa, cabelo, animação facial). O MetaHuman não traz roupa suméria: ela terá de ser modelada.')]
S += [P('Pendências abertas', 'h2')]
S += bullets(['Conferir as 15 fontes nos livros (todas estão "a conferir").', 'Revisar o roteiro do Ato 1 com George 2003 e Brandão 2017 (lista de 5 conferências no fim do arquivo).', 'Definir o nome final do jogo.', 'Anotar a configuração do PC (processador, RAM, placa de vídeo) e ajustar as metas de desempenho.', 'Ajustar o ritmo do medo jogando a prévia do Ato 2 com fones.'])

# 5. Ferramentas
S += [PageBreak(), P('5. O que instalar no PC', 'h1')]
S += [P('O PC precisa, segundo a Epic, de Windows 11, 32 GB de RAM e placa de vídeo com 8 GB ou mais. Reserve pelo menos <b>150 GB livres em SSD</b>. Instale nesta ordem: o download do Unreal é o mais longo, então comece por ele.')]
S += [tabela([['Ferramenta', 'Para quê', 'Quando', 'Observações'],
 ['Driver de vídeo', 'Rodar o Unreal sem travar', 'Já', 'NVIDIA ou AMD, versão estável mais recente.'],
 ['Epic Games Launcher + Unreal Engine 5', 'O motor do jogo: níveis, Blueprints, luz, animação, cinemáticas', 'Já', 'Versão estável mais recente (5.7 ou mais nova). Grátis; royalty de 5% só acima de US$ 1 milhão de receita bruta por jogo. Download de dezenas de GB.'],
 ['Conta Epic (uma por pessoa)', 'Launcher, Fab e MetaHuman', 'Já', 'Ativar verificação em duas etapas.'],
 ['Git for Windows', 'Controle de versão', 'Já', 'Já vem com o Git LFS. Rodar "git lfs install" uma vez.'],
 ['GitHub Desktop', 'Usar o Git sem linha de comando', 'Já (opcional)', 'Cada um com a própria conta, de preferência em perfis separados do Windows.'],
 ['Fab (dentro do editor)', 'Materiais fotográficos: terra, tijolo de barro, reboco, água', 'Fim de semana', 'Os assets não entram no Git: baixam de novo em cada máquina.'],
 ['MetaHuman', 'Personagens realistas', 'Fim de semana', 'Incluído na licença do Unreal. Roupas de época à parte.'],
 ['Blender', 'Roupas e objetos de época, ajustes de malha', 'Fase 4', 'Grátis.'],
 ['Visual Studio', 'Só se o projeto usar C++', 'Depois', 'O protótipo começa só com Blueprints. Se precisar, usar a versão indicada pela Epic para a versão do Unreal instalada.'],
 ['Controle de videogame', 'Testar como jogador', 'Fase 3', 'Qualquer controle compatível com Windows.'],
 ['Python 3 (opcional)', 'Rodar o validador e os exportadores de dados', 'Fase 3', 'Hoje o Claude roda esses scripts na nuvem; no PC é opcional.']], [3.6 * cm, 4.2 * cm, 2.2 * cm, 7 * cm])]
S += [P('Primeiro fim de semana (resumo de docs/fim-de-semana-pc.md)', 'h2')]
S += bullets(['<b>Sábado, sessão 1:</b> adicionar o amigo como colaborador no GitHub; clonar o repositório numa pasta curta (C:\\dev\\gilgamesh); criar o projeto Unreal "Gilgamesh" (Third Person, Blueprint, sem Starter Content); primeiro commit.',
 '<b>Sábado, sessão 2:</b> nível Open World; importar o blockout de Uruk; ligar a colisão; Player Start em Eanna; andar até a porta sul e subir o zigurate; anotar o FPS. <b>Este é o teste decisivo do PC.</b>',
 '<b>Domingo, sessão 3:</b> materiais da Fab no blockout; luz de fim de tarde; MetaHuman de teste de Gilgamesh pela ficha.',
 '<b>Domingo, sessão 4:</b> structs e DataTables; Blueprint do fragmento (guia 01); anotar no diário a posição do zigurate (para o Claude fechar a conversão de coordenadas).'])

# 6. Como trabalhamos
S += [PageBreak(), P('6. Como trabalhamos em dupla', 'h1')]
S += [P('Arquivos do Unreal (.uasset e .umap) <b>não se juntam</b> como código: se os dois editam o mesmo arquivo ao mesmo tempo, o trabalho de um se perde. As regras de docs/colaboracao.md evitam isso:')]
S += bullets(['<b>Travas:</b> antes de editar um Blueprint, material ou nível, travar o arquivo no Git LFS ("git lfs lock") e destravar depois do push.', '<b>Níveis:</b> One File Per Actor (já ativo em níveis Open World), para os dois mexerem em partes diferentes de Uruk.', '<b>Ramos:</b> um ramo por tarefa; juntar na main por Pull Request depois de abrir o projeto e apertar Play.', '<b>Divisão:</b> uma pessoa puxa <i>Sistemas</i> (Blueprints de jogo); a outra puxa <i>Mundo e arte</i> (Uruk, materiais, MetaHumans, cinemáticas). Roteiro, dados e pesquisa são dos dois, com o Claude.', '<b>Nomes:</b> prefixos padrão (BP_, WBP_, DT_, S_, SM_, M_, MI_, T_, L_) e pastas por assunto em Content/Gilgamesh.', '<b>Ritual:</b> começo de sessão com pull e travas; fim com push, destravar e 2 ou 3 linhas no diário. O diário é o que o Claude lê para continuar de onde vocês pararam.'])
S += [P('Papel do Claude', 'h2')]
S += bullets(['Roteiro, Codex, fragmentos e dados (YAML), com validação.', 'Pesquisa histórica e visual com fontes.', 'Guias passo a passo de Blueprints, materiais e configuração.', 'Prévias jogáveis no navegador para testar ideias antes do PC.', 'Exportação de dados e da planta de Uruk para o Unreal.', 'No PC, pode trabalhar direto no repositório (lendo e alterando arquivos), o que diminui o copiar e colar.'])
S += [P('7. Riscos principais', 'h1')]
S += [tabela([['Risco', 'O que fazemos'],
 ['Escopo grande demais', 'Protótipo do Ato 1 primeiro e decisão formal na fase 6; atos cortáveis.'],
 ['Personagens realistas caros e o "vale da estranheza"', 'Fichas com fonte, testes cedo, câmera e luz que favoreçam a silhueta.'],
 ['Anacronismos mais visíveis no realismo', 'Pesquisa visual com lista do que evitar; cada asset com ficha.'],
 ['Conflito de arquivos em dupla', 'Travas do LFS, ramos, um dono por arquivo.'],
 ['Cota grátis do GitHub LFS (10 GiB de armazenamento e 10 GiB de banda por mês)', 'Assets da Fab e MetaHumans fora do Git; acompanhar o uso todo mês.'],
 ['Hardware abaixo do recomendado', 'Teste decisivo na sessão 2; escalabilidade média; Lumen em modo software.'],
 ['Erros históricos ou de tradução', 'Fontes em todo texto; revisão com edição crítica; Codex com camadas.']], [6 * cm, 11 * cm])]
S += [Spacer(1, 10), caixa('<b>Próximo passo:</b> sábado, instalar tudo e fazer o teste decisivo (Gilgamesh andando na Uruk em escala real). Até lá, pelo celular: jogar as prévias, anotar o que ajustar no medo e conferir as fontes nos livros que estiverem à mão.', colors.HexColor('#eef3ea'), VERDE)]
doc.build(S)
