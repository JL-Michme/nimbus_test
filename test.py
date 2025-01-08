'''
Create and call a python function that : 
- stores a random integer A between 1 and 9
- stores a random integer B between 1 and 9
- multiplies A and B together as C
- Prints A and C for every result until C = 4
- If C = 4 , print ‘Success!’ and the results for A and B
- Store your code on a GitHub account and share it with the email-address given in the SQL test, including your CV
'''

import random

def la_mia_funzione():

    while True:
        #Si Generano due numeri random usando la libreria random tra 1 e 9 uno nella variabile A e l'altro nella variabile B
        A = random.randint(1, 9)
        B = random.randint(1, 9)
        # Si moltiplicano i due numeri e si salva il risultato nella variabile C
        C = A * B
        # Si stampa il valore di A e C finche C non è uguale a 4
        print(f"A: {A}, C: {C}")
        # nel caso C sia uguale a 4, stampa il messaggio di successo e i valori di A e B per poi uscire dal ciclo while
        if C == 4:
            #Se C è uguale a 4 si va a stampare il messaggio di successo e i valori di A e B
            print(f"Success! A: {A}, B: {B}")
            break

la_mia_funzione()