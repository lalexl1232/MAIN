#include <iostream>
using namespace std;

int main(){
    char *s1 = new char[256];
    char *promej = new char[256];
    strcpy(s1, "s11111 s122 s333333");
    char *s2 = new char[256];
    strcpy(s2, "s113 s122 2348 s11");
    char *tmp, *tmp2;
    char *rez = new char[200];
    strcpy(rez, "");
    tmp = strtok(s1, " ");
    while (tmp != NULL){
        if(strlen(tmp) > strlen(rez))
            if ((tmp2 = strstr(s2, tmp)) != NULL) {
                if ((s2[strlen(tmp2)] == ' ') || (s2[strlen(tmp2)] == '\0'))
                    strcpy(rez, tmp);
            }
        for (int i = 0; i < (strlen(s1)- strlen(tmp2)); i++) {
            promej[i] = s1[i+ strlen(tmp2) + 1];
        }
        tmp = strtok(promej, " ");
        //tmp = strtok(NULL, " ");
    }
    cout << "rez = " << rez;
}