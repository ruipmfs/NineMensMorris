# Rui Pedro Santos   Aluno n 98966

'''********************************************************************************************************************************'''

# TAD POSICAO (2.1.1)

# - Construtor
def cria_posicao(c, l):
	'''
	Recebe duas cadeias de caracteres (uma da coluna e outra da linha), devolvendo a posicao correspondente.

	INPUT: coluna (str), linha (str)    OUTPUT: posicao (str)
	'''

	if c not in ('a', 'b', 'c') or l not in ('1', '2', '3') or type(c) != str or type(l) != str:
		raise ValueError('cria_posicao: argumentos invalidos')

	if c == 'a': return (int(l) - 1) * 3 + 1

	if c == 'b': return (int(l) - 1) * 3 + 2

	if c == 'c': return (int(l) - 1) * 3 + 3

def cria_copia_posicao(p):
	'''
	Recebe uma posicao e devolve uma copia nova da posicao.

	INPUT: posicao   OUTPUT: posicao
	'''

	c = obter_pos_c(p)
	l = obter_pos_l(p)

	return cria_posicao(c, l)

# - Seletores
def obter_pos_c(p):
	'''
	Recebe uma posicao e devolve a coluna correspondente dessa posicao.

	INPUT: posicao    OUTPUT: coluna (str)
	'''

	if p in (1, 4, 7): return 'a' 

	if p in (2, 5, 8): return 'b'
		
	if p in (3, 6, 9): return 'c' 
		
def obter_pos_l(p):
	'''
	Recebe uma posicao e devolve a linha correspondente dessa posicao.

	INPUT: posicao    OUTPUT: linha (str)
	'''

	if p in (1, 2, 3): return '1'

	if p in (4, 5, 6): return '2'

	if p in (7, 8, 9): return '3'

# - Reconhecedor
def eh_posicao(arg):
	'''
	Recebe um argumento e devolve True se este e um TAD posicao e False caso contrario.

	INPUT: argumento (universal)    OUTPUT: booleano
	'''

	return type(arg) == int and (1 <= arg <= 9)

# - Teste
def posicoes_iguais(p1, p2):
	'''
	Recebe duas posicoes e devolve True apenas se ambas forem posicoes validas e iguais.

	INPUT: p1 (posicao), p2 (posicao)    OUTPUT: bool
	'''

	return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

# - Transformador
def posicao_para_str(p):
	'''
	Recebe uma posicao e devolve a mesma em Str (formato 'cl').

	INPUT: posicao    OUTPUT: posicao (str)
	'''

	return str(obter_pos_c(p) + obter_pos_l(p))

# FUNCOES ALTO NIVEL PARA TAD POSICAO
def obter_posicoes_adjacentes(p):
	'''
	Recebe uma posicao e devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a ordem de leitura do tabuleiro.

	INPUT: posicao    OUTPUT: tuplo de posicoes (tuple())
	'''

	if posicoes_iguais(p, cria_posicao('a', '1')):
		return (cria_posicao('b', '1'), cria_posicao('a', '2'), cria_posicao('b', '2'))
	if posicoes_iguais(p, cria_posicao('b', '1')):
		return (cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('b', '2'))
	if posicoes_iguais(p, cria_posicao('c', '1')):
		return (cria_posicao('b', '1'), cria_posicao('b', '2'), cria_posicao('c', '2'))
	if posicoes_iguais(p, cria_posicao('a', '2')):
		return (cria_posicao('a', '1'), cria_posicao('b', '2'), cria_posicao('a', '3'))
	if posicoes_iguais(p, cria_posicao('b', '2')):
		return (cria_posicao('a', '1'), cria_posicao('b', '1'), cria_posicao('c', '1'), cria_posicao('a', '2'),
				cria_posicao('c', '2'), cria_posicao('a', '3'), cria_posicao('b', '3'), cria_posicao('c', '3'))
	if posicoes_iguais(p, cria_posicao('c', '2')):
		return (cria_posicao('c', '1'), cria_posicao('b', '2'), cria_posicao('c', '3'))
	if posicoes_iguais(p, cria_posicao('a', '3')):
		return (cria_posicao('a', '2'), cria_posicao('b', '2'), cria_posicao('b', '3'))
	if posicoes_iguais(p, cria_posicao('b', '3')):
		return (cria_posicao('b', '2'), cria_posicao('a', '3'), cria_posicao('c', '3'))
	if posicoes_iguais(p, cria_posicao('c', '3')):
		return (cria_posicao('b', '2'), cria_posicao('c', '2'), cria_posicao('b', '3'))

