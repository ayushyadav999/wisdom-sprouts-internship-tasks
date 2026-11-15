from collections import Counter, defaultdict, OrderedDict, deque
import heapq


def task1():
    numbers = list(map(int, input("Enter numbers: ").split()))
    largest = None
    second = None
    for number in numbers:
        if largest is None or number > largest:
            if number != largest:
                second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number
    print("Second largest:", second if second is not None else "Not found")


def task2():
    numbers = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target sum: "))
    seen = set()
    pairs = set()
    for number in numbers:
        needed = target - number
        if needed in seen:
            pairs.add(tuple(sorted((number, needed))))
        seen.add(number)
    print("Pairs:", list(pairs))


def task3():
    numbers = list(map(int, input("Enter numbers: ").split()))
    result = [number for number in numbers if number != 0]
    result.extend([0] * (len(numbers) - len(result)))
    print(result)


def task4():
    numbers = list(map(int, input("Enter numbers from 1 to N with one missing: ").split()))
    n = int(input("Enter N: "))
    missing = n * (n + 1) // 2 - sum(numbers)
    print("Missing number:", missing)


def task5():
    numbers = list(map(int, input("Enter numbers: ").split()))
    counts = Counter(numbers)
    duplicates = [number for number, count in counts.items() if count > 1]
    print("Duplicates:", duplicates)


def task6():
    text = input("Enter a string: ")
    counts = Counter(text)
    for char in text:
        if counts[char] == 1:
            print("First non-repeating character:", char)
            break
    else:
        print("No non-repeating character")


def task7():
    first = input("Enter first string: ").replace(" ", "").lower()
    second = input("Enter second string: ").replace(" ", "").lower()
    if len(first) != len(second):
        print("Not anagrams")
        return
    counts = {}
    for char in first:
        counts[char] = counts.get(char, 0) + 1
    for char in second:
        if char not in counts or counts[char] == 0:
            print("Not anagrams")
            return
        counts[char] -= 1
    print("Anagrams")


def task8():
    first = list(map(int, input("Enter first sorted array: ").split()))
    second = list(map(int, input("Enter second sorted array: ").split()))
    result = []
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    result.extend(first[i:])
    result.extend(second[j:])
    print("Merged array:", result)


def task9():
    numbers = input("Enter array elements: ").split()
    k = int(input("Enter K: "))
    if numbers:
        k %= len(numbers)
        result = numbers[-k:] + numbers[:-k] if k else numbers
    else:
        result = numbers
    print("Rotated array:", result)


def task10():
    first = list(map(int, input("Enter first array: ").split()))
    second = list(map(int, input("Enter second array: ").split()))
    counts = Counter(second)
    result = []
    for number in first:
        if counts[number] > 0:
            result.append(number)
            counts[number] -= 1
    print("Intersection:", result)


def task11():
    numbers = list(map(int, input("Enter numbers: ").split()))
    if not numbers:
        print("Array is empty")
        return
    current = best = numbers[0]
    for number in numbers[1:]:
        current = max(number, current + number)
        best = max(best, current)
    print("Maximum subarray sum:", best)


def task12():
    text = input("Enter a string: ")
    last_seen = {}
    start = 0
    longest = ""
    for i, char in enumerate(text):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = i
        if i - start + 1 > len(longest):
            longest = text[start:i + 1]
    print("Longest substring:", longest)
    print("Length:", len(longest))


def task13():
    words = input("Enter words separated by spaces: ").split()
    if not words:
        print("Common prefix:")
        return
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                break
    print("Longest common prefix:", prefix)


