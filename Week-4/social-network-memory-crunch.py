import random
import numpy as np
from scipy.sparse import lil_matrix
import heapq

def create_tracker(n_users, is_sparse=True):
    return lil_matrix((n_users, n_users), dtype=np.int32) if is_sparse else {}

def add_group_interaction(tracker, group, is_sparse=True):
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            if is_sparse:
                tracker[group[i], group[j]] += 1
                tracker[group[j], group[i]] += 1
            else:
                tracker.setdefault(group[i], {}).setdefault(group[j], 0)
                tracker.setdefault(group[j], {}).setdefault(group[i], 0)
                tracker[group[i]][group[j]] += 1
                tracker[group[j]][group[i]] += 1
    return tracker

def top_3_interactions(tracker, user, is_sparse=True):
    if is_sparse:
        row = tracker[user].toarray().flatten()
        return heapq.nlargest(3, range(len(row)), key=lambda i: row[i]) if np.any(row) else []
    else:
        return heapq.nlargest(3, tracker.get(user, {}), key=tracker[user].get) if user in tracker else []

def generate_random_data(n_users, n_groups, group_size):
    return [random.sample(range(n_users), group_size) for _ in range(n_groups)]

def estimate_memory(tracker, is_sparse=True):
    if is_sparse:
        sparse_matrix = tracker.tocsr()
        return sparse_matrix.data.nbytes + sparse_matrix.indptr.nbytes + sparse_matrix.indices.nbytes
    else:
        return sum(len(v) for v in tracker.values()) * 12

def main(n_users, n_groups, group_size):
    groups = generate_random_data(n_users, n_groups, group_size)
    sparse_tracker = create_tracker(n_users, is_sparse=True)
    simple_tracker = create_tracker(n_users, is_sparse=False)
    
    for group in groups:
        sparse_tracker = add_group_interaction(sparse_tracker, group, is_sparse=True)
        simple_tracker = add_group_interaction(simple_tracker, group, is_sparse=False)
    
    print(f"Sparse Matrix Memory Usage: {estimate_memory(sparse_tracker)} bytes")
    print(f"Simple Dict Memory Usage: {estimate_memory(simple_tracker, is_sparse=False)} bytes")
    print(f"Top 3 interactions for user 0 (Sparse): {top_3_interactions(sparse_tracker, 0, is_sparse=True)}")
    print(f"Top 3 interactions for user 0 (Simple): {top_3_interactions(simple_tracker, 0, is_sparse=False)}")

main(10000, 5000, 5)
main(10000, 5000, 10)
main(100000, 50000, 5)
main(100000, 50000, 10)
main(100000, 100000, 10)
