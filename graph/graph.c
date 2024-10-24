#include <stdio.h>
#include <stdbool.h>

#define SIZE 7

// Komşuluk matrisi
int adjacency_matrix[SIZE][SIZE] = {
    {0, 1, 1, 0, 0, 1, 0},
    {1, 0, 0, 1, 1, 0, 0},
    {0, 1, 1, 1, 0, 1, 0},
    {0, 1, 0, 0, 1, 0, 0},
    {1, 0, 1, 1, 0, 1, 0},
    {0, 1, 0, 1, 0, 0, 1},
    {1, 0, 1, 0, 1, 0, 0}
};

// BFS Fonksiyonu
void bfs(int start_node) {
    bool visited[SIZE] = {false};
    int queue[SIZE];
    int front = 0, rear = 0;

    // Başlangıç düğümünü işaretle ve kuyruğa ekle
    visited[start_node] = true;
    queue[rear++] = start_node;

    printf("BFS ile dolaşım: ");

    while (front < rear) {
        int node = queue[front++];
        printf("%d ", node);

        // Komşuları kontrol et
        for (int i = 0; i < SIZE; i++) {
            if (adjacency_matrix[node][i] == 1 && !visited[i]) {
                queue[rear++] = i;
                visited[i] = true;
            }
        }
    }

    printf("\n");
}

// DFS Yardımcı Fonksiyonu
void dfs_helper(int node, bool visited[]) {
    visited[node] = true;
    printf("%d ", node);

    // Komşuları kontrol et
    for (int i = 0; i < SIZE; i++) {
        if (adjacency_matrix[node][i] == 1 && !visited[i]) {
            dfs_helper(i, visited);
        }
    }
}

// DFS Fonksiyonu
void dfs(int start_node) {
    bool visited[SIZE] = {false};
    printf("DFS ile dolaşım: ");
    dfs_helper(start_node, visited);
    printf("\n");
}

// Ana Fonksiyon
int main() {
    int start_node = 0; // Başlangıç düğümü
    bfs(start_node);
    dfs(start_node);
    return 0;
}