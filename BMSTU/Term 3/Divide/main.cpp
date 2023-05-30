#include <iostream>
using namespace std;

class OneN{
private:
    int n;
    int count = 0;
public:
    OneN(int n){
        this->n = n;
    }

    int run(){
        int tempN = n;
        int l = 0;
        while (tempN != 0){
            tempN /= 10;
            l++;
        }

        for (int i = 1; i <= n; i++) {
            if (Yes_No(i)){
                count++;
                cout.width(l);
                cout << i << " ";
                if (count % 8 == 0)
                    cout << endl;
            }
        }
        cout << endl;
        cout << "count = " << count;
        return count;
    }

    bool Yes_No(int x){
        int temp = x;
        while (temp != 0){
            if ((temp % 10 != 0) && ((x % (temp % 10)) == 0)){
                temp = temp / 10;
            } else {
                return false;
            }
        }
        return true;
    }
};
int main() {
    int n;
    cout << "Enter n = ";
    cin >> n;
    OneN a(n);
    a.run();
    return 0;
}
