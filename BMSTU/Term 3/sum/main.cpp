#include <iostream>
using namespace std;

int fact(int n){
    if (n < 2){
        return 1;
    } else {
        return n * fact(n -1);
    }
}

class Summ {
private:
    float x;
    int n;
    double sum;
public:
    Summ(float x, int n){
        this->x=x;
        this->n=n;
    }

    double CountSum(){
        sum = ((-1)/(x*(fact(n-1))));
        for (int i = 2; i <= n; i++) {
            sum *= (((-2) * (i - 1) * (2 * i - 1) * (n - i + 1))/x);
        }
        return sum;
    }

};
int main() {
    Summ aa(2, 5);
    cout << aa.CountSum();
}
