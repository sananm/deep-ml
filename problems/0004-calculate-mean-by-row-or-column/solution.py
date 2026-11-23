def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode not in ("row", "column"):
        return []

    means = []
    if mode == "row":
        for i in matrix:
            means.append(sum(i)/len(i))
    else:
        for i in range(len(matrix[0])):
            total = 0
            for j in range(len(matrix)):
                total+=matrix[j][i]
            means.append(total/len(matrix))


    return means