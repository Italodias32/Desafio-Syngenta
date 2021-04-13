# Desafio Syngenta Digital

## Desafio 1

Inicialmente, foi proposto que um código fosse criado para contagem de pixels verdes de uma imagem, bem como encontrar uma mensagem escondida no arquivo. 

Para resolução do desafio, foi utilizado a linguagem de programação Python, pois a possibilidade de uso de uma framework, OPENCV, permite conferir de forma rápida se os trechos de código escritos estavam corretos. Isso porque, a ideia de uma mensagem escondida trouxe a possibilidade de alguma técnica de esteganografia, assim sendo, é necessário fazer a manipulação dos dados binários do código. Logo, para conferir se a primeira parte do desafio estava correta é possível utilizar o OPENCV.

Com base nisso, a primeira coisa a ser feita é realizar a leitura do arquivo e ler o cabeçalho do BITMAP para conferir alguns dados importantes da imagem, como o número de pixels e o número de bits por pixels.

```python
    file_name = sys.argv[1] 
    file_name = file_name.split(".")[0]

    with open(f'{file_name}.bmp','rb') as image:
    	image.seek(10, 0)
    	offset = int.from_bytes(image.read(4),"little")
    
   	image.seek(18, 0)
    	image_w = int.from_bytes(image.read(4),"little")
    	image_h = int.from_bytes(image.read(4),"little")
    
    	print('Header data:') #Bmp header data
    	print('Width of the bitmap in pixels = ', image_w)
    	print('Height of the bitmap in pixels. Positive for bottom to top pixel order = ', image_h)
    	print('Number of color planes being used = ', int.from_bytes(image.read(2),"little"))
    	print('Number of bits per pixel = ', int.from_bytes(image.read(2),"little"))
    	print('BI_RGB, no pixel array compression used = ', int.from_bytes(image.read(4),"little"))
    	print('Size of the raw bitmap data (including padding) = ' + str(int.from_bytes(image.read(4),"little")) + '\n')
```

Com os de largura, image_w, e altura, image_h, é possível percorrer toda a imagem, já que o tamanho dos dados em bitmap com padding é igual ao produto de largura por altura, ou seja, não possui preenchimento de dados. 

Com o valor de offset é possível mover o cursor que percorre a imagem para o primeiro bit que contém os dados da figura e como, segundo o cabeçalho, o número de bits por pixels é 8, significa que cada pixels possui 256 possibilidades de cores. 

```python
    image.seek(offset, 0)
    
    image_list = []
    
    for line in range(image_h): #Pixel count
        for byte in range(image_w):
            	byte = image.read(1)
	    	image_list = search_in_list(image_list,int.from_bytes(byte,"little"))
```

A função search_in_list busca uma cor em uma lista, se a cor está presente ela incrementa o contador, se não ele adiciona a cor e coloca o contador de cores em 1. Essa função se aproveitou da tipagem dinâmica do Python, da noção de escopo e da manipulação de dados no stack. Toda vez que a função é chamada uma nova lista é criada, passando a antiga lista como referência, assim, a referência da lista antiga é substituída pela nova, como a tipagem é dinâmica, assim que a referência é perdida o interpretador do Python retira o dado do stack. Em resumo, uma lista de cores é criada.

```python
    def search_in_list(list, value):
	found_flag = 0
	if len(list) != 0:
        	for i in list:
            		if i[0] == value:
                		i[1] = i[1] + 1
                		found_flag = 1
	if found_flag == 0:
		list.append([value, 1])
	return list
```

Ademais, os valores de bits estão na forma little endian para organização dos bits menos significativos. O resultado obtido é exibido na figura a seguir:

Logo, o número de pontos verdes é de 298.

## Desafio 2 - Tentativas

1. Para o desafio 2, a primeira tentativa foi aplicar métodos de esteganografia sobre a imagem. Primeiro foi criado um vetor com o bit menos significativo de cada pixels e esse valor foi salvo em uma string, quando um contador indicava 8 bits um caracter de quebra de linha era adicionado na string, \n, por fim, um split era aplicado sobre o caracter \n e cada elemento da lista formada era convertido de binário para inteiro e de inteiro para char, esse char era concatenado em um array. 

2. A segunda tentativa, envolvia contar no número de pixels verdes por linha e transformar em um binário, a cada oito números. Foi constatado que todas as linhas possuíam 1 pixels verde, assim todos os números obtidos eram igual a 255, 11111111 em binário. Ou seja, sem a mensagem.

```python
    for line in range(image_h): #Pixel count
        for byte in range(image_w):
            byte = image.read(1)
            image_list = search_in_list(image_list,int.from_bytes(byte,"little"))
            little = int.from_bytes(byte,"big")
            little = bin(little)
            little = little[-1]
            little_endian = little_endian + little
            if cont % 8 == 7:
                little_endian = little_endian + '\n'
            cont = cont + 1
            if int.from_bytes(byte,"little") == 51:
                cont = cont + 1
        image_point_per_line.append([line, cont])
        image_str = image_str + str(cont)
        if line % 8 == 7:
            image_str = image_str + '\n'
        cont = 0
```

3. A terceira tentativa foi com relação a realização do mesmo procedimento anterior, mas avaliando com relação às colunas, todavia algumas colunas apresentavam 2 pixels verdes. Assim, um split era aplicado a cada caracter “2” e o restante dos números era transformado para inteiro e depois para char, não obtendo nenhuma mensagem também.

```python
    for col in range(image_w): #Pixel count
        for line in range(image_h):
            byte = image.read(1)
            image_char = chr(int.from_bytes(byte,"little"))
            image_list = search_in_list(image_list,int.from_bytes(byte,"little"))
            if int.from_bytes(byte,"little") == 255:
                cont = cont + 1
        image_point_per_line.append([col, cont])
        image_str = image_str + str(cont)
        if col % 8 == 7:
            image_str = image_str + '\n'
        cont = 0
```

4. A quarta tentativa foi alterar os tons das imagens, todavia pelo algoritmo desenvolvido para a primeira parte, apenas 3 cores de pixel eram visíveis, verde, preto e branco.

Em resumo, as tentativas foram concentradas em analisar os dados binários da imagem e infelizmente nenhuma mensagem foi encontrada.
 
