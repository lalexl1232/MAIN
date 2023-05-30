#include <iostream>
using namespace std;

class Complex{
public:
    double Re;
    double Im;

    Complex(){
    }

    Complex(double Re, double Im){
        cout <<"constucr2"<< endl;
        this->Re = Re;
        this->Im = Im;
    }

    void Myprint(){
        cout << Re<< " + "<< "("<< Im<< ")"<< "i"<<  endl;
    }

    Complex operator+(Complex b){
        cout<< "sum"<< endl;
        return Complex(Re + b.Re, Im + b.Im);
    }

    Complex operator-(Complex b){
        cout<< "minus" << endl;
        return Complex(this->Re - b.Re, this->Im - b.Im);
    }

    Complex operator*(Complex b){
        cout<< "mult" << endl;
        return Complex(this->Re * b.Re - this->Im * b.Im, this->Re * b.Im + this->Im * b.Re);
    }

    Complex operator/(Complex b){
        cout << "devide"<< endl;
        return Complex((this->Re * b.Re + this->Im * b.Im)/(b.Re * b.Re + b.Im * b.Im),
                       (b.Re * this->Im - this->Re * b.Im)/(b.Re * b.Re + b.Im * b.Im));
    }
};

int main() {
    Complex a (1, 2);
    Complex b (3, 4);
    Complex d(1, 1);
    Complex c;
    c = a + b * d;
    c.Myprint();
    c= a + (b * d);
    c.Myprint();
    c = a - b;
    c.Myprint();
    c = a * b;
    c.Myprint();
    c = a / b;
    c.Myprint();
}
