class Recursao:
    """
    Classe para estudo de recursão em programação
    """
    
    def __init__(self):
        print("Construindo classe.")
    
    @staticmethod
    def fact (n) :
        """
        Função recursiva para o cálculo de fatorial
        """
        if n < 0:
            raise ValueError('Negative number not allowed')
        elif n % 1 != 0:
            raise ValueError('Non integer numbers not allowed')
        elif n==0:
            return 1
        else:
            return n*Recursao.fact(n-1)
    
    @staticmethod
    def fib (n) :
        """
        Função recursiva para cálculo da sequência de fibonacci
        """
        if n < 0:
            raise ValueError('Negative number not allowed')
        elif n % 1 != 0:
            raise ValueError('Non integer numbers not allowed')
        elif n==0 or n==1:
            return 1
        else:
            return Recursao.fib(n-1) + Recursao.fib(n-2)
    
    @staticmethod
    def newton3 (x0,a,b,c,d) :
        """
        Função recursiva para calcular o método de newton para uma função do terceiro grau
        """

        x = x0 - (a*x0**3 + b*x0**2 + c*x0 + d)/(3*a*x0**2 + 2*b*x0 + c)

        if abs(x - x0) < 1e-6:
            return x
        else:
            return Recursao.newton3(x,a,b,c,d)
    
    @staticmethod
    def poly_newton (x0,args) :
        """
        Função recursiva para calcular o método de newton para uma função de grau n
        """
        
        precisao = 1e-14
        
        try:
#             print(x0)
            # soma da funcao no ponto x0:
            soma = sum([val*x0**(i) for i, val in enumerate(args)])
            
            # calculo da derivada da funcao no ponto x0:
            d = [i*val for i, val in enumerate(args) if i!=0]
            dsoma = sum([val*x0**(i) for i, val in enumerate(d)])

            # calculando o ponto x_(n+1):
            x = x0 - soma/dsoma

            # teste se a diferença entre o ultimo e o atual pontos é menor que um certo valor:
            if abs(x - x0) < precisao:
                return x
            else:
                return Recursao.poly_newton(x,args)
            
        except RecursionError:
            print("Sem raízes reais!")
            
    @staticmethod
    def briot_ruffini (x0, args) :
        """
        Função com o método de briot-ruffini para divisão entre polinomios
        """
        # invertendo a lista com os argumentos:
        args.reverse()
        
        # criando lista vazia para o resultado da divisao:
        divisao = []
        
        # iteração para conseguir os argumentos do polinomio resultante da divisão:
        for i, val in enumerate(args):
            if i==0:
                divisao.append(val)
            else:
                divisao.append(x0*divisao[i-1] + val)
        
        # salvando o resto em uma variável e invertendo os argumentos resultantes:
        resto = divisao.pop()
        divisao.reverse()
        
        return [divisao, resto]
    
    @staticmethod
    def eq_solver (x0, args_0) :
        """
        Junta os métodos briot_ruffini e poly_newton para achar todas as raízes de uma função de grau n
        """
        args = [args_0]
        roots = []
        for i in range(len(args_0)-1):
            print(i, ":")
            roots.append(Recursao.poly_newton(x0, args[i]))
            print("x"+str(i)+" =", roots[i],"\n")
            args.append(Recursao.briot_ruffini(roots[i], args[i])[0])
            print(args[i+1],"\n")

        return roots
    
    @staticmethod
    def durand_kerner (args) :
        pass
        
if __name__ == "__main__":
    print("Biblioteca de estudos de recursão e resolução de problemas númericos de João Mário Magalhães")