def task14():
    words = input("Enter words separated by spaces: ").split()
    groups = {}
    for word in words:
        key = tuple(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    print("Anagram groups:", list(groups.values()))


def task15():
    numbers = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Enter K: "))
    if k < 1 or k > len(numbers):
        print("Invalid K")
        return
    heap = []
    for number in numbers:
        if len(heap) < k:
            heapq.heappush(heap, number)
        elif number > heap[0]:
            heapq.heapreplace(heap, number)
    print("Kth largest:", heap[0])


def task16():
    text = input("Enter parentheses string: ")
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    valid = True
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                valid = False
                break
    print("Balanced" if valid and not stack else "Not balanced")


def task17():
    numbers = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target sum: "))
    prefix_positions = {0: [-1]}
    total = 0
    result = []
    for i, number in enumerate(numbers):
        total += number
        for start_index in prefix_positions.get(total - target, []):
            result.append(numbers[start_index + 1:i + 1])
        prefix_positions.setdefault(total, []).append(i)
    print("Subarrays:", result)


def task18():
    intervals = []
    count = int(input("Enter number of intervals: "))
    for i in range(count):
        start, end = map(int, input("Enter start and end: ").split())
        intervals.append([start, end])
    intervals.sort(key=lambda item: item[0])
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    print("Merged intervals:", merged)


def task19():
    numbers = list(map(int, input("Enter rotated sorted array: ").split()))
    target = int(input("Enter target: "))
    left, right = 0, len(numbers) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            answer = mid
            break
        if numbers[left] <= numbers[mid]:
            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1
    print("Index:", answer)


def task20():
    numbers = set(map(int, input("Enter numbers: ").split()))
    longest = 0
    for number in numbers:
        if number - 1 not in numbers:
            current = number
            length = 1
            while current + 1 in numbers:
                current += 1
                length += 1
            longest = max(longest, length)
    print("Longest consecutive sequence length:", longest)


def task21():
    heights = list(map(int, input("Enter bar heights: ").split()))
    left, right = 0, len(heights) - 1
    left_max = right_max = water = 0
    while left < right:
        if heights[left] < heights[right]:
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
            right -= 1
    print("Trapped rainwater:", water)


def task22():
    first = list(map(int, input("Enter first sorted array: ").split()))
    second = list(map(int, input("Enter second sorted array: ").split()))
    if len(first) > len(second):
        first, second = second, first
    m, n = len(first), len(second)
    low, high = 0, m
    while low <= high:
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i
        left_a = float("-inf") if i == 0 else first[i - 1]
        right_a = float("inf") if i == m else first[i]
        left_b = float("-inf") if j == 0 else second[j - 1]
        right_b = float("inf") if j == n else second[j]
        if left_a <= right_b and left_b <= right_a:
            if (m + n) % 2:
                median = max(left_a, left_b)
            else:
                median = (max(left_a, left_b) + min(right_a, right_b)) / 2
            print("Median:", median)
            return
        if left_a > right_b:
            high = i - 1
        else:
            low = i + 1
    print("Invalid input")


def task23():
    numbers = list(map(int, input("Enter numbers: ").split()))
    if not numbers:
        print("Array is empty")
        return
    max_product = min_product = answer = numbers[0]
    for number in numbers[1:]:
        if number < 0:
            max_product, min_product = min_product, max_product
        max_product = max(number, max_product * number)
        min_product = min(number, min_product * number)
        answer = max(answer, max_product)
    print("Maximum product:", answer)


def task24():
    numbers = list(map(int, input("Enter numbers: ").split()))
    present = set(numbers)
    missing = 1
    while missing in present:
        missing += 1
    print("Smallest missing positive:", missing)


def task25():
    numbers = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter K: "))
    counts = {0: 1}
    total = answer = 0
    for number in numbers:
        total += number
        answer += counts.get(total - target, 0)
        counts[total] = counts.get(total, 0) + 1
    print("Number of subarrays:", answer)


def task26():
    numbers = list(map(int, input("Enter numbers: ").split()))
    if not numbers:
        print("Longest increasing subsequence: []")
        return
    tails = []
    previous = [-1] * len(numbers)
    tail_indices = []
    for i, number in enumerate(numbers):
        low, high = 0, len(tails)
        while low < high:
            mid = (low + high) // 2
            if tails[mid] < number:
                low = mid + 1
            else:
                high = mid
        if low == len(tails):
            tails.append(number)
            tail_indices.append(i)
        else:
            tails[low] = number
            tail_indices[low] = i
        if low > 0:
            previous[i] = tail_indices[low - 1]
    sequence = []
    index = tail_indices[-1]
    while index != -1:
        sequence.append(numbers[index])
        index = previous[index]
    sequence.reverse()
    print("Longest increasing subsequence:", sequence)


def task27():
    coins = list(map(int, input("Enter coin values: ").split()))
    amount = int(input("Enter amount: "))
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)
    if dp[amount] == float("inf"):
        print("Change cannot be made")
    else:
        print("Minimum coins:", dp[amount])


