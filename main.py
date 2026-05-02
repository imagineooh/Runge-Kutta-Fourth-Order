def rk4(f1, f2, iterations, x0, y0):

    h = 0.000001

    yn = []
    tn = []
    t0 = 0
    yn.append([x0, y0])
    tn.append(t0)

    for n in range(iterations):
        if n == 0:
            k1 = [f1(x0, y0), f2(x0, y0)]
            k2 = [f1(x0 + h / 2 * k1[0], y0 + h / 2 * k1[1]), f2(x0 + h / 2 * k1[0], y0 + h / 2 * k1[1])]
            k3 = [f1(x0 + h / 2 * k2[0], y0 + h / 2 * k2[1]), f2(x0 + h / 2 * k2[0], y0 + h / 2 * k2[1])]
            k4 = [f1(x0 + h * k3[0], y0 + h * k3[1]), f2(x0 + h * k3[0], y0 + h * k3[1])]

            x0 = x0 + (h / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
            y0 = y0 + (h / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            yn.append([x0, y0])
            tn.append(t0 + h)
        else:
            k1 = [f1(yn[n][0], yn[n][1]), f2(yn[n][0], yn[n][1])]
            k2 = [f1(yn[n][0] + h * k1[0] / 2, yn[n][1] + h * k1[1] / 2),
                  f2(yn[n][0] + h * k1[0] / 2, yn[n][1] + h * k1[1] / 2)]
            k3 = [f1(yn[n][0] + h * k2[0] / 2, yn[n][1] + h * k2[1] / 2),
                  f2(yn[n][0] + h * k2[0] / 2, yn[n][1] + h * k2[1] / 2)]
            k4 = [f1(yn[n][0] + h * k3[0], yn[n][1] + h * k3[1]),
                  f2(yn[n][0] + h * k3[0], yn[n][1] + h * k3[1])]
            yn.append([
                yn[n][0] + (h / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
                yn[n][1] + (h / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
                ])
            tn.append(tn[n] + h)
    x_vals = [val[0] for val in yn]
    y_vals = [val[1] for val in yn]

    return x_vals, y_vals