def posicao_para_inteiro(p):
	'''
	Recebe uma posicao e transforma a mesma em inteiro (1 a 9).

	INPUT: posicao    OUTPUT: inteiro (1 a 9)
	'''
	c = obter_pos_c(p)
	l = obter_pos_l(p)

	if c == 'a': return (int(l) - 1) * 3 + 1

	if c == 'b': return (int(l) - 1) * 3 + 2

	if c == 'c': return (int(l) - 1) * 3 + 3

'''********************************************************************************************************************************'''

# TAD PECA (2.1.2)

# - Construtor
def cria_peca(s):
	'''
	Recebe uma cadeia de caracteres validos que identifica o jogador ('X' ou 'O') ou uma peca livre (' ') e devolve a peca
	correspondente.

	INPUT: identificador (str)    OUTPUT: peca
	'''

	if s == 'X': return 1

	elif s == 'O': return -1

	elif s == ' ': return 0

	else: raise ValueError('cria_peca: argumento invalido')

def cria_copia_peca(j):
	'''
	Recebe uma peca e devolve uma copia nova da peca.

	INPUT: peca    OUTPUT: peca (copia)
	'''
	
	return j

# - Reconhecedor
def eh_peca(arg):
	'''
	Recebe um argumento e devolve True se este for um TAD peca e False caso contrario.

	INPUT: argumento (universal)    OUTPUT: booleano
	'''
	
	return type(arg) == int and arg in (1, 0, -1)

# - Teste
def pecas_iguais(j1, j2):
	'''
	Recebe duas pecas e devolve True apenas se ambas forem validas e iguais.

	INPUT: j1 (peca), j2 (peca)   OUTPUT: booleano
	'''
	
	return eh_peca(j1) and eh_peca(j2) and j1 == j2

# - Transformador
def peca_para_str(j):
	'''
	Recebe uma peca e devolve uma cadeia de caracteres que representa o jogador dono da peca ('X', 'O' ou ' ').

	INPUT: peca    OUTPUT: Identificador do dono da peca (str)
	'''
	
	if j == 1: return '[X]'

	elif j == -1: return '[O]'

	elif j == 0: return '[ ]'

# FUNCOES ALTO NIVEL PARA TAD PECA
def peca_para_inteiro(j):
	'''
	Recebe uma peca e devolve um inteiro (-1, 1 ou 0), dependendo se a peca e do jogador 'X', 'O' ou ' ', respetivamente.

	INPUT: peca    OUTPUT: inteiro (1, -1 ou 0)
	'''
	if peca_para_str(j) == '[X]': return 1

	elif peca_para_str(j) == '[O]': return -1

	elif peca_para_str(j) == '[ ]': return 0

'''********************************************************************************************************************************'''

# TAD TABULEIRO (2.1.3)

# - Construtor
def cria_tabuleiro():
	'''
	Devolve um tabuleiro do jogo do moinho sem posicoes ocupadas por pecas de jogadores.

	INPUT:    OUTPUT: tabuleiro vazio (str)
	'''
	return [cria_peca(' ') for i in range(9)]

def cria_copia_tabuleiro(t):
	'''
	Recebe um tabuleiro e devolve uma copia nova do tabuleiro.

	INPUT: tabuleiro    OUTPUT: tabuleiro (copia)
	'''

	return [cria_copia_peca(t[i]) for i in range(len(t))]  # Altera o ID de cada linha do tabuleiro

# - Seletores
def obter_peca(t, p):
	'''
	Recebe um tabuleiro e uma posicao e devolve a peca correpondente a essa posicao (devolve a peca livre caso a posicao 
	estiver livre).

	INPUT: tabuleiro, posicao    OUTPUT: peca
	'''

	return t[posicao_para_inteiro(p)-1]

