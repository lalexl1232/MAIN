#include <iostream>
using namespace std;

class Mass{
public:
    string text = "Ваш массив: ";
    int length;
    int *arr;

    Mass(int length){
        this->length = length;
        get_memory();
    }

    Mass(int length1, int length2){
        this->length = length1 + length2;
        get_memory();
    }

    void get_memory() {
        arr = new int[length];
    }

    int MyPrint(){
        cout << text;
        for (int i = 0; i < length; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    void init(){
        cout << "Введите элементы массива: " << endl;
        for (int i = 0; i < length; i++) {
            cout << "[" << i << "]"<< " : ";
            cin >> arr[i];
        }
    }


    int find(int number){
        cout << "Номер искомого элемента: ";
        for (int i = 0; i < length; i++) {
            if(arr[i] == number){
                cout << (i + 1) << endl;
                return (i + 1);
            }
        }
        return -1;
    }

    void *add(Mass arr1, Mass arr2){
        text = "Объединение двух массивов: ";
        for (int i = 0; i < arr1.length; i++)
            arr[i] = arr1.arr[i];
        for (int j = 0; j < arr2.length; j++)
            arr[arr1.length + j] = arr2.arr[j];
        cout << endl;
        return arr;
    }

    void sort(){
        text = "Отсортированный массив: ";
        for (int j = 0; j < length; j++) {
            for (int i = 0; i < length-1; i++) {
                if (arr[i] > arr[i+1]){
                    int z = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = z;
                }
            }
        }
    }
};

int main() {
    int length1;
    int length2;
    cout << "Введите длинну первого массива: ";
    cin >> length1;
    Mass arr1 (length1);
    arr1.init();
    arr1.MyPrint();
    cout << "Введите длинну второго массива: ";
    cin >> length2;
    Mass arr2 (length2);
    arr2.init();
    arr2.MyPrint();
    Mass sum(arr1.length, arr2.length);
    sum.add(arr1, arr2);
    sum.MyPrint();
    sum.sort();
    sum.MyPrint();
    cout << "Введите число которое хотите найти: ";
    int n;
    cin >> n;
    sum.find(n);
}