def task28():
    text = input("Enter a string: ")
    words = input("Enter dictionary words separated by spaces: ").split()
    word_set = set(words)
    dp = [False] * (len(text) + 1)
    dp[0] = True
    for i in range(1, len(text) + 1):
        for j in range(i):
            if dp[j] and text[j:i] in word_set:
                dp[i] = True
                break
    print("Can be segmented:", dp[len(text)])


def task29():
    numbers = list(map(int, input("Enter jump lengths: ").split()))
    if len(numbers) <= 1:
        print("Minimum jumps: 0")
        return
    jumps = current_end = farthest = 0
    for i in range(len(numbers) - 1):
        farthest = max(farthest, i + numbers[i])
        if i == current_end:
            if farthest == current_end:
                print("Last index cannot be reached")
                return
            jumps += 1
            current_end = farthest
            if current_end >= len(numbers) - 1:
                print("Minimum jumps:", jumps)
                return


def task30():
    prices = list(map(int, input("Enter stock prices: ").split()))
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    print("Maximum profit:", profit)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def task31():
    capacity = int(input("Enter cache capacity: "))
    cache = LRUCache(capacity)
    while True:
        choice = input("Enter get, put or exit: ").lower()
        if choice == "get":
            key = input("Enter key: ")
            print(cache.get(key))
        elif choice == "put":
            key = input("Enter key: ")
            value = input("Enter value: ")
            cache.put(key, value)
        elif choice == "exit":
            break
        else:
            print("Invalid choice")


class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, value):
        self.stack.append(value)
        if not self.minimum or value <= self.minimum[-1]:
            self.minimum.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.minimum[-1]:
            self.minimum.pop()
        return value

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.minimum[-1] if self.minimum else None


def task32():
    stack = MinStack()
    while True:
        choice = input("Enter push, pop, top, min or exit: ").lower()
        if choice == "push":
            stack.push(int(input("Enter value: ")))
        elif choice == "pop":
            print("Popped:", stack.pop())
        elif choice == "top":
            print("Top:", stack.top())
        elif choice == "min":
            print("Minimum:", stack.getMin())
        elif choice == "exit":
            break
        else:
            print("Invalid choice")


def task33():
    rows = int(input("Enter number of rows: "))
    grid = []
    for i in range(rows):
        grid.append(list(map(int, input("Enter row values (0 or 1): ").split())))
    if not grid:
        print("Number of islands: 0")
        return
    columns = len(grid[0])
    visited = set()
    islands = 0
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1 and (r, c) not in visited:
                islands += 1
                queue = [(r, c)]
                visited.add((r, c))
                while queue:
                    x, y = queue.pop()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < columns and grid[nx][ny] == 1 and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
    print("Number of islands:", islands)


def task34():
    graph = {}
    edges = int(input("Enter number of edges: "))
    for i in range(edges):
        start, end, weight = input("Enter start end weight: ").split()
        weight = int(weight)
        graph.setdefault(start, []).append((end, weight))
        graph.setdefault(end, [])
    source = input("Enter starting node: ")
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))
    print("Shortest distances:", distances)