def obter_vetor(t, s):
	'''
	Recebe um tabuleiro e uma cad. de caracteres correspondente a uma linha/coluna. Devolve um tuplo contendo todas as pecas
	da linha/coluna especificada.

	INPUT: tabuleiro, linha/coluna (str)    OUTPUT: tuplo de pecas
	'''
	
	if s == '1': return (t[0], t[1], t[2])

	if s == '2': return (t[3], t[4], t[5])

	if s == '3': return (t[6], t[7], t[8])

	if s == 'a': return (t[0], t[3], t[6])

	if s == 'b': return (t[1], t[4], t[7])

	if s == 'c': return (t[2], t[5], t[8])

# - Modificadores
def coloca_peca(t, j, p):
	'''
	Recebe um tabuleiro, uma peca e uma posicao e modifica destrutivamente o tabuleiro colocando a peca recebida na posicao
	recebida. Devolve o tabuleiro modificado.

	INPUT: tabuleiro, peca, posicao    OUTPUT: tabuleiro (modificado)
	'''

	t[posicao_para_inteiro(p)-1] = j

	return t

def remove_peca(t, p):
	'''
	Recebe um tabuleiro e uma posicao, modificando destrutivamente o tabuleiro removendo a peca do tabuleiro na posicao recebida.
	Devolve o tabuleiro modificado.

	INPUT: tabuleiro, posicao    OUTPUT: tabuleiro (modificado)
	'''

	t[posicao_para_inteiro(p)-1] = cria_peca(' ')
		
	return t

def move_peca(t, p1, p2):
	'''
	Recebe um tabuleiro e duas posicoes diferentes, modificando destrutivamente o tabuleiro recebido movendo a peca da posicao p1
	para a posicao p2, devolvendo o tabuleiro modificado.

	INPUT: tabuleiro, p1 (posicao), p2 (posicao)    OUTPUT: tabuleiro (modificado)
	'''

	peca = obter_peca(t, p1)

	return coloca_peca(remove_peca(t, p1), peca, p2)

# - Reconhecedor
def eh_tabuleiro(arg):
	'''
	Recebe um argumento e devolve True se este corresponder a um TAD tabuleiro e False caso contrario.

	INPUT: argumento    OUTPUT: booleano
	'''
	
	contador = 0
	
	# Se o contador chegar ao 9 significa que todas as posicoes / constituicao do tabuleiro sao validas

	if (type(arg) == list) and (len(arg) == 9):
		for i in range(9):
			if eh_peca(arg[i]):
				if len(obter_posicoes_jogador(arg, cria_peca('X'))) <= 3 and len(obter_posicoes_jogador(arg, cria_peca('O'))) <= 3 \
				and conta_ganhador(arg) <= 1 \
				and abs(len(obter_posicoes_jogador(arg, cria_peca('X'))) - len(obter_posicoes_jogador(arg, cria_peca('O')))) <= 1:
					contador += 1

	return contador == 9

def eh_posicao_livre(t, p):
	'''
	Recebe um tabuleiro e uma posicao. Se a posicao recebida estiver livre no tabuleiro recebido,
	a funcao devolve True, caso contrario devolve False.

	INPUT: tabuleiro, posicao    OUTPUT: booleano
	'''

	return t[posicao_para_inteiro(p)-1] == cria_peca(' ')

# - Teste
def tabuleiros_iguais(t1, t2):
	'''
	Recebe dois tabuleiros e apenas devolve True se ambos forem iguais.

	INPUT: tabuleiro, tabuleiro    OUTPUT: booleano
	'''

	if eh_tabuleiro(t1) and eh_tabuleiro(t2):
		lst = []

		for i in range(len(t1)):
			lst += [pecas_iguais(t1[i], t2[i])]
		return all(lst)

	return False

# - Transformador
def tabuleiro_para_str(t):
	'''
	Recebe um tabuleiro e devolve a cadeia de caracteres que representa o mesmo.

	INPUT: tabuleiro    OUTPUT: tabuleiro (str)
	'''

	grelha  = '   a   b   c\n'
	grelha += '1 ' + peca_para_str(t[0]) + '-' + peca_para_str(t[1]) + '-' + peca_para_str(t[2]) + '\n'
	grelha += '   | \\ | / |\n'
	grelha += '2 ' + peca_para_str(t[3]) + '-' + peca_para_str(t[4]) + '-' + peca_para_str(t[5]) + '\n'
	grelha += '   | / | \\ |\n'	
	grelha += '3 ' + peca_para_str(t[6]) + '-' + peca_para_str(t[7]) + '-' + peca_para_str(t[8])	

	return grelha

