from graphviz import Digraph

class Graficar():
    
    def graficar(self, matriz):
        dot = Digraph(comment = "Variable")

        dot.node('raiz', 'Matrices')
        #Raiz apunta al nodo Padre
        dot.node('padre','Ejemplo')
        dot.edge('raiz', 'padre')
        #Padre apunta al nodo Fila
        dot.node('fila', 'n=' + str(len(matriz)))
        dot.edge('padre', 'fila')
        #Padre apunta al nodo Columna
        dot.node('columna', 'm=' + str(len(matriz[0])))
        dot.edge('padre', 'columna')

        contador = 1
        salto = len(matriz)
        
        for columna in range(len(matriz[0])):
            primero = 0
            for fila in range(len(matriz)):
                dot.node(str(contador), str(matriz[fila][columna]))
                
                if primero == 0: 
                    dot.edge('padre', str(contador))
                    primero += 1
                    contador += 1
                else:
                    dot.edge(str(contador-1), str(contador))
                    contador += 1
        
        dot.render("Matriz", format="png", view=True)

    
