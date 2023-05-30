#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;
class Stud
{
public:
    char* name;
    int year;
    float mark;
    Stud()
    {
        name=NULL;
        year=0;
        mark=0.0;
    }
    Stud(char* n) : Stud()
    {
        name=new char[strlen(n)+1];
        strcpy(name, n);
    }
    bool load(ifstream& fileInput)
    {
        char name[40];
        fileInput>>name;
        if(fileInput.eof())
            return 0;
        this->name=new char[strlen(name)+1];
        strcpy(this->name, name);
        fileInput>>year>>mark;
        return 1;
    }
//	void* keyof()
//	{
//		return name; // return &year;
//	}
    int compare(Stud* k1)
    {
        return strcmp(name, k1->name);
    }
    void show()
    {
        cout<<name<<" "<<year<<" "<<mark<<endl;
    }
};
class MyInt
{
public:
    int i;
    MyInt()
    {
        i=0;
    }
    MyInt(int n)
    {
        i=n;
    }
    bool load(ifstream& fileInput)
    {
        int n=-7777;
        fileInput>>n;
        if(fileInput.eof() && n==-7777)
            return 0;
        i=n;
        return 1;
    }
    int compare(MyInt* k1)
    {
        return (i - k1->i);
    }
    void show()
    {
        cout<<i<<" ";
    }
};
template <class T> class Collection
{
public:
    void** arr;
    int limit, delta, count;

    Collection() : limit(0), delta(0), count(0) {
        arr = NULL;
    }
    Collection(int l, int d) : limit(l), delta(d), count(0) {
        arr=new void*[limit];
    }
    void setLimit(int lim)
    {
        void** arr2=new void*[lim];
        memcpy( arr2, arr, count*sizeof(void *) );
        delete arr;
        arr=arr2;
        limit=lim;
    }
    void insert(void* v)
    {
        if(count==limit)
            setLimit(count+delta);
        arr[count]=v;
        ++count;
    }
    void* at(int& index)
    {
        return arr[index];
    }
    void show()
    {
        for(int i=0; i<count; i++)
        {
            ((T*)(at(i)))->show();
        }
        cout<<endl;
    }
    void load(ifstream& fileInput)
    {
        while(1)
        {
            T* st=new T();
            if(st->load(fileInput)==0)
                break;
            this->insert(st);
        }
    }
};
template <class T> class SortedCollection : public Collection <T>
{
public:
    SortedCollection(int lim, int del) : Collection<T>::Collection(lim, del){}

    int compare(void* k1, void* k2)
    {
        return ((T*)k1)->compare((T*)k2);
    }
    int search(void* v)
    {
        int index=0;
        if(this->count==0)
            index=-1;
        else
            while(this->compare(v, this->arr[index]) >= 0)
            {
                index++;
                if(index==this->count)
                    break;
            }
        return index;
    }
    void insert(void* v)
    {
        if(this->count==this->limit)
            Collection<T>::setLimit(this->count+this->delta);
        int index = search(v);
        if(index==-1)
        {
            this->arr[0]=v;
        }
        else
        {
            for(int i=this->count; i>index; i--)
                this->arr[i]=this->arr[i-1];
            this->arr[index]=v;
        }
        this->count++;
    }
    void init(Collection <T> & col)
    {
        for(int i=0; i<col.count; i++)
        {
            void* v=col.at(i);
            this->insert(v);
        }
    }
};
//Users/lalexl/CLionProjects/sem2/collection/
int main()
{
    ifstream fileInput("/Users/lalexl/CLionProjects/sem2/collection/student.txt");
    if(!fileInput){
        cout<<"errror1"<< endl;
    }
    Collection <Stud> col(4,2);
    col.load(fileInput);
    fileInput.close();
    col.show();
    cout<< "--------------------"<< endl;

    ifstream fileInput2("/Users/lalexl/CLionProjects/sem2/collection/MyInt.txt");
    if(!fileInput2){
        cout<<"errror2"<< endl;
    }
    Collection <MyInt> col2(4,2);
    col2.load(fileInput2);
    fileInput2.close();
    col2.show();
    cout<< "--------------------"<< endl;

    SortedCollection <Stud> s_c(4, 2);
    s_c.init(col);
    s_c.Collection<Stud>::show();
    cout<< "--------------------"<< endl;

    SortedCollection <MyInt> s_c2(4, 2);
    s_c2.init(col2);
    s_c2.Collection<MyInt>::show();
}










