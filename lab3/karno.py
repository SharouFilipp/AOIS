from typing import List, Dict, Tuple, Set

def make_kmap(values: List[int], variables: int) -> Tuple[Dict[Tuple[int, int], int], int, int]:
    if variables < 2 or variables > 5:
        raise ValueError("Количество переменных должно быть 2-5")
    sizes = {2: (2, 2), 3: (2, 4), 4: (4, 4), 5: (4, 8)}
    rows, cols = sizes[variables]
    orders = {
        2: [(0,0), (0,1), (1,1), (1,0)],
        3: [(0,0), (0,1), (0,3), (0,2), (1,0), (1,1), (1,3), (1,2)],
        4: [(0,0), (0,1), (0,3), (0,2), (1,0), (1,1), (1,3), (1,2),
            (3,0), (3,1), (3,3), (3,2), (2,0), (2,1), (2,3), (2,2)],
        5: [(0,0), (0,1), (0,3), (0,2), (0,6), (0,7), (0,5), (0,4),
            (1,0), (1,1), (1,3), (1,2), (1,6), (1,7), (1,5), (1,4),
            (3,0), (3,1), (3,3), (3,2), (3,6), (3,7), (3,5), (3,4),
            (2,0), (2,1), (2,3), (2,2), (2,6), (2,7), (2,5), (2,4)]
    }
    kmap = {}
    for idx, (row, col) in enumerate(orders[variables]):
        kmap[(row, col)] = values[idx] if idx < len(values) else 0
    return kmap, rows, cols

def get_rectangles(size: int, max_rows: int, max_cols: int) -> List[Tuple[int, int]]:
    rectangles = []
    if size == 32 and max_rows >= 4 and max_cols >= 8:
        rectangles.append((4, 8))
    if size == 16:
        if max_rows >= 2 and max_cols >= 8:
            rectangles.append((2, 8))
    if size == 8:
        if max_rows >= 2 and max_cols >= 4:
            rectangles.append((2, 4))
        if max_rows >= 1 and max_cols >= 8:
            rectangles.append((1, 8))
    if size == 4:
        if max_rows >= 2 and max_cols >= 2:
            rectangles.append((2, 2))
        if max_rows >= 1 and max_cols >= 4:
            rectangles.append((1, 4))
    if size == 2:
        if max_rows >= 1 and max_cols >= 2:
            rectangles.append((1, 2))
    if size == 1:
        rectangles.append((1, 1))
    return rectangles

def find_all_groups(kmap: Dict[Tuple[int, int], int], rows: int, cols: int) -> List[List[Tuple[int, int]]]:
    groups = []
    covered = set()
    ones = {pos for pos, val in kmap.items() if val == 1}
    for size in [32, 16, 8, 4, 2, 1]:
        rectangles = get_rectangles(size, rows, cols)
        rectangles.sort(key=lambda x: x[0] * x[1], reverse=True)
        for h, w in rectangles:
            for i in range(rows):
                for j in range(cols):
                    group = []
                    valid = True
                    for di in range(h):
                        for dj in range(w):
                            pos = ((i + di) % rows, (j + dj) % cols)
                            if kmap.get(pos, 0) != 1:
                                valid = False
                                break
                            group.append(pos)
                        if not valid:
                            break
                    if valid and group and not any(pos in covered for pos in group):
                        groups.append(group)
                        covered.update(group)
    groups.sort(key=len, reverse=True)
    return groups

def coords_to_binary(row: int, col: int, variables: int) -> str:
    if variables == 2:
        row_gray = [0, 1][row]
        col_gray = [0, 1][col]
        return f"{row_gray:01b}{col_gray:01b}"
    elif variables == 3:
        row_gray = [0, 1][row]
        col_gray = [0, 1, 3, 2][col]
        return f"{row_gray:01b}{col_gray:02b}"
    elif variables == 4:
        row_gray = [0, 1, 3, 2][row]
        col_gray = [0, 1, 3, 2][col]
        return f"{row_gray:02b}{col_gray:02b}"
    elif variables == 5:
        row_gray = [0, 1, 3, 2][row]
        col_gray = [0, 1, 3, 2, 6, 7, 5, 4][col]
        return f"{row_gray:02b}{col_gray:03b}"
    return ""

def find_implicant(group: List[Tuple[int, int]], variables: int) -> str:
    if not group:
        return ""
    binaries = [coords_to_binary(row, col, variables) for row, col in group]
    implicant = []
    for pos in range(variables):
        bits = {binary[pos] for binary in binaries}
        if len(bits) == 1:
            bit = bits.pop()
            var = chr(ord('a') + pos)
            implicant.append(var if bit == '1' else f"!{var}")
    return " & ".join(implicant) if implicant else "1"

def get_essential_implicants(groups: List[List[Tuple[int, int]]], ones: Set[Tuple[int, int]], variables: int) -> List[str]:
    implicants = [(group, find_implicant(group, variables)) for group in groups]
    implicants = [(group, imp) for group, imp in implicants if imp]
    if not implicants:
        return []
    essential = []
    covered_ones = set()
    minterms = {minterm for minterm in ones}
    for group, imp in implicants:
        group_set = set(group)
        if any(minterm in group_set and sum(1 for g, _ in implicants if minterm in g) == 1 for minterm in minterms - covered_ones):
            essential.append(imp)
            covered_ones.update(group_set)
    remaining_minterms = minterms - covered_ones
    while remaining_minterms:
        best_imp = None
        best_group = None
        max_coverage = 0
        for group, imp in implicants:
            coverage = len(set(group) & remaining_minterms)
            if coverage > max_coverage and imp not in essential:
                max_coverage = coverage
                best_imp = imp
                best_group = group
        if best_imp:
            essential.append(best_imp)
            covered_ones.update(best_group)
            remaining_minterms = minterms - covered_ones
        else:
            break
    return essential

def print_kmap(kmap: Dict[Tuple[int, int], int], rows: int, cols: int):
    row_labels = ['00', '01', '11', '10']
    col_labels = ['000', '001', '011', '010', '110', '111', '101', '100']
    print("      " + "  ".join(col_labels[:cols]))
    print("    +" + "---" * cols + "-+")
    for i in range(rows):
        row = [str(kmap.get((i, j), 0)) for j in range(cols)]
        print(f"{row_labels[i]} | {'  '.join(row)} |")
    print("    +" + "---" * cols + "-+")

def minimize_sdnf(values: List[str], variables: int) -> str:
    values = list(map(int, values))
    kmap, rows, cols = make_kmap(values, variables)
    print_kmap(kmap, rows, cols)
    ones = {pos for pos, val in kmap.items() if val == 1}
    if not ones:
        return "0"
    groups = find_all_groups(kmap, rows, cols)
    implicants = get_essential_implicants(groups, ones, variables)
    if not implicants:
        return "0"
    return " | ".join(f"({imp})" for imp in implicants)

def minimize_scnf(values: List[str], variables: int) -> str:
    values = list(map(int, values))
    kmap, rows, cols = make_kmap(values, variables)
    print_kmap(kmap, rows, cols)
    ones = {pos for pos, val in kmap.items() if val == 0}
    if not ones:
        return "0"
    groups = find_all_groups(kmap, rows, cols)
    implicants = get_essential_implicants(groups, ones, variables)
    if not implicants:
        return "0"
    return " | ".join(f"({imp})" for imp in implicants)

