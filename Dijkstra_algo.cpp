#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main() {
    int u, v, num, i, j, l, k, s[10], min, cost[10][10], dist[10], path[10], n;

    system("cls");
    printf("\nENTER NUMBER OF VERTICES: ");
    scanf("%d", &n);

    printf("\nENTER ADJACENCY MATRIX (use -1 for no direct path):\n");
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            scanf("%d", &cost[i][j]);
            if (i == j) {
                cost[i][j] = 0;
            } else if (cost[i][j] == -1) {
                cost[i][j] = 30000;
            }
        }
    }

    printf("\nENTER SOURCE VERTEX: ");
    scanf("%d", &v);

    system("cls");
    for (i = 1; i <= n; i++) {
        s[i] = 0;
        path[i] = v;
        dist[i] = cost[v][i];
    }

    dist[v] = 0;

    for (num = 2; num <= n; num++) {
        min = 30000;
        u = 0;
        for (i = 1; i <= n; i++) {
            if (s[i] != 1 && dist[i] < min) {
                min = dist[i];
                u = i;
            }
        }
        s[u] = 1;

        for (i = 1; i <= n; i++) {
            if (s[i] != 1 && dist[i] > min + cost[u][i]) {
                dist[i] = min + cost[u][i];
                path[i] = u;
            }
        }
    }

    printf("\nPATH MATRIX:\n");
    printf("\nDISTANCE\tNODE\tPATH\n");

    for (i = 1; i <= n; i++) {
        printf("\n %d\t\t%d\t", dist[i], i);
        j = i;
        do {
            printf(" --> %d", path[j]);
            u = path[j];
            j = u;
        } while (u != v);
    }

    //getch();
}