def tuplo_para_tabuleiro(t):
	'''
	Recebe um tuplo contendo 3 tuplos de 3 inteiros (3 linhas) e devolve o seu tabuleiro correspondente.

	INPUT: tabuleiro (tuplo)    OUTPUT: tabuleiro
	'''

	lst = []
	
	for i in range(len(t)):
		for j in range(len(t[i])):
			if t[i][j] == -1:
				lst += [cria_peca('O')]
			elif t[i][j] == 1:
				lst += [cria_peca('X')]
			elif t[i][j] == 0:
				lst += [cria_peca(' ')]

	return lst

# FUNCOES ALTO NIVEL PARA TAD TABULEIRO
def obter_ganhador(t):
	'''
	Recebe um tabuleiro e este devolve a peca do jogador que tiver ganho o jogo (3 pecas em linha).
	Caso nao haja jogador ganhador devolve a peca livre (' ').

	INPUT: tabuleiro    OUTPUT: peca (jogador ganhador / livre)
	'''

	# FALTA ABSTRACAO NA COMPARACAO DE PECAS

	for i in ('1', '2', '3', 'a', 'b', 'c'):
		v = obter_vetor(t, i)
		if all([pecas_iguais(p, cria_peca('X')) for p in v]):
			return cria_peca('X')
		elif all([pecas_iguais(p, cria_peca('O')) for p in v]):
			return cria_peca('O')
	return cria_peca(' ')

def obter_posicoes_livres(t):
	'''
	Recebe um tabuleiro e devolve um tuplo contendo todas as posicoes livres, isto e, todas as posicoes que nao estao ocupadas
	por pecas de jogadores.

	INPUT: tabuleiro    OUTPUT: posicoes livres (tuplo)
	'''

	tpl = ()

	for i in ('1', '2', '3'):
		for j in ('a', 'b', 'c'):
			pos = cria_posicao(j, i)
			peca = obter_peca(t, pos)
			if pecas_iguais(peca, cria_peca(' ')):
				tpl += (pos,)

	return tpl

def obter_posicoes_jogador(t, j):
	'''
	Recebe um tabuleiro e uma peca e devolve um tuplo contendo todas as posicoes do tabuleiro recebido ocupadas pelo jogador.

	INPUT: tabuleiro, peca    OUTPUT: posicoes do jogador (tuplo)
	'''
	tpl = ()

	for i in ('1', '2', '3'):
		for k in ('a', 'b', 'c'):
			pos = cria_posicao(k, i)
			peca = obter_peca(t, pos)
			if pecas_iguais(peca, j):
				tpl += (pos,)

	return tpl

'''********************************************************************************************************************************'''

#FUNCOES ADICIONAIS (2.2)

def em_colocacao(t):
	'''
	FUNCAO AUXILIAR
	Verifica se um tabuleiro esta em fase de colocacao ou de movimento
	Recebe um tabuleiro e devolve True se o tabuleiro esta em fase de colocacao e False casa contrario.

	INPUT: tabuleiro    OUTPUT: booleano
	'''

	posOcupadas = len(obter_posicoes_jogador(t, cria_peca('O'))) + len(obter_posicoes_jogador(t, cria_peca('X')))

	if posOcupadas < 6:
		return True

	return False

