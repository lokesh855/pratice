//Character stuffing is commonly used in data communication protocols to ensure the
//receiving system correctly interprets the transmitted data. It helps frame the data so that the
//receiver can easily identify the start and end of each data frame. One common use case of
//character stuffing is serial communication, where data is transmitted one bit at a time over a
//communication channel.
#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
int i=0,j=0,n,pos;
char a[20],b[50];
printf("enter string\n");
scanf("%s",&a);
n=strlen(a);
printf("enter position\n");
scanf("%d",&pos);
if(pos>n)
{
printf("invalid position, Enter again less than %d:",n);
scanf("%d",&pos);
}
b[0]='d';
b[1]='l';
b[2]='e';
b[3]='s';
b[4]='t';
b[5]='x';
j=6;
while(i<n) {
if(i==pos-1)

{
b[j]='d';
b[j+1]='l';
b[j+2]='e';
b[j+3]='r';
b[j+4]='d';
b[j+5]='l';
b[j+6]='e';
j=j+7; }
if(a[i]=='d' && a[i+1]=='l' && a[i+2]=='e') {
b[j]='d';
b[j+1]='l';
b[j+2]='e';
j=j+3; }
b[j]=a[i];
i++;
j++; }
b[j]='d';
b[j+1]='l';
b[j+2]='e';
b[j+3]='e';
b[j+4]='t';
b[j+5]='x';
b[j+6]='\0';
printf("\nframe after stuffing:\n");

printf("%s",b);
getch();
}
