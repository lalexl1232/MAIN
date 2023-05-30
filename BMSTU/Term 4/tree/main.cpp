#include <iostream>

using namespace std;

class Node {
public:
    int value;
    Node *left;
    Node *right;

    Node(int value) {
        this->value = value;
        left = NULL;
        right = NULL;
    }
};

class Tree {
private:

public:
    Node * head;
    Tree(){
        head = NULL;
    }

    void Add(Node*& node, int value) {
        Node* elem = new Node(value);
        //cout<<"add"<<endl;
        if(node == NULL){
            node = elem;
            return;
        }
        if(value <= node->value){
            Add(node->left, value);
        } else {
            Add(node->right, value);
        }
    }

    void print(Node* head){
        if (head == NULL)
            return;
        print(head->left);
        cout<< head->value<< " ";
        print(head->right);
    }
};

int main(){
    int m[10]={-17, 2, 10, -3, -10,25,20, 17, 5, 2};
    Tree t1= Tree();
    for (int i = 0; i <10; i++) {
        t1.Add(t1.head, m[i]);
    }
   t1.print(t1.head);
}