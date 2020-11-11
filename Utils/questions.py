import random


alunos = random.sample({'cana', 'pedro', 'felipe'}, 3)
questoes = random.sample(range(1, 6), 5)

it = iter(questoes)

for aluno in alunos:
    print(aluno, next(it), next(it, None))
