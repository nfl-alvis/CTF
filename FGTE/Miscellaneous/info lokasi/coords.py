import matplotlib.pyplot as plt

def load_coords(filename):
    xs, ys = [], []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "," not in line:
                continue
            x, y = line.split(",")
            xs.append(int(x))
            ys.append(int(y))
    return xs, ys

xs, ys = load_coords("coords.txt")

plt.figure(figsize=(12, 6))
plt.scatter(xs, ys, s=5)
plt.gca().invert_yaxis()
plt.axis("equal")
plt.grid(True, linewidth=0.3)

plt.title("Plot Koordinat dari coords.txt")
plt.show()

