import matplotlib.pyplot as plt
import numpy as np
import mathutil
import popup


def graph():
    fig = plt.figure(figsize=(10.5, 8))
    ax = fig.add_subplot(111)

    valueX = 1
    a = []
    a.append(0.0)
    while len(a) < int(popup.factor):
        a.append(valueX / popup.factor)
        valueX = valueX + 1
    b = []
    b.append(0.0)

    while len(b) < int(popup.factor):
        b.append(0.0)

    x = a
    y = b

    li, = ax.plot(x, y)

    fig.suptitle('test title', fontsize=20)
    plt.xlabel('Params(t) t = %s' % popup.factor)
    plt.ylabel('Curvature (k)')
    plt.title('Curvature Graph')
    plt.grid(True)

    plt.xticks(np.arange(0.0, 1.05, 0.05))
    plt.yticks(np.arange(-1.0, 1.2, 0.1))

    plt.savefig("test.png")

    # Desenha e mostra o grafico
    fig.canvas.draw()
    plt.show(block=False)

    # Loop para manter as informacoes atualizadas
    while True:
        try:
            curvature = []

            if mathutil.curvatureK:
                minimum = min(mathutil.curvatureK)
                maximum = max(abs(i) for i in mathutil.curvatureK)

                for x in mathutil.curvatureK:
                    k = x / maximum
                    curvature.append(k)

            if len(curvature) != 0:
                y = curvature

            else:
                y = b

            li.set_ydata(y)
            fig.canvas.draw()

        except Exception as error:
            raise error
            break