def obter_movimento_manual(t, j): # 2.2.1
	'''
	Recebe um tabuleiro e uma peca de um jogador, devolvendo um tuplo com uma ou duas posicoes que representam uma posicao ou
	um movimento introduzido manualmente pelo jogador.

	INPUT: tabuleiro, peca    OUTPUT: lista de posicoes (tuplo)
	'''

	# VERIFICACAO DE ARGUMENTOS
	if not eh_tabuleiro(t) or not eh_peca(j):
		raise ValueError('obter_movimento_manual: escolha invalida')
	
	# FASE DE COLOCACAO
	if em_colocacao(t):
		pos = str(input('Turno do jogador. Escolha uma posicao: '))

		if len(pos) != 2 or pos[0] not in ('a', 'b', 'c') or pos[1] not in ('1', '2', '3') or type(pos) != str \
			or not eh_posicao_livre(t, cria_posicao(pos[0], pos[1])):
			raise ValueError('obter_movimento_manual: escolha invalida')
		return (cria_posicao(pos[0], pos[1]),)

	# FASE DE MOVIMENTO
	else:
		pos = str(input('Turno do jogador. Escolha um movimento: '))

		if len(pos) != 4 or pos[0] not in ('a', 'b', 'c') or pos[2] not in ('a', 'b', 'c') \
			or pos[1] not in ('1', '2', '3') or pos[3] not in ('1', '2', '3'):
			raise ValueError('obter_movimento_manual: escolha invalida')

		if posicoes_iguais(cria_posicao(pos[0], pos[1]), cria_posicao(pos[2], pos[3])):
			contador = 0
			for i in obter_posicoes_jogador(t, j):
				for k in obter_posicoes_adjacentes(i):
					if obter_peca(t, k) == cria_peca(' '):
						contador += 1
			if contador == 0:
				return (cria_posicao(pos[0], pos[1]), cria_posicao(pos[2], pos[3]))
			else:
				raise ValueError('obter_movimento_manual: escolha invalida')

		if not eh_posicao(cria_posicao(pos[0], pos[1])) or not eh_posicao(cria_posicao(pos[2], pos[3])) \
			or cria_posicao(pos[0], pos[1]) not in obter_posicoes_jogador(t, j) \
			or cria_posicao(pos[2], pos[3]) not in obter_posicoes_livres(t) \
			or cria_posicao(pos[2], pos[3]) not in obter_posicoes_adjacentes(cria_posicao(pos[0], pos[1])):
			raise ValueError('obter_movimento_manual: escolha invalida')
		return (cria_posicao(pos[0], pos[1]), cria_posicao(pos[2], pos[3]))

def obter_movimento_auto(t, j, estg): # 2.2.2
	'''
	Recebe um tabuleiro, uma peca e uma cad. de caracteres representando o nivel de dificuldade do jogo. Devolve um tuplo com
	uma ou duas posicoes que representam uma posicao ou um movimento escolhido automaticamente.

	INPUT: tabuleiro, peca, dificuldade do jogo (str)    OUTPUT: lista de posicoes (tuplo)
	'''
	
	if em_colocacao(t):
		posDisp = obter_posicoes_livres(t)

		if crit_1(t, j) != None: return (crit_1(t, j),)
		elif crit_2(t, j) != None: return (crit_2(t, j),)
		elif crit_3(t, j) != None: return (crit_3(t, j),)
		elif crit_4(t, j) != None: return (crit_4(t, j),)
		elif crit_5(t, j) != None: return (crit_5(t, j),)

	else:
		if estg == 'facil': return estg_facil(t, j)
			
		elif estg == 'normal': return estg_normal(t, j)
			
		elif estg == 'dificil': return estg_dificil(t, j)			

def minimax(t, j, depth, seq_movimentos):
	'''
	FUNCAO RECURSIVA MINIMAX
	Recebe um tabuleiro, uma peca, uma peca ganhadora (mesma peca que a do computador), a profundidade e uma seq
	de movimentos (vazia). Ira analisar todas as hipoteses de jogada e devolver a que permite ganhar o jogo mais
	rapidamente consoante a profundidade (depth).

	INPUT: tabuleiro, peca, peca ganhadora, profundidade, seq vazia (tuplo)    OUTPUT: melhor resultado (lista),
	melhor seq de movimentos (tuplo)
	'''

	if not pecas_iguais(obter_ganhador(t), cria_peca(' ')) or depth == 0:
		return peca_para_inteiro(obter_ganhador(t)), seq_movimentos
	if pecas_iguais(j, cria_peca('O')):
		outro_jogador = cria_peca('X')
	else:
		outro_jogador = cria_peca('O')
	melhor_sequencia_movimentos = None
	melhor_resultado = peca_para_inteiro(outro_jogador)
	for posJogador in obter_posicoes_jogador(t, j):
		for posAdjacente in obter_posicoes_adjacentes(posJogador):
			if eh_posicao_livre(t, posAdjacente):
				novo_tabuleiro = cria_copia_tabuleiro(t)
				move_peca(novo_tabuleiro, posJogador, posAdjacente)
				novo_resultado, nova_seq_movimentos = minimax(novo_tabuleiro, outro_jogador, depth - 1, seq_movimentos + (posJogador, posAdjacente))
				if melhor_sequencia_movimentos == None or (pecas_iguais(j, cria_peca('X')) and novo_resultado > melhor_resultado) or (pecas_iguais(j, cria_peca('O')) and novo_resultado < melhor_resultado):
					melhor_resultado, melhor_sequencia_movimentos = novo_resultado, nova_seq_movimentos
	return melhor_resultado, melhor_sequencia_movimentos

