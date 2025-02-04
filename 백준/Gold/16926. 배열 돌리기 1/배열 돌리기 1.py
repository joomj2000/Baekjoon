import sys
from collections import deque

def rotate_layer(layer, R):
    """한 층의 요소를 R번 회전한 후 반환"""
    queue = deque(layer)
    queue.rotate(-R)  # 왼쪽으로 R번 회전
    return list(queue)

def get_layer(matrix, layer_idx, N, M):
    """layer_idx 번째 껍질의 요소들을 추출"""
    layer = []
    # 위(왼쪽 → 오른쪽)
    for j in range(layer_idx, M - layer_idx):
        layer.append(matrix[layer_idx][j])
    # 오른쪽(위쪽 → 아래쪽)
    for i in range(layer_idx + 1, N - layer_idx):
        layer.append(matrix[i][M - layer_idx - 1])
    # 아래 (오른쪽 → 왼쪽)
    for j in range(M - layer_idx - 2, layer_idx - 1, -1):
        layer.append(matrix[N - layer_idx - 1][j])
    # 왼쪽(아래쪽 → 위쪽)
    for i in range(N - layer_idx - 2, layer_idx, -1):
        layer.append(matrix[i][layer_idx])

    return layer

def set_layer(matrix, layer_idx, rotated_layer, N, M):
    """회전된 layer를 다시 matrix에 삽입"""
    idx = 0
    #위(왼쪽 → 오른쪽)
    for j in range(layer_idx, M - layer_idx):
        matrix[layer_idx][j] = rotated_layer[idx]
        idx += 1
    #오른쪽(위쪽 → 아래쪽)
    for i in range(layer_idx + 1, N - layer_idx):
        matrix[i][M - layer_idx - 1] = rotated_layer[idx]
        idx += 1
    #아래(오른쪽 → 왼쪽)
    for j in range(M - layer_idx - 2, layer_idx - 1, -1):
        matrix[N - layer_idx - 1][j] = rotated_layer[idx]
        idx += 1
    #왼쪽(아래쪽 → 위쪽)
    for i in range(N - layer_idx - 2, layer_idx, -1):
        matrix[i][layer_idx] = rotated_layer[idx]
        idx += 1

def rotate_matrix(matrix, N, M, R):
    """전체 행렬을 R번 회전"""
    num_layers = min(N, M) // 2  # 회전할 껍질(layer)의 개수

    for layer_idx in range(num_layers):
        layer = get_layer(matrix, layer_idx, N, M)
        rotated_layer = rotate_layer(layer, R)
        set_layer(matrix, layer_idx, rotated_layer, N, M)


N, M, R = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

rotate_matrix(matrix, N, M, R)

for row in matrix:
    print(*row)
