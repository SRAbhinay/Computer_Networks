
#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdlib.h>
#include <string.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/types.h>
#include <unistd.h>
#include <unistd.h>
#define MAX 80
#define MAX 80
#define PORT 8080
#define PORT 8080
#define SA struct sockaddr
#define SA struct sockaddr
void func(int connfd)
void func(int connfd)
{
{
char buff[MAX];
char buff[MAX];
int n;
int n;
for (;;) {
for (;;) {
bzero(buff, MAX);
bzero(buff, MAX);
read(connfd, buff, sizeof(buff));
read(connfd, buff, sizeof(buff));
printf("
printf("\\n");n");
printf("From client: %sEnter a message to client : ", buff);
printf("From client: %sEnter a message to client : ", buff);
bzero(buff, MAX);
bzero(buff, MAX);
n = 0;
n = 0;
while ((buff[n++]
while ((buff[n++] = getchar()) != '= getchar()) != '\\n')n')
;
;
write(connfd, buff, sizeof(buff));
write(connfd, buff, sizeof(buff));
if (strncmp("exit", buff, 4) == 0)
if (strncmp("exit", buff, 4) == 0)
{
{
printf("Server Exit...
printf("Server Exit...\\n");n");
break;
break;
}
}
}
}
}
}
int main()
int main()
{
{
int sockfd, connfd, len;
int sockfd, connfd, len;
struct sockaddr_in servaddr, cli;
struct sockaddr_in servaddr, cli;
sockfd = socket(AF_INET, SOCK_STREAM, 0);
sockfd = socket(AF_INET, SOCK_STREAM, 0);
if (sockfd ==
if (sockfd == --1) {1) {
printf("socket creation failed...
printf("socket creation failed...\\n");n");
exit(0);
exit(0);
}
}
else
else
printf("Socket successfully created..
printf("Socket successfully created..\\n");n");
bzero(&servaddr, sizeof(servaddr));
bzero(&servaddr, sizeof(servaddr));
servaddr.sin_family = AF_INET;
servaddr.sin_family = AF_INET;
servaddr.sin_addr.s_addr = h
servaddr.sin_addr.s_addr = htonl(INADDR_ANY);tonl(INADDR_ANY);
servaddr.sin_port = htons(PORT);
servaddr.sin_port = htons(PORT);
if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) {
if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) {
printf("socket bind failed...
printf("socket bind failed...\\n");n");
exit(0);
exit(0);
}
}
else
else
printf("Socket successfully binded..
printf("Socket successfully binded..\\n");n");
if ((listen(sockfd, 5)) != 0) {
if ((listen(sockfd, 5)) != 0) {
printf("
printf("Listen failed...Listen failed...\\n");n");
exit(0);
exit(0);
}
}
else
else
printf("Server listening..
printf("Server listening..\\n");n");
len = sizeof(cli);
len = sizeof(cli);
connfd = accept(sockfd, (SA*)&cli, &len);
connfd = accept(sockfd, (SA*)&cli, &len);
if (connfd < 0) {
if (connfd < 0) {
printf("server accept failed...
printf("server accept failed...\\n");n");
exit(0);
exit(0);
}
}
else
else
printf("server accept the client...
printf("server accept the client...\\n");n");
func(connfd)
func(connfd);;
close(sockfd);
close(sockfd);
}
}