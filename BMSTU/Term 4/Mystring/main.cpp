#include <iostream>
#include <cstring>
using namespace std;

class Mystring{
private:
    char* str;
public:

    Mystring(char* str){
        this->str = new char[strlen(str)];
        strcpy(this->str, str);
    }

    Mystring(){
        str = NULL;
    }

    Mystring(Mystring const &a){
        this->str = a.str;
    }

    int length(){
        return strlen(str);
    }

    char* getstr(){
        return str;
    }

    Mystring devideR(int n){      // возвращает после n элемента|||| n включительно
        char* s;
        strcpy(s, str + n);
        Mystring rez(s);
        return rez;
    }

    Mystring devideL(int n){    //возвращает до n элемента n не включительно
        char* s;
        strncpy(s, str, n);
        Mystring rez(s);
        return rez;
    }

    Mystring operator+(char c){//добавление элемента в конец // работает
        char *s;
        strcpy(s, str);
        s[strlen(str)] = c;
        return Mystring (s);

    }

    Mystring operator+(char* str2){    //сложение строк // работает
        char* s;
        s = new char[strlen(str) + strlen(str2) + 1];
        strcpy(s, str);
        s = strcat(s, str2);
        Mystring rez(s);
        return rez;
    }

    Mystring operator+(Mystring str2){    //сложение строк  // работает
        return Mystring (*this+(str2.getstr()));
    }



    char* find(char* str){              //контекстный поиск
        return strstr(this->str, str);
    }

    Mystring zamena(char* y, char* z){              //замена части строки
        char* s = new char[strlen(str) - strlen(y) + strlen(z) + 1];
        char* tmp = find(y);
        if (tmp != NULL){
            strncpy(s, str, tmp - str);
            strcat(s, z);
            strcat(s, tmp + strlen(y));
            return Mystring(s);
        } else
            return Mystring (tmp);
    }

    Mystring zamena(Mystring y, char* z){
        return zamena(y.getstr(), z);
    }

    Mystring zamena(Mystring y, Mystring z){
        return zamena(y.getstr(), z.getstr());
    }

    Mystring operator-(char* str){
        return zamena(str, "");
    }

    void print(){
        cout<< str<< endl;
    }
};

int main() {
    Mystring a ("abbakcm");
    Mystring b ("aaabbc");
    Mystring c ("cccc");
    Mystring d ("qwerty");
    a.print();
    b.print();
    c.print();
    d.print();
    cout << "--------------------"<< endl;
    Mystring f = a.zamena("bba", "cccc");
    f.print();
    Mystring x = f.zamena(c, "qwerty");
    x.print();
    Mystring e = a + b;
    e.print();
    Mystring p = x.zamena(d, b);
    p.print();



}
