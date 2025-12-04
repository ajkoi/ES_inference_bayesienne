from random import choice, randint
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Button

desdic = {4: 1 / 5, 6: 1 / 5, 8: 1 / 5, 10: 1 / 5, 20: 1 / 5}


def updatedic(result):
    for key, values in desdic.items():
        if values == 0:
            pass
        else:
            values *= p_result_de(key, result) / p(result)
        desdic[key] = values
    sumdic = sum(desdic.values())
    for key, values in desdic.items():
        desdic[key] = values / sumdic


def p(results):
    somme = 0
    prob = 0
    for key, val in desdic.items():
        if val == 0:
            pass
        else:
            if results <= key:
                prob += 1
        somme += key
    return prob / somme


def p_result_de(de, result):
    if result > de:
        return 0
    else:
        return 1 / de


fig, ax = plt.subplots(1, 3, figsize=(12, 7))
fig.tight_layout()
bottom = np.zeros(1)
bars = []
for key, val in desdic.items():
    # plot = ax.bar(["dés"], git push -u origin mainval, label=str(key), bottom=bottom)
    bars.append(ax[0].bar(["dés"], val, label=f"dé {key}", bottom=bottom))
    bottom += val

# ax[1].text(15, 1, "heellooo")
ax[0].legend(loc="upper right")

de = choice(list(desdic.keys()))

# ax[1].axis("off")
y_position = 0.9
text_objects = []
for key, val in desdic.items():
    text = ax[1].text(
        0.5, y_position, f"Dé {key}: {val:.3f}", ha="center", va="center", fontsize=12
    )
    text_objects.append(text)
    y_position -= 0.1

resultats = []

text = ax[2].text(0.1, 0.9, f"{resultats}", va="center", fontsize=15, wrap=True)


def next(event):
    result = randint(1, de)
    resultats.append(result)
    updatedic(result)
    bottoms = np.zeros(1)
    values = list(desdic.values())
    # print(len(values))
    for i in range(len(values)):
        for bar, val, bottom in zip(bars[i], [values[i]], bottoms):
            # print("ee")
            # print(val)
            # print(bottom)
            bar.set_y(bottom)
            bar.set_height(val)
        bottoms += values[i]

    y_position = 0.9
    for i, (key, val) in enumerate(desdic.items()):
        text_objects[i].set_text(f"Dé {key}: {val:.5f}")
        text_objects[i].set_y(y_position)
        y_position -= 0.1

    text.set_text(f"{resultats}")
    fig.canvas.draw_idle()
    # plt.draw()


axnext = fig.add_axes((0.81, 0.05, 0.1, 0.075))
bnext = Button(axnext, "Next")
bnext.on_clicked(next)

plt.show()
