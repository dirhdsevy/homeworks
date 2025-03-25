from figures import create_figure

def read_figures(filename):
    figs = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                tokens = line.split()
                if not tokens:
                    continue
                name = tokens[0]
                try:
                    params = list(map(float, tokens[1:]))
                except ValueError:
                    continue
                fig = create_figure(name, params)
                if fig:
                    figs.append(fig)
    except FileNotFoundError:
        print(f"File {filename} not found")
    return figs

def main():
    filenames = ["input01.txt", "input02.txt", "input03.txt"]
    figs = []
    for file in filenames:
        figs.extend(read_figures(file))

    if not figs:
        result = "No valid figures found."
    else:
        max_fig = max(figs, key=lambda fig: fig.volume(), default=None)
        if max_fig is not None:
            result = (
                f"Фігура з найбільшою мірою: {max_fig}\n"
                f"Міра: {max_fig.volume():.2f}"
            )
        else:
            result = "No valid figure"

    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(result)
    print("Результат записано у output.txt")

if __name__ == "__main__":
    main()
