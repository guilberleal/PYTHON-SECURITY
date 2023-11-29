import random, string
import os

tamanho = int(input('Digite o tamanho da senha desejada: '))
chars = string.ascii_letters + string.digits + '!@#$%&*,./?'

rnd = random.SystemRandom()

print("".join(rnd.choice(chars)for i in range(tamanho)))