def estg_facil(t, j):
	'''
	ESTRATEGIA FACIL
	Funcao que permite jogar na dificuldade facil. Recebe um tabuleiro e uma peca e devolve um tuplo contendo um movimento valido.

	INPUT: tabuleiro, peca    OUTPUT: movimento (tuplo)
	'''

	for pos in obter_posicoes_jogador(t, j):
		for i in obter_posicoes_adjacentes(pos):
			if eh_posicao_livre(t, i):
				return (pos, i)

def estg_normal(t, j):
	'''
	ESTRATEGIA NORMAL
	Funcao que permite jogar na dificuldade normal. Recebe um tabuleiro e uma peca e devolve um tuplo contendo um movimento valido.

	INPUT: tabuleiro, peca    OUTPUT: movimento (tuplo)
	'''

	melhor_resultado, melhor_sequencia_movimentos = minimax(t, j, 1, ())
	return melhor_sequencia_movimentos[0], melhor_sequencia_movimentos[1]

def estg_dificil(t, j):
	'''
	ESTRATEGIA DIFICIL
	Funcao que permite jogar na dificuldade dificil. Recebe um tabuleiro e uma peca e devolve um tuplo contendo um movimento valido.

	INPUT: tabuleiro, peca    OUTPUT: movimento (tuplo)
	'''

	melhor_resultado, melhor_sequencia_movimentos = minimax(t, j, 5, ())
	return melhor_sequencia_movimentos[0], melhor_sequencia_movimentos[1]

def crit_1(t, j):
	'''
	CRITERIO 1: VITORIA
	Recebe um tabuleiro e uma peca. Se a vitoria for possivel na proxima jogada, ou seja, uma sequencia de 3 pecas correspondentes
	a recebida for possivel, devolver essa posicao.

	INPUT: tabuleiro, peca    OUTPUT: posicao
	'''

	for posicao in obter_posicoes_livres(t):
		tabTeste = cria_copia_tabuleiro(t)
		tabTeste = coloca_peca(tabTeste, j, posicao)
		if pecas_iguais(j, obter_ganhador(tabTeste)):
			return posicao

def crit_2(t, j):
	'''
	CRITERIO 2: BLOQUEIO
	Recebe um tabuleiro e uma peca. Se o bloqueio for possivel na proxima jogada, ou seja, uma sequencia de 3 pecas nao correspondentes
	a recebida for possivel, devolver essa posicao.

	INPUT: tabuleiro, peca    OUTPUT: posicao
	'''

	if pecas_iguais(j, cria_peca('X')):
		pecaAdversario = cria_peca('O')
	else:
		pecaAdversario = cria_peca('X')
		
	for posicao in obter_posicoes_livres(t):
		tabTeste = cria_copia_tabuleiro(t)
		tabTeste = coloca_peca(tabTeste, pecaAdversario, posicao)
		if pecas_iguais(pecaAdversario, obter_ganhador(tabTeste)):
			return posicao

def crit_3(t, j): 
	'''
	CRITERIO 3: CENTRO
	Recebe um tabuleiro e uma peca. Se a posicao central (b2) estiver livre, devolver essa posicao.

	INPUT: tabuleiro, peca    OUTPUT: posicao
	'''

	if cria_posicao('b', '2') in obter_posicoes_livres(t): return cria_posicao('b', '2')

def crit_4(t, j):
	'''
	CRITERIO 4: CANTOS
	Recebe um tabuleiro e uma peca. Se algum dos cantos estiver livre, devolver essa posicao. Se existirem varios cantos
	disponiveis, devolver aquele que corresponde ao primeiro canto disponivel, por ordem crescente de posicao.

	INPUT: tabuleiro, peca    OUTPUT: posicao
	'''

	if cria_posicao('a', '1') in obter_posicoes_livres(t): return cria_posicao('a', '1')
	elif cria_posicao('c', '1') in obter_posicoes_livres(t): return cria_posicao('c', '1')
	elif cria_posicao('a', '3') in obter_posicoes_livres(t): return cria_posicao('a', '3')
	elif cria_posicao('c', '3') in obter_posicoes_livres(t): return cria_posicao('c', '3')

