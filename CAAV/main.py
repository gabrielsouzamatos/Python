from View import view
from Controller import controller
from Model import model
from View_GUI import view_GUI
controller = controller()
model = model()


op = input('Escolha a versão [G(gráfica)/T(texto)]:')

if op in 'Gg':
    view = view_GUI(controller)
elif op in 'Tt':
    view = view(controller)
else:
    print('Opção inválida!')
    exit()


controller.set(view, model)

view.run()