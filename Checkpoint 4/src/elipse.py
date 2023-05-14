import math

# Define os parâmetros da elipse (semieixos a e b, centro C, ângulo de rotação θ)
a = 194.5  # semieixo maior em metros (distância média da Terra ao Sol)
b = 194.5   # semieixo menor em metros (distância mínima da Terra ao Sol)
c = 50
Cx = 0        # coordenada x do centro da elipse
Cy = 0        # coordenada y do centro da elipse
Cz = 0
theta = math.pi/4  # ângulo de rotação em radianos

# Define o número de pontos a serem gerados
num_points = 14

# Gera a lista de pontos na elipse


for i in range(num_points):
    t = 2*math.pi*i/num_points
    phi = math.pi/2  # Ângulo de rotação em torno do eixo z (pode ser alterado para mudar a orientação da elipse)
    x = a*math.cos(t)*math.cos(phi) + Cx
    y = b*math.cos(t)*math.sin(phi) + Cy
    z = c*math.sin(t) + Cz
    print(f'<point x="{x}" y="{z}" z="{y}" />')