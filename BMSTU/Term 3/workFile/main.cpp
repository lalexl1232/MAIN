#include <fstream>
#include <iostream>
//#include <conio.h>
using namespace std;



class Stud
{
public:
    char* name;
    int year;
    float mark;

    Stud(char* n, int y, float m)
    {
        name = new char[strlen(n) + 1];
//        strcpy_s(name,strlen(n)+1, n);
        year = y;
        mark = m;
    }

    int compareTo(Stud* arg)
    {
        return strcmp(name, arg->name);
    }

    void print()
    {
        cout << name << '\t' << year << "\t" << mark << endl;
    }
};

class Elem
{
public:
    Stud* inf;
    Elem* next;
    Elem(Stud* inf)
    {
        this->inf = inf;
        next = NULL;
    }
    void print()
    {
        inf->print();
    }

    int compareTo(Elem* arg)
    {
        return inf->compareTo(arg->inf);
    }



};


class Spis
{
public:
    Elem* head;
    Spis()
    {
        head = NULL;
    }

    void push(Elem* arg)
    {
        Elem* tek = head;
        Elem* pred = head;
        while ((tek != NULL) && (arg->compareTo(tek) > 0))
        {
            pred = tek;
            tek = tek->next;
        }
        if (tek == pred) {
            arg->next = head;
            head = arg;
        }
        else
        {
            arg->next = pred -> next;
            pred->next = arg;
        }
    }

    void print()
    {
        Elem* elem = head;
        while (elem != NULL)
        {
            elem->print();
            elem = elem->next;
        }
    }
};

int main(int args, char** argv)
{
    Stud* mas[40];
    int ind = 0;
    ifstream f("stud.txt");
    char name[20];
    int y;
    float m;
    while (1)
    {
        f >> name;
        if (f.eof())break;
        f >> y >> m;
        Stud* stud = new Stud(name, y, m);
        mas[ind++] = stud;
    }

    for (int j = 0; j < ind; j++)
    {
        mas[j]->print();
        //cout << mas[j]->name << "\t" << mas[j]->year << "\t" << mas[j]->mark << endl;
        //cout << mas[j]->mark << "\t\t" << mas[j]->name << "\t\t" << mas[j]->year << endl;
    }
    cout << "__________________" << endl;
    Spis spis;
    for (int j = 0; j < ind; j++)
    {
        Elem* elem = new Elem(mas[j]);
        spis.push(elem);
    }
    spis.print();

    return 0;
}