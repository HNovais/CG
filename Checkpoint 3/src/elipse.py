import math

# Define os parâmetros da elipse (semieixos a e b, centro C, ângulo de rotação θ)
a = 149.6e6   # semieixo maior em metros (distância média da Terra ao Sol)
b = 149.1e6   # semieixo menor em metros (distância mínima da Terra ao Sol)
Cx = 0        # coordenada x do centro da elipse
Cy = 0        # coordenada y do centro da elipse
theta = math.pi/4  # ângulo de rotação em radianos

# Define o número de pontos a serem gerados
num_points = 1000

# Gera a lista de pontos na elipse
points = []
for i in range(num_points):
    t = 2*math.pi*i/num_points
    x = a*math.cos(t)*math.cos(theta) - b*math.sin(t)*math.sin(theta) + Cx
    y = a*math.cos(t)*math.sin(theta) + b*math.sin(t)*math.cos(theta) + Cy
    print("\n")
    print(f'<point x="{x}" y="0" z="{y}" />')