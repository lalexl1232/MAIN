#include <iostream>
using namespace std;

class A{
public:
    int x;
    void f1(){
        cout<< "A ";
    }
    virtual void f2(){
        f1();
        cout<< x;
    }
};

class B: public A{
public:
    int x;
    void f1(){
        cout<< "B ";
    }
    void f2(){
        f1();
        cout << A::x<< " "<< x ;
    }
};

class C: public B{
public:
    int x;
    void f1(){
        cout << "C ";
    }
    void f2(){
        f1();
        cout<<A::x<< " "<< B::x<<" "<< x ;
    }
};

int main() {
    A objA;
    B objB;
    C objC;
    objA = objB;
    objA = objC;
    objB = objC;
    objA.x = 1;
    objB.A::x = 4;
    objB.x = 2;
    objC.B::x = 6;
    objC.A::x = 5;
    objC.x = 3;
    A* mass[10];
    for(int i = 0; i < 10; i++){
        if (i % 3 == 0)
            mass[i] = &objA;
        else if (i % 3 == 1)
            mass[i] = &objB;
        else
            mass[i] = &objC;
    }
    for (int i = 0; i < 10; i++) {
        mass[i]->f2();
        cout << endl;
    }
    for (int i = 0; i < 10; ++i) {
        mass[i]->f1();
        cout<< endl;
    }
}
