with open('citacao.txt', 'a') as arquivo:
       
            arquivo.write(input("adicone a sua citação ")+ "\n")
            pergunta = input("deseja adicionar outo pergunta ")
            while pergunta == "s":
                arquivo.write(input(" adicone a adione sua nova citação citação.")+"\n")
                pergunta = input("deseja adicionar outro pergunta ")