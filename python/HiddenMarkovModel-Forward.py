#%% Probabilidades de la cadena

A = [[0.5 , 0.5],    # Cambiar clima -> clima  ej: A X1,X0 = 0.5
     [0.3 , 0.7]]    # P(X1,X0) = 0.5

B = [[0.8 , 0.2],    # Cambiar clima -> ánimo  ej: B Y0,X1 = 0.4
     [0.4 , 0.6]]    # P(Y0,Y1) = 0.4

C = [0.375 , 0.625]  # Vector probabilidad ó pronóstico del clima para los compas

E = [0,0,1]          # Orden de eventos Y0 = 0 y Y1 = 1
                      # 0 = :(   1 = :)



#problema: dado un clima, en tres días distintos, cual es la probabilidad
#          de estar triste, al día siguiente triste, y al tercer día
#          felíz?

# se resuelve con cadenas ocultas de Markov, se usará el algoritmo Forward.

# Rta: 0.1344



#%% Markov como matriz

def alpha(t,E):
    global A,B,C
    if t == 1:
        v = []
        for i in range(len(B)):
            v.append(round(C[i]*B[i][E[0]],4))
        return v

    else:
        u = [0 for i in range(len(A))]
        for j in range(len(B)):
            for k in range(len(B)):
                u[j] += (alpha(t-1 , E)[k] * A[k][j] * B[j][E[t-1]])
        return u


#print(alpha(3,E)) #Testing



def HMM(E):
    return sum(alpha(len(E),E))* 100

print("Probabilidad de Tiempo t bajo los eventos E: "+ str(HMM(E)) + " %")

