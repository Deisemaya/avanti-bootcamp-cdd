
zoo = ("tigre", "gato", "cachorro", "canguru", "camelo", "baleia")
animal = input('Escolha um animal: ').lower()
if animal in zoo:
    print("animal na lista")
else:
    print("animal ausente")