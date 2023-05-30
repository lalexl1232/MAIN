#include <iostream>
#include <fstream>
using namespace std;

class Stud{
public:
    string Surname;
    int YearBorn;
    float AverageMark;
    Stud(string surname, int year, float mark){
        this->Surname = surname;
        this->YearBorn = year;
        this->AverageMark = mark;
    }
    void MyPrint(){
        cout<< Surname<< " "<< YearBorn<< " "<< AverageMark<< endl;
    }
};
Stud *sort_by_name(Stud* dat[56], int length){
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length-1; j++) {
            if(dat[j]->Surname > dat[j+1]->Surname){
                Stud a = dat[j];
                dat[j] = dat[j+1];
                dat[j+1] = a;
            }
        }
    }
    return dat;
}
int main() {
    Stud *data[56];
    Stud *sortData[56];
    int i=0;
    ifstream f1;
    f1.open("stud.txt");
    string name;
    int y;
    float m;
    while (!f1.eof()) {
        f1 >> name;
        if (f1.eof()) break;
        f1>> y >> m;
        data[i] = new Stud(name, y, m);
        i++;
    }
    sortData = sort_by_name(data, i);
}

