#include <iostream>
using namespace std;

class Elem{
public:
    char inf;
    int key;
    Elem* next;

    Elem(char inf, int key){
        this->inf = inf;
        this->key = key;
        next = NULL;
    }

    void print(){
        cout<< inf<< " : "<< key<< "   ";
    }
};

class Table{
public:
    Elem* head;
    Table() {
        head = NULL;
    }

    bool empty(){
        return head == NULL;
    }

    virtual void add(char value, int k){
        Elem* elem = new Elem(value, k);
        elem->next = head;
        head = elem;
    }

    void print(){
        Elem* tmp = head;
        while (tmp != NULL){
            tmp->print();
            tmp = tmp->next;
        }
        cout<< endl;
    }

    virtual Elem* search(int k){
        Elem* tmp = head;
        while(tmp != NULL){
            if(tmp->key == k)
                return tmp;
            tmp = tmp->next;
        }
        return NULL;
    }

    void del(int k){
        Elem* curr = head;
        Elem* pred = head;
        while(curr != NULL && curr->key != k){
            pred = curr;
            curr = curr->next;
        }
        if (curr == NULL){
            cout<< "No Key"<< endl;
            return;
        }
        if (curr->key == k){
            pred->next = curr->next;
            delete curr;
        }

    }
};

class TableKey: public Table{
public:

    void add(char value, int k){
        if ((head!= NULL) && (head->key <= k)){
            Elem* tmp = head;
            while ((tmp->next != NULL) && (tmp->next->key < k)){
                tmp = tmp->next;
            }

            Elem* elem = new Elem(value, k);
            elem->next = tmp->next;
            tmp->next = elem;
        } else {
            Elem* elem = new Elem(value, k);
            elem->next = head;
            head = elem;
        }
    }
};

class TableNum: public Table{
public:
    Elem* search(int k){
        if(head->key != k){
            Elem* tmp = head;
            while ((tmp->next != NULL) && (tmp->next->key != k)){
                tmp = tmp->next;
            }

            if(tmp->next == NULL){
                return NULL;
            } else{
                Elem* tmp1 = tmp->next;
                tmp->next = tmp1->next;
                tmp1->next = head;
                head = tmp1;

                return tmp1;
            }
        } else
            return head;
    }
};

int main() {
    Table table;
    const int n = 10;
    int key[n] = {1, 23, 34, 2, 20, -19, -8, 4, 76, 123};
    char inf[n] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'r', 'h', 'x'};
    for (int i = 0; i < n; i++) {
        table.add(inf[i], key[i]);
    }
    table.print();
    cout<< endl;
    table.search(23)->print();
    cout<< endl;
    table.del(20);
    table.print();
    cout<< endl;
    TableKey tablekey;
    for (int i = 0; i < n; i++) {
        tablekey.add(inf[i], key[i]);
    }
    tablekey.print();
    cout<< endl;

    TableNum tablenum;
    for (int i = 0; i < n; i++){
        tablenum.add(inf[i], key[i]);
    }
    tablenum.print();
    tablenum.search(23)->print();
    cout<< endl;
    tablenum.print();
    cout<< endl;
    tablenum.search(-19)->print();
    cout<< endl;
    tablenum.print();
    cout<< endl;
}