def crit_5(t, j):
	'''
	CRITERIO 5: LATERAIS
	Recebe um tabuleiro e uma peca. Se alguma das laterais estiver livre, devolver essa posicao. Se existirem varias laterais
	disponiveis, devolver aquela que corresponde a primeira lateral disponivel, por ordem crescente de posicao.

	INPUT: tabuleiro, peca    OUTPUT: posicao
	'''

	if cria_posicao('b', '1') in obter_posicoes_livres(t): return cria_posicao('b', '1')
	elif cria_posicao('a', '2') in obter_posicoes_livres(t): return cria_posicao('a', '2')
	elif cria_posicao('c', '2') in obter_posicoes_livres(t): return cria_posicao('c', '2')
	elif cria_posicao('b', '3') in obter_posicoes_livres(t): return cria_posicao('b', '3')

def conta_ganhador(t):
	'''
	Conta o numero de ganhadores, isto e, conta o numero de linhas / colunas que verificam a vitoria de um jogador.
	Recebe um tabuleiro e devolve um inteiro que corresponde ao numero de linhas / colunas ganhadoras.

	INPUT: tabuleiro    OUTPUT: inteiro (contador)
	'''
	contador = 0
	for i in ('1', '2', '3', 'a', 'b', 'c'):
		if obter_vetor(t, i) == (cria_peca('X'), cria_peca('X'), cria_peca('X')) \
		or obter_vetor(t, i) == (cria_peca('O'), cria_peca('O'), cria_peca('O')):
			contador += 1

	return contador

def moinho(str1, str2): # 2.2.3
	'''
	FUNCAO PRINCIPAL que permite jogar o jogo do moinho. Recebe duas cad. de caracteres, a peca com que o jogador deseja jogar
	e o nivel de dificuldade do jogo, respetivamente. Devolve uma cad. de caracteres que define o jogador ganhador ('[X]' ou '[O]'
	
	INPUT: peca jogador (str), dificuldade do jogo (str)    OUTPUT: peca jogador ganhador (str)
	'''
	t = cria_tabuleiro()

	if isinstance(str1, str) and str1 == '[X]':
		jogadorPeca = cria_peca('X')
		botPeca = cria_peca('O')
	elif isinstance(str1, str) and str1 == '[O]':
		jogadorPeca = cria_peca('O')
		botPeca = cria_peca('X')
	else:
		raise ValueError('moinho: argumentos invalidos')

	if isinstance(str2, str) and str2 in ('facil', 'normal', 'dificil'):
		estg = str2

	print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade " + estg + ".")

	print(tabuleiro_para_str(t))

	#Funcoes auxiliares para as jogadas (jogador e computador)
	
	def jogada_jogador(t, jogadorPeca):
		'''Realiza a jogada por parte do jogador

		INPUT: tabuleiro, ID (jogador)   OUTPUT: tabuleiro'''

		tuploPos = obter_movimento_manual(t, jogadorPeca)

		if em_colocacao(t):
			return coloca_peca(t, jogadorPeca, tuploPos[0])

		else:
			return move_peca(t, tuploPos[0], tuploPos[1])

	def jogada_bot(t, botPeca, estg):
		'''Realiza a jogada do computador

		INPUT: tabuleiro, ID (computador)'''

		print('Turno do computador (' + estg + '):')

		tuploPos = obter_movimento_auto(t, botPeca, estg)

		if em_colocacao(t):
			return coloca_peca(t, botPeca, tuploPos[0])

		else:
			return move_peca(t, tuploPos[0], tuploPos[1])

	vencedor = False
	resultado = obter_ganhador(t)
	vezJogador = False

	if pecas_iguais(jogadorPeca, cria_peca('X')):
		vezJogador = True

	while not vencedor:
		if vezJogador:
			t = jogada_jogador(t, jogadorPeca)
		
		else:
			t = jogada_bot(t, botPeca, estg)
			
		print(tabuleiro_para_str(t))
		resultado = obter_ganhador(t)

		if pecas_iguais(resultado, jogadorPeca):
			return peca_para_str(jogadorPeca)

		elif pecas_iguais(resultado, botPeca):
			return peca_para_str(botPeca)

		vezJogador = not vezJogador