#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>   

struct frame {
    char ack;
    int data;
} frm[10];

int n, r;

void sender(void);
void recvack(void);
void resend_gb(void);

int main() {
    srand(time(0));
    sender();
    recvack();
    resend_gb();
    printf("\nAll frames have been sent successfully.\n");
    return 0;
}

void sender() {
    printf("\nEnter the number of frames to be sent: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("\nEnter data for frame [%d]: ", i + 1);
        scanf("%d", &frm[i].data);
        frm[i].ack = 'y'; 
    }
}

void recvack() {
    r = rand() % n; 
    frm[r].ack = 'n'; 
    printf("\nThe frame number %d was not received.\n", r + 1);
}

void resend_gb() {
    printf("\nResending from frame %d onwards...\n", r + 1);
    for (int i = r; i < n; i++) { 
        sleep(2); 
        frm[i].ack = 'y'; 
        printf("Frame %d received with data: %d\n", i + 1, frm[i].data);
    }
}

