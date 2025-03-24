from figures.factory import create_figure

def read_figures_from_files(filenames):
    figs = []
    for filename in filenames:
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
    figs = read_figures_from_files(filenames)

    if not figs:
        print("No valid figures found.")
        return

    max_m, max_fig = -float("inf"), None
    for fig in figs:
        try:
            m = fig.volume()
        except:
            continue
        if m is not None and m > max_m:
            max_m, max_fig = m, fig

    print(max_fig, max_m) if max_fig else print("No valid figure")

if __name__ == "__main__":
    main()
