#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#define PORT 8080
using namespace std;
int main(int argc, char const *argv[]) {
int sock = 0, valread;
struct sockaddr_in serv_addr;
char buffer[1024] = {0};
if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
cout << "\n Socket creation error \n";
return -1;
}
serv_addr.sin_family = AF_INET;
serv_addr.sin_port = htons(PORT);
if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
cout << "\nInvalid address/ Address not supported \n";
return -1;
}
if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
cout << "\nConnection Failed \n";
return -1;
}
valread = read(sock, buffer, 1024);
cout << buffer << endl;
return 0;
}