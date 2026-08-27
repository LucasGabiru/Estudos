import time  # Biblioteca padrão para dar intervalo de tempo

# range(início, fim, passo negativo)
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # Espera 1 segundo entre cada número

print("🚀 Decolar!")

import time 

for i in range (100, 0 , -10):
    print(f"seu personagem esta sangrando voce tem {i} de vida" )
    time.sleep(1)

print("Voce Morreu")