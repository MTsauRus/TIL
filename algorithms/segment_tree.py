### 세그먼트 트리
def segment_tree():
    # arr: 배열
    # tree: 세그먼트 트리
    # node: 노드 번호
    # start~end: node에 저장되어 있는 합의 범위
    def init(arr, tree, node, start, end):
        if start == end: # 리프 노드일 때
            tree[node] = arr[start]
        else:
            init(arr, tree, node*2, start, (start+end)//2) # 왼쪽 자식
            init(arr, tree, node*2+1, (start+end)//2+1, end) # 오른쪽 자식
            tree[node] = tree[node*2] + tree[node*2+1] # 현재 노드 = 왼쪽 자식 + 오른쪽 자식
    
    # 구간 합을 구하는 쿼리
    # left~right: 원하는 구간 합
    def query(tree, node, start, end, left, right):
        if left > end or right < start: # 원하는 구간이 세그먼트 트리 구간을 벗어날 때
            return 0
        if left <= start and end <= right: # 현재 탐색 구간(start~end)가 원하는 구간(left~right) 안에 포함될 때
            return tree[node] # 현재 루트 노드(sum(start, end))를 반환한다.
        lsum = query(tree, node*2, start, (start+end)//2, left, right)
        rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
        return lsum + rsum
    
    # 특정 인덱스의 값이 수정되었을 때의 세그먼트 트리 업데이트
    # index: 수정될 값의 인덱스
    # val: arr[index] = val
    # index에 해당하는 리프 노드를 먼저 찾고, 이 값을 바탕으로 세그먼트 트리를 재구성하는 방식 채택
    def update(arr, tree, node, start, end, index, val):
        if index < start or end < index: # 현재 탐색 범위에 인덱스가 포함되지 않을 때
            return
        if start == end: # 리프 노드일 때, arr과 tree의 값을 업데이트하자.
            arr[index] = val
            tree[node] = val
            return
        update(arr, tree, node*2, start, (start+end)//2, index, val) # 왼쪽 자식 탐색
        update(arr, tree, node*2+1, (start+end)//2+1, end, index, val) # 오른쪽 자식 탐색
        tree[node] = tree[node*2] + tree[node*2+1]
        
        