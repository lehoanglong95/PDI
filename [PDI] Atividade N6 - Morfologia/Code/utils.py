import matplotlib.image as mpimg
import numpy as np

# leitura da imagem
def LerImagem(nome):
    imagem = mpimg.imread(nome)
    return imagem

# as operações foram interpretadas como sendo as classicas
# utilizando dos pixels nas correspondentes de uma imagem 
# para outra

def operation(img1,img2, operation):
    img1 = np.array(img1[:,:,0], dtype=bool)
    img2 = np.array(img2[:,:,0], dtype=bool)
    x,y = np.shape(img1)
    if(operation == 'and'):
        return [[img1[i][j] and img2[i][j] for j in range(y)]for i in range(x)]
    elif(operation == 'or'):
        return [[img1[i][j] or img2[i][j] for j in range(y)]for i in range(x)]
    elif(operation == 'xor'):
        return [[((not img1[i][j]) and (img2[i][j])) or ((img1[i][j]) and (not img2[i][j])) for j in range(y)]for i in range(x)]
    # seria um xnor?
    elif(operation == 'xand'):
        return [[((not img1[i][j]) and (not img2[i][j])) or ((img1[i][j]) and (img2[i][j])) for j in range(y)]for i in range(x)]


# quando for utilizado deve definir quanto deverá ser transladado
# por padrão os espaços desconhecidos (fora do escopo da imagem o-
# riginal) são preenchidos com 0
def translacao(conjunto, Zx = 0, Zy = 0):
    x,y = np.shape(conjunto) 
    return [
        [
            conjunto[Zx+i][Zy+j]
            if Zx+i>0 and Zy+j>0 and Zx+i<x and Zy+j<y
            else 0 
            for j in range(y)
        ]
        for i in range(x)
    ]

# def reflexao(conjunto):
# TODO será util para implementação da dilatação

# def intersercao(A,B):
# TODO será util para implementação da dilatação