def task35():
    vertices = input("Enter vertices separated by spaces: ").split()
    directed = input("Is the graph directed? (yes/no): ").lower() == "yes"
    graph = {vertex: [] for vertex in vertices}
    edges = int(input("Enter number of edges: "))
    for i in range(edges):
        a, b = input("Enter edge: ").split()
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, [])
        if not directed:
            graph[b].append(a)

    if directed:
        state = {node: 0 for node in graph}

        def visit(node):
            state[node] = 1
            for neighbor in graph[node]:
                if state[neighbor] == 1:
                    return True
                if state[neighbor] == 0 and visit(neighbor):
                    return True
            state[node] = 2
            return False

        cycle = any(state[node] == 0 and visit(node) for node in graph)
    else:
        visited = set()

        def visit(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if visit(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        cycle = any(node not in visited and visit(node, None) for node in graph)
    print("Cycle detected" if cycle else "No cycle")


def task36():
    vertices = input("Enter vertices separated by spaces: ").split()
    graph = {vertex: [] for vertex in vertices}
    indegree = {vertex: 0 for vertex in vertices}
    edges = int(input("Enter number of edges: "))
    for i in range(edges):
        a, b = input("Enter directed edge: ").split()
        graph.setdefault(a, [])
        graph.setdefault(b, [])
        indegree.setdefault(a, 0)
        indegree.setdefault(b, 0)
        graph[a].append(b)
        indegree[b] += 1
    queue = deque([node for node in indegree if indegree[node] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) == len(indegree):
        print("Topological order:", order)
    else:
        print("Graph is not a DAG")


def task37():
    n = int(input("Enter number of queens: "))
    board = [-1] * n
    solutions = []

    def solve(row, columns, diagonals1, diagonals2):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if col not in columns and row - col not in diagonals1 and row + col not in diagonals2:
                board[row] = col
                solve(row + 1, columns | {col}, diagonals1 | {row - col}, diagonals2 | {row + col})
                board[row] = -1

    solve(0, set(), set(), set())
    print("Number of solutions:", len(solutions))
    for solution in solutions:
        for col in solution:
            print("." * col + "Q" + "." * (n - col - 1))
        print()


def task38():
    text = input("Enter a string or array elements separated by spaces: ")
    items = list(text) if " " not in text else text.split()
    results = []

    def generate(start):
        if start == len(items):
            results.append("".join(items) if " " not in text else items.copy())
            return
        used = set()
        for i in range(start, len(items)):
            if items[i] not in used:
                used.add(items[i])
                items[start], items[i] = items[i], items[start]
                generate(start + 1)
                items[start], items[i] = items[i], items[start]

    generate(0)
    print("Permutations:", results)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def serialize(root):
    if root is None:
        return "#"
    return str(root.value) + "," + serialize(root.left) + "," + serialize(root.right)


def deserialize(data):
    values = iter(data.split(","))

    def build():
        value = next(values)
        if value == "#":
            return None
        node = TreeNode(int(value))
        node.left = build()
        node.right = build()
        return node

    return build()


def task39():
    root = TreeNode(int(input("Enter root value: ")))
    left = input("Enter left child value or # for none: ")
    right = input("Enter right child value or # for none: ")
    if left != "#":
        root.left = TreeNode(int(left))
    if right != "#":
        root.right = TreeNode(int(right))
    data = serialize(root)
    print("Serialized tree:", data)
    new_root = deserialize(data)
    print("Deserialized root:", new_root.value)


def task40():
    root = TreeNode(int(input("Enter root value: ")))
    left = input("Enter left child value or # for none: ")
    right = input("Enter right child value or # for none: ")
    if left != "#":
        root.left = TreeNode(int(left))
    if right != "#":
        root.right = TreeNode(int(right))

    first = int(input("Enter first node value: "))
    second = int(input("Enter second node value: "))

    def find_lca(node, a, b):
        if node is None or node.value == a or node.value == b:
            return node
        left_result = find_lca(node.left, a, b)
        right_result = find_lca(node.right, a, b)
        if left_result and right_result:
            return node
        return left_result or right_result

    result = find_lca(root, first, second)
    if result:
        print("Lowest common ancestor:", result.value)
    else:
        print("Common ancestor not found")


tasks = {
    1: task1, 2: task2, 3: task3, 4: task4, 5: task5,
    6: task6, 7: task7, 8: task8, 9: task9, 10: task10,
    11: task11, 12: task12, 13: task13, 14: task14, 15: task15,
    16: task16, 17: task17, 18: task18, 19: task19, 20: task20,
    21: task21, 22: task22, 23: task23, 24: task24, 25: task25,
    26: task26, 27: task27, 28: task28, 29: task29, 30: task30,
    31: task31, 32: task32, 33: task33, 34: task34, 35: task35,
    36: task36, 37: task37, 38: task38, 39: task39, 40: task40
}

print("Python Coding Interview Questions")
print("Enter a question number from 1 to 40, or 0 to exit.")

while True:
    choice = input("\nEnter question number: ")
    if choice == "0":
        print("Program ended")
        break
    if choice.isdigit() and int(choice) in tasks:
        tasks[int(choice)]()
    else:
        print("Please enter a number between 1 and 40")
