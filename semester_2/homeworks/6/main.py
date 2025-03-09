from figures_storozhuk import read_figures_from_file

def main():
    files = ["input01.txt", "input02.txt", "input03.txt"]
    figures = []

    for file in files:
        figures.extend(read_figures_from_file(file))

    if not figures:
        print("Фігури не зчитано або дані відсутні.")
        return

    max_area_fig = max(figures, key=lambda f: f.area() if f.area() is not None else -float('inf'))
    max_perim_fig = max(figures, key=lambda f: f.perimeter() if f.perimeter() is not None else -float('inf'))

    print("Фігура з найбільшою площею:")
    print(f"{max_area_fig} -> Площа = {max_area_fig.area():.3f}")
    print("Фігура з найбільшим периметром:")
    print(f"{max_perim_fig} -> Периметр = {max_perim_fig.perimeter():.3f}")

if __name__ == '__main__':
    